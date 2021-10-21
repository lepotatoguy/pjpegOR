#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:31:53 2021

@author: user
"""
import os

user = ""

path = f'/home/{user}/pjpeg/scan_lossy/original'
files=os.listdir(path)
#print(files)
files.sort()
#removing unnecessary file
# files.remove("get_size.py")
#print(files)

size_diff_avg = 0

destination_jpg = f"/home/{user}/pjpeg/scan_lossy/original"
destination_pjpeg = f"/home/{user}/pjpeg/scan_lossy/pjpeg"
destination_failed_pjpeg = f"/home/{user}/pjpeg/scan_lossy/failed_pjpeg"

j=1
for file in files:
    print(str(j) + " out of " + str(len(files)))
    print(file)
    image_original = os.path.getsize(os.path.join(destination_jpg,file))
    image_compressed_name = file.strip(".jpg")
    image_compressed_name = image_compressed_name + "_t.jpg"
    image_compressed = os.path.getsize(os.path.join(destination_pjpeg,image_compressed_name))

    size_diff = ((image_original - image_compressed) / image_original) * 100       
    size_diff_avg = size_diff_avg + size_diff
    print(size_diff_avg/j)
    j = j + 1

size_diff_avg = size_diff_avg/j
print("Average File Size Decreased: "+str(size_diff_avg) + " percent")
