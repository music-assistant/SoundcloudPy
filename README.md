# Soundcloud python async client

Async client for connecting to the Soundcloud API.

This is a Wrapped API that it is used from soundcloud web browser, its is subjected to changes and `NOT OFFICIAL`

This package is based on soundcloudpy from Naím Rodríguez https://github.com/naim-prog
Original package https://github.com/naim-prog/soundcloud-py

## Installation

The package is published on PyPI and can be installed by running:
```
pip install soundcloudpy
```

## How to get OAuth and Client id

1. Go to [soundcloud](https://soundcloud.com) and login in
2. Open the "Inspect" tool (F12 on most browsers)
3. Refresh the page
4. Go to the page "Network" on the inspect terminal
5. Search on the column "File" for the "client_id" and the "oauth_token" cookie for "Authorization"

`client_id`: string of 32 bytes alphanumeric

`authorization`: string that begins with OAuth and a string (the o-auth token is "OAuth . . .")

Example (OAuth and client_id are NOT real, use yours):

```
python -m example --client_id jHvc9wa0Ejf092wj3f3920w3F920as02 --auth_token 'OAuth 3-26432-21446-asdif2309fj'
```


## Functions

* Own account details
* User public details
* Own following
* Who to follow
* Last tracks reproduced info
* User profiles from tracks likes
* Track details
* Tracks liked
* Tracks by genre recent
* Tracks by genre popular
* Popular track from user
* Own playlists
* Playlists details
* Playlists by genre
* Playlists from user
* Recommended tracks of a track
* Stream URL's of a track (you can use it to reproduce the audio in VLC for example)
* Comments of a track
* Get mixed selection of playlists
* Search
* Subscribe feed
* Albums from user
* All feed from user


## DISCLAIMER

I take no responsability for the issues you may have with your soundcloud account or for breaching the [Terms of Use](https://developers.soundcloud.com/docs/api/terms-of-use) of soundcloud
