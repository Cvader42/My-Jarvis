import spotipy
from spotipy.oauth2 import SpotifyOAuth

def play_music(source, track_name):
    if source == "spotify":
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your_spotify_client_id", client_secret="your_spotify_client_secret"))
        results = sp.search(q=track_name, type="track", limit=1)
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.start_playback(uris=[track_uri])
            return f"Playing {track_name} on Spotify."
        else:
            return f"Couldn't find {track_name} on Spotify."
    else:
        return f"Invalid source: {source}"

def create_playlist(playlist_name):
    """Creates a new playlist on Spotify with the specified name."""

    # Create a Spotify object.
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your_spotify_client_id", client_secret="your_spotify_client_secret"))

    # Create the playlist.
    sp.user_playlists_create(user=sp.current_user()["id"], name=playlist_name)


def shuffle_playlist(playlist_id):
    """Shuffles the songs in the specified playlist on Spotify."""

    # Create a Spotify object.
    sp = spotipy.Spotify()

    # Shuffle the playlist.
    sp.playlist_shuffle(playlist_id)


def add_song_to_playlist(playlist_id, song_uri):
    """Adds a song to the specified playlist on Spotify."""

    # Create a Spotify object.
    sp = spotipy.Spotify()

    # Add the song to the playlist.
    sp.playlist_add_items(playlist_id, [song_uri])


def remove_song_from_playlist(playlist_id, song_uri):
    """Removes a song from the specified playlist on Spotify."""

    # Create a Spotify object.
    sp = spotipy.Spotify()

    # Remove the song from the playlist.
    sp.playlist_remove_items(playlist_id, [song_uri])


def get_lyrics(song_uri):
    """Gets the lyrics for the specified song on Spotify."""

    # Create a Spotify object.
    sp = spotipy.Spotify()

    # Get the lyrics.
    lyrics = sp.track_lyrics(song_uri)

    # Return the lyrics.
    return lyrics


def get_music_video(song_uri):
    """Gets the link to the music video for the specified song on Spotify."""

    # Create a Spotify object.
    sp = spotipy.Spotify()

    # Get the music video URL.
    video_url = sp.track_get_audio_features(song_uri)["preview_url"]

    # Return the music video URL.
    return video_url


def get_top_songs(genre):
    """Gets a list of the top songs of the specified genre on Spotify."""

    # Create a Spotify object.
    sp = spotipy.Spotify()

    # Get the top songs of the specified genre.
    results = sp.search(q=f"genre:{genre}", type="track", limit=50)

    # Return the list of songs.
    return results['tracks']['items']


def get_latest_releases():
    """Gets a list of the latest releases on Spotify."""

    # Create a Spotify object.
    sp = spotipy.Spotify()

    # Get the latest releases.
    results = sp.new_releases()

    # Return the list of songs.
    return results['items']


def get_recommendations(song_uri):
    """Gets a list of songs that are similar to the specified song on Spotify."""

    # Create a Spotify object.
    sp = spotipy.Spotify()

    # Get the recommendations.
    recommendations = sp.recommendations(seed_tracks=[song_uri])

    # Return the list of songs.
    return recommendations['tracks']
