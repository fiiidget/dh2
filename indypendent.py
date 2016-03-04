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

linkurl = []

ids = [63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 144, 182, 183, 184, 185, 186, 187, 188, 189, 190, 1919, 192, 193, 194, 195, 196, 197]
for x in ids:
    url = ('https://indypendent.org/node/'+str(x))

    issue_page = requests.get(url)
    if issue_page.status_code != 200:
        uprint ("uh, oops? that's a broken page")

    issue_html = issue_page.text

    soup = BeautifulSoup(issue_html, "html.parser")

    article_box = soup.find_all("div", attrs = {"class": "view view-issue-articles view-id-issue_articles view-display-id-entity_view_3 issue-section-national view-dom-id-3"})

    # for a_box in article_box:
    #     uprint(a_box.text)

    for a_box in article_box:
        article_links = a_box.find_all("div", attrs = {"class": "view-content"})
        for an_article in article_links:
            links = an_article.find_all("div", attrs = {"class": "views-field views-field-title"})
            for link in links:
                a_link = link.find_all("a")
                for thing in a_link:
                    linkurl.append(thing["href"])

# uprint(linkurl)
uprint(len(linkurl))
# with open("indylinks.csv", "wb") as indyfile:
#     # indyfile.write()
# # file = open("indylinks.csv",'wb')
#
#     wr = csv.writer(indyfile)
#
#     for item in linkurl:
#         wr.writerow(item)
