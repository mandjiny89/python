# import requests
# from bs4 import BeautifulSoup
# import re
#
# # user_input = input("Enter the year you like to pickup top 100 songs year fomat YYYY-MM-DD: ")
#
# URL = f"https://www.billboard.com/charts/hot-100/2010-10-01"
#
# response = requests.get(URL)
# top_100 = response.text
#
# soup = BeautifulSoup(top_100, "html.parser")
# song_filter = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
#
# song_list =[]
# for item in song_filter:
#     song_list.append(re.sub('\s+', '', item.find("h3").getText()))
#
# print(song_list)

# 2010-10-01


from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)