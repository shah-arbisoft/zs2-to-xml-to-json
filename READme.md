# zs2-to-xml-to-json

This repository contains some scripts which are mainly related to the extraction and transformation of high resolution and metadata from `zs2` files. 

----

## File Converter

The file converter script is located in `scripts/file_conversion`. The script was build with the help of the [zs2decode library](https://github.com/cpetrich/zs2decode) and converts multiple `zs2` files. Initially the `zs2` file is converted to an `xml` file which can be already used. The second step is the conversion of the `xml` file to a `json` file. The `json` file is used within the transformation script, to get mandatory metadata and high resolution data for further tasks like visualization or analytics. 

----

## JSON Data Transformation


to be defined and described


----

## JSON Format Output 

to be defined and described



----

## Repository Information

### Special thanks

The Conversion Script was built based on the [zs2decode library](https://github.com/cpetrich/zs2decode) with the following documentation at [zs2decode library documentation](https://zs2decode.readthedocs.io/en/latest/). Many thanks for sharing these great library!