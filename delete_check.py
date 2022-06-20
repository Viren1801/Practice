from os import path, scandir, remove


def read_folders(data_dir):
    folder_elements = scandir(data_dir)
    counter = 0
    # reading all sub-folders of the dataset & tqdm is used for creating a progress bar
    for element in folder_elements:
        if element.is_file():
            print(element.name)
        elif element.is_dir():
            read_folders(element)
            
data_dir = r"E:\Imagesforscan"
read_folders(data_dir)
            

        
      