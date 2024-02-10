from api import auth, playlists


PLAYLIST_ID = "1Zho4YP5gNLjwCV4lqeFfJ"
authorize = auth.authorize("playlist-modify-public")

active_token = auth.get_token()

track_list = playlists.get_playlist_songs(active_token, PLAYLIST_ID)


playlists.create_empty_playlist(active_token)

# playlists.fill_playlist(PLAYLIST_ID, track_list)