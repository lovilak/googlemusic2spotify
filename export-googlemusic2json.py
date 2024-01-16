import os
import json
from config import *
from common import *

def main():
  if not os.path.exists(GOOGLE_DIR):
    os.makedirs(GOOGLE_DIR)
  youtube = youtube_connect(APIKEY_FILE)
  request = youtube.playlists().list(part="snippet", mine=True, maxResults=50)
  
  response = request.execute()
  playlist_export = 'google_playlist_export.json'
  export_to_json(response, playlist_export)
  parsed_data = parse_json_file(playlist_export)

  if parsed_data:
      data = (parsed_data)['items']
  else:
      print("Failed to parse JSON file. Please check the file path.")

  for i in data:
      pl_tittle = i['snippet']['title']
      pl_id = i['id']
      request = youtube.playlistItems().list(part="snippet", playlistId=pl_id, maxResults=50)
      response = request.execute()

      if not os.path.exists(GOOGLE_DIR + '/' + pl_tittle):
        os.makedirs(GOOGLE_DIR + '/' + pl_tittle)

      pl_file = pl_tittle + '_info.json'
      pl_path = GOOGLE_DIR + '/' + pl_tittle + '/' + pl_file
      export_to_json(response, pl_path)
      parsed_pl = parse_json_file(pl_path)
      i = 0

      while True:
        i = i + 1
        if 'nextPageToken' in parsed_pl:
          _ptoken = parsed_pl['nextPageToken']
          request = youtube.playlistItems().list(part="snippet", playlistId=pl_id, maxResults=50, pageToken=_ptoken)
          response = request.execute()

          pl_file = pl_tittle + '_info_' + i.__str__() + '.json'
          pl_path = GOOGLE_DIR + '/' + pl_tittle + '/' + pl_file
          export_to_json(response, pl_path)
          parsed_pl = parse_json_file(pl_path)
        else:
          break

if __name__ == "__main__":
	main()
