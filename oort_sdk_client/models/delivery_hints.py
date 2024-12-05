# coding: utf-8

"""
    OORT Agent SDK Interface

    Client interface to the OORT agent.  # noqa: E501

    The version of the OpenAPI document: 1.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from oort_sdk_client.configuration import Configuration


class DeliveryHints(object):
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
        'dest_path': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'dest_path': 'dest_path',
        'mode': 'mode'
    }

    def __init__(self, dest_path=None, mode=None, local_vars_configuration=None):  # noqa: E501
        """DeliveryHints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dest_path = None
        self._mode = None
        self.discriminator = None

        self.dest_path = dest_path
        self.mode = mode

    @property
    def dest_path(self):
        """Gets the dest_path of this DeliveryHints.  # noqa: E501

        Path of the file on the destination filesystem  # noqa: E501

        :return: The dest_path of this DeliveryHints.  # noqa: E501
        :rtype: str
        """
        return self._dest_path

    @dest_path.setter
    def dest_path(self, dest_path):
        """Sets the dest_path of this DeliveryHints.

        Path of the file on the destination filesystem  # noqa: E501

        :param dest_path: The dest_path of this DeliveryHints.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dest_path is None:  # noqa: E501
            raise ValueError("Invalid value for `dest_path`, must not be `None`")  # noqa: E501

        self._dest_path = dest_path

    @property
    def mode(self):
        """Gets the mode of this DeliveryHints.  # noqa: E501

        File mode in octal form. For example: \"760\" means that the user can read+write+execute, the group can read+write, and others have no access   # noqa: E501

        :return: The mode of this DeliveryHints.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DeliveryHints.

        File mode in octal form. For example: \"760\" means that the user can read+write+execute, the group can read+write, and others have no access   # noqa: E501

        :param mode: The mode of this DeliveryHints.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mode is None:  # noqa: E501
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

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
        if not isinstance(other, DeliveryHints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeliveryHints):
            return True

        return self.to_dict() != other.to_dict()
