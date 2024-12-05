# coding: utf-8

"""
    OORT Agent SDK Interface

    Client interface to the OORT agent.  # noqa: E501

    The version of the OpenAPI document: 1.5
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import oort_sdk_client
from oort_sdk_client.models.delivery_hints import DeliveryHints  # noqa: E501
from oort_sdk_client.rest import ApiException

class TestDeliveryHints(unittest.TestCase):
    """DeliveryHints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeliveryHints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = oort_sdk_client.models.delivery_hints.DeliveryHints()  # noqa: E501
        if include_optional :
            return DeliveryHints(
                dest_path = '0', 
                mode = '0'
            )
        else :
            return DeliveryHints(
                dest_path = '0',
                mode = '0',
        )

    def testDeliveryHints(self):
        """Test DeliveryHints"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
