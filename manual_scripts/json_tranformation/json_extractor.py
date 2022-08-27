import copy
import json
import os

import threading
import helpers


class JsonPathExtractor():

    def __init__(self, name: str='', json_path_file_name: str='', data: json=None):
        """
        Initialize the class

        Args:
            name: Name of the Json file
            json_path_file_name: Name of the file which contains all json paths, needs to be extracted  
            data: Data for the json file
        """

        self.output_data = {}
        self.file_name = name
        self.data = data or self.load_data_from_json_file()
        self.json_extractor_paths = self.get_json_path_rules(json_path_file_name)
        self.save_path = helpers.get_filename(name, '.json', 'modified_json')


    def load_data_from_json_file(self, file_name: str = ''):
        """
        Loads data from given json file and return it as json data.

        Args:
            file_name: Name of the file from data json data is to be loaded.
        
        Returns:
            json: Return the data as json. 
        """
        file_name = file_name or self.file_name
        file_path = os.path.abspath(os.getcwd()) + os.sep + file_name

        with open(file_path) as f:
            return json.load(f)

    def get_json_path_rules(self, file_name):
        file_name = file_name or 'json_paths'
        with open(f"{file_name}.txt", "r") as f:
            return  [line.strip() for line in f.readlines()]


    def get_list_of_all_matched_keys(self, key_name: str, json_data: json):
        """
        Gather all the keys available in json_data for given key name.
        Suppose we have a key_name "Elems[]" then it will return list of all available Elems0 to Elems[N].

        Args:
            key_name: Element key_name
            json_data: Source of data from which keys to be found

        Returns:
            list: list of available numbered key_names from source json_data
        """
        key_name = key_name.split('[]')[0]
        list_of_keys = list(json_data)

        return [key for key in list_of_keys if key_name in key]


    def change_value_to_list_of_float_if_key_is_data_array(self, key: str, value: str):
        """
            Convert value to list of float if key is equal to "DataArray".
            
            Args:
                key: String to be checked if Keu is equal to "DataArray" or not.
                value: String to be converted to list of float values.
            
            Returns:
                list/str: list of float values if converted else return the same value as it is.
        """
        if key == 'DataArray':
            value = value[1:-1]  # remove "[" and "]" from string value
            if value:
                value = value.split(',')  # change string to list of string values
                return [float(x) for x in value]  # return list after changing it's values type from str to float
            return []
        return value


    def follow_path_and_set_value(self, list_of_keys: list, val: str):
        """
        Parse the last key by following all the keys for the current json data and place this value for the last key.

        Args:
            list_of_keys: list of keys where last key will be set equal to given "val"
            val: Value to be set to last key from list of keys
        """
        temp_output = self.output_data

        for key in list_of_keys[:-1]:  # ignoring last key for this loop
            if key not in temp_output:  # if key is not created in temp_json then create this key
                temp_output[key] = {}   # and set it to empty dict
            temp_output = temp_output[key]

        required_key_for_current_value = list_of_keys[-1]
        val = self.change_value_to_list_of_float_if_key_is_data_array(required_key_for_current_value, val)
        temp_output[required_key_for_current_value] = val


    def extract_single_keys_path_from_data(self, keys_list: list, original_data: json, pre_keys: list=[]):
        """
        In our new json data, Create this same path with all keys: values from the original json data. 

        Args:
            keys_list: list of keys which represents the json path to be extracted.
            data: the original json data from where data will be extacted
            pre_keys: sometimes previous keys are also need which are then appened before to keys_list.
        """
        value = self.get_value_from_data(keys_list, original_data, pre_keys)
        if value:                                                        #  if key exist in original json data then in new modified json, create path,
            self.follow_path_and_set_value(pre_keys + keys_list, value)  #  follow it and place the value for the last key.


    def get_value_from_data(self, keys: list, data: json, pre_keys: list=[]):
        """
        Parse through path by using these keys on original json data to access the value for @value.
        If any of the key has [] in it then it will find all available numbered matched keys for it and create
        multiple parts for it.
        For example:
        we have a path: Document.Body.Elem[].Guid.@value and we have Elem1, Elem2 and Elem3 keys available in source json data.
        the it will follow 3 paths from it such as:
            path1: Document.Body.Elem1.Guid.@value
            path2: Document.Body.Elem2.Guid.@value
            path3: Document.Body.Elem3.Guid.@value

        Args:
            keys: A path is splitted into list of keys. such as "Document.Body" -> ["Document", "Body"]
            data: the original json data from where data will be extacted
            pre_keys: sometimes previous keys are also need which are then appened before to keys_list.

        Returns:
            str: value of key where key is "@value"

        """
        parsed_all_keys = True
        copy_data = copy.deepcopy(data)
        for key_name in keys:
            if '[]' in key_name:
                list_of_available_numbered_keys = self.get_list_of_all_matched_keys(key_name, copy_data)
                current_key_index = keys.index(key_name)
                previous_keys = pre_keys + keys[: current_key_index]

                for key in list_of_available_numbered_keys:
                    current_numbered_key_index = keys.index(key_name)
                    following_keys = keys[current_numbered_key_index+1: ]
                    new_keys = [key] + following_keys
                    self.extract_single_keys_path_from_data(new_keys, copy_data, previous_keys)

                parsed_all_keys = False
                break

            else:
                if not copy_data.get(key_name):
                    with open('unfound_paths.txt', 'a') as file:
                        file.write('.'.join(keys) + '\n')
                    return
                copy_data = copy_data.get(key_name)
        
        if parsed_all_keys:
            return copy_data.get('@value')


    def extract_required_json_data(self, json_paths: list, data: json):
        """
        Extract required json paths data from given data dict.

        Args:
            json_paths: List of json paths for which data is needed to be extracted from the original json data
            data: Original data dict from where data will be extracted
        """
        for path in json_paths:
            print(path)
            keys = path.split('.')[:-1]  # -1 for ignoring @value from keys
            self.extract_single_keys_path_from_data(keys, data)


    def create_and_start_threads_to_perform_extraction(self, required_json_paths: list):
        """ 
        Create and start N threads where N is equal to N number of lists of required json_paths.
        
        Args:
            required_json_paths: List of lists where each list contain some json_paths.
        """
        threads = []
        for paths_list in required_json_paths:
            thread = threading.Thread(target=self.extract_required_json_data, args=(paths_list, self.data))
            thread.start()
            threads.append(thread)

        return threads

    


    def wait_for_all_threads_to_complete(self, threads: list):
        """ 
        Wait for all the threads to complete their job so required json data is 
        gathered before writing it to file.

        Args:
            threads: List of threads
        """
        [x.join() for x in threads]

    
    def save_this_modified_json_data_to_file(self, save_path: str=''):
        save_path = save_path or self.save_path
        with open(save_path, 'w') as f:
            f.write(json.dumps(self.output_data))


    def extract_data_from_json(self):
        """
        Extract Json data from the original Json file based on the Json Paths provided in a file(json_path_file_name).
        Exactly 8 threads will be used for this job to complete such as we have 80 json data paths tp extract then 8 threads
        will be created where each thread will work on 10 paths to extact. And after each thread finishes, all data extracted
        then it is written to a file.
        """
        list_of_required_json_paths = helpers.split_list_into_equal_n_lists_of_values(self.json_extractor_paths, 8)
        all_threads = self.create_and_start_threads_to_perform_extraction(list_of_required_json_paths)  
        self.wait_for_all_threads_to_complete(all_threads)
        self.save_this_modified_json_data_to_file()

