#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:46:30 2021

@author: lepotatoguy

This script checks for unmatched JPEG image pairs in a specified directory based on filename patterns.
It:
- Lists all files in the target directory, excluding the file named 'file_check'.
- For each file ending with '_t.jpg' (progressive image), checks whether a corresponding '_p.jpg' (baseline image) with the same base name exists.
- For each file ending with '_p.jpg' (baseline image), checks whether a corresponding '_t.jpg' exists.
- Prints the filename of any image that does not have a matching counterpart.

The script assumes:
- Filenames follow the convention '[basename]_t.jpg' for progressive images and '[basename]_p.jpg' for baseline images.
- All relevant files are directly within the specified directory (no subdirectories).
- Non-image or unrelated files (except 'file_check') are ignored.
"""


import os
path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/processed'
files=os.listdir(path)
files.sort()
files.remove("file_check.py")
#print(files)

file_name = ""
file_name2 = ""
for file in files:
    if file.find("_t.jpg") != -1:
        file_name = file.replace('_t.jpg','')
        for i in range(0,len(files)):
            file_name2 = files[i].replace('_p.jpg','')
            if (file_name != file_name2) and (i == len(files)-1):
                print(file)
            elif file_name == file_name2:
                break
            else:
                pass
    elif file.find("_p.jpg") != -1:
        file_name = file.replace('_p.jpg','')
        for j in range(0,len(files)):
            file_name2 = files[j].replace('_p.jpg','')
            if (file_name != file_name2) and (j == len(files)-1):
                print(file)
            elif file_name == file_name2:
                pass
            else:
                pass
    else:
        pass