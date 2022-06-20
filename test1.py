from os import listdir, path, scandir, walk
from tqdm import tqdm
from threading import Thread
from queue import Queue
import shutil
import os


# Number of threads to execute
NO_OF_THREADS = 4
queue_objects = [Queue() for i in range(NO_OF_THREADS)]


# TODO File copy code with all exceptions
def copy_data(q):
    dest_path = "E:\\folder1"
    '''
    Take source destination from queue and copy to the given destination 

    Args:
            q(queue): Single queue containing source path of files

    Returns:
            None
    '''
    pbar = tqdm(total=q.qsize(), position=0, leave=True)
    while not q.empty():
        image_path = q.get()
        # copy code
        shutil.copy2(image_path,dest_path)
        pbar.update(1)
    pbar.close()



#  Read all folders recursively
def read_folders(data_dir, destination_dir):
    '''
    Read folders recursively and put files into queues

    Args:
            data_dir(str): Source path
            destination_dir(str): Destination path

    Returns:
            None
    '''
    folder_elements = scandir(data_dir)
    counter = 0
    # reading all sub-folders of the dataset & tqdm is used for creating a progress bar
    for element in folder_elements:
        element_path = path.join(data_dir, element)
        destination_path = path.join(destination_dir, element)


        if path.isfile(element_path) and element_path[-4:] in ['.jpg', '.png', '.bmp']:
            
            for i in range(0,NO_OF_THREADS+1):
                if counter % NO_OF_THREADS == i:
                    queue_objects[i].put(element_path, destination_path)
                
    
        
            #counter += 1

        elif path.isdir(element_path):
            read_folders(element_path, destination_dir)


if __name__ == '__main__':
    dataset_folder = "E:\\Imagesforscan"
    destination_dir = "E:\\folder1"
    read_folders(dataset_folder, destination_dir)

    # Start n separate threads
    for thread in queue_objects:
        Thread(target=copy_data, args=(thread,)).start()
        print(thread.qsize())
        



