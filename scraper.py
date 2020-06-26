import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(res.text, "html.parser")

# Grab all links and votes in lists
links = soup.select(".storylink")
votes = soup.select(".score")

print(votes[0].get("id"))
