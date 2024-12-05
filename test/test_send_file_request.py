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
from oort_sdk_client.models.send_file_request import SendFileRequest  # noqa: E501
from oort_sdk_client.rest import ApiException

class TestSendFileRequest(unittest.TestCase):
    """SendFileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SendFileRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = oort_sdk_client.models.send_file_request.SendFileRequest()  # noqa: E501
        if include_optional :
            return SendFileRequest(
                destination = '0', 
                filepath = 'a', 
                topic = '0', 
                options = oort_sdk_client.models.send_options.SendOptions(
                    ttl_params = oort_sdk_client.models.ttl_params.TTLParams(
                        urgent = 56, 
                        bulk = 56, 
                        surplus = 56, ), 
                    reliable = True, 
                    tags = {
                        'key' : '0'
                        }, 
                    delivery_hints = {
                        'key' : '0'
                        }, )
            )
        else :
            return SendFileRequest(
                destination = '0',
                filepath = 'a',
                topic = '0',
        )

    def testSendFileRequest(self):
        """Test SendFileRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
