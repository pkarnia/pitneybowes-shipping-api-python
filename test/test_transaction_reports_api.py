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
from pitneybowes_shippingapi.api.transaction_reports_api import TransactionReportsApi  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException


class TestTransactionReportsApi(unittest.TestCase):
    """TransactionReportsApi unit test stubs"""

    def setUp(self):
        self.api = pitneybowes_shippingapi.api.transaction_reports_api.TransactionReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_transaction_report(self):
        """Test case for get_transaction_report

        This operation retrieves all transactions for a specified period of time.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
