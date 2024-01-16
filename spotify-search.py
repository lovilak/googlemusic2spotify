from config import *
from common import *
import sys
import spotipy.util as util

SPOTIPY_CLIENT_ID = SPOTIPY_CLIENT_ID
SPOTIPY_CLIENT_SECRET = SPOTIPY_CLIENT_SECRET
SPOTIPY_REDIRECT_URI = SPOTIPY_REDIRECT_URI

sp = sp_connect(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

user_id = sp.current_user()['id']
print(user_id)

dirs = list_directory(GOOGLE_DIR)
print(dirs)

for dir in dirs:
    infos = list_directory(GOOGLE_DIR + '/' + dir)
    for info in infos:
        file = GOOGLE_DIR + '/' + dir + '/' + info

        data = parse_json_file(file)
        for track in data['items']:
            trackName = track['snippet']['title']
            artistName = ((track['snippet']['videoOwnerChannelTitle']).split('-'))[0]
            print("%s  %s" % (trackName, artistName))
            q = "artist:%s track:%s" % (artistName, trackName)
            try:
                sp_search = sp.search(q)
                track_id = sp_search['tracks']['items'][0]['id']
                print(track_id)
                track_uris = [ 'spotify:track:' + track_id ]
            except Exception as e:
                print(f"An error occurred: {e}")
