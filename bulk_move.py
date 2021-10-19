import shutil
import os
import PIL
import subprocess
import time

startTime = time.time()
failed_file = []

# source = "/home/joyanta/test/"
# destination_jpg = "/home/joyanta/original"
# destination_pjpeg = "/home/joyanta/pjpeg"
# destination_failed_pjpeg = "/home/joyanta/failed_pjpeg"

source = "/home/joyanta/pjpeg/main_test/"

files=os.listdir(source)
files.sort()


destination_jpg = "/home/joyanta/pjpeg/original"
destination_pjpeg = "/home/joyanta/pjpeg/pjpeg"
destination_failed_pjpeg = "/home/joyanta/pjpeg/failed_pjpeg"






#Need to create the folder earlier so that the nobabs can enter




for file in files:
    try:

            idx = files.index(file)
            print(str(idx) + " out of " + str(len(files)-1))
            print(file)

                #Firstly moving files which can't be transferred in pjpeg
            img_size = os.path.getsize(os.path.join(source,file))
            if(img_size == 0):
                failed_file.append(file)
                name = file[:-4]
                name_m = name+".jpg"
                new_path = os.rename(os.path.join(source,name_m), os.path.join(destination_failed_pjpeg,name_m))
                print(os.path.join(destination_failed_pjpeg,name_m))
                continue
            else:
                # print(file)
                name = file[-6:] #getting the extension if it is jpeg or pjpeg
                if name == "_t.jpg":
                    new_path = os.rename(os.path.join(source,file), os.path.join(destination_pjpeg,file))
                    print(new_path)
                elif file.find(".py") != -1:
                    pass
                elif file.find(".txt") != -1:
                    pass
                else:
                    name = file[:-4]
                    name_t = name+"_t.jpg"
                    img_size_t = os.path.getsize(os.path.join(source,name_t))
                    if(img_size_t == 0): #matching file that has faulty pjpeg, will stay in the main folder
                        pass
                    else: #if normally transforms pjpeg, then normally move
                        new_path = os.rename(os.path.join(source,file), os.path.join(destination_jpg,file))
                        print(new_path) 

    except FileNotFoundError as e:
        continue

for file in failed_file:
    with open('failed_pjpeg_list.txt', 'a+') as f:
        f.writelines("%s \n" %(file))
        f.flush()
        # print(file)

print("All Done.")
time_final = time.time() - startTime
print("Time took: "+str(time_final) + " seconds")


#Alternative

#Need to create the folder earlier so that the nobabs can enter

# for file in files:
#     print(file)
#     name = file[-6:] #getting the extension if it is jpeg or pjpeg
#     if name == "_t.jpg":
#         new_path = os.rename(os.path.join(source,file), os.path.join(destination_pjpeg,file))
#         print(new_path)
#     elif file.find(".py") != -1:
#         pass
#     elif file.find(".txt") != -1:
#         pass
#     else:
#        new_path = os.rename(os.path.join(source,file), os.path.join(destination_jpg,file))
#        print(new_path) 