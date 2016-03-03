from bs4 import BeautifulSoup
import requests
from time import sleep
import sys
import csv
import urllib

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

url = ("https://indypendent.org/node/63") #replace node number with each number in the range of issues that we want to scrape
issue_page = requests.get(url)
if issue_page.status_code != 200:
    uprint ("uh, oops? that's a broken page")

issue_html = issue_page.text

soup = BeautifulSoup(issue_html, "html.parser")

article_box = soup.find_all("div", attrs = {"class": "ds-2col-stacked node node-issue node-promoted view-mode-full clearfix"})

# for a_box in article_box:
#     uprint(a_box.text)

for a_box in article_box:
    article_links = a_box.find_all("div", attrs = {"class": "view-content"})

    # for an_article in article_links:
    #     uprint(an_article['href'])

    for an_article in article_links:
        a_link = an_article.find_all("a")
        uprint(a_link["href"])

        #
