import os

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

####### new clone
def create_empty_playlist(token, user_id = "129462827"):

    scope = "playlist-modify-public"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope))

    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    data = {
        "name": "DeleteMe again",
        "description": "Cloned playlist",
        "public": True
    }

    try :
        res = requests.post(
            url = url,
            headers = headers,
            data = data
        )
        print(f"Success!\n{res.body}")
    except :
        print("failed to create new empty playlist")

    print(f"response: {res.json()}")
    return res


def get_playlist_songs(token, playlist_id):
    
    URL = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    headers = {
        "Authorization" : f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    res = requests.get(
        URL,
        headers = headers
    )

    tracks = res.json()["items"]
    track_ids = [track["track"]["id"] for track in tracks]

    return track_ids


def fill_playlist(list_id, song_ids):

    scope = "playlist-modify-public"
    sp_auth = spotipy.Spotify(auth_manager=SpotifyOAuth(scope))

    sp_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    playlist = sp_client.playlist(list_id)

    spotipy.Spotify()

    try:

        sp_auth.playlist_change_details(
            list_id,
            name = f"Clone of {playlist['name']}"
        )
        print("here")
        
    except :
        print("failed to change song name")

    try :
        # try to remove songs first?
        res = sp_auth.playlist_add_items(
            list_id,
            song_ids
        )
    except :
        print("failed to add songs to list")

    # print(res)
    print("successful clone!")
    return res

##############


########## existing clone

def empty_playlist(list_id):
    #remove all songs
    return

def refresh_playlist(list_id, song_ids):
    empty_playlist(list_id)
    fill_playlist(list_id, song_ids)
    return

#############