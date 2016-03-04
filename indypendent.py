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

ids = range(172, 204, 1)
for x in ids:
    url = ('https://indypendent.org/issue/'+str(x))
# The only problem here is that issue 175 for some reason has the url 175-0,
# and if we could get that in here, it would be complete from 2013 thru 1st of 2015.
# Think about how to do this.

    issue_page = requests.get(url)
    if issue_page.status_code != 200:
        uprint ("uh, oops? that's a broken page", url)

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
# uprint(len(linkurl))
# with open("indylinks.csv", "wb") as indyfile:
#     # indyfile.write()
# # file = open("indylinks.csv",'wb')
#
#     wr = csv.writer(indyfile)
#
#     for item in linkurl:
#         wr.writerow(item)

for page in linkurl:
    url = ("https://indypendent.org/"+str(page))

    article_page = requests.get(url)
    if issue_page.status_code != 200:
        uprint ("uh, oops? that's a broken page", url)

    article_html = article_page.text

    soup = BeautifulSoup(article_html, "html.parser")

    article_text = soup.find_all("div", attrs = {"class" : "even"})
    for article in article_text:
        # articletxt = article.text
        # #articletxt.encode('utf-8')
        with open ('articles.csv', "a") as file:
            file.write(str((article.text).encode("utf-8", "ignore")))
# this just does one file for now I think. Work on writing ot individual txt files. kthx
