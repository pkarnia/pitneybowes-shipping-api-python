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
from pitneybowes_shippingapi.models.dimension_rules import DimensionRules  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestDimensionRules(unittest.TestCase):
    """DimensionRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DimensionRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.dimension_rules.DimensionRules()  # noqa: E501
        if include_optional :
            return DimensionRules(
                required = True, 
                unit_of_measurement = '0', 
                min_parcel_dimensions = pitneybowes_shippingapi.models.dimension_rules_min_parcel_dimensions.DimensionRules_minParcelDimensions(
                    length = 1.337, 
                    width = 1.337, 
                    height = 1.337, 
                    unit_of_measurement = '0', ), 
                max_parcel_dimensions = pitneybowes_shippingapi.models.dimension_rules_max_parcel_dimensions.DimensionRules_maxParcelDimensions(
                    length = 56, 
                    width = 1.337, 
                    height = 56, 
                    unit_of_measurement = '0', ), 
                min_length_plus_girth = 56, 
                max_length_plus_girth = 56
            )
        else :
            return DimensionRules(
        )

    def testDimensionRules(self):
        """Test DimensionRules"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
