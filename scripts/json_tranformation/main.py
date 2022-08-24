import helpers
from json_extractor import JsonPathExtractor


def perform_json_path_extraction(file_name: str):
    json_extractor_object = JsonPathExtractor(file_name)
    json_extractor_object.extract_data_from_json()


if __name__ == '__main__':
    """

    """
    SELECTED_DIR = 'scripts\json_tranformation\json_files'
    # get all files available in a directory
    files = helpers.get_files_in(SELECTED_DIR, '.json')

    for file in files:
        try:
            print(f"Started  JSON Path Extraction  =======>> {file}")
            perform_json_path_extraction(file)
            print(f"Completed ======>> {file}")
        except:
            print(f"Failed ======>> {file}")

