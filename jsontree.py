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
folders = ["api_BerkeleyBarb", "api_FOXNews", "api_Indypendent", "api_MainstreamMedia", "api_PopCulture"]
filetext = []

for item in folders:
    indir = "C:\\Users\\Sarah Hackney\\Desktop\\APIJSON\\"+str(item)
    for root, dirs, filenames in os.walk(indir):
        for g in filenames:

            with open(indir+"\\"+str(g), "r", encoding = "utf-8") as f:

                for txt in f:

                    filetext = str(txt)
                f.close()

            file = open(indir+"\\"+"new_"+str(item)+"\\"+str(g), "a", encoding = "utf-8")
            file.write("{\"doc\": ")




            file.write(filetext)
            file.write("}")
