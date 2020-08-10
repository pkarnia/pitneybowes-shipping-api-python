# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pitneybowes_shippingapi
from pitneybowes_shippingapi.models.iso_country_code import ISOCountryCode  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestISOCountryCode(unittest.TestCase):
    """ISOCountryCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ISOCountryCode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.iso_country_code.ISOCountryCode()  # noqa: E501
        if include_optional :
            return ISOCountryCode(
            )
        else :
            return ISOCountryCode(
        )

    def testISOCountryCode(self):
        """Test ISOCountryCode"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
