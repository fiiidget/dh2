import os
import glob
import codecs
import csv
import sys
import re
import json

open_path = "C:\\Users\\Sarah Hackney\\Desktop\\samplefiles",

for file in os.listdir("C:\\Users\\Sarah Hackney\\Desktop\\samplefiles"):
    ## this will open a json file for you to write to & name it the same thing as your input file.
    with open ('%s.json'%file, 'w') as fp:
        try:
           f = open(os.path.join(open_path,file), 'r', encoding = "utf-8")
           content = f.read()

           data = [content.text]

           file.write("{ \"doc\": "+data([])+"}")



        except:
            pass
