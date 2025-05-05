#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:31:53 2021

@author: lepotatoguy

This script analyzes a folder of image files to compute statistics about their dimensions and file sizes.
For each image, it categorizes:
- Width into ranges: 0–100 px, 100–1000 px, >1000 px
- Height into ranges: 0–100 px, 100–1000 px, >1000 px
- File size into ranges: 0–100 KB, 100–1000 KB, >1000 KB

At the end, it reports:
- Total number of images in each size range
- Maximum width observed in each width range
- Maximum height observed in each height range

Assumes input directory contains only image files (except 'get_size.py', which is excluded).
"""
import os
import PIL
path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/final/processed/t'
files=os.listdir(path)
#print(files)
files.sort()
files.remove("get_size.py")
#print(files)

#size
a = [0] *1335 #0-100kb
b = [0] *1335 #100-1000kb
c = [0] *1335 #1000kb-999999kb


#res (Width)
d = [-1] *1335 #0-100px
e = [-1] *1335 #100-1000px
f = [-1] *1335 #1000-max


#res (Height)
aa = [-1] *1335 #0-100px
ab = [-1] *1335 #100-1000px
ac = [-1] *1335 #1000-max


x = 0
y = 0
z = 0

j=1
for file in files:
    image = PIL.Image.open(file)
    width, height = image.size
    if (width>0) and (width<100):
        d[j]=width
        print("0 to 100 nicche")
    elif (width>100) and (width<1000):
        e[j]=width
        #print("100 to 1000 nicche")
    elif (width<0):
        print("invalid")
        break
    else:
        f[j]=width
        #print("1000 er beshi nicche")

for file in files:
    image = PIL.Image.open(file)
    width, height = image.size        
    if (height>0) and (height<100):
        aa[j]=height
    elif (height>100) and (height<1000):
        ab[j]=height
    elif (height<0):
        print("invalid")
        break
    else:
        ac[j]=height
    
for file in files:
    i = int(os.path.getsize(file))*0.001
    #print(file)
    #print(i)
    if (i>0) and (i<100):
        a[j]=1
    elif (i>100) and (i<1000):
        b[j]=1
    elif (i<0):
        print("invalid")
        break
    else:
        c[j]=1
    
    j = j + 1
    
for k in a:
    if str(k).find("1") != -1:
        x = x+1
        
for l in b:
    if str(l).find("1") != -1:
        y = y+1
        
for m in c:
    if str(m).find("1") != -1:
        z = z+1

print("Total:")
print("0-100kb: "+str(x)+" pictures")
print("100-1000kb: "+str(y)+" pictures")
print("1000kb-inf: "+str(z)+" pictures")


print ("Max Width")        
print(max(d))
print(max(e))
print(max(f))    

print ("Max Height")  
print(max(aa))
print(max(ab))
print(max(ac))      
        

