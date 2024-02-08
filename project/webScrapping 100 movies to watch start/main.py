import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")
list_of_movies = [title.getText() for title in soup.find_all(name="h3", class_="title")]
list_rev = list_of_movies[::-1]

with open("top_100_movies.txt", "w") as movies:
    for item in list_rev:
        movies.write(f'{item}\n)

