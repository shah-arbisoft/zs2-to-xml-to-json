# zs2-to-xml-to-json

This repository contains some scripts which are mainly related to the extraction and transformation of high resolution and metadata from `zs2` files. 

----

## Content

1. manual_scripts: Folder with manual scripts, to extract information from the zs2 files
2. automated_scripts: Folder with small automation (folder watch, file conversion, transformation), to extract information from the zs2 files
3. docs: docs about the json paths - how shall the txt file look like
4. drafts: first steps with the zs2decode library


----

## File Converter

The file converter script was build with the help of the [zs2decode library](https://github.com/cpetrich/zs2decode) and converts multiple `zs2` files. Initially the `zs2` file is converted to an `xml` file which can be already used. The second step is the conversion of the `xml` file to a `json` file. The `json` file is used within the transformation script, to get mandatory metadata and high resolution data for further tasks like visualization or analytics. 


----

## JSON Data Transformation

The main step within the transformation script is the selection of the necessary keys and values.
Therefore a text file with the definition of the `json` path is necessary, which is described as the following:  

```text
Document.Header.Name.@value
Document.Header.Kommentar.Text.@value
Document.Header.SeriesName.@value
Document.Body.batch.Guid.@value
Document.Body.batch.EventsDef.EventDefinitions.Elem[].Guid.@value
Document.Body.batch.Series.Guid.@value 
Document.Body.batch.Series.SeriesElements.Elem[].Guid.@value
```

Based on the Definition Input and the `json` File the elements will be extracted and saved as a modified `json` file.


----

## JSON Format Output 

Based on the Definition Input and the `json` File the elements will be extracted and saved as a modified `json` file.
The structure of the initial `json` file will be kept, not necessary paths and data will be dropped and the final `json` file will be stored in the `modified_json` folder. This output can be used as a raw data input for further processing. 


---- 

## Folder watch for automation 

For watching a folder with zs2 files and convert them directly after a new file is inside the folder, the automated script can be used. 
Therefore only the `watcher.py` needs to be started and the script will convert `zs2` files which are located at the folder `zs2_files`. If there are already `json` files available which need to be transformed, they need to be stored inside the `json_files` folder. If that is not the case, the `watcher.py` script will store the extracted json inside the `json_files` folder and afterwards they will get transformed. 


----

## Repository Information

### Special thanks

The Conversion Script was built based on the [zs2decode library](https://github.com/cpetrich/zs2decode) with the following documentation at [zs2decode library documentation](https://zs2decode.readthedocs.io/en/latest/). Many thanks for sharing these great library!