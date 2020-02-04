# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:24:17 2020

@author: Dell
"""

import os, sys
# import the Python Image processing Library
from PIL import Image

for infile in os.listdir("./"):
    #print("file : " + infile)
    if infile[-3:] == "tif" or infile[-3:] == "bmp" :
       # print "is tif or bmp"
       outfile = infile[:-3] + "jpeg"
       
       # Create an Image object from an Image
       im = Image.open(infile)
       
       # Crop 
       # (left,top,left+width,top+height) tuple
       cropped = im.crop((32,32,64,64))
       
       #print("new filename : " + outfile)
       out = cropped.convert("RGB")
       out.save(outfile, "JPEG", quality=100)


for filename in os.listdir():
    if filename.endswith('.tif'):
        os.unlink(filename)
        #print(filename)