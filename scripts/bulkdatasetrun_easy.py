"""
Created on 2021

@author: lepotatoguy

This script batch-recompresses a list of JPEG images using 'jpegtran' with a custom scan optimization script.
It:
- Reads a list of image filenames from 'readme.txt' (assumed to contain one filename per line).
- For each filename, strips the newline and file extension to obtain the base name.
- Defines the source (baseline JPEG) and destination (progressive JPEG) filenames.
- Invokes 'jpegtran' with optimization, progressive encoding, and a custom scan script to generate a recompressed output for each image.
- Prints progress updates for each processed image, showing index and filename.
- Records and prints the total execution time for the batch process.

The script assumes:
- The input filenames in 'readme.txt' follow the format '[basename].jpg'.
- The JPEG files are present in the working directory.
- A valid scan script named 'script_final (compression).txt' is available in the working directory.
"""


import subprocess
import time
startTime = time.time()

print("Let the game begin.")

# firstly run the fileList.py file. 
# and then getting the readme file (list of file), run this file

f = open('readme.txt')

arr = f.readlines()

import os

for name in arr:
            idx = arr.index(name)
            print(str(idx) + " out of " + str(len(arr)-1))
            name = name.strip('\n')
            print(name)
            # name = name[:-4] # I don't know why it was working with -4 but in dataset, it works with -5. it removes the .jpg part
            name = name[:-5]
            name_t = name+"_t.jpg" #progressive
            name_m = name+".jpg" #normal
            scan_name = "script_final (compression)"
            subprocess.call(["jpegtran", "-optimize", "-progressive", "-scans", f"{scan_name}.txt", "-outfile", name_t, name_m])
            print(name + " Done.")        

print("All Done.")
time_final = time.time() - startTime
print("Time took: "+str(time_final) + " seconds")
