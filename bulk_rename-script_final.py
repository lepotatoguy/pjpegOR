#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 00:57:29 2021

@author: lepotatoguy
"""


stuff = "jpegtran -optimize -progressive -scans script_final.txt -outfile "
i=0
name = str(i)+"_p.jpg "+str(i)+".jpg"
final_str = ""
for i in range(1,1374):
    name = str(i)+"_p.jpg "+str(i)+"_t.jpg"
    stuff = stuff + name
    final_str = final_str + stuff + " && "
    stuff = "jpegtran -optimize -progressive -scans script_final.txt -outfile "
    
print(final_str)



