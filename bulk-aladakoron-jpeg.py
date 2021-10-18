#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:40:53 2021

@author: lepotatoguy
"""


import os
path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/test-multiple_fruits'
files=os.listdir(path)
print(files)
i=1
for file in files:
    if file.find(".jpg") != -1:
        pass
    elif file.find(".jpeg") != -1:
        pass
    else:
        os.remove(file)
    