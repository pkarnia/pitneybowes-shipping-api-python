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
from pitneybowes_shippingapi.models.parcel_protection_quote_request import ParcelProtectionQuoteRequest  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestParcelProtectionQuoteRequest(unittest.TestCase):
    """ParcelProtectionQuoteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionQuoteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.parcel_protection_quote_request.ParcelProtectionQuoteRequest()  # noqa: E501
        if include_optional :
            return ParcelProtectionQuoteRequest(
                parcel_protection_account_id = '0', 
                parcel_protection_program_id = '0', 
                shipment_info = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info.ParcelProtectionQuoteRequest_shipmentInfo(
                    carrier = '0', 
                    service_id = '0', 
                    insurance_coverage_value = 56, 
                    insurance_coverage_value_currency = '0', 
                    parcel_info = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_parcel_info.ParcelProtectionQuoteRequest_shipmentInfo_parcelInfo(
                        commodity_list = [
                            pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_parcel_info_commodity_list.ParcelProtectionQuoteRequest_shipmentInfo_parcelInfo_commodityList(
                                category_path = '0', 
                                item_code = '0', 
                                name = '0', 
                                url = '0', )
                            ], ), 
                    shipper_info = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_shipper_info.ParcelProtectionQuoteRequest_shipmentInfo_shipperInfo(
                        shipper_id = '0', 
                        address = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_shipper_info_address.ParcelProtectionQuoteRequest_shipmentInfo_shipperInfo_address(
                            address_lines = [
                                '0'
                                ], 
                            city_town = '0', 
                            state_province = '0', 
                            postal_code = '0', 
                            country_code = '0', ), ), 
                    consignee_info = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_consignee_info.ParcelProtectionQuoteRequest_shipmentInfo_consigneeInfo(
                        address = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_shipper_info_address.ParcelProtectionQuoteRequest_shipmentInfo_shipperInfo_address(
                            address_lines = [
                                '0'
                                ], 
                            city_town = '0', 
                            state_province = '0', 
                            postal_code = '0', 
                            country_code = '0', ), ), )
            )
        else :
            return ParcelProtectionQuoteRequest(
                shipment_info = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info.ParcelProtectionQuoteRequest_shipmentInfo(
                    carrier = '0', 
                    service_id = '0', 
                    insurance_coverage_value = 56, 
                    insurance_coverage_value_currency = '0', 
                    parcel_info = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_parcel_info.ParcelProtectionQuoteRequest_shipmentInfo_parcelInfo(
                        commodity_list = [
                            pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_parcel_info_commodity_list.ParcelProtectionQuoteRequest_shipmentInfo_parcelInfo_commodityList(
                                category_path = '0', 
                                item_code = '0', 
                                name = '0', 
                                url = '0', )
                            ], ), 
                    shipper_info = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_shipper_info.ParcelProtectionQuoteRequest_shipmentInfo_shipperInfo(
                        shipper_id = '0', 
                        address = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_shipper_info_address.ParcelProtectionQuoteRequest_shipmentInfo_shipperInfo_address(
                            address_lines = [
                                '0'
                                ], 
                            city_town = '0', 
                            state_province = '0', 
                            postal_code = '0', 
                            country_code = '0', ), ), 
                    consignee_info = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_consignee_info.ParcelProtectionQuoteRequest_shipmentInfo_consigneeInfo(
                        address = pitneybowes_shippingapi.models.parcel_protection_quote_request_shipment_info_shipper_info_address.ParcelProtectionQuoteRequest_shipmentInfo_shipperInfo_address(
                            address_lines = [
                                '0'
                                ], 
                            city_town = '0', 
                            state_province = '0', 
                            postal_code = '0', 
                            country_code = '0', ), ), ),
        )

    def testParcelProtectionQuoteRequest(self):
        """Test ParcelProtectionQuoteRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
