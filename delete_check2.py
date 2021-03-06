import shutil
from os import path, scandir, remove
from queue import Queue
from threading import Thread
import numpy as np


from tqdm import tqdm

# Number of threads to execute
NO_OF_THREADS = 4
queue_objects = [Queue() for i in range(NO_OF_THREADS)]

src_list=[]
dst_list=[]

# TODO File copy code with all exceptions
def copy_data(q):
    '''
    Take source destination from queue and copy to the given destination 

    Args:
            q(queue): Single queue containing source path of files

    Returns:
            None
    '''
    pbar = tqdm(total=q.qsize(), position=0, leave=True)
    while not q.empty():
        image_path, dest_path = q.get()
        shutil.copy(image_path, dest_path)
        pbar.update(1)
    pbar.close()


#  Read all folders recursively
def read_folders(data_dir, destination_dir):
    
    folder_elements = scandir(data_dir)
    counter = 0
    # reading all sub-folders of the dataset & tqdm is used for creating a progress bar
    for element in folder_elements:
        element_path = path.join(data_dir, element.path)

        destination_path = path.join(destination_dir)

        if element.is_file() and element_path[-4:] in ['.jpg', '.png', '.bmp']:
            queue_objects[counter % NO_OF_THREADS].put(
                (element_path, destination_path))
            counter += 1
            src_list.append(element.name)

        elif element.is_dir():
            read_folders(element_path, destination_path)
            
            
#  reading the destination files
def read_destination_files(destination_dir):
    folder_elements = scandir(destination_dir)
    for element in folder_elements:
        dst_list.append(element.name)
        
#  checking if source file is deleted if any
def source_check():
    diff_list = np.setdiff1d(dst_list,src_list)
    print("The file named" ,diff_list, "is deleted from source")
    


def sync_source_destination(destination_dir):
    folder_elements = scandir(destination_dir)
    for element in folder_elements:
        if element.name not in src_list:
            delete_from_destination(element.path)
            
            



#  Reading the full path and deleting the file present in the path
def delete_from_destination(path_name):
    file_path = path.join(path_name)
    remove(file_path)
    print("file named", file_path, "is deleted")


if __name__ == '__main__':
    dataset_folder = r"E:\folder1"
    destination_dir = r"E:\folder2"
    
    #dest_img_path=r"#"

    read_folders(dataset_folder, destination_dir)
    
    # Start n separate threads
    #for obj in queue_objects:
        #Thread(target=copy_data, args=(obj,)).start()
        
    # Calling delete function    
    #delete_from_destination(dest_img_path)
    
    read_destination_files(destination_dir)
    #source_check()
    sync_source_destination(destination_dir)
    
