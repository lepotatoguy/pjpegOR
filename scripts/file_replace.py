#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:55:38 2021

@author: lepotatoguy

This script organizes image files in the specified directory by moving them into subfolders based on their filename suffix:
- Files ending with '_t.jpg' are moved to the 't' subfolder.
- Files ending with '_p.jpg' are moved to the 'p' subfolder.
- Python scripts and other files are ignored.
The script skips specific entries (folders like 'p', 't', and this code 'file_replace.py') from processing.
"""

import os

path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/processed_f'
files=os.listdir(path)
files.remove("p")
files.remove("t")
files.remove("file_replace.py")

for file in files:
    src=file
    print(file)
    if file.find(".py") != -1:
        print("We have a python file here.")
        pass
    elif file.find("_t.jpg") != -1:
        src_f = "/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/processed_f/"+file
        dst="/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/processed_f/t/"+file
        #dst=""+str(i)+".jpg"
        os.rename(src,dst)
        
    elif file.find("_p.jpg") != -1:
        src_f = "/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/processed_f/"+file
        dst="/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/processed_f/p/"+file
        #dst=""+str(i)+".jpg"
        os.rename(src,dst)
        
    # elif file.find(".jpeg") != -1:
    #     dst=""+str(i)+"_t.jpeg"
    #     #dst=""+str(i)+".jpeg"
    #     os.rename(src,dst)
    #     i+=1
    else:
        pass
