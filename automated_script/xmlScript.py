import os
import helpers

from zs2decode import parser, util
from dotenv import load_dotenv


load_dotenv()

class Xml:

    def __init__(self, name='', data=None):
        self.file_name = name
        self.data = data
        self.save_path = helpers.get_filename(name, '.xml', os.getenv('XML_FILES_PATH'))

    def get_data(self) -> str:
        """ Getter for getting xml data of current xml file. """
        return self.data

    def get_file_name(self) -> str:
        """ Getter for getting xml file name. """
        return self.file_name
    
    def get_file_path(self) -> str:
        """ Getter for getting relatve save location path of current xml file. """
        return self.save_path

    def zs2_file_to_xml_data(self, zs2_file: str):
        """
        Read zs2 file and convert it into XML data and set it to self.data attribute.

        Args:
            zs2_file: relative full path of a zs2 file which needs to be converted to xml data
        """
        # load and decompress file
        data_stream = parser.load(zs2_file)
        # separate binary data stream into chunks
        raw_chunks = parser.data_stream_to_chunks(data_stream)
        # convert binary chunk data into lists of Python objects
        chunks = parser.parse_chunks(raw_chunks)
        # output as text file
        data = util.chunks_to_XML(chunks)
        self.data = data

    def save_xml_data_to_xml_file(self, data: str = '', out_path: str = ''):
        """
        Save current xml data to a xml file with path value of self.save_path.

        Args:
            data    : XML data which is to be saved to an xml file
            out_path : save location of xml file where this xml data will be saved.
        """
        out_path = out_path or self.save_path
        data = data or self.data
        with open(out_path, 'wb') as f:
            f.write(data)

        print("Saved to XML file successfully")
        

    def zs2_file_to_xml_file(self, zs2_file_path: str):
        """
        Read contents from a ZS2 file, convert it to XML data and then saved to an XML file.

        Args:
            zs2_file_path : zs2 file which is to be converted to an xml file with xml data
        """
        self.zs2_file_to_xml_data(zs2_file_path)
        self.save_xml_data_to_xml_file(self.data, self.save_path)
