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


class AdcsEulerT(object):
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
        'roll': 'float',
        'pitch': 'float',
        'yaw': 'float'
    }

    attribute_map = {
        'roll': 'roll',
        'pitch': 'pitch',
        'yaw': 'yaw'
    }

    def __init__(self, roll=None, pitch=None, yaw=None, local_vars_configuration=None):  # noqa: E501
        """AdcsEulerT - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._roll = None
        self._pitch = None
        self._yaw = None
        self.discriminator = None

        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    @property
    def roll(self):
        """Gets the roll of this AdcsEulerT.  # noqa: E501


        :return: The roll of this AdcsEulerT.  # noqa: E501
        :rtype: float
        """
        return self._roll

    @roll.setter
    def roll(self, roll):
        """Sets the roll of this AdcsEulerT.


        :param roll: The roll of this AdcsEulerT.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and roll is None:  # noqa: E501
            raise ValueError("Invalid value for `roll`, must not be `None`")  # noqa: E501

        self._roll = roll

    @property
    def pitch(self):
        """Gets the pitch of this AdcsEulerT.  # noqa: E501


        :return: The pitch of this AdcsEulerT.  # noqa: E501
        :rtype: float
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this AdcsEulerT.


        :param pitch: The pitch of this AdcsEulerT.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and pitch is None:  # noqa: E501
            raise ValueError("Invalid value for `pitch`, must not be `None`")  # noqa: E501

        self._pitch = pitch

    @property
    def yaw(self):
        """Gets the yaw of this AdcsEulerT.  # noqa: E501


        :return: The yaw of this AdcsEulerT.  # noqa: E501
        :rtype: float
        """
        return self._yaw

    @yaw.setter
    def yaw(self, yaw):
        """Sets the yaw of this AdcsEulerT.


        :param yaw: The yaw of this AdcsEulerT.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and yaw is None:  # noqa: E501
            raise ValueError("Invalid value for `yaw`, must not be `None`")  # noqa: E501

        self._yaw = yaw

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
        if not isinstance(other, AdcsEulerT):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdcsEulerT):
            return True

        return self.to_dict() != other.to_dict()
