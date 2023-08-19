import applemusic

def play_music(source, track_name):
    """Plays the specified song on Apple Music.

    Args:
        source (str): The source of the music.
        track_name (str): The name of the song.

    Returns:
        str: A message indicating whether the song was played successfully.
    """

    # Check if the source is valid.
    if source != "apple_music":
        return f"Invalid source: {source}"

    # Search for the song on Apple Music.
    client = applemusic.api.Client()
    results = client.search(query=track_name, type="track", limit=1)

    # If the song is found, play it.
    if results['songs'][0]:
        song_uri = results['songs'][0]['uri']
        client.play(song_uri)
        return f"Playing {track_name} on Apple Music."

    # Otherwise, return an error message.
    else:
        return f"Couldn't find {track_name} on Apple Music."

def shuffle_playlist(playlist_id):
    """Shuffles the songs in the specified playlist on Apple Music."""

    # Import the necessary modules.
    import applemusic

    # Create an Apple Music object.
    client = applemusic.api.Client()

    # Shuffle the playlist.
    client.playlists.shuffle(playlist_id)


def add_song_to_playlist(playlist_id, song_uri):
    """Adds a song to the specified playlist on Apple Music."""

    # Import the necessary modules.
    import applemusic

    # Create an Apple Music object.
    client = applemusic.api.Client()

    # Add the song to the playlist.
    client.playlists.add_tracks(playlist_id, [song_uri])


def remove_song_from_playlist(playlist_id, song_uri):
    """Removes a song from the specified playlist on Apple Music."""

    # Import the necessary modules.
    import applemusic

    # Create an Apple Music object.
    client = applemusic.api.Client()

    # Remove the song from the playlist.
    client.playlists.remove_tracks(playlist_id, [song_uri])


def get_lyrics(song_uri):
    """Gets the lyrics for the specified song from Apple Music."""

    # Import the necessary modules.
    import applemusic

    # Create an Apple Music object.
    client = applemusic.api.Client()

  def create_playlist(playlist_name):
    """Creates a new playlist on Apple Music with the specified name."""

    # Import the necessary modules.
    import applemusic

    # Create an Apple Music object.
    client = applemusic.api.Client()

    # Create the playlist.
    client.playlists.create(name=playlist_name)


def get_top_songs(genre):
    """Gets a list of the top songs of the specified genre on Apple Music."""

    # Import the necessary modules.
    import applemusic

    # Create an Apple Music object.
    client = applemusic.api.Client()

    # Get the top songs of the specified genre.
    results = client.search(query=f"genre:{genre}", type="track", limit=50)

    # Return the list of songs.
    return results['songs']


def get_latest_releases():
    """Gets a list of the latest releases on Apple Music."""

    # Import the necessary modules.
    import applemusic

    # Create an Apple Music object.
    client = applemusic.api.Client()

    # Get the latest releases.
    results = client.new_releases()

    # Return the list of songs.
    return results['items']


def get_recommendations(song_uri):
    """Gets a list of songs that are similar to the specified song on Apple Music."""

    # Import the necessary modules.
    import applemusic

    # Create an Apple Music object.
    client = applemusic.api.Client()

    # Get the recommendations.
    recommendations = client.recommendations(seed_tracks=[song_uri])

    # Return the list of songs.
    return recommendations['tracks']
 


