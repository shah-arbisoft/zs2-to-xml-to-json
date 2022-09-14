from ntpath import join
import time
import os
import shutil

from dotenv import load_dotenv
from helpers import create_path_folders_if_not_exist


load_dotenv()  # load all environmental variables


def get_current_files(folder_path):
    os.chdir(folder_path)
    listed_files = os.listdir(folder_path)
    os.chdir(BASE_DIR)
    return listed_files



def unzip_folder():
    folder_path = os.path.join(BASE_DIR, *(os.getenv('ARCHIVE_PATH').split('/')))
    try:
        shutil.unpack_archive(filename=f'{folder_path}.zip', extract_dir=folder_path, format='zip')
    except:
        pass
    
def move_file_to_respective_archive_folder(file):
    file_type = file.split(".")[-1]
    if file_type == 'json':
        move_from = full_path_for_json_files
        move_from_2 = os.path.join(os.getenv('MODIFIED_JSON_SAVE_PATH'), file)
        eko = 'modified_json'

    else:  # zs2
        move_from = full_path_for_zs2_files
        move_from_2 = os.path.join('xml_files', file.replace('zs2', 'xml'))
        eko = 'xml'

    move_from = os.path.join(move_from, file)
    archive_path = os.getenv('ARCHIVE_PATH')
    hehe = [BASE_DIR, *archive_path.split('/'), f'{file_type}_files']

    to_move = os.path.join(*hehe)
    hehe[-1] = eko
    to_move_1 = os.path.join(*hehe)


    os.makedirs(to_move, exist_ok=True)
    os.makedirs(to_move_1, exist_ok=True)

    to_move = os.path.join(to_move, file)
    to_move_1 = os.path.join(to_move_1, file)

    shutil.move(move_from_2, to_move_1)
    shutil.move(move_from, to_move)



def zip_folder():
    folder_path = os.path.join(BASE_DIR, os.getenv('ARCHIVE_PATH'))
    shutil.make_archive(folder_path, 'zip', folder_path)


def clean_space():
    archive_full_path = os.path.join(BASE_DIR, *(os.getenv('ARCHIVE_PATH').split('/')))
    shutil.rmtree(archive_full_path, ignore_errors=True)
    shutil.rmtree(os.path.join(BASE_DIR, 'xml_files'), ignore_errors=True)


if __name__ == '__main__':
    BASE_DIR = os.getcwd()

    json_files_path = os.getenv('JSON_FILES_PATH')
    zs2_files_path = os.getenv('ZS2_FILES_PATH')

    full_path_for_json_files = os.path.join(BASE_DIR, json_files_path)
    full_path_for_zs2_files =  os.path.join(BASE_DIR, zs2_files_path)

    create_path_folders_if_not_exist(full_path_for_json_files)
    create_path_folders_if_not_exist(full_path_for_zs2_files)

    while True:
        time.sleep(5)
        
        current_json_files = get_current_files(full_path_for_json_files)
        current_zs2_files = get_current_files(full_path_for_zs2_files)

        if current_json_files:
                print('new json files added are ')
                print(current_json_files)

        if current_zs2_files:
                print('new zs2 files added are ')
                print(current_zs2_files)

        added_files = current_json_files + current_zs2_files
        for file in added_files:
            os.system(f'python main.py {file}')

            unzip_folder()
            move_file_to_respective_archive_folder(file)
            zip_folder()
            clean_space()

