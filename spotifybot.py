import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="53a8d3a122c54ee0a5e88c2f387dff47",
                                               client_secret="abf4797a1c5748c99e6ec6fc09c6c191",
                                               redirect_uri="www.madify.in",
                                               scope="user-library-read"))

# Search for a song
results = sp.search(q='song name', type='track')
song_uri = results['tracks']['items'][0]['uri'] # Get the URI of the first song in the search results

# Play the song
sp.start_playback(uris=[song_uri])
