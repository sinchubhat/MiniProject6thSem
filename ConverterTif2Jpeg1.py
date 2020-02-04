# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:56:05 2020

@author: Dell
"""
import os, sys
from PIL import Image

for infile in os.listdir("./"):
    print("file : " + infile)
    if infile[-3:] == "tif" or infile[-3:] == "bmp" :
       # print "is tif or bmp"
       outfile = infile[:-3] + "jpeg"
       im = Image.open(infile)
       print("new filename : " + outfile)
       out = im.convert("RGB")
       out.save(outfile, "JPEG", quality=90)