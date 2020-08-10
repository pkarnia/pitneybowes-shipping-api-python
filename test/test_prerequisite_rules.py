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
from pitneybowes_shippingapi.models.prerequisite_rules import PrerequisiteRules  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestPrerequisiteRules(unittest.TestCase):
    """PrerequisiteRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrerequisiteRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.prerequisite_rules.PrerequisiteRules()  # noqa: E501
        if include_optional :
            return PrerequisiteRules(
                special_service_codes = 'ADSIG', 
                min_input_value = 1.337
            )
        else :
            return PrerequisiteRules(
        )

    def testPrerequisiteRules(self):
        """Test PrerequisiteRules"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
