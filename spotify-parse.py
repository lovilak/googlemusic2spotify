from config import *
from common import *

file_path='playlist.json'
parsed_data = parse_json_file(file_path)

if parsed_data:
    data = (parsed_data)['tracks']['items'][0]['id']
    print(data)
