import os
import sys
from jsonScript import Json
from json_extractor import JsonPathExtractor
from xmlScript import Xml

from dotenv import load_dotenv


load_dotenv()

def zs2_file_to_xml_and_json_file(file_name: str):
    try:
        print(f"Started ZS2 to JSON conversion  =======>> {file_name}")
        file_name = os.path.join(os.getenv('ZS2_FILES_PATH'), file_name)
        xml_object = Xml(name=file_name)
        xml_object.zs2_file_to_xml_file(file_name)
        xml_data = xml_object.get_data()

        json_object = Json(name=file_name)
        json_object.xml_data_to_json_file(xml_data)
        print(f"Completed ======>> {file}")

    except:
            print(f"Failed ======>> {file_name}")


def perform_json_path_extraction(file_name: str):
    try:
        print(f"Started  JSON Path Extraction  =======>> {file_name}")
        file_name = os.path.join(os.getenv('JSON_FILES_PATH'), file_name)
        json_extractor_object = JsonPathExtractor(file_name)
        json_extractor_object.extract_data_from_json()
        print(f"Completed ======>> {file}")

    except:
            print(f"Failed ======>> {file_name}")


def get_required_function_for_file(file):
    file_extension = file.split('.')[-1]
    if file_extension == 'json':
        return perform_json_path_extraction
    elif file_extension == 'zs2':
        return zs2_file_to_xml_and_json_file
    return None


if __name__ == '__main__':
    """

    """
    files = sys.argv[1]
    files = files.split(',')
    operation_function = get_required_function_for_file(files[0])
    if files and operation_function:
        for file in files:
            operation_function(file)
    
    