from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_news_page = response.text

soup = BeautifulSoup(yc_news_page, "html.parser")
article_tag = soup.find_all(name="span", class_="titleline")

article_text = []
article_link = []
for article in article_tag:
    article_text.append(article.getText())
    article_link.append(article.find("a").get("href"))


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_upvote = max(article_upvote)
list_index = article_upvote.index(max_upvote)
print(article_text[list_index])
print(article_link[list_index])
print(article_upvote[list_index])