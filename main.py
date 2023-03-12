from api import token, playlists


PLAYLIST_ID = "1Zho4YP5gNLjwCV4lqeFfJ"

track_list = playlists.get_playlist_songs(PLAYLIST_ID)
print("got songs")

playlists.create_empty_playlist()
print("made empty playlist")

# playlists.fill_playlist(PLAYLIST_ID, track_list)