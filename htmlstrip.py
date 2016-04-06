import html2text
import os
import glob
import codecs
import csv
import sys
import re

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

subject_terms = ["Espionage"] #, "Police", "Privacy", "Reconnaissance", "security", "Snowden", "spy", "surveillance"]

article_list = []
article_names = []
for term in subject_terms:
    indir = "c:\\Users\\Sarah Hackney\\Desktop\\Indy Articles\\"+str(term)
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:

            article_names.append(f)

    for g in article_names:

        try:
            file = open(str(term)+"_"+str(g)+".txt", "w")
            with open(indir+"\\"+str(g), "r", encoding = "utf-8") as thisfile:
                for text in thisfile:

                    matchObj = re.match( r'<div class="group-header">(.*)<div class="group-footer">', cleanertext, re.dotall)
                    # trying to do the regex first and get by div classes
                    if searchObj:
                        file.write(searchObj.group())



        except:
            continue

        # try:
        #     file = open(str(term)+"_"+str(g)+".txt", "w")
        #     # with open(file, "r", encoding = "utf-8") as againfile:
        #     with open(indir+"\\"+str(term)+"_"+str(g)+".txt", "r", encoding = "utf-8") as againfile:
        #         for cleanertext in againfile:
        #             h = html2text.HTML2Text()
        #             h.ignore_links = True
        #
        #             file.write(h.handle(text))
        #
        #
        #
        #
        # except:
        #     continue





# By\n(.*)\*\s\*\s\*
