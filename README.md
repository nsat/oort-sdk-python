# oort-sdk-client
Client interface to the OORT agent.

- API version: 1.3
- Package version: 1.0.0
For more information, please visit [https://developers.spire.com/oort-docs/index.html](https://developers.spire.com/oort-docs/index.html)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import oort_sdk_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import oort_sdk_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import oort_sdk_client
from oort_sdk_client.rest import ApiException
from pprint import pprint



# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)
    adcs_command_request = oort_sdk_client.AdcsCommandRequest() # AdcsCommandRequest | The file and parameters for sending

    try:
        api_response = api_instance.command_adcs(adcs_command_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SdkApi->command_adcs: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:2005/sdk/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SdkApi* | [**command_adcs**](docs/SdkApi.md#command_adcs) | **POST** /adcs | 
*SdkApi* | [**get_adcs**](docs/SdkApi.md#get_adcs) | **GET** /adcs | 
*SdkApi* | [**get_tfrs**](docs/SdkApi.md#get_tfrs) | **GET** /tfrs | 
*SdkApi* | [**query_available_files**](docs/SdkApi.md#query_available_files) | **GET** /query_available_files/{topic} | 
*SdkApi* | [**retrieve_file**](docs/SdkApi.md#retrieve_file) | **POST** /retrieve_file | 
*SdkApi* | [**send_file**](docs/SdkApi.md#send_file) | **POST** /send_file | 


## Documentation For Models

 - [AdcsCommandRequest](docs/AdcsCommandRequest.md)
 - [AdcsCommandResponse](docs/AdcsCommandResponse.md)
 - [AdcsEulerT](docs/AdcsEulerT.md)
 - [AdcsHk](docs/AdcsHk.md)
 - [AdcsQuatT](docs/AdcsQuatT.md)
 - [AdcsResponse](docs/AdcsResponse.md)
 - [AdcsTarget](docs/AdcsTarget.md)
 - [AdcsXyzFloatT](docs/AdcsXyzFloatT.md)
 - [AvailableFilesResponse](docs/AvailableFilesResponse.md)
 - [DeliveryHints](docs/DeliveryHints.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [FileInfo](docs/FileInfo.md)
 - [RetrieveFileRequest](docs/RetrieveFileRequest.md)
 - [SendFileRequest](docs/SendFileRequest.md)
 - [SendFileResponse](docs/SendFileResponse.md)
 - [SendOptions](docs/SendOptions.md)
 - [TTLParams](docs/TTLParams.md)
 - [TfrsResponse](docs/TfrsResponse.md)


