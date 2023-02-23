from bs4 import BeautifulSoup
import lxml
import requests

# Parsing a live website
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

movies_web = response.text
soup = BeautifulSoup(movies_web, "html.parser")

movies = []

movie_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for i in movies:
        file.write(f"{i}\n")