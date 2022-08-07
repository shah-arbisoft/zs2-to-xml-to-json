import json
import os
from xml.etree.ElementTree import fromstring

import pandas as pd
import zs2decode.parser
import zs2decode.util
from xmljson import badgerfish as bf
from pandas import json_normalize
import datetime


# TODO: make script more modular (REUSABILITY!):
#   one script for conversion from zs2 (only zs2 files to be considered) to xml (store xml files in another folder)
#   one script for conversion from xml to json (store json files in another folder)
#   one script for metadata extraction based on exported json file! goal is a reduced json file (each dataset from the metadata json files shall be defined in a function)


def save_xml(out_path: str, data):
    with open(out_path, 'wb') as f:
        f.write(data)


def save_json(out_path: str, json_data):
    json_data = json.dumps(json_data)
    with open(out_path, 'w') as f:
        f.write(json_data)


def zs2_to_xml(in_file: str):
    # load and decompress file
    data_stream = zs2decode.parser.load(in_file)
    # separate binary data stream into chunks
    raw_chunks = zs2decode.parser.data_stream_to_chunks(data_stream)
    # convert binary chunk data into lists of Python objects
    chunks = zs2decode.parser.parse_chunks(raw_chunks)
    # output as text file
    data = zs2decode.util.chunks_to_XML(chunks)
    return data


def xml_to_json(xml_filepath: str):
    with open(xml_filepath) as f:
        xml = f.read()
    return bf.data(fromstring(xml))


def findelements(series_elements):
    # get all series elements
    elements = []
    for c in range(series_elements["Count"]["@value"]):
        if series_elements[f"Elem{c}"]:
            ele = series_elements[f"Elem{c}"]
            if "SeriesElements" in ele.keys():
                new_series = ele.pop("SeriesElements")
                elements.extend(findelements(new_series))
            elements.append(ele)
    return elements


# ----------------------------------------------------------------------------------------------------------------------
def get_files_in(directory: str):
    # TODO: only list files with extension ".zs2" 

    """
    return a list of all files in a given directory
    """
    files = []
    for entry in os.scandir(directory):
        if entry.is_file():
            files.append(entry.path)
        elif entry.is_dir():
            files.extend(get_files_in(entry.path))
    return files


def unix_time_readable(t: float, date_delim: str = "/", time_delim: str = ":"):
    return datetime.datetime.fromtimestamp(t).strftime(
        f'%d{date_delim}%m{date_delim}%Y_%H{time_delim}%M{time_delim}%S')


def get_metadata(json_data, first_elem_index: int):
    # Document/Body/batch/Series/SeriesElements/Elem0/EvalContext/ParamContext/ParameterListe/Elem106/QS_TextPar
    data = json_data["Document"]["Body"]["batch"]["Series"]["SeriesElements"][
        f"Elem{first_elem_index}"]["EvalContext"]["ParamContext"][
            "ParameterListe"]["Elem106"]["QS_TextPar"]
    metadata = data.get('@value', None)

    # type_ = data.get('@type', None)

    if metadata is not None:
        metadata = metadata.split(",")
        metadata = metadata[1][2:-1]
        return metadata
    return "nil"


def all_possible_metadata_fom_json(json_data):
    array = []
    i = 0
    while 1:
        try:
            array.append(get_metadata(json_data, i))
            i += 1
        except KeyError:
            break
    return [i for i in array if i != '']


def get_filename(zs2_filename: str, ext: str):
    """
    generates a new filename with the same path but different extension
    eg. ./folder/file.zs2 -> ./folder/file.json
    """
    dirname, basename = os.path.split(zs2_filename)
    filename = basename.split(".")
    filename = dirname + os.sep + "".join(filename[:-1]) + ext
    return filename


# ----------------------------------------------------------------------------------------------------------------------


def get_data(zs2_file_path: str) -> pd.DataFrame:
    print(f"procesing file: {zs2_file_path}")
    json_file = get_filename(zs2_file_path, ".json")

    xml_data = zs2_to_xml(zs2_file_path)
    json_data = bf.data(fromstring(xml_data))

    # save xml_data and json_data to disk
    save_json(json_file, json_data)
    save_xml(get_filename(zs2_file_path, ".xml"), xml_data)

    # define all necessary JSON Paths for Series Data Extraction
    document = json_data["Document"]
    body = document["Body"]
    batch = body["batch"]
    series = batch["Series"]
    document = json_data["Document"]["Body"]["batch"]["Series"]
    # normalize series elements
    series_elements = series["SeriesElements"]
    series_elements_df = json_normalize(series_elements)
    elements = findelements(series_elements)

    series_elements_all = pd.json_normalize(elements)
    series_elements_all = series_elements_all[~series_elements_all['@value'].
                                              str.contains("batch.TSpecimen")]

    # drop all columns with unique values
    nunique = series_elements_all.nunique()
    cols_to_drop = nunique[nunique == 1].index
    series_elements_all = series_elements_all.drop(cols_to_drop, axis=1)

    # drop all values with nan values
    series_elements_all = series_elements_all.dropna(axis=1, how='all')

    # reset index of dataframe
    series_elements_all = series_elements_all.reset_index()

    # drop last row of dataframe
    series_elements_all = series_elements_all[:-1]

    # get the concrete data from the dataframe
    #or row in series_elements_all.iterrows():

    # NOTE first element index is always set to zero.
    #metadata = get_metadata(json_data, first_elem_index=0)
    metadata = all_possible_metadata_fom_json(json_data)
    if isinstance(metadata, list):
        for d in metadata:
            print(d)
    elif isinstance(metadata, str):
        print(metadata)
    
    values = pd.DataFrame(
        {
            "y":
            series_elements_all[
                'RealTimeCapture.Trs.SingleGroupDataBlock.DataChannels.Elem0.DataArray.@value'],
            "x":
            series_elements_all[
                'RealTimeCapture.Trs.SingleGroupDataBlock.DataChannels.Elem1.DataArray.@value'],
            "metadata":
            metadata
        },
        columns=['y', 'x', "metadata"])

    return values



def get_data_from_list(files_list: str) -> list:
    """
    returns a list of pandas DataFrames
    """
    return [get_data(file) for file in files_list if file.endswith(".zs2")]




if __name__ == '__main__':
    """
    # get data from a single file
    data = get_data("./file3.zs2")
    """
    
    # get data from all files in a directory
    files = get_files_in("./")
    print(files)

    df_final = None 

    # TODO: Resolve issue with Value Error in Script: "Array has less values"
    try:
        for i in files:
            df_final = get_data(i)
            df_final
    except ValueError:
        pass  # do nothing!