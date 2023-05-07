import spotipy
from dotenv import dotenv_values
import openai
import json
import argparse

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]

sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id=config["SPOTIFY_CLIENT_ID"],
        client_secret=config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://localhost:9999",
        scope="playlist-modify-private"
    )
)

current_user = sp.current_user()

print(current_user)