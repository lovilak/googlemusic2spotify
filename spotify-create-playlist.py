from config import *
from common import *
import sys
import spotipy.util as util
import logging

logging.basicConfig(filename=SPOTIFY_LOG, level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

sp = sp_connect(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
user_id = sp.current_user()['id']
dirs = list_directory(GOOGLE_DIR)

for dir in dirs:
    infos = list_directory(GOOGLE_DIR + '/' + dir)
    playlist_name = dir
    playlist_description = dir
    playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)

    for info in infos:
        file = GOOGLE_DIR + '/' + dir + '/' + info

        data = parse_json_file(file)
        for track in data['items']:
            _trackName = track['snippet']['title']
            _artistName = track['snippet']['videoOwnerChannelTitle']
            if len(_trackName.split('-')) > 0:
                trackName = (_trackName.split('-'))[0]
            else:
                trackName = _trackName

            if len(_artistName.split('-')) > 0:
                artistName = (_artistName.split('-'))[0]
            else:
                artistName = _artistName

            trackName = '"{}"'.format(trackName.strip())
            artistName = '"{}"'.format(artistName.strip())
            print("%s  %s" % (trackName, artistName))
            q = "artist:%s track:%s" % (artistName, trackName)
            try:
                sp_search = sp.search(q)
                track_id = sp_search['tracks']['items'][0]['id']

                track_uri = [ 'spotify:track:' + track_id ]
                sp.playlist_add_items(playlist['id'], track_uri)
                print(track_uri)

            except Exception as e:
                print(f"An error occurred: {e}")
                logger.error(q)
