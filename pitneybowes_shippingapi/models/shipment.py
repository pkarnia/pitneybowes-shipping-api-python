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


class Shipment(object):
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
        'additional_addresses': 'list[AdditionalAddress]',
        'alt_return_address': 'Address',
        'carrier_payments': 'list[CarrierPayment]',
        'customs': 'Customs',
        'documents': 'list[Document]',
        'from_address': 'Address',
        'hazmat_details': 'HazmatDetails',
        'parcel': 'Parcel',
        'parcel_tracking_number': 'str',
        'rates': 'list[Rate]',
        'references': 'list[Parameter]',
        'shipment_id': 'str',
        'shipment_options': 'list[Parameter]',
        'shipment_type': 'str',
        'sold_to_address': 'Address',
        'to_address': 'Address'
    }

    attribute_map = {
        'additional_addresses': 'additionalAddresses',
        'alt_return_address': 'altReturnAddress',
        'carrier_payments': 'carrierPayments',
        'customs': 'customs',
        'documents': 'documents',
        'from_address': 'fromAddress',
        'hazmat_details': 'hazmatDetails',
        'parcel': 'parcel',
        'parcel_tracking_number': 'parcelTrackingNumber',
        'rates': 'rates',
        'references': 'references',
        'shipment_id': 'shipmentId',
        'shipment_options': 'shipmentOptions',
        'shipment_type': 'shipmentType',
        'sold_to_address': 'soldToAddress',
        'to_address': 'toAddress'
    }

    def __init__(self, additional_addresses=None, alt_return_address=None, carrier_payments=None, customs=None, documents=None, from_address=None, hazmat_details=None, parcel=None, parcel_tracking_number=None, rates=None, references=None, shipment_id=None, shipment_options=None, shipment_type=None, sold_to_address=None, to_address=None, local_vars_configuration=None):  # noqa: E501
        """Shipment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_addresses = None
        self._alt_return_address = None
        self._carrier_payments = None
        self._customs = None
        self._documents = None
        self._from_address = None
        self._hazmat_details = None
        self._parcel = None
        self._parcel_tracking_number = None
        self._rates = None
        self._references = None
        self._shipment_id = None
        self._shipment_options = None
        self._shipment_type = None
        self._sold_to_address = None
        self._to_address = None
        self.discriminator = None

        if additional_addresses is not None:
            self.additional_addresses = additional_addresses
        if alt_return_address is not None:
            self.alt_return_address = alt_return_address
        if carrier_payments is not None:
            self.carrier_payments = carrier_payments
        if customs is not None:
            self.customs = customs
        if documents is not None:
            self.documents = documents
        self.from_address = from_address
        if hazmat_details is not None:
            self.hazmat_details = hazmat_details
        self.parcel = parcel
        if parcel_tracking_number is not None:
            self.parcel_tracking_number = parcel_tracking_number
        self.rates = rates
        if references is not None:
            self.references = references
        if shipment_id is not None:
            self.shipment_id = shipment_id
        if shipment_options is not None:
            self.shipment_options = shipment_options
        if shipment_type is not None:
            self.shipment_type = shipment_type
        if sold_to_address is not None:
            self.sold_to_address = sold_to_address
        self.to_address = to_address

    @property
    def additional_addresses(self):
        """Gets the additional_addresses of this Shipment.  # noqa: E501


        :return: The additional_addresses of this Shipment.  # noqa: E501
        :rtype: list[AdditionalAddress]
        """
        return self._additional_addresses

    @additional_addresses.setter
    def additional_addresses(self, additional_addresses):
        """Sets the additional_addresses of this Shipment.


        :param additional_addresses: The additional_addresses of this Shipment.  # noqa: E501
        :type: list[AdditionalAddress]
        """

        self._additional_addresses = additional_addresses

    @property
    def alt_return_address(self):
        """Gets the alt_return_address of this Shipment.  # noqa: E501


        :return: The alt_return_address of this Shipment.  # noqa: E501
        :rtype: Address
        """
        return self._alt_return_address

    @alt_return_address.setter
    def alt_return_address(self, alt_return_address):
        """Sets the alt_return_address of this Shipment.


        :param alt_return_address: The alt_return_address of this Shipment.  # noqa: E501
        :type: Address
        """

        self._alt_return_address = alt_return_address

    @property
    def carrier_payments(self):
        """Gets the carrier_payments of this Shipment.  # noqa: E501


        :return: The carrier_payments of this Shipment.  # noqa: E501
        :rtype: list[CarrierPayment]
        """
        return self._carrier_payments

    @carrier_payments.setter
    def carrier_payments(self, carrier_payments):
        """Sets the carrier_payments of this Shipment.


        :param carrier_payments: The carrier_payments of this Shipment.  # noqa: E501
        :type: list[CarrierPayment]
        """

        self._carrier_payments = carrier_payments

    @property
    def customs(self):
        """Gets the customs of this Shipment.  # noqa: E501


        :return: The customs of this Shipment.  # noqa: E501
        :rtype: Customs
        """
        return self._customs

    @customs.setter
    def customs(self, customs):
        """Sets the customs of this Shipment.


        :param customs: The customs of this Shipment.  # noqa: E501
        :type: Customs
        """

        self._customs = customs

    @property
    def documents(self):
        """Gets the documents of this Shipment.  # noqa: E501


        :return: The documents of this Shipment.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Shipment.


        :param documents: The documents of this Shipment.  # noqa: E501
        :type: list[Document]
        """

        self._documents = documents

    @property
    def from_address(self):
        """Gets the from_address of this Shipment.  # noqa: E501


        :return: The from_address of this Shipment.  # noqa: E501
        :rtype: Address
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this Shipment.


        :param from_address: The from_address of this Shipment.  # noqa: E501
        :type: Address
        """
        if self.local_vars_configuration.client_side_validation and from_address is None:  # noqa: E501
            raise ValueError("Invalid value for `from_address`, must not be `None`")  # noqa: E501

        self._from_address = from_address

    @property
    def hazmat_details(self):
        """Gets the hazmat_details of this Shipment.  # noqa: E501


        :return: The hazmat_details of this Shipment.  # noqa: E501
        :rtype: HazmatDetails
        """
        return self._hazmat_details

    @hazmat_details.setter
    def hazmat_details(self, hazmat_details):
        """Sets the hazmat_details of this Shipment.


        :param hazmat_details: The hazmat_details of this Shipment.  # noqa: E501
        :type: HazmatDetails
        """

        self._hazmat_details = hazmat_details

    @property
    def parcel(self):
        """Gets the parcel of this Shipment.  # noqa: E501


        :return: The parcel of this Shipment.  # noqa: E501
        :rtype: Parcel
        """
        return self._parcel

    @parcel.setter
    def parcel(self, parcel):
        """Sets the parcel of this Shipment.


        :param parcel: The parcel of this Shipment.  # noqa: E501
        :type: Parcel
        """
        if self.local_vars_configuration.client_side_validation and parcel is None:  # noqa: E501
            raise ValueError("Invalid value for `parcel`, must not be `None`")  # noqa: E501

        self._parcel = parcel

    @property
    def parcel_tracking_number(self):
        """Gets the parcel_tracking_number of this Shipment.  # noqa: E501


        :return: The parcel_tracking_number of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._parcel_tracking_number

    @parcel_tracking_number.setter
    def parcel_tracking_number(self, parcel_tracking_number):
        """Sets the parcel_tracking_number of this Shipment.


        :param parcel_tracking_number: The parcel_tracking_number of this Shipment.  # noqa: E501
        :type: str
        """

        self._parcel_tracking_number = parcel_tracking_number

    @property
    def rates(self):
        """Gets the rates of this Shipment.  # noqa: E501


        :return: The rates of this Shipment.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this Shipment.


        :param rates: The rates of this Shipment.  # noqa: E501
        :type: list[Rate]
        """
        if self.local_vars_configuration.client_side_validation and rates is None:  # noqa: E501
            raise ValueError("Invalid value for `rates`, must not be `None`")  # noqa: E501

        self._rates = rates

    @property
    def references(self):
        """Gets the references of this Shipment.  # noqa: E501


        :return: The references of this Shipment.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this Shipment.


        :param references: The references of this Shipment.  # noqa: E501
        :type: list[Parameter]
        """

        self._references = references

    @property
    def shipment_id(self):
        """Gets the shipment_id of this Shipment.  # noqa: E501


        :return: The shipment_id of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, shipment_id):
        """Sets the shipment_id of this Shipment.


        :param shipment_id: The shipment_id of this Shipment.  # noqa: E501
        :type: str
        """

        self._shipment_id = shipment_id

    @property
    def shipment_options(self):
        """Gets the shipment_options of this Shipment.  # noqa: E501


        :return: The shipment_options of this Shipment.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._shipment_options

    @shipment_options.setter
    def shipment_options(self, shipment_options):
        """Sets the shipment_options of this Shipment.


        :param shipment_options: The shipment_options of this Shipment.  # noqa: E501
        :type: list[Parameter]
        """

        self._shipment_options = shipment_options

    @property
    def shipment_type(self):
        """Gets the shipment_type of this Shipment.  # noqa: E501


        :return: The shipment_type of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._shipment_type

    @shipment_type.setter
    def shipment_type(self, shipment_type):
        """Sets the shipment_type of this Shipment.


        :param shipment_type: The shipment_type of this Shipment.  # noqa: E501
        :type: str
        """
        allowed_values = ["OUTBOUND", "RETURN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and shipment_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `shipment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(shipment_type, allowed_values)
            )

        self._shipment_type = shipment_type

    @property
    def sold_to_address(self):
        """Gets the sold_to_address of this Shipment.  # noqa: E501


        :return: The sold_to_address of this Shipment.  # noqa: E501
        :rtype: Address
        """
        return self._sold_to_address

    @sold_to_address.setter
    def sold_to_address(self, sold_to_address):
        """Sets the sold_to_address of this Shipment.


        :param sold_to_address: The sold_to_address of this Shipment.  # noqa: E501
        :type: Address
        """

        self._sold_to_address = sold_to_address

    @property
    def to_address(self):
        """Gets the to_address of this Shipment.  # noqa: E501


        :return: The to_address of this Shipment.  # noqa: E501
        :rtype: Address
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """Sets the to_address of this Shipment.


        :param to_address: The to_address of this Shipment.  # noqa: E501
        :type: Address
        """
        if self.local_vars_configuration.client_side_validation and to_address is None:  # noqa: E501
            raise ValueError("Invalid value for `to_address`, must not be `None`")  # noqa: E501

        self._to_address = to_address

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
        if not isinstance(other, Shipment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Shipment):
            return True

        return self.to_dict() != other.to_dict()