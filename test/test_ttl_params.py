# coding: utf-8

"""
    OORT Agent SDK Interface

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import oort_sdk_client
from oort_sdk_client.models.ttl_params import TTLParams  # noqa: E501
from oort_sdk_client.rest import ApiException

class TestTTLParams(unittest.TestCase):
    """TTLParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TTLParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = oort_sdk_client.models.ttl_params.TTLParams()  # noqa: E501
        if include_optional :
            return TTLParams(
                urgent = 56, 
                bulk = 56, 
                surplus = 56
            )
        else :
            return TTLParams(
        )

    def testTTLParams(self):
        """Test TTLParams"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
