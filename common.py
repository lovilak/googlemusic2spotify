import os
import json
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def list_directory(directory_path):
    """
    List the contents of a directory.
    :param directory_path: The path of the directory.
    """
    try:
        directory_contents = os.listdir(directory_path)
        return directory_contents
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except PermissionError:
        print(f"Permission denied to access directory '{directory_path}'.")


def export_to_json(info_dict, _file):
  with open(_file, 'w', encoding='utf-8') as json_file:
      json.dump(info_dict, json_file, ensure_ascii=False, indent=4)

def parse_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in '{file_path}': {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def sp_connect(client_id, client_secret, redirect_uri):
  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope='playlist-modify-private'))
  return sp

def youtube_connect(client_secrets_file):
  scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
  os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
  api_service_name = "youtube"
  api_version = "v3"
  flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
  credentials = flow.run_local_server()
  youtube = googleapiclient.discovery.build(api_service_name,
                                        api_version,
                                        credentials=credentials)
  return youtube

