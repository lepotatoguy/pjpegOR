#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:15:20 2021

@author: lepotatoguy
"""

arr = [-1] * 1336


import os
path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/processed_f/t'
files=os.listdir(path)
files.remove("missing.py")
i = 1
for i in files:
    info = i.replace("_t.jpg","")
    arr[int(info)] = 1
    
for k in range(len(arr)):
    if arr[k] == -1:
        print(k)
