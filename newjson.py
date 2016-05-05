import html2text
import os
import glob
import codecs
import csv
import sys
import re
from bs4 import BeautifulSoup

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# subject_terms = ["Espionage", "Police", "Privacy", "Reconnaissance", "security", "Snowden", "spy", "surveillance"]

# article_list = []
# article_names = []
# for term in subject_terms:
indir = "c:\\Users\\shackney\\Desktop\\"
for root, dirs, filenames in os.walk(indir):
	for f in filenames:



		try:

			with open(indir+"\\"+str(f), "r", encoding = "utf-8") as thisfile:


				newjson = []

				newjson.append(thisfile.text)


				file = open(indir+"\\"+"new"+"_"+str(f)+".json", "w", encoding = "utf-8")
				file.write("{ "doc": "+newjson+"}")





            except:
                continue
   