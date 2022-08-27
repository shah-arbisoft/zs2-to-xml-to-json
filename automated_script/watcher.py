import time
import os

def do_something():
    pass

def get_current_files(folder_path):
    os.chdir(folder_path)
    listed_files = os.listdir(folder_path)
    os.chdir(BASE_DIR)
    return listed_files


if __name__ == '__main__':
    BASE_DIR = os.getcwd()
    full_path_for_json_files = os.path.join(BASE_DIR,'json_files')
    full_path_for_zs2_files =  os.path.join(BASE_DIR,'zs2_files')

    json_files = get_current_files(full_path_for_json_files)
    zs2_files = get_current_files(full_path_for_zs2_files)

    while True:
        time.sleep(5)
        added_files = []
        
        current_json_files = get_current_files(full_path_for_json_files)
        current_zs2_files = get_current_files(full_path_for_zs2_files)
        
        
        if json_files != current_json_files:
            added_files = [x for x in current_json_files if x not in json_files]
            if added_files:
                print('new json files added are : ')
                print(added_files)
            json_files = current_json_files

        if zs2_files != current_zs2_files:
            added_files = [x for x in current_zs2_files if x not in zs2_files]
            if added_files:
                print('new zs2 files added are ')
                print(added_files)
            zs2_files = current_zs2_files

        added_files = ",".join(added_files)
        if added_files:
            os.system(f'python main.py {added_files}')
            
