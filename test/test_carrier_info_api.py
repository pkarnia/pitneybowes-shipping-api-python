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

import pitneybowes_shippingapi
from pitneybowes_shippingapi.api.carrier_info_api import CarrierInfoApi  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException


class TestCarrierInfoApi(unittest.TestCase):
    """CarrierInfoApi unit test stubs"""

    def setUp(self):
        self.api = pitneybowes_shippingapi.api.carrier_info_api.CarrierInfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_carrier_facilities(self):
        """Test case for get_carrier_facilities

        Find Carrier Facilities  # noqa: E501
        """
        pass

    def test_get_carrier_license_agreement(self):
        """Test case for get_carrier_license_agreement

        This operation retrieves a carrier's license agreement.  # noqa: E501
        """
        pass

    def test_get_carrier_service_rules(self):
        """Test case for get_carrier_service_rules

        Retrieves the rules governing the carrier's services.  # noqa: E501
        """
        pass

    def test_get_carrier_supported_destination(self):
        """Test case for get_carrier_supported_destination

        This operation returns a list of supported destination countries to which the carrier offers international shipping services.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
