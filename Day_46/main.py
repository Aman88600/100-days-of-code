from get_100_songs import get_songs


# Getting the date
date = input("What Year would you like to travel to ? write data in this format YYYY-MM-DD:")
print(date)
songs_list = get_songs(date)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your credentials here
CLIENT_ID = "774edc442c564ff0bf541ec98bae61da"
CLIENT_SECRET = "489ad08cf14a409fa086d5ee66629f63"
REDIRECT_URI = "https://localhost:8888/callback"  # Must match dashboard




# Set up the Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:8888/callback",  # must match dashboard
    scope="playlist-modify-public"
))

# Track URIs to add (use real Spotify track URIs)
track_uris = []
def get_uri(song_name):
    results = sp.search(q=song_name, type="track", limit=1)
    track_uri = results['tracks']['items'][0]['uri']
    return track_uri

# tracing all 100 songs
for song in songs_list:
    uri = get_uri(song)
    track_uris.append(uri)

# Get current user's Spotify ID
user_id = sp.current_user()['id']

# Create the playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=date,
    public=True,
    description="Created with Python and Spotipy!"
)

# Add tracks to the new playlist
sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

# Output the playlist URL
print("Playlist created:", playlist['external_urls']['spotify'])
