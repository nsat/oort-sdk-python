# coding: utf-8

"""
    OORT Agent SDK Interface

    Client interface to the OORT agent.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from oort_sdk_client.configuration import Configuration


class TTLParams(object):
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
        'urgent': 'int',
        'bulk': 'int',
        'surplus': 'int'
    }

    attribute_map = {
        'urgent': 'urgent',
        'bulk': 'bulk',
        'surplus': 'surplus'
    }

    def __init__(self, urgent=9000, bulk=43200, surplus=172800, local_vars_configuration=None):  # noqa: E501
        """TTLParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._urgent = None
        self._bulk = None
        self._surplus = None
        self.discriminator = None

        if urgent is not None:
            self.urgent = urgent
        if bulk is not None:
            self.bulk = bulk
        if surplus is not None:
            self.surplus = surplus

    @property
    def urgent(self):
        """Gets the urgent of this TTLParams.  # noqa: E501

        TTL in seconds for urgent items  # noqa: E501

        :return: The urgent of this TTLParams.  # noqa: E501
        :rtype: int
        """
        return self._urgent

    @urgent.setter
    def urgent(self, urgent):
        """Sets the urgent of this TTLParams.

        TTL in seconds for urgent items  # noqa: E501

        :param urgent: The urgent of this TTLParams.  # noqa: E501
        :type: int
        """

        self._urgent = urgent

    @property
    def bulk(self):
        """Gets the bulk of this TTLParams.  # noqa: E501

        TTL in seconds for bulk items  # noqa: E501

        :return: The bulk of this TTLParams.  # noqa: E501
        :rtype: int
        """
        return self._bulk

    @bulk.setter
    def bulk(self, bulk):
        """Sets the bulk of this TTLParams.

        TTL in seconds for bulk items  # noqa: E501

        :param bulk: The bulk of this TTLParams.  # noqa: E501
        :type: int
        """

        self._bulk = bulk

    @property
    def surplus(self):
        """Gets the surplus of this TTLParams.  # noqa: E501

        TTL in seconds for surplus items  # noqa: E501

        :return: The surplus of this TTLParams.  # noqa: E501
        :rtype: int
        """
        return self._surplus

    @surplus.setter
    def surplus(self, surplus):
        """Sets the surplus of this TTLParams.

        TTL in seconds for surplus items  # noqa: E501

        :param surplus: The surplus of this TTLParams.  # noqa: E501
        :type: int
        """

        self._surplus = surplus

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
        if not isinstance(other, TTLParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TTLParams):
            return True

        return self.to_dict() != other.to_dict()
