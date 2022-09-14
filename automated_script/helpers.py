""" Helper functions for the script"""

import os
from pathlib import Path


def get_filename(zs2_filename: str, ext: str, save_location_folder_name: str=''):
    """
    Creates a folder with given extension name if "save_location_folder_name" is not provided or 
    folder not already exist. Generates a new filename with given extension instead of ZS2 and 
    return the full relative path. New folder is created in same directory where the the main.py is.
    eg for a zs2 file with extension = json:
        ./folder/file.zs2 -> ../json_output/file.json
    """
    _, basename = os.path.split(zs2_filename)
    filename = basename.split(".")
    save_location_folder_name = save_location_folder_name or f'./{ext[1:]}_files'

    if not os.path.exists(save_location_folder_name):
        os.makedirs(save_location_folder_name)
    filename = save_location_folder_name + os.sep + "".join(filename[:-1]) + ext
    return filename


def get_files_in(directory: str, file_extension: str):
    """
    return a list of all files which matches the extension type in a given directory

    Args:
        directory      : path of given directory containing the input files
        file_extension : extension type to consider files only with matching extension   
    """
    files = []
    for entry in os.scandir(directory):
        if entry.is_file():
            if entry.name.endswith(file_extension):
                files.append(entry.path)
        elif entry.is_dir():
            files.extend(get_files_in(entry.path, file_extension))
    return files


def split_list_into_equal_n_lists_of_values(given_list, n):
    """ Split a given list into N equivalent lists where values from original list is distributed among the n lists
    
    Args:
        given_list : List to be devided into N pieces
        n : It represents the number of pieces the list should be sliced into 

        """
    k, m = divmod(len(given_list), n)
    return list(given_list[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def create_path_folders_if_not_exist(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    