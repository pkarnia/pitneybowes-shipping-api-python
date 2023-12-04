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

from pbshipping.configuration import Configuration


class TrackingAddress(object):
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
        'name': 'str',
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'city': 'str',
        'state_or_province': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'city': 'city',
        'state_or_province': 'stateOrProvince',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, name=None, address1=None, address2=None, address3=None, city=None, state_or_province=None, postal_code=None, country=None, local_vars_configuration=None):  # noqa: E501
        """TrackingAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._city = None
        self._state_or_province = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if address3 is not None:
            self.address3 = address3
        if city is not None:
            self.city = city
        if state_or_province is not None:
            self.state_or_province = state_or_province
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def name(self):
        """Gets the name of this TrackingAddress.  # noqa: E501


        :return: The name of this TrackingAddress.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrackingAddress.


        :param name: The name of this TrackingAddress.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address1(self):
        """Gets the address1 of this TrackingAddress.  # noqa: E501


        :return: The address1 of this TrackingAddress.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this TrackingAddress.


        :param address1: The address1 of this TrackingAddress.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this TrackingAddress.  # noqa: E501


        :return: The address2 of this TrackingAddress.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this TrackingAddress.


        :param address2: The address2 of this TrackingAddress.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def address3(self):
        """Gets the address3 of this TrackingAddress.  # noqa: E501


        :return: The address3 of this TrackingAddress.  # noqa: E501
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """Sets the address3 of this TrackingAddress.


        :param address3: The address3 of this TrackingAddress.  # noqa: E501
        :type: str
        """

        self._address3 = address3

    @property
    def city(self):
        """Gets the city of this TrackingAddress.  # noqa: E501


        :return: The city of this TrackingAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this TrackingAddress.


        :param city: The city of this TrackingAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state_or_province(self):
        """Gets the state_or_province of this TrackingAddress.  # noqa: E501


        :return: The state_or_province of this TrackingAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_or_province

    @state_or_province.setter
    def state_or_province(self, state_or_province):
        """Sets the state_or_province of this TrackingAddress.


        :param state_or_province: The state_or_province of this TrackingAddress.  # noqa: E501
        :type: str
        """

        self._state_or_province = state_or_province

    @property
    def postal_code(self):
        """Gets the postal_code of this TrackingAddress.  # noqa: E501


        :return: The postal_code of this TrackingAddress.  # noqa: E501
        :rtype: int
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this TrackingAddress.


        :param postal_code: The postal_code of this TrackingAddress.  # noqa: E501
        :type: int
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this TrackingAddress.  # noqa: E501


        :return: The country of this TrackingAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this TrackingAddress.


        :param country: The country of this TrackingAddress.  # noqa: E501
        :type: str
        """

        self._country = country

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
        if not isinstance(other, TrackingAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackingAddress):
            return True

        return self.to_dict() != other.to_dict()
