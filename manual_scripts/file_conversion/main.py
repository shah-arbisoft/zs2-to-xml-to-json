import helpers
from jsonScript import Json
from xmlScript import Xml




def zs2_file_to_xml_and_json_file(file_name: str):
    xml_object = Xml(name=file_name)
    xml_object.zs2_file_to_xml_file(file_name)
    xml_data = xml_object.get_data()

    json_object = Json(name=file_name)
    json_object.xml_data_to_json_file(xml_data)



if __name__ == '__main__':
    """
    # get data from a single file
    data = get_data("./file3.zs2")
    """
    
    # get data from all files in a directory
    files = helpers.get_files_in("./raw_data", '.zs2')

    for file in files:
        try:
            print(f"Started  =======>> {file}")
            zs2_file_to_xml_and_json_file(file)
            print(f"Completed ======>> {file}")
        except:
            print(f"Failed ======>> {file}")

