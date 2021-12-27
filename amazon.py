import requests
from bs4 import BeautifulSoup


# Tutorial from https://realpython.com/beautiful-soup-web-scraper-python/#challenges-of-web-scraping

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
