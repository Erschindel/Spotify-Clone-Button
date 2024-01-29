# GET songs from my playlist
import requests

from api import auth, playlists


# def getSongs(playlist_id):
    
#     URL = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
#     get_token = token.access_token

#     headers = {
#         "Authorization" : f"Bearer {get_token}",
#         "Content-Type": "application/json"
#     }
    
#     res = requests.get(
#         URL,
#         headers = headers
#     )
#     tracks = res.json()["items"]
    

#     # print([item["track"]["name"] for item in tracks])
#     print(tracks[0]["track"].keys())
#     # print(tracks[0]["added_by"].keys())
#     # user_id = tracks[0]["added_by"]["id"]
#     # print(user_id, type(user_id))
#     # playlists.create_empty_playlist(user_id)


PLAYLIST_ID = "1Zho4YP5gNLjwCV4lqeFfJ"

authorize = auth.authorize("playlist-modify-public")

active_token = auth.get_token()

track_list = playlists.get_playlist_songs(active_token, PLAYLIST_ID)

# print(track_list)

playlists.create_empty_playlist(active_token)
# playlists.fill_playlist(PLAYLIST_ID, track_list)