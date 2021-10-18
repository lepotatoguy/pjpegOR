import subprocess
import time
startTime = time.time()

print("Let the game begin.")

f = open('readme.txt')

arr = f.readlines()

import os

for name in arr:
            idx = arr.index(name)
            print(str(idx) + " out of " + str(len(arr)))
            name = name.strip('\n')
            print(name)
            # name = name[:-4] # I don't know why it was working with -4 but in dataset, it works with -5. it removes the .jpg part
            name = name[:-5]
            name_t = name+"_t.jpg" #progressive
            name_m = name+".jpg" #normal
            subprocess.call(["jpegtran", "-optimize", "-progressive", "-scans", "script.txt", "-outfile", name_t, name_m])
            print(name + " Done.")        

print("All Done.")
time_final = time.time() - startTime
print("Time took: "+str(time_final) + " seconds")
