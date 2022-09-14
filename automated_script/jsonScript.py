import json
import os
import helpers
from xml.etree.ElementTree import fromstring

from xmljson import badgerfish as bf
from dotenv import load_dotenv


load_dotenv()

class Json:

    def __init__(self, name='', data=None):
        """
        Initialize the class

        Args:
            name: Name of the Json file
            data: Data for the json file
        """
        self.file_name = name
        self.data = data
        self.save_path = helpers.get_filename(name, '.json', os.getenv('JSON_FILES_PATH'))

    def get_data(self) -> bf.data:
        """ Getter for getting json data of json file. """
        return self.data

    def get_file_name(self) -> str:
        """ Getter for getting json file name. """
        return self.file_name
    
    def get_file_path(self) -> str:
        """ Getter for getting relatve save location path of current json file. """
        return self.save_path

    def save_json_data_to_json_file(self, data: bf.data = '', out_path: str = ''):
        """
        Save current json data to a json file with path value of self.save_path.

        Args:
            data    : JSON data which is to be saved to json file
            outpath : Save location for json file where this json data will be saved.
        """
        out_path = out_path or self.save_path
        json_data = json.dumps(data)
        with open(out_path, 'w') as f:
            f.write(json_data)
        print("Saved to Json file successfully")

    def xml_file_to_json_data(self, xml_file: str):
        """
        Read xml file and convert it into JSON data and set it to self.data attribute.

        Args:
            xml_file: relative full path of a xml file which needs to be converted to json data
        """
        with open(xml_file) as f:
            xml_data = f.read()
        self.data = self.xml_data_to_json_data(xml_data)


    def xml_data_to_json_data(self, xml_data: str):
        """
        Convert given xml data to json data and set it to self.data attribute

        Args:
            xml_data  : XML data which is to be converted to json data
        """
        self.data = bf.data(fromstring(xml_data))

    def xml_data_to_json_file(self, xml_data, out_path=''):
        """
        Convert given xml data to json data and save it to a xml file with
        path value of self.save_path.

        Args:
            xml_data  : XML data which is to be converted and saved to a json file 
            out_path   : save location of json file where this json data will be saved.
        """
        out_path = out_path or self.save_path
        self.xml_data_to_json_data(xml_data)
        self.save_json_data_to_json_file(self.data, self.save_path)
