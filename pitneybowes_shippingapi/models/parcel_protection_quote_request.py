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


class ParcelProtectionQuoteRequest(object):
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
        'parcel_protection_account_id': 'str',
        'parcel_protection_program_id': 'str',
        'shipment_info': 'ParcelProtectionQuoteRequestShipmentInfo'
    }

    attribute_map = {
        'parcel_protection_account_id': 'parcelProtectionAccountID',
        'parcel_protection_program_id': 'parcelProtectionProgramID',
        'shipment_info': 'shipmentInfo'
    }

    def __init__(self, parcel_protection_account_id=None, parcel_protection_program_id=None, shipment_info=None, local_vars_configuration=None):  # noqa: E501
        """ParcelProtectionQuoteRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parcel_protection_account_id = None
        self._parcel_protection_program_id = None
        self._shipment_info = None
        self.discriminator = None

        if parcel_protection_account_id is not None:
            self.parcel_protection_account_id = parcel_protection_account_id
        if parcel_protection_program_id is not None:
            self.parcel_protection_program_id = parcel_protection_program_id
        self.shipment_info = shipment_info

    @property
    def parcel_protection_account_id(self):
        """Gets the parcel_protection_account_id of this ParcelProtectionQuoteRequest.  # noqa: E501


        :return: The parcel_protection_account_id of this ParcelProtectionQuoteRequest.  # noqa: E501
        :rtype: str
        """
        return self._parcel_protection_account_id

    @parcel_protection_account_id.setter
    def parcel_protection_account_id(self, parcel_protection_account_id):
        """Sets the parcel_protection_account_id of this ParcelProtectionQuoteRequest.


        :param parcel_protection_account_id: The parcel_protection_account_id of this ParcelProtectionQuoteRequest.  # noqa: E501
        :type: str
        """

        self._parcel_protection_account_id = parcel_protection_account_id

    @property
    def parcel_protection_program_id(self):
        """Gets the parcel_protection_program_id of this ParcelProtectionQuoteRequest.  # noqa: E501


        :return: The parcel_protection_program_id of this ParcelProtectionQuoteRequest.  # noqa: E501
        :rtype: str
        """
        return self._parcel_protection_program_id

    @parcel_protection_program_id.setter
    def parcel_protection_program_id(self, parcel_protection_program_id):
        """Sets the parcel_protection_program_id of this ParcelProtectionQuoteRequest.


        :param parcel_protection_program_id: The parcel_protection_program_id of this ParcelProtectionQuoteRequest.  # noqa: E501
        :type: str
        """

        self._parcel_protection_program_id = parcel_protection_program_id

    @property
    def shipment_info(self):
        """Gets the shipment_info of this ParcelProtectionQuoteRequest.  # noqa: E501


        :return: The shipment_info of this ParcelProtectionQuoteRequest.  # noqa: E501
        :rtype: ParcelProtectionQuoteRequestShipmentInfo
        """
        return self._shipment_info

    @shipment_info.setter
    def shipment_info(self, shipment_info):
        """Sets the shipment_info of this ParcelProtectionQuoteRequest.


        :param shipment_info: The shipment_info of this ParcelProtectionQuoteRequest.  # noqa: E501
        :type: ParcelProtectionQuoteRequestShipmentInfo
        """
        if self.local_vars_configuration.client_side_validation and shipment_info is None:  # noqa: E501
            raise ValueError("Invalid value for `shipment_info`, must not be `None`")  # noqa: E501

        self._shipment_info = shipment_info

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
        if not isinstance(other, ParcelProtectionQuoteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParcelProtectionQuoteRequest):
            return True

        return self.to_dict() != other.to_dict()
