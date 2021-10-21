# Usage:
#
# python3 script.py --input original.png --output modified.png
# Based on: https://github.com/mostafaGwely/Structural-Similarity-Index-SSIM-

# 1. Import the necessary packages
from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
#import argparse
import imutils
import cv2
import os
import sys
import pandas as pd
from pandas import DataFrame
import time

startTime = time.time()


# path = '/home/user_name/pjpeg/Scan 1 (copy)/dataset-final/final/processed/all' #for linux
# path = "D:\\PJPEG\\final_dataset\\all" #for windows
path = "/home/joyanta/pjpeg/original/"
files = os.listdir(path)

# removing unnecessary files
# files.remove("get_size.py")

destination_jpg = "/home/joyanta/pjpeg/original"
destination_pjpeg = "/home/joyanta/pjpeg/pjpeg"


exp = files  # all experiments will be in this variable

amount_pic = len(files)

avg_ssim = 0  # ssim average

i = 0  # picture number

pic_name = ""

# 2. Construct the argument parse and parse the arguments

for file in exp:
    print(str(i+1) + " out of " + str(amount_pic))
    test_a = file  # one picture but compressed (pjpeg)
    test_b = file  # the same picture but original one
    if True:
        if test_a.find("_t.jpg") != -1:
            pass
        else:
            pic_name = test_a.strip('.jpg')
            test_a = str(pic_name)+"_t.jpg"
            test_b = str(pic_name)+".jpg"
            original = os.path.join(destination_jpg, test_b)
            compressed = os.path.join(destination_pjpeg, test_a)

        # 3. Load the two input images
        imageA = cv2.imread(original)  # original_image.jpg
        imageB = cv2.imread(compressed)  # compressed_image.jpg

        # 4. Convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        # 5. Compute the Structural Similarity Index (SSIM) between the two
        #    images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")

        # 6. You can print only the score if you want

        avg_ssim = avg_ssim + float(score)
        i = i + 1
        print(avg_ssim/i)


avg_ssim = avg_ssim/i

print("Average SSIM is: "+str(avg_ssim))
print("")
time_final = time.time() - startTime
print("Time took: "+str(time_final) + " seconds")
