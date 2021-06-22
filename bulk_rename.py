import os
path = '/home/lepotatoguy/pjpeg/Scan 1 (copy)/dataset-final/total (copy)'
files=os.listdir(path)
#print(files)
files.sort()
files.remove("bulk_rename.py")
files.remove("bulkdatasetrun.py")
files.remove("script.txt")
files.remove("script_final.txt")
print(files)


i=912
# try:
#     for file in files:
#         src=file
#         if file.find(".py") != -1:
#             print("ekhanei problem")
#             pass
#         elif file.find(".jpg") != -1:
#             dst=""+str(i)+".jpg"
#             os.rename(src,dst)
#             i+=1
#         elif file.find(".jpeg") != -1:
#             dst=""+str(i)+".jpeg"
#             os.rename(src,dst)
#             i+=1
#         else:
#             pass
# except (FileNotFoundError, IOError):
#     print("pera dicche")
    
for file in files:
    src=file
    print(file)
    if file.find(".py") != -1:
        print("ekhanei problem")
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

    
    
    
    