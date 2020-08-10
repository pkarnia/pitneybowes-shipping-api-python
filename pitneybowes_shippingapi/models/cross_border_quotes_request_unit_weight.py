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


class CrossBorderQuotesRequestUnitWeight(object):
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
        'weight': 'int',
        'unit_of_measurement': 'str'
    }

    attribute_map = {
        'weight': 'weight',
        'unit_of_measurement': 'unitOfMeasurement'
    }

    def __init__(self, weight=None, unit_of_measurement=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesRequestUnitWeight - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._weight = None
        self._unit_of_measurement = None
        self.discriminator = None

        self.weight = weight
        self.unit_of_measurement = unit_of_measurement

    @property
    def weight(self):
        """Gets the weight of this CrossBorderQuotesRequestUnitWeight.  # noqa: E501


        :return: The weight of this CrossBorderQuotesRequestUnitWeight.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CrossBorderQuotesRequestUnitWeight.


        :param weight: The weight of this CrossBorderQuotesRequestUnitWeight.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and weight is None:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

    @property
    def unit_of_measurement(self):
        """Gets the unit_of_measurement of this CrossBorderQuotesRequestUnitWeight.  # noqa: E501


        :return: The unit_of_measurement of this CrossBorderQuotesRequestUnitWeight.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        """Sets the unit_of_measurement of this CrossBorderQuotesRequestUnitWeight.


        :param unit_of_measurement: The unit_of_measurement of this CrossBorderQuotesRequestUnitWeight.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unit_of_measurement is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_of_measurement`, must not be `None`")  # noqa: E501

        self._unit_of_measurement = unit_of_measurement

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
        if not isinstance(other, CrossBorderQuotesRequestUnitWeight):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesRequestUnitWeight):
            return True

        return self.to_dict() != other.to_dict()
