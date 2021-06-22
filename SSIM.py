#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:37:25 2021

@author: lepotatoguy
"""


# Usage:
#
# python3 script.py --input original.png --output modified.png
# Based on: https://github.com/mostafaGwely/Structural-Similarity-Index-SSIM-

# 1. Import the necessary packages
from skimage.measure import compare_ssim
#import argparse
import imutils
import cv2
import os
import sys
import pandas as pd
from pandas import DataFrame
# from colorama import Fore, init, Back, Style
# import openpyxl
# import re


path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/final/processed/all'
files=os.listdir(path)
#print(files)
#files.sort()
files.remove("get_size.py")
files.remove("SSIM.py")
files.remove("SSIM.xlsx")
#files.remove("ssim_final.xlsx")

# excel_path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/final/processed/all/SSIM.xlsx'

# df = pd.read_excel('SSIM.xlsx')

# ssim_col = [0] * 1335

# ssim_pic = [0] * 1335

exp = files #etar moddhei shob experiment hobe

avg_ssim = 0

i = 0

num = ""

# 2. Construct the argument parse and parse the arguments
for file in exp:
    # if (len(file) == 7): # 1 to 9 
    #     test_a = file
    #     if test_a.find("_t.jpg") != -1:
    #         num = file[0:1]
    #         test_b = file[0:1]+"_p.jpg"
    #     else: 
    #         num = file[0:1]
    #         test_b = file[0:1]+"_t.jpg"
    #     # print(str(test_a))
    #     print(test_b)
    # if (len(file) == 8): # 10 to 99 
    #     test_a = file
    #     if test_a.find("_t.jpg") != -1:
    #         num = file[0:2]
    #         test_b = file[0:2]+"_p.jpg"
    #     else: 
    #         num = file[0:2]
    #         test_b = file[0:2]+"_t.jpg"
    #     # print(str(test_a))
    #     print(test_b)
    if (len(file) == 9): # 100 to 999 
        test_a = file
        if test_a.find("_t.jpg") != -1:
            num = file[0:3]
            test_b = file[0:3]+"_p.jpg"
        else: 
            num = file[0:3]
            test_b = file[0:3]+"_t.jpg"
        # print(str(test_a))
        print(test_b)
    # elif (len(file) == 10): # 1000 to 9999
    #     test_a = file
    #     if test_a.find("_t.jpg") != -1:
    #         num = file[0:4]
    #         test_b = file[0:4]+"_p.jpg"
    #     else: 
    #         num = file[0:4]
    #         test_b = file[0:4]+"_t.jpg"
    #     # print(str(test_a))
    #     print(test_b)
        
        # 3. Load the two input images
        imageA = cv2.imread(test_a)
        imageB = cv2.imread(test_b)

        # 4. Convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        # 5. Compute the Structural Similarity Index (SSIM) between the two
        #    images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")

        # 6. You can print only the score if you want
        #print("SSIM: {}".format(score))
        
        avg_ssim = avg_ssim + float(score)
        # ssim_col[i]=score
        # ssim_pic[i]=num
        
        # name=sheet_obj.cell(row=i,column=1) 
        # name.value = num;
        # ssim=sheet_obj.cell(row=i,column=2) 
        # ssim.value = score;
        # wb_obj.save()

        print(num)
        exp.remove(file)
        exp.remove(test_b)
        
#df = pd.DataFrame({'Picture': ssim_pic, 'SSIM': ssim_col})
# df = pd.DataFrame(ssim_pic, columns=['Picture'])
# df = pd.DataFrame(ssim_col, columns=['SSIM'])

# writer = pd.ExcelWriter('ssim_final.xlsx', engine='xlsxwriter')

# df.to_excel(writer, sheet_name='Sheet1')

# writer.save()
        
#avg_ssim = avg_ssim/1333

print("Average SSIM is: "+str(avg_ssim))    

