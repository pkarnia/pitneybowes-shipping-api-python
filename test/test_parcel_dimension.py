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
from pitneybowes_shippingapi.models.parcel_dimension import ParcelDimension  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestParcelDimension(unittest.TestCase):
    """ParcelDimension unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelDimension
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.parcel_dimension.ParcelDimension()  # noqa: E501
        if include_optional :
            return ParcelDimension(
                length = 1.337, 
                height = 1.337, 
                width = 1.337, 
                unit_of_measurement = 'CM', 
                irregular_parcel_girth = 1.337
            )
        else :
            return ParcelDimension(
        )

    def testParcelDimension(self):
        """Test ParcelDimension"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
