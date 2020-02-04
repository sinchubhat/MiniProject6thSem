# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:01:01 2020

@author: Dell
"""

import os
for filename in os.listdir():
    if filename.endswith('.tif'):
        os.unlink(filename)
        print(filename)


