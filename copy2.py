import shutil
import os
import glob

dir_path='E:\\Imagesforscan\\images1'
dir_path2='E:\\folder1'

folder_elements = glob.iglob('E:\Imagesforscan/**/*', recursive=True)

#for file in :
#    if file in os.listdir(dir_path2):
#        print(file+"exists")
#    elif file not in os.listdir(dir_path2):
#        full_file_name = os.path.join(dir_path, file)
#        if os.path.isfile(full_file_name):
#            shutil.copy(full_file_name, dir_path2)
#    else:
#        break
    
for file in folder_elements:
    if file in os.listdir(dir_path2):
        print(file+"exists")
    elif file not in os.listdir(dir_path2):
        full_file_name = os.path.join(dir_path, file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dir_path2)
    else:
        break
    
