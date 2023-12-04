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


class TrackingResponseScanDetailsList(object):
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
        'event_date': 'date',
        'event_time': 'str',
        'event_city': 'str',
        'event_state_or_province': 'str',
        'postal_code': 'str',
        'country': 'str',
        'scan_type': 'str',
        'scan_description': 'str',
        'package_status': 'str'
    }

    attribute_map = {
        'event_date': 'eventDate',
        'event_time': 'eventTime',
        'event_city': 'eventCity',
        'event_state_or_province': 'eventStateOrProvince',
        'postal_code': 'postalCode',
        'country': 'country',
        'scan_type': 'scanType',
        'scan_description': 'scanDescription',
        'package_status': 'packageStatus'
    }

    def __init__(self, event_date=None, event_time=None, event_city=None, event_state_or_province=None, postal_code=None, country=None, scan_type=None, scan_description=None, package_status=None, local_vars_configuration=None):  # noqa: E501
        """TrackingResponseScanDetailsList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_date = None
        self._event_time = None
        self._event_city = None
        self._event_state_or_province = None
        self._postal_code = None
        self._country = None
        self._scan_type = None
        self._scan_description = None
        self._package_status = None
        self.discriminator = None

        if event_date is not None:
            self.event_date = event_date
        if event_time is not None:
            self.event_time = event_time
        if event_city is not None:
            self.event_city = event_city
        if event_state_or_province is not None:
            self.event_state_or_province = event_state_or_province
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if scan_type is not None:
            self.scan_type = scan_type
        if scan_description is not None:
            self.scan_description = scan_description
        if package_status is not None:
            self.package_status = package_status

    @property
    def event_date(self):
        """Gets the event_date of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The event_date of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: date
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this TrackingResponseScanDetailsList.


        :param event_date: The event_date of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: date
        """

        self._event_date = event_date

    @property
    def event_time(self):
        """Gets the event_time of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The event_time of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this TrackingResponseScanDetailsList.


        :param event_time: The event_time of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: str
        """

        self._event_time = event_time

    @property
    def event_city(self):
        """Gets the event_city of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The event_city of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: str
        """
        return self._event_city

    @event_city.setter
    def event_city(self, event_city):
        """Sets the event_city of this TrackingResponseScanDetailsList.


        :param event_city: The event_city of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: str
        """

        self._event_city = event_city

    @property
    def event_state_or_province(self):
        """Gets the event_state_or_province of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The event_state_or_province of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: str
        """
        return self._event_state_or_province

    @event_state_or_province.setter
    def event_state_or_province(self, event_state_or_province):
        """Sets the event_state_or_province of this TrackingResponseScanDetailsList.


        :param event_state_or_province: The event_state_or_province of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: str
        """

        self._event_state_or_province = event_state_or_province

    @property
    def postal_code(self):
        """Gets the postal_code of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The postal_code of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: int
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this TrackingResponseScanDetailsList.


        :param postal_code: The postal_code of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: int
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The country of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this TrackingResponseScanDetailsList.


        :param country: The country of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def scan_type(self):
        """Gets the scan_type of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The scan_type of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this TrackingResponseScanDetailsList.


        :param scan_type: The scan_type of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: str
        """

        self._scan_type = scan_type

    @property
    def scan_description(self):
        """Gets the scan_description of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The scan_description of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: str
        """
        return self._scan_description

    @scan_description.setter
    def scan_description(self, scan_description):
        """Sets the scan_description of this TrackingResponseScanDetailsList.


        :param scan_description: The scan_description of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: str
        """

        self._scan_description = scan_description

    @property
    def package_status(self):
        """Gets the package_status of this TrackingResponseScanDetailsList.  # noqa: E501


        :return: The package_status of this TrackingResponseScanDetailsList.  # noqa: E501
        :rtype: str
        """
        return self._package_status

    @package_status.setter
    def package_status(self, package_status):
        """Sets the package_status of this TrackingResponseScanDetailsList.


        :param package_status: The package_status of this TrackingResponseScanDetailsList.  # noqa: E501
        :type: str
        """

        self._package_status = package_status

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
        if not isinstance(other, TrackingResponseScanDetailsList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackingResponseScanDetailsList):
            return True

        return self.to_dict() != other.to_dict()
