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
from pitneybowes_shippingapi.models.weight_rules import WeightRules  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestWeightRules(unittest.TestCase):
    """WeightRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WeightRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.weight_rules.WeightRules()  # noqa: E501
        if include_optional :
            return WeightRules(
                required = True, 
                unit_of_measurement = '0', 
                min_weight = 1.337, 
                max_weight = 1.337
            )
        else :
            return WeightRules(
        )

    def testWeightRules(self):
        """Test WeightRules"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
