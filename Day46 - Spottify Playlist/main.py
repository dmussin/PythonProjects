from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

SONG_LIST = []


# Spotify

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="a5472a069e1a49ae9ec10dc59fe5fe7f",
        client_secret="c6a543c82f6b470bac0aadc12cb5e2ea",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Input
date_input = input("Which year do you want to travel to? Type teh date in this format YYYY-MM-DD: ")


# BeautifulSoup
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date_input}")
response.raise_for_status()

top_music = response.text
soup = BeautifulSoup(top_music, "html.parser")

songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")

for song in songs:
    song = BeautifulSoup(str(song), "html.parser")

    song_title = song.find(name="h3", id="title-of-a-story")
    song_title = song_title.getText().rstrip().lstrip()
    SONG_LIST.append(f"{song_title}")
print(SONG_LIST)

song_names = SONG_LIST
print(song_names)

song_uris = []
year = date_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
