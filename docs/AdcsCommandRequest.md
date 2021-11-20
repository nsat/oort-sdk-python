# AdcsCommandRequest

Request to set ADCS mode and parameters
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | SPACS attitude control command | 
**aperture** | **str** | Aperture (imager, antenna, etc) name to use in ADCS pointing requests | [optional] 
**target** | [**AdcsTarget**](AdcsTarget.md) |  | [optional] 
**angle** | **float** |  | [optional] 
**vector** | [**AdcsXyzFloatT**](AdcsXyzFloatT.md) |  | [optional] 
**quat** | [**AdcsQuatT**](AdcsQuatT.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


