# zs2-to-xml-to-json

This repository contains some scripts which are mainly related to the extraction and transformation of high resolution and metadata from `zs2` files. 

----

## File Converter

The file converter script is located in `scripts/file_conversion`. The script was build with the help of the [zs2decode library](https://github.com/cpetrich/zs2decode) and converts multiple `zs2` files. Initially the `zs2` file is converted to an `xml` file which can be already used. The second step is the conversion of the `xml` file to a `json` file. The `json` file is used within the transformation script, to get mandatory metadata and high resolution data for further tasks like visualization or analytics. 

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

to be defined and described



----

## Repository Information

### Special thanks

The Conversion Script was built based on the [zs2decode library](https://github.com/cpetrich/zs2decode) with the following documentation at [zs2decode library documentation](https://zs2decode.readthedocs.io/en/latest/). Many thanks for sharing these great library!