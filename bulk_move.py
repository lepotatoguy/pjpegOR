import shutil
import os
path = '/home/joyanta/test/'
files=os.listdir(path)
# print(files)

source = "/home/joyanta/test/"
destination_jpg = "/home/joyanta/original"
destination_pjpeg = "/home/joyanta/pjpeg"


for file in files:
    print(file)
    name = file[-6:] #getting the extension if it is jpeg or pjpeg
    if name == "_t.jpg":
        new_path = os.rename(os.path.join(source,file), os.path.join(destination_pjpeg,file))
        print(new_path)
    elif file.find(".py") != -1:
        pass
    elif file.find(".txt") != -1:
        pass
    else:
       new_path = os.rename(os.path.join(source,file), os.path.join(destination_jpg,file))
       print(new_path) 



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