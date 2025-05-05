"""
Created on 2021

@author: lepotatoguy

This script performs batch renaming of image files in a specified directory. It:
- Lists all files in the directory and removes 'bulk_rename.py' from processing.
- Iterates through the remaining files, targeting files with '.jpg' or '.jpeg' extensions.
- Renames each image file by assigning a new filename composed of a sequential number (starting at 912) and appending '_t' before the extension (e.g., '912_t.jpg').
- Here, the processed _t.jpg indicates a progressive image, while .jpg indicates a baseline image.
- Skips files with '.py' extensions or unsupported file types without modifying them.

The script avoids renaming Python scripts and preserves non-target files. The original filenames are assumed to be directly accessible in the working directory (i.e., no subdirectories handled).
"""



import os
path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/qutubcomplex/train_2/5'
files=os.listdir(path)
files.sort()
files.remove("bulk_rename.py") #removing the script from the directory


i=912
    
for file in files:
    src=file
    print(file)
    if file.find(".py") != -1:
        print("You have a python file in the directory, please remove it or keep it outside the directory")
        pass
    elif file.find(".jpg") != -1:
        dst=""+str(i)+"_t.jpg"
        os.rename(src,dst)
        i+=1
    elif file.find(".jpeg") != -1:
        dst=""+str(i)+"_t.jpeg"
        os.rename(src,dst)
        i+=1
    else:
        pass

    
    
    
    