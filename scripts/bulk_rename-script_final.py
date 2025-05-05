#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 00:57:29 2021

@author: lepotatoguy


This script generates a batch shell command to compress multiple JPEG images using `jpegtran` with
a progressive scan script (`script_final.txt`). It builds a command string that:
- Iterates over image numbers 1 to 1373.
- For each image, generates:
    jpegtran -optimize -progressive -scans script_final.txt -outfile <N>_p.jpg <N>_t.jpg
- Concatenates all commands with '&&' so they execute sequentially in a shell.

The final shell command is printed to stdout for manual use or further automation.

Requirements:
- Input files named '<N>_t.jpg' (1 ≤ N ≤ 1373) must exist.
- `jpegtran` must be installed and accessible from the command line.
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



