#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:40:53 2021

@author: lepotatoguy

This script performs cleanup of a specified directory by removing all files that are not JPEG images.
It:
- Lists all files in the target directory.
- Iterates through each file, checking the filename extension.
- Keeps files with '.jpg' or '.jpeg' extensions unchanged.
- Deletes all other files from the directory.

The script assumes all files are located directly in the specified path (no subdirectory traversal) and requires file access permissions.
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
    