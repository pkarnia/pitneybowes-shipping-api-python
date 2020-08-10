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


class Parcel(object):
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
        'dimension': 'ParcelDimension',
        'weight': 'ParcelWeight',
        'value_of_goods': 'float',
        'currency_code': 'str'
    }

    attribute_map = {
        'dimension': 'dimension',
        'weight': 'weight',
        'value_of_goods': 'valueOfGoods',
        'currency_code': 'currencyCode'
    }

    def __init__(self, dimension=None, weight=None, value_of_goods=None, currency_code=None, local_vars_configuration=None):  # noqa: E501
        """Parcel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dimension = None
        self._weight = None
        self._value_of_goods = None
        self._currency_code = None
        self.discriminator = None

        if dimension is not None:
            self.dimension = dimension
        if weight is not None:
            self.weight = weight
        if value_of_goods is not None:
            self.value_of_goods = value_of_goods
        if currency_code is not None:
            self.currency_code = currency_code

    @property
    def dimension(self):
        """Gets the dimension of this Parcel.  # noqa: E501


        :return: The dimension of this Parcel.  # noqa: E501
        :rtype: ParcelDimension
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this Parcel.


        :param dimension: The dimension of this Parcel.  # noqa: E501
        :type: ParcelDimension
        """

        self._dimension = dimension

    @property
    def weight(self):
        """Gets the weight of this Parcel.  # noqa: E501


        :return: The weight of this Parcel.  # noqa: E501
        :rtype: ParcelWeight
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Parcel.


        :param weight: The weight of this Parcel.  # noqa: E501
        :type: ParcelWeight
        """

        self._weight = weight

    @property
    def value_of_goods(self):
        """Gets the value_of_goods of this Parcel.  # noqa: E501


        :return: The value_of_goods of this Parcel.  # noqa: E501
        :rtype: float
        """
        return self._value_of_goods

    @value_of_goods.setter
    def value_of_goods(self, value_of_goods):
        """Sets the value_of_goods of this Parcel.


        :param value_of_goods: The value_of_goods of this Parcel.  # noqa: E501
        :type: float
        """

        self._value_of_goods = value_of_goods

    @property
    def currency_code(self):
        """Gets the currency_code of this Parcel.  # noqa: E501

        Currency code as per [IOS 4217](https://en.wikipedia.org/wiki/ISO_4217)  # noqa: E501

        :return: The currency_code of this Parcel.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Parcel.

        Currency code as per [IOS 4217](https://en.wikipedia.org/wiki/ISO_4217)  # noqa: E501

        :param currency_code: The currency_code of this Parcel.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

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
        if not isinstance(other, Parcel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Parcel):
            return True

        return self.to_dict() != other.to_dict()
