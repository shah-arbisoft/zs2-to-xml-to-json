""" Helper functions for the script"""

import os

def get_filename(zs2_filename: str, ext: str):
    """
    Creates a folder with given extension name if not already exist. Generates a new filename 
    with given extension instead of ZS2 and return the full relative path. New folder is created
    in same directory where the the main.py is.
    eg for a zs2 file with extension = json:
        ./folder/file.zs2 -> ../json_output/file.json
    """
    _, basename = os.path.split(zs2_filename)
    filename = basename.split(".")
    dir_name = f'./{ext[1:]}_files'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    filename = dir_name + os.sep + "".join(filename[:-1]) + ext
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