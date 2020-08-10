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


class ParcelProtectionQuoteResponseParcelProtectionFeesBreakup(object):
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
        'base_premium': 'float',
        'technology_fee': 'float'
    }

    attribute_map = {
        'base_premium': 'basePremium',
        'technology_fee': 'technologyFee'
    }

    def __init__(self, base_premium=None, technology_fee=None, local_vars_configuration=None):  # noqa: E501
        """ParcelProtectionQuoteResponseParcelProtectionFeesBreakup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_premium = None
        self._technology_fee = None
        self.discriminator = None

        self.base_premium = base_premium
        self.technology_fee = technology_fee

    @property
    def base_premium(self):
        """Gets the base_premium of this ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.  # noqa: E501


        :return: The base_premium of this ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.  # noqa: E501
        :rtype: float
        """
        return self._base_premium

    @base_premium.setter
    def base_premium(self, base_premium):
        """Sets the base_premium of this ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.


        :param base_premium: The base_premium of this ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and base_premium is None:  # noqa: E501
            raise ValueError("Invalid value for `base_premium`, must not be `None`")  # noqa: E501

        self._base_premium = base_premium

    @property
    def technology_fee(self):
        """Gets the technology_fee of this ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.  # noqa: E501


        :return: The technology_fee of this ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.  # noqa: E501
        :rtype: float
        """
        return self._technology_fee

    @technology_fee.setter
    def technology_fee(self, technology_fee):
        """Sets the technology_fee of this ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.


        :param technology_fee: The technology_fee of this ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and technology_fee is None:  # noqa: E501
            raise ValueError("Invalid value for `technology_fee`, must not be `None`")  # noqa: E501

        self._technology_fee = technology_fee

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
        if not isinstance(other, ParcelProtectionQuoteResponseParcelProtectionFeesBreakup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParcelProtectionQuoteResponseParcelProtectionFeesBreakup):
            return True

        return self.to_dict() != other.to_dict()
