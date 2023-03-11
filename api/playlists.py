import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

from . import token

####### new clone
def create_empty_playlist(user_id = "129462827"):

    scope = "playlist-modify-public"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope))
    print(SpotifyOAuth(scope))

    res = sp.user_playlist_create(
        user_id,
        name="New Playlist",
        public=True,
        collaborative=False,
        description="Cloned playlist"
    )

    print(res.json())
    print("testing Git")
    return res

    # headers = {
    #     "Authorization" : f"Bearer {token}",
    #     "Content-Type": "application/json",
    #     "Accept": "application/json"
    # }

    # data = {
    #     "name": "New Playlist",
    #     "description": "Cloned playlist",
    #     "public": True
    # }

    # try :
    #     res = requests.post(
    #         url,
    #         headers,
    #         data
    #     )
    #     print(res.body)
    # except :
    #     print("failed to create new empty playlist")

    # print(res.status_code)
    # return res.status_code


def get_playlist_songs(playlist_id):
    
    URL = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    get_token = token.access_token

    headers = {
        "Authorization" : f"Bearer {get_token}",
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