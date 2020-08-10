# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pitneybowes_shippingapi.configuration import Configuration


class CrossBorderQuotesErrorsQuoteLines(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'line_id': 'str',
        'merchant_com_ref_id': 'str',
        'quantity': 'int',
        'unit_errors': 'list[CrossBorderQuotesErrorsUnitErrors]'
    }

    attribute_map = {
        'line_id': 'lineId',
        'merchant_com_ref_id': 'merchantComRefId',
        'quantity': 'quantity',
        'unit_errors': 'unitErrors'
    }

    def __init__(self, line_id=None, merchant_com_ref_id=None, quantity=None, unit_errors=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesErrorsQuoteLines - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._line_id = None
        self._merchant_com_ref_id = None
        self._quantity = None
        self._unit_errors = None
        self.discriminator = None

        if line_id is not None:
            self.line_id = line_id
        if merchant_com_ref_id is not None:
            self.merchant_com_ref_id = merchant_com_ref_id
        if quantity is not None:
            self.quantity = quantity
        if unit_errors is not None:
            self.unit_errors = unit_errors

    @property
    def line_id(self):
        """Gets the line_id of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501


        :return: The line_id of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this CrossBorderQuotesErrorsQuoteLines.


        :param line_id: The line_id of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501
        :type: str
        """

        self._line_id = line_id

    @property
    def merchant_com_ref_id(self):
        """Gets the merchant_com_ref_id of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501


        :return: The merchant_com_ref_id of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501
        :rtype: str
        """
        return self._merchant_com_ref_id

    @merchant_com_ref_id.setter
    def merchant_com_ref_id(self, merchant_com_ref_id):
        """Sets the merchant_com_ref_id of this CrossBorderQuotesErrorsQuoteLines.


        :param merchant_com_ref_id: The merchant_com_ref_id of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501
        :type: str
        """

        self._merchant_com_ref_id = merchant_com_ref_id

    @property
    def quantity(self):
        """Gets the quantity of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501


        :return: The quantity of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CrossBorderQuotesErrorsQuoteLines.


        :param quantity: The quantity of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def unit_errors(self):
        """Gets the unit_errors of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501


        :return: The unit_errors of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501
        :rtype: list[CrossBorderQuotesErrorsUnitErrors]
        """
        return self._unit_errors

    @unit_errors.setter
    def unit_errors(self, unit_errors):
        """Sets the unit_errors of this CrossBorderQuotesErrorsQuoteLines.


        :param unit_errors: The unit_errors of this CrossBorderQuotesErrorsQuoteLines.  # noqa: E501
        :type: list[CrossBorderQuotesErrorsUnitErrors]
        """

        self._unit_errors = unit_errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CrossBorderQuotesErrorsQuoteLines):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesErrorsQuoteLines):
            return True

        return self.to_dict() != other.to_dict()
