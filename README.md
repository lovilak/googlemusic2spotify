# GoogleMusic2Spotify

Create Python env
-------------
```
yum -y install python38 python3 gcc.x86_64 python36-devel.x86_64 git vim
pip3 install python38
virtualenv python38
source python38/bin/activate
```

## google
```
Create OAuth client ID -> DesktopApp -> apikey.json
../python3/bin/pip3 install -r requirements
```

## spotipy
```
./python3/bin/pip3 install pandas multidict typing_extensions yarl async_timeout idna_ssl attrs aiosignal charset_normalizer spotipy spotify

Get dev credentials
```

# usage
```
cp config.py_example config.py (with the right values)
```

export google playlist
-------------
```
../python3/bin/python3 export-googlemusic2json.py
```

import google playlist to spotify
-------------
```
../python3/bin/python3 spotify-create-playlist.py
```
