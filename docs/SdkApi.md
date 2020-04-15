# oort_sdk_client.SdkApi

All URIs are relative to *http://localhost:2005/sdk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_available_files**](SdkApi.md#query_available_files) | **GET** /query_available_files/{topic} | 
[**retrieve_file**](SdkApi.md#retrieve_file) | **POST** /retrieve_file | 
[**send_file**](SdkApi.md#send_file) | **POST** /send_file | 


# **query_available_files**
> AvailableFilesResponse query_available_files(topic)



### Example

```python
from __future__ import print_function
import time
import oort_sdk_client
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)
    topic = 'topic_example' # str | 

    try:
        api_response = api_instance.query_available_files(topic)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SdkApi->query_available_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic** | **str**|  | 

### Return type

[**AvailableFilesResponse**](AvailableFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_file**
> FileInfo retrieve_file(retrieve_file_request)



### Example

```python
from __future__ import print_function
import time
import oort_sdk_client
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)
    retrieve_file_request = oort_sdk_client.RetrieveFileRequest() # RetrieveFileRequest | 

    try:
        api_response = api_instance.retrieve_file(retrieve_file_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SdkApi->retrieve_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieve_file_request** | [**RetrieveFileRequest**](RetrieveFileRequest.md)|  | 

### Return type

[**FileInfo**](FileInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_file**
> SendFileResponse send_file(send_file_request)



### Example

```python
from __future__ import print_function
import time
import oort_sdk_client
from oort_sdk_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with oort_sdk_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = oort_sdk_client.SdkApi(api_client)
    send_file_request = oort_sdk_client.SendFileRequest() # SendFileRequest | The file and parameters for sending

    try:
        api_response = api_instance.send_file(send_file_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SdkApi->send_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_file_request** | [**SendFileRequest**](SendFileRequest.md)| The file and parameters for sending | 

### Return type

[**SendFileResponse**](SendFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

