# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pitneybowes_shippingapi.api_client import ApiClient
from pitneybowes_shippingapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ParcelProtectionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_parcel_protection(self, x_pb_transaction_id, parcel_protection_reference_id, void_parcel_protection_request, **kwargs):  # noqa: E501
        """Parcel Protection Coverage  # noqa: E501

        This API lets merchants request Pitney Bowes [Parcel Protection](https://shipping.pitneybowes.com/faqs/parcel-protection.html) coverage for shipments. Merchants can request coverage for shipments created with the Shipping APIs as well as for shipments created with other platforms.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_parcel_protection(x_pb_transaction_id, parcel_protection_reference_id, void_parcel_protection_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param str parcel_protection_reference_id: Required. The identifier for the PB Parcel Protection policy that is being voided. (required)
        :param VoidParcelProtectionRequest void_parcel_protection_request: manifest (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: VoidParcelProtectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.cancel_parcel_protection_with_http_info(x_pb_transaction_id, parcel_protection_reference_id, void_parcel_protection_request, **kwargs)  # noqa: E501

    def cancel_parcel_protection_with_http_info(self, x_pb_transaction_id, parcel_protection_reference_id, void_parcel_protection_request, **kwargs):  # noqa: E501
        """Parcel Protection Coverage  # noqa: E501

        This API lets merchants request Pitney Bowes [Parcel Protection](https://shipping.pitneybowes.com/faqs/parcel-protection.html) coverage for shipments. Merchants can request coverage for shipments created with the Shipping APIs as well as for shipments created with other platforms.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_parcel_protection_with_http_info(x_pb_transaction_id, parcel_protection_reference_id, void_parcel_protection_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param str parcel_protection_reference_id: Required. The identifier for the PB Parcel Protection policy that is being voided. (required)
        :param VoidParcelProtectionRequest void_parcel_protection_request: manifest (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(VoidParcelProtectionResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_pb_transaction_id',
            'parcel_protection_reference_id',
            'void_parcel_protection_request',
            'x_pb_unified_error_structure'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_parcel_protection" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_pb_transaction_id' is set
        if self.api_client.client_side_validation and ('x_pb_transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_pb_transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_pb_transaction_id` when calling `cancel_parcel_protection`")  # noqa: E501
        # verify the required parameter 'parcel_protection_reference_id' is set
        if self.api_client.client_side_validation and ('parcel_protection_reference_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['parcel_protection_reference_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `parcel_protection_reference_id` when calling `cancel_parcel_protection`")  # noqa: E501
        # verify the required parameter 'void_parcel_protection_request' is set
        if self.api_client.client_side_validation and ('void_parcel_protection_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['void_parcel_protection_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `void_parcel_protection_request` when calling `cancel_parcel_protection`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parcel_protection_reference_id' in local_var_params and local_var_params['parcel_protection_reference_id'] is not None:  # noqa: E501
            query_params.append(('parcelProtectionReferenceId', local_var_params['parcel_protection_reference_id']))  # noqa: E501

        header_params = {}
        if 'x_pb_unified_error_structure' in local_var_params:
            header_params['X-PB-UnifiedErrorStructure'] = local_var_params['x_pb_unified_error_structure']  # noqa: E501
        if 'x_pb_transaction_id' in local_var_params:
            header_params['X-PB-TransactionId'] = local_var_params['x_pb_transaction_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'void_parcel_protection_request' in local_var_params:
            body_params = local_var_params['void_parcel_protection_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/v1/parcel-protection/void', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VoidParcelProtectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_parcel_protection_coverage(self, x_pb_transaction_id, parcel_protection_create_request, **kwargs):  # noqa: E501
        """Parcel Protection Coverage  # noqa: E501

        This API lets merchants request Pitney Bowes [Parcel Protection](https://shipping.pitneybowes.com/faqs/parcel-protection.html) coverage for shipments. Merchants can request coverage for shipments created with the Shipping APIs as well as for shipments created with other platforms.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parcel_protection_coverage(x_pb_transaction_id, parcel_protection_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param ParcelProtectionCreateRequest parcel_protection_create_request: manifest (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ParcelProtectionCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_parcel_protection_coverage_with_http_info(x_pb_transaction_id, parcel_protection_create_request, **kwargs)  # noqa: E501

    def get_parcel_protection_coverage_with_http_info(self, x_pb_transaction_id, parcel_protection_create_request, **kwargs):  # noqa: E501
        """Parcel Protection Coverage  # noqa: E501

        This API lets merchants request Pitney Bowes [Parcel Protection](https://shipping.pitneybowes.com/faqs/parcel-protection.html) coverage for shipments. Merchants can request coverage for shipments created with the Shipping APIs as well as for shipments created with other platforms.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parcel_protection_coverage_with_http_info(x_pb_transaction_id, parcel_protection_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param ParcelProtectionCreateRequest parcel_protection_create_request: manifest (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ParcelProtectionCreateResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_pb_transaction_id',
            'parcel_protection_create_request',
            'x_pb_unified_error_structure'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_parcel_protection_coverage" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_pb_transaction_id' is set
        if self.api_client.client_side_validation and ('x_pb_transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_pb_transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_pb_transaction_id` when calling `get_parcel_protection_coverage`")  # noqa: E501
        # verify the required parameter 'parcel_protection_create_request' is set
        if self.api_client.client_side_validation and ('parcel_protection_create_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['parcel_protection_create_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `parcel_protection_create_request` when calling `get_parcel_protection_coverage`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_pb_unified_error_structure' in local_var_params:
            header_params['X-PB-UnifiedErrorStructure'] = local_var_params['x_pb_unified_error_structure']  # noqa: E501
        if 'x_pb_transaction_id' in local_var_params:
            header_params['X-PB-TransactionId'] = local_var_params['x_pb_transaction_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'parcel_protection_create_request' in local_var_params:
            body_params = local_var_params['parcel_protection_create_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/v1/parcel-protection/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParcelProtectionCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_parcel_protection_quote(self, x_pb_transaction_id, parcel_protection_quote_request, **kwargs):  # noqa: E501
        """Parcel Protection Quote  # noqa: E501

        This API provides a quote for covering a shipment through Pitney Bowes [Parcel Protection](https://www.pitneybowes.com/us/ecommerce-delivery-services/parcel-protection.html).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parcel_protection_quote(x_pb_transaction_id, parcel_protection_quote_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param ParcelProtectionQuoteRequest parcel_protection_quote_request: manifest (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ParcelProtectionQuoteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_parcel_protection_quote_with_http_info(x_pb_transaction_id, parcel_protection_quote_request, **kwargs)  # noqa: E501

    def get_parcel_protection_quote_with_http_info(self, x_pb_transaction_id, parcel_protection_quote_request, **kwargs):  # noqa: E501
        """Parcel Protection Quote  # noqa: E501

        This API provides a quote for covering a shipment through Pitney Bowes [Parcel Protection](https://www.pitneybowes.com/us/ecommerce-delivery-services/parcel-protection.html).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parcel_protection_quote_with_http_info(x_pb_transaction_id, parcel_protection_quote_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param ParcelProtectionQuoteRequest parcel_protection_quote_request: manifest (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ParcelProtectionQuoteResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_pb_transaction_id',
            'parcel_protection_quote_request',
            'x_pb_unified_error_structure'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_parcel_protection_quote" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_pb_transaction_id' is set
        if self.api_client.client_side_validation and ('x_pb_transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_pb_transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_pb_transaction_id` when calling `get_parcel_protection_quote`")  # noqa: E501
        # verify the required parameter 'parcel_protection_quote_request' is set
        if self.api_client.client_side_validation and ('parcel_protection_quote_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['parcel_protection_quote_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `parcel_protection_quote_request` when calling `get_parcel_protection_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_pb_unified_error_structure' in local_var_params:
            header_params['X-PB-UnifiedErrorStructure'] = local_var_params['x_pb_unified_error_structure']  # noqa: E501
        if 'x_pb_transaction_id' in local_var_params:
            header_params['X-PB-TransactionId'] = local_var_params['x_pb_transaction_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'parcel_protection_quote_request' in local_var_params:
            body_params = local_var_params['parcel_protection_quote_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/v1/parcel-protection/quote', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParcelProtectionQuoteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_parcel_protection_reports(self, x_pb_transaction_id, developer_id, policy_created_from_date, **kwargs):  # noqa: E501
        """Parcel Protection Reports  # noqa: E501

        This operation retrieves the policy status and other information on the Parcel Protection policies you have purchased for your shipments. Further Details https://shipping.pitneybowes.com/api/get-parcel-protection-reports.html  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parcel_protection_reports(x_pb_transaction_id, developer_id, policy_created_from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param str developer_id: Required. Your Pitney Bowes developer ID. (required)
        :param str policy_created_from_date: The beginning of the date range. Specify this value in UTC using the ISO 8601 standard. You must include both date and time, and you must end the time with Z to indicate a zero offset. (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param str policy_created_to_date: The end of the date range. Specify this value in UTC using the ISO 8601 standard. You must include both date and time, and you must end the time with Z to indicate a zero offset.
        :param str policy_reference_id: The unique identifier for the PB Parcel Protection policy.].
        :param str parcel_tracking_number: The parcel tracking number of the shipment that the policy applies to.
        :param str merchant_id: The merchant's Shipper ID. This is the value of the postalReportingNumber element in the Merchant Object.
        :param str policy_status: Whether the policy is active or voided.
        :param str size: The number of transactions to return per page in the result set.
        :param str page: The index number of the page to return. Page index numbering starts at 0. Specifying page=0 returns the first page of the result set.
        :param str sort: Defines a property to sort on and the sort order. Sort order can be ascending (asc) or descending (desc).
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ParcelProtectionPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_parcel_protection_reports_with_http_info(x_pb_transaction_id, developer_id, policy_created_from_date, **kwargs)  # noqa: E501

    def get_parcel_protection_reports_with_http_info(self, x_pb_transaction_id, developer_id, policy_created_from_date, **kwargs):  # noqa: E501
        """Parcel Protection Reports  # noqa: E501

        This operation retrieves the policy status and other information on the Parcel Protection policies you have purchased for your shipments. Further Details https://shipping.pitneybowes.com/api/get-parcel-protection-reports.html  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_parcel_protection_reports_with_http_info(x_pb_transaction_id, developer_id, policy_created_from_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param str developer_id: Required. Your Pitney Bowes developer ID. (required)
        :param str policy_created_from_date: The beginning of the date range. Specify this value in UTC using the ISO 8601 standard. You must include both date and time, and you must end the time with Z to indicate a zero offset. (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param str policy_created_to_date: The end of the date range. Specify this value in UTC using the ISO 8601 standard. You must include both date and time, and you must end the time with Z to indicate a zero offset.
        :param str policy_reference_id: The unique identifier for the PB Parcel Protection policy.].
        :param str parcel_tracking_number: The parcel tracking number of the shipment that the policy applies to.
        :param str merchant_id: The merchant's Shipper ID. This is the value of the postalReportingNumber element in the Merchant Object.
        :param str policy_status: Whether the policy is active or voided.
        :param str size: The number of transactions to return per page in the result set.
        :param str page: The index number of the page to return. Page index numbering starts at 0. Specifying page=0 returns the first page of the result set.
        :param str sort: Defines a property to sort on and the sort order. Sort order can be ascending (asc) or descending (desc).
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ParcelProtectionPolicyResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_pb_transaction_id',
            'developer_id',
            'policy_created_from_date',
            'x_pb_unified_error_structure',
            'policy_created_to_date',
            'policy_reference_id',
            'parcel_tracking_number',
            'merchant_id',
            'policy_status',
            'size',
            'page',
            'sort'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_parcel_protection_reports" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_pb_transaction_id' is set
        if self.api_client.client_side_validation and ('x_pb_transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_pb_transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_pb_transaction_id` when calling `get_parcel_protection_reports`")  # noqa: E501
        # verify the required parameter 'developer_id' is set
        if self.api_client.client_side_validation and ('developer_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['developer_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `developer_id` when calling `get_parcel_protection_reports`")  # noqa: E501
        # verify the required parameter 'policy_created_from_date' is set
        if self.api_client.client_side_validation and ('policy_created_from_date' not in local_var_params or  # noqa: E501
                                                        local_var_params['policy_created_from_date'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `policy_created_from_date` when calling `get_parcel_protection_reports`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'developer_id' in local_var_params:
            path_params['developerId'] = local_var_params['developer_id']  # noqa: E501

        query_params = []
        if 'policy_created_from_date' in local_var_params and local_var_params['policy_created_from_date'] is not None:  # noqa: E501
            query_params.append(('policyCreatedFromDate', local_var_params['policy_created_from_date']))  # noqa: E501
        if 'policy_created_to_date' in local_var_params and local_var_params['policy_created_to_date'] is not None:  # noqa: E501
            query_params.append(('policyCreatedToDate', local_var_params['policy_created_to_date']))  # noqa: E501
        if 'policy_reference_id' in local_var_params and local_var_params['policy_reference_id'] is not None:  # noqa: E501
            query_params.append(('policyReferenceId', local_var_params['policy_reference_id']))  # noqa: E501
        if 'parcel_tracking_number' in local_var_params and local_var_params['parcel_tracking_number'] is not None:  # noqa: E501
            query_params.append(('parcelTrackingNumber', local_var_params['parcel_tracking_number']))  # noqa: E501
        if 'merchant_id' in local_var_params and local_var_params['merchant_id'] is not None:  # noqa: E501
            query_params.append(('merchantId', local_var_params['merchant_id']))  # noqa: E501
        if 'policy_status' in local_var_params and local_var_params['policy_status'] is not None:  # noqa: E501
            query_params.append(('policyStatus', local_var_params['policy_status']))  # noqa: E501
        if 'size' in local_var_params and local_var_params['size'] is not None:  # noqa: E501
            query_params.append(('size', local_var_params['size']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

        header_params = {}
        if 'x_pb_unified_error_structure' in local_var_params:
            header_params['X-PB-UnifiedErrorStructure'] = local_var_params['x_pb_unified_error_structure']  # noqa: E501
        if 'x_pb_transaction_id' in local_var_params:
            header_params['X-PB-TransactionId'] = local_var_params['x_pb_transaction_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/v1/parcel-protection/{developerId}/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParcelProtectionPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
