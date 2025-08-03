# from bs4 import BeautifulSoup # type: ignore
# import requests # pyright: ignore[reportMissingModuleSource]


# response = requests.get(url="https://news.ycombinator.com/newest")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)


# articles = soup.find_all(name="tr", class_="athing")
# for article in articles:
#     title_tag = article.find("span", class_="titleline").find("a")
#     link_tag = title_tag.get("href")
#     vote = soup.find(name="span", class_="score").text
#     print(title_tag.text)
#     print(link_tag)
#     print(vote)


import requests
from bs4 import BeautifulSoup
import time
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console screen
    print("Scraping Hacker News...\n")

    response = requests.get("https://news.ycombinator.com/newest")
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("tr", class_="athing")

    for article in articles:
        # Get title and link
        title_tag = article.find("span", class_="titleline").find("a")
        title = title_tag.text
        link = title_tag.get("href")

        # Get votes using article ID
        article_id = article.get("id")
        vote_tag = soup.find("span", id=f"score_{article_id}")
        vote = vote_tag.text if vote_tag else "0 points"

        print("Title:", title)
        print("Link:", link)
        print("Votes:", vote)
        print("-" * 40)

    time.sleep(1)  # Wait 1 second before scraping again
