import os
import glob
import codecs
import csv
import sys
import re


indir = "C:\\Users\\Sarah Hackney\\Desktop\\samplefiles"
for root, dirs, filenames in os.walk(indir):
    for f in filenames:

        try:

            with open(indir+"\\"+str(f), "r", encoding = "utf-8") as thisfile:


                newjson = []

                newjson.append(thisfile.text)


                file = open(indir+"\\"+"new"+"_"+str(f)+".json", "w", encoding = "utf-8")
                file.write("{ \"doc\": "+newjson+"}")





        except:
            continue
print(newjson)
