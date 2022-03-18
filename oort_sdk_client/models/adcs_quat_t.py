# coding: utf-8

"""
    OORT Agent SDK Interface

    Client interface to the OORT agent.  # noqa: E501

    The version of the OpenAPI document: 1.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from oort_sdk_client.configuration import Configuration


class AdcsQuatT(object):
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
        'q1': 'float',
        'q2': 'float',
        'q3': 'float',
        'q4': 'float'
    }

    attribute_map = {
        'q1': 'q1',
        'q2': 'q2',
        'q3': 'q3',
        'q4': 'q4'
    }

    def __init__(self, q1=None, q2=None, q3=None, q4=None, local_vars_configuration=None):  # noqa: E501
        """AdcsQuatT - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._q1 = None
        self._q2 = None
        self._q3 = None
        self._q4 = None
        self.discriminator = None

        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4

    @property
    def q1(self):
        """Gets the q1 of this AdcsQuatT.  # noqa: E501


        :return: The q1 of this AdcsQuatT.  # noqa: E501
        :rtype: float
        """
        return self._q1

    @q1.setter
    def q1(self, q1):
        """Sets the q1 of this AdcsQuatT.


        :param q1: The q1 of this AdcsQuatT.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and q1 is None:  # noqa: E501
            raise ValueError("Invalid value for `q1`, must not be `None`")  # noqa: E501

        self._q1 = q1

    @property
    def q2(self):
        """Gets the q2 of this AdcsQuatT.  # noqa: E501


        :return: The q2 of this AdcsQuatT.  # noqa: E501
        :rtype: float
        """
        return self._q2

    @q2.setter
    def q2(self, q2):
        """Sets the q2 of this AdcsQuatT.


        :param q2: The q2 of this AdcsQuatT.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and q2 is None:  # noqa: E501
            raise ValueError("Invalid value for `q2`, must not be `None`")  # noqa: E501

        self._q2 = q2

    @property
    def q3(self):
        """Gets the q3 of this AdcsQuatT.  # noqa: E501


        :return: The q3 of this AdcsQuatT.  # noqa: E501
        :rtype: float
        """
        return self._q3

    @q3.setter
    def q3(self, q3):
        """Sets the q3 of this AdcsQuatT.


        :param q3: The q3 of this AdcsQuatT.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and q3 is None:  # noqa: E501
            raise ValueError("Invalid value for `q3`, must not be `None`")  # noqa: E501

        self._q3 = q3

    @property
    def q4(self):
        """Gets the q4 of this AdcsQuatT.  # noqa: E501


        :return: The q4 of this AdcsQuatT.  # noqa: E501
        :rtype: float
        """
        return self._q4

    @q4.setter
    def q4(self, q4):
        """Sets the q4 of this AdcsQuatT.


        :param q4: The q4 of this AdcsQuatT.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and q4 is None:  # noqa: E501
            raise ValueError("Invalid value for `q4`, must not be `None`")  # noqa: E501

        self._q4 = q4

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
        if not isinstance(other, AdcsQuatT):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdcsQuatT):
            return True

        return self.to_dict() != other.to_dict()
