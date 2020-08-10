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


class CrossBorderQuotesRequestDescriptions(object):
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
        'locale': 'str',
        'name': 'str',
        'parents_names': 'list[str]'
    }

    attribute_map = {
        'locale': 'locale',
        'name': 'name',
        'parents_names': 'parentsNames'
    }

    def __init__(self, locale=None, name=None, parents_names=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesRequestDescriptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._locale = None
        self._name = None
        self._parents_names = None
        self.discriminator = None

        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = name
        if parents_names is not None:
            self.parents_names = parents_names

    @property
    def locale(self):
        """Gets the locale of this CrossBorderQuotesRequestDescriptions.  # noqa: E501


        :return: The locale of this CrossBorderQuotesRequestDescriptions.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this CrossBorderQuotesRequestDescriptions.


        :param locale: The locale of this CrossBorderQuotesRequestDescriptions.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this CrossBorderQuotesRequestDescriptions.  # noqa: E501


        :return: The name of this CrossBorderQuotesRequestDescriptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CrossBorderQuotesRequestDescriptions.


        :param name: The name of this CrossBorderQuotesRequestDescriptions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parents_names(self):
        """Gets the parents_names of this CrossBorderQuotesRequestDescriptions.  # noqa: E501


        :return: The parents_names of this CrossBorderQuotesRequestDescriptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._parents_names

    @parents_names.setter
    def parents_names(self, parents_names):
        """Sets the parents_names of this CrossBorderQuotesRequestDescriptions.


        :param parents_names: The parents_names of this CrossBorderQuotesRequestDescriptions.  # noqa: E501
        :type: list[str]
        """

        self._parents_names = parents_names

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
        if not isinstance(other, CrossBorderQuotesRequestDescriptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesRequestDescriptions):
            return True

        return self.to_dict() != other.to_dict()
