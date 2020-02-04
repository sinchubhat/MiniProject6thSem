# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:12:02 2020

@author: Dell
"""

# import the Python Image processing Library

from PIL import Image

 

# Create an Image object from an Image

imageObject  = Image.open("./0000ec92553fda4ce39889f9226ace43cae3364e.jpeg")

 

# Crop 
# (left,top,left+width,top+height) tuple
cropped     = imageObject.crop((32,32,64,64))

 

# Display the cropped portion

cropped.show()