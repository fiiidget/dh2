# find the directory
# create a new file with the filename you're using and +New or something
# write {"doc": to that file
# append the regular document text to that file
# append } to the end
# profit.

import os
import glob
import sys
import re
filetext = []

indir = "C:\\Users\\Sarah Hackney\\Desktop\\samplefiles"
for root, dirs, filenames in os.walk(indir):
    for g in filenames:

        with open(indir+"\\"+str(g), "r", encoding = "utf-8") as f:

            for txt in f:

                filetext = str(txt)
            f.close()

        file = open(indir+"\\"+"newerfiles"+"\\"+str(g), "a", encoding = "utf-8")
        file.write("{\"doc\": ")




        file.write(filetext)
        file.write("}")
