# coding: utf-8

"""
    OORT Agent SDK Interface

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from oort_sdk_client.configuration import Configuration


class RetrieveFileRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'save_path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'save_path': 'save_path'
    }

    def __init__(self, id=None, save_path=None, local_vars_configuration=None):  # noqa: E501
        """RetrieveFileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._save_path = None
        self.discriminator = None

        self.id = id
        self.save_path = save_path

    @property
    def id(self):
        """Gets the id of this RetrieveFileRequest.  # noqa: E501


        :return: The id of this RetrieveFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RetrieveFileRequest.


        :param id: The id of this RetrieveFileRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def save_path(self):
        """Gets the save_path of this RetrieveFileRequest.  # noqa: E501

        The destination path to save the file. Must be an absolute path.  # noqa: E501

        :return: The save_path of this RetrieveFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._save_path

    @save_path.setter
    def save_path(self, save_path):
        """Sets the save_path of this RetrieveFileRequest.

        The destination path to save the file. Must be an absolute path.  # noqa: E501

        :param save_path: The save_path of this RetrieveFileRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and save_path is None:  # noqa: E501
            raise ValueError("Invalid value for `save_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                save_path is not None and not re.search(r'^\/.*', save_path)):  # noqa: E501
            raise ValueError(r"Invalid value for `save_path`, must be a follow pattern or equal to `/^\/.*/`")  # noqa: E501

        self._save_path = save_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RetrieveFileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetrieveFileRequest):
            return True

        return self.to_dict() != other.to_dict()
