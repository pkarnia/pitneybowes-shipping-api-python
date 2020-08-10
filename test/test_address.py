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
from pitneybowes_shippingapi.models.address import Address  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestAddress(unittest.TestCase):
    """Address unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Address
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.address.Address()  # noqa: E501
        if include_optional :
            return Address(
                address_lines = [
                    '0'
                    ], 
                carrier_route = '0', 
                city_town = '0', 
                company = '0', 
                country_code = '0', 
                delivery_point = '0', 
                email = '0', 
                name = '0', 
                phone = '0', 
                postal_code = '0', 
                residential = True, 
                state_province = '0', 
                status = 'PARSED', 
                tax_id = '0', 
                tax_id_type = 'EIN'
            )
        else :
            return Address(
                country_code = '0',
        )

    def testAddress(self):
        """Test Address"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()