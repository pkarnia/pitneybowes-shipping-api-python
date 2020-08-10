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
from pitneybowes_shippingapi.models.cross_border_quotes_response_quote_lines import CrossBorderQuotesResponseQuoteLines  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestCrossBorderQuotesResponseQuoteLines(unittest.TestCase):
    """CrossBorderQuotesResponseQuoteLines unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesResponseQuoteLines
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.cross_border_quotes_response_quote_lines.CrossBorderQuotesResponseQuoteLines()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesResponseQuoteLines(
                line_id = '0', 
                item_id = '0', 
                quote_line_id = '0', 
                quantity = 56, 
                unit_rates = pitneybowes_shippingapi.models.cross_border_quotes_response_unit_rates.CrossBorderQuotesResponse_unitRates(
                    unit_price = 1.337, 
                    total_tax_amount = 1.337, 
                    total_duty_amount = 56, 
                    service_id = '0', 
                    base_charge = 1.337, 
                    delivery_commitment = pitneybowes_shippingapi.models.cross_border_quotes_response_unit_rates_delivery_commitment.CrossBorderQuotesResponse_unitRates_deliveryCommitment(
                        min_estimated_number_of_days = 56, 
                        max_estimated_number_of_days = 56, ), 
                    total_carrier_charge = 1.337, ), 
                line_rates = pitneybowes_shippingapi.models.cross_border_quotes_response_line_rates.CrossBorderQuotesResponse_lineRates(
                    line_price = 1.337, 
                    total_tax_amount = 1.337, 
                    total_duty_amount = 56, 
                    service_id = '0', 
                    base_charge = 1.337, 
                    delivery_commitment = pitneybowes_shippingapi.models.cross_border_quotes_response_unit_rates_delivery_commitment.CrossBorderQuotesResponse_unitRates_deliveryCommitment(
                        min_estimated_number_of_days = 56, 
                        max_estimated_number_of_days = 56, ), 
                    total_carrier_charge = 1.337, )
            )
        else :
            return CrossBorderQuotesResponseQuoteLines(
        )

    def testCrossBorderQuotesResponseQuoteLines(self):
        """Test CrossBorderQuotesResponseQuoteLines"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
