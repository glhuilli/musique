import os
from typing import List

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from musique.types import Song


_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")


def create_playlist(playlist_name: str, songs: List[Song]) -> int:
    """
    Creates the playlist given the name and the list of songs

    Note that first it creates the list and then adds the songs.
    """
    scope = "playlist-modify-public"
    sp_client = spotipy.Spotify(auth_manager=SpotifyOAuth(_CLIENT_ID, _CLIENT_SECRET, _REDIRECT_URI, scope=scope))
    user = sp_client.me()
    user_id = user["id"]

    # First we create the playlist
    playlist_id = _create_new_playlist(sp_client, user_id, playlist_name)

    # Then we find the songs
    track_ids = _search_tracks(sp_client, songs)

    # Finally we add the songs to the playlist
    return add_songs_to_playlist(sp_client, user_id, playlist_id, track_ids)


def _create_new_playlist(sp_client, user_id, playlist_name):
    playlist = sp_client.user_playlist_create(user_id, playlist_name)
    return playlist["id"]


def _search_tracks(sp_client, songs: List[Song]):
    track_ids = []
    for song in songs:
        query = f'artist:{song.artist} track:{song.title}'
        result = sp_client.search(query, type='track', limit=1)
        if result['tracks']['items']:
            track_id = result['tracks']['items'][0]['id']
            track_ids.append(track_id)
            print(f'Found track: {song.artist} - {song.title}')
        else:
            print(f'*** Track not found: {song.artist} - {song.title}')
    return track_ids


def add_songs_to_playlist(sp_client, user_id, playlist_id, track_ids) -> int:
    sp_client.user_playlist_add_tracks(user_id, playlist_id, track_ids)
    return len(track_ids)
