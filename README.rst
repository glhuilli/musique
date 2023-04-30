============================================================
MusiQue -- A Spotify Playlist Generator Powered with ChatGPT
============================================================

This project generates a personalized Spotify playlist using OpenAI and Spotify libraries.

"Musique" has a simple translation as it means "Music" in French, but the suffix "Que" also means "What" in Spanish, which was the main inspiration to pick this name for this repository. Altogether, the idea behind the MusiQue name is to represent the concept of "Que musica" (in Spanish) or "What music" in English.

The OpenAI's ChatGPT is used to analyze the user's music preferences and recommend songs, while the Spotify library is used to create the playlist and add the recommended songs to it.

Prerequisites
=============

- Python 3.9 or higher
- A Spotify Developer account with a registered application (client ID, client secret, and redirect URI)
- OpenAI API key

Installation
============

1. Clone this repository.

2. Install the required libraries:

   .. code-block:: shell

       pip install openai spotipy

3. Set the following environment variables:

   - SPOTIFY_CLIENT_ID: Your Spotify client ID
   - SPOTIFY_CLIENT_SECRET: Your Spotify client secret
   - SPOTIFY_REDIRECT_URI: Your Spotify redirect URI
   - OPENAI_API_KEY: Your OpenAI API key

   You can set these environment variables using the command line:

   .. code-block:: shell

       export SPOTIPY_CLIENT_ID='your_client_id'
       export SPOTIPY_CLIENT_SECRET='your_client_secret'
       export SPOTIPY_REDIRECT_URI='your_redirect_uri'
       export OPENAI_API_KEY='your_openai_api_key'


Usage
=====

Run the "run.py" script:

.. code-block:: shell

    python run.py

The script will prompt instructions you want to give to ChatGPT, generate a list of recommended songs, create a new playlist in your Spotify account, and add the recommended songs to the playlist.

For example

.. code-block:: shell

    python run.py --prompt "list of 50 songs that would be great for a baby shower but not nursery rhymes or children songs" --playlist_name "babyshower songs"


License
=======

This project is licensed under the MIT License. See the LICENSE file for details.
