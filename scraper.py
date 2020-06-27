import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, "html.parser")

# Grab all links and votes in lists
links = soup.select(".storylink")
subtext = soup.select(".subtext")


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))

            # Appends a dictionary to the hn list
            hn.append({"title": title, "link": href, "votes": points})

    return hn


pprint.pprint(create_custom_hn(links, subtext))
