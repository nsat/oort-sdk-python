# coding: utf-8

"""
    OORT Agent SDK Interface

    Client interface to the OORT agent.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import oort_sdk_client
from oort_sdk_client.models.adcs_command_response import AdcsCommandResponse  # noqa: E501
from oort_sdk_client.rest import ApiException

class TestAdcsCommandResponse(unittest.TestCase):
    """AdcsCommandResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdcsCommandResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = oort_sdk_client.models.adcs_command_response.AdcsCommandResponse()  # noqa: E501
        if include_optional :
            return AdcsCommandResponse(
                status = 'OK', 
                reason = '0', 
                mode = '0', 
                target = oort_sdk_client.models.adcs_target.AdcsTarget(
                    lat = 1.337, 
                    lon = 1.337, ), 
                vector = oort_sdk_client.models.adcs_xyz_float_t.Adcs_xyz_float_t(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ), 
                quat = oort_sdk_client.models.adcs_quat_t.Adcs_quat_t(
                    q1 = 1.337, 
                    q2 = 1.337, 
                    q3 = 1.337, 
                    q4 = 1.337, )
            )
        else :
            return AdcsCommandResponse(
                status = 'OK',
                mode = '0',
        )

    def testAdcsCommandResponse(self):
        """Test AdcsCommandResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
