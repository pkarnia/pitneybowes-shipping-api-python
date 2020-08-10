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


class Customs(object):
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
        'customs_info': 'CustomsInfo',
        'customs_items': 'list[CustomsItem]'
    }

    attribute_map = {
        'customs_info': 'customsInfo',
        'customs_items': 'customsItems'
    }

    def __init__(self, customs_info=None, customs_items=None, local_vars_configuration=None):  # noqa: E501
        """Customs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._customs_info = None
        self._customs_items = None
        self.discriminator = None

        if customs_info is not None:
            self.customs_info = customs_info
        if customs_items is not None:
            self.customs_items = customs_items

    @property
    def customs_info(self):
        """Gets the customs_info of this Customs.  # noqa: E501


        :return: The customs_info of this Customs.  # noqa: E501
        :rtype: CustomsInfo
        """
        return self._customs_info

    @customs_info.setter
    def customs_info(self, customs_info):
        """Sets the customs_info of this Customs.


        :param customs_info: The customs_info of this Customs.  # noqa: E501
        :type: CustomsInfo
        """

        self._customs_info = customs_info

    @property
    def customs_items(self):
        """Gets the customs_items of this Customs.  # noqa: E501


        :return: The customs_items of this Customs.  # noqa: E501
        :rtype: list[CustomsItem]
        """
        return self._customs_items

    @customs_items.setter
    def customs_items(self, customs_items):
        """Sets the customs_items of this Customs.


        :param customs_items: The customs_items of this Customs.  # noqa: E501
        :type: list[CustomsItem]
        """

        self._customs_items = customs_items

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
        if not isinstance(other, Customs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Customs):
            return True

        return self.to_dict() != other.to_dict()
