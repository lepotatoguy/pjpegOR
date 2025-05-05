#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:15:20 2021

@author: lepotatoguy

This script checks for missing numbered image files in a specified directory.
It assumes files are named with the format '<number>_t.jpg' and are numbered from 0 to 1335.
For each existing file, it marks its index as present; at the end, it prints the indices of files that are missing.
"""

number_of_images = 1336
arr = [-1] * number_of_images


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
