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


class Rate(object):
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
        'alternate_base_charge': 'float',
        'alternate_total_charge': 'float',
        'base_charge': 'float',
        'base_charge_taxes': 'list[Tax]',
        'carrier': 'Carrier',
        'currency_code': 'str',
        'delivery_commitment': 'DeliveryCommitment',
        'destination_zone': 'float',
        'dimensional_weight': 'ParcelWeight',
        'discounts': 'list[Discount]',
        'induction_postal_code': 'str',
        'parcel_type': 'ParcelType',
        'rate_type_id': 'str',
        'service_id': 'Services',
        'special_services': 'list[SpecialService]',
        'surcharges': 'list[Surcharge]',
        'total_carrier_charge': 'float',
        'total_tax_amount': 'float'
    }

    attribute_map = {
        'alternate_base_charge': 'alternateBaseCharge',
        'alternate_total_charge': 'alternateTotalCharge',
        'base_charge': 'baseCharge',
        'base_charge_taxes': 'baseChargeTaxes',
        'carrier': 'carrier',
        'currency_code': 'currencyCode',
        'delivery_commitment': 'deliveryCommitment',
        'destination_zone': 'destinationZone',
        'dimensional_weight': 'dimensionalWeight',
        'discounts': 'discounts',
        'induction_postal_code': 'inductionPostalCode',
        'parcel_type': 'parcelType',
        'rate_type_id': 'rateTypeId',
        'service_id': 'serviceId',
        'special_services': 'specialServices',
        'surcharges': 'surcharges',
        'total_carrier_charge': 'totalCarrierCharge',
        'total_tax_amount': 'totalTaxAmount'
    }

    def __init__(self, alternate_base_charge=None, alternate_total_charge=None, base_charge=None, base_charge_taxes=None, carrier=None, currency_code=None, delivery_commitment=None, destination_zone=None, dimensional_weight=None, discounts=None, induction_postal_code=None, parcel_type=None, rate_type_id=None, service_id=None, special_services=None, surcharges=None, total_carrier_charge=None, total_tax_amount=None, local_vars_configuration=None):  # noqa: E501
        """Rate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alternate_base_charge = None
        self._alternate_total_charge = None
        self._base_charge = None
        self._base_charge_taxes = None
        self._carrier = None
        self._currency_code = None
        self._delivery_commitment = None
        self._destination_zone = None
        self._dimensional_weight = None
        self._discounts = None
        self._induction_postal_code = None
        self._parcel_type = None
        self._rate_type_id = None
        self._service_id = None
        self._special_services = None
        self._surcharges = None
        self._total_carrier_charge = None
        self._total_tax_amount = None
        self.discriminator = None

        if alternate_base_charge is not None:
            self.alternate_base_charge = alternate_base_charge
        if alternate_total_charge is not None:
            self.alternate_total_charge = alternate_total_charge
        if base_charge is not None:
            self.base_charge = base_charge
        if base_charge_taxes is not None:
            self.base_charge_taxes = base_charge_taxes
        self.carrier = carrier
        if currency_code is not None:
            self.currency_code = currency_code
        if delivery_commitment is not None:
            self.delivery_commitment = delivery_commitment
        if destination_zone is not None:
            self.destination_zone = destination_zone
        if dimensional_weight is not None:
            self.dimensional_weight = dimensional_weight
        if discounts is not None:
            self.discounts = discounts
        if induction_postal_code is not None:
            self.induction_postal_code = induction_postal_code
        self.parcel_type = parcel_type
        if rate_type_id is not None:
            self.rate_type_id = rate_type_id
        if service_id is not None:
            self.service_id = service_id
        if special_services is not None:
            self.special_services = special_services
        if surcharges is not None:
            self.surcharges = surcharges
        if total_carrier_charge is not None:
            self.total_carrier_charge = total_carrier_charge
        if total_tax_amount is not None:
            self.total_tax_amount = total_tax_amount

    @property
    def alternate_base_charge(self):
        """Gets the alternate_base_charge of this Rate.  # noqa: E501


        :return: The alternate_base_charge of this Rate.  # noqa: E501
        :rtype: float
        """
        return self._alternate_base_charge

    @alternate_base_charge.setter
    def alternate_base_charge(self, alternate_base_charge):
        """Sets the alternate_base_charge of this Rate.


        :param alternate_base_charge: The alternate_base_charge of this Rate.  # noqa: E501
        :type: float
        """

        self._alternate_base_charge = alternate_base_charge

    @property
    def alternate_total_charge(self):
        """Gets the alternate_total_charge of this Rate.  # noqa: E501


        :return: The alternate_total_charge of this Rate.  # noqa: E501
        :rtype: float
        """
        return self._alternate_total_charge

    @alternate_total_charge.setter
    def alternate_total_charge(self, alternate_total_charge):
        """Sets the alternate_total_charge of this Rate.


        :param alternate_total_charge: The alternate_total_charge of this Rate.  # noqa: E501
        :type: float
        """

        self._alternate_total_charge = alternate_total_charge

    @property
    def base_charge(self):
        """Gets the base_charge of this Rate.  # noqa: E501


        :return: The base_charge of this Rate.  # noqa: E501
        :rtype: float
        """
        return self._base_charge

    @base_charge.setter
    def base_charge(self, base_charge):
        """Sets the base_charge of this Rate.


        :param base_charge: The base_charge of this Rate.  # noqa: E501
        :type: float
        """

        self._base_charge = base_charge

    @property
    def base_charge_taxes(self):
        """Gets the base_charge_taxes of this Rate.  # noqa: E501


        :return: The base_charge_taxes of this Rate.  # noqa: E501
        :rtype: list[Tax]
        """
        return self._base_charge_taxes

    @base_charge_taxes.setter
    def base_charge_taxes(self, base_charge_taxes):
        """Sets the base_charge_taxes of this Rate.


        :param base_charge_taxes: The base_charge_taxes of this Rate.  # noqa: E501
        :type: list[Tax]
        """

        self._base_charge_taxes = base_charge_taxes

    @property
    def carrier(self):
        """Gets the carrier of this Rate.  # noqa: E501


        :return: The carrier of this Rate.  # noqa: E501
        :rtype: Carrier
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this Rate.


        :param carrier: The carrier of this Rate.  # noqa: E501
        :type: Carrier
        """
        if self.local_vars_configuration.client_side_validation and carrier is None:  # noqa: E501
            raise ValueError("Invalid value for `carrier`, must not be `None`")  # noqa: E501

        self._carrier = carrier

    @property
    def currency_code(self):
        """Gets the currency_code of this Rate.  # noqa: E501

        ISO-4217  # noqa: E501

        :return: The currency_code of this Rate.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Rate.

        ISO-4217  # noqa: E501

        :param currency_code: The currency_code of this Rate.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def delivery_commitment(self):
        """Gets the delivery_commitment of this Rate.  # noqa: E501


        :return: The delivery_commitment of this Rate.  # noqa: E501
        :rtype: DeliveryCommitment
        """
        return self._delivery_commitment

    @delivery_commitment.setter
    def delivery_commitment(self, delivery_commitment):
        """Sets the delivery_commitment of this Rate.


        :param delivery_commitment: The delivery_commitment of this Rate.  # noqa: E501
        :type: DeliveryCommitment
        """

        self._delivery_commitment = delivery_commitment

    @property
    def destination_zone(self):
        """Gets the destination_zone of this Rate.  # noqa: E501


        :return: The destination_zone of this Rate.  # noqa: E501
        :rtype: float
        """
        return self._destination_zone

    @destination_zone.setter
    def destination_zone(self, destination_zone):
        """Sets the destination_zone of this Rate.


        :param destination_zone: The destination_zone of this Rate.  # noqa: E501
        :type: float
        """

        self._destination_zone = destination_zone

    @property
    def dimensional_weight(self):
        """Gets the dimensional_weight of this Rate.  # noqa: E501


        :return: The dimensional_weight of this Rate.  # noqa: E501
        :rtype: ParcelWeight
        """
        return self._dimensional_weight

    @dimensional_weight.setter
    def dimensional_weight(self, dimensional_weight):
        """Sets the dimensional_weight of this Rate.


        :param dimensional_weight: The dimensional_weight of this Rate.  # noqa: E501
        :type: ParcelWeight
        """

        self._dimensional_weight = dimensional_weight

    @property
    def discounts(self):
        """Gets the discounts of this Rate.  # noqa: E501


        :return: The discounts of this Rate.  # noqa: E501
        :rtype: list[Discount]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this Rate.


        :param discounts: The discounts of this Rate.  # noqa: E501
        :type: list[Discount]
        """

        self._discounts = discounts

    @property
    def induction_postal_code(self):
        """Gets the induction_postal_code of this Rate.  # noqa: E501


        :return: The induction_postal_code of this Rate.  # noqa: E501
        :rtype: str
        """
        return self._induction_postal_code

    @induction_postal_code.setter
    def induction_postal_code(self, induction_postal_code):
        """Sets the induction_postal_code of this Rate.


        :param induction_postal_code: The induction_postal_code of this Rate.  # noqa: E501
        :type: str
        """

        self._induction_postal_code = induction_postal_code

    @property
    def parcel_type(self):
        """Gets the parcel_type of this Rate.  # noqa: E501


        :return: The parcel_type of this Rate.  # noqa: E501
        :rtype: ParcelType
        """
        return self._parcel_type

    @parcel_type.setter
    def parcel_type(self, parcel_type):
        """Sets the parcel_type of this Rate.


        :param parcel_type: The parcel_type of this Rate.  # noqa: E501
        :type: ParcelType
        """
        if self.local_vars_configuration.client_side_validation and parcel_type is None:  # noqa: E501
            raise ValueError("Invalid value for `parcel_type`, must not be `None`")  # noqa: E501

        self._parcel_type = parcel_type

    @property
    def rate_type_id(self):
        """Gets the rate_type_id of this Rate.  # noqa: E501


        :return: The rate_type_id of this Rate.  # noqa: E501
        :rtype: str
        """
        return self._rate_type_id

    @rate_type_id.setter
    def rate_type_id(self, rate_type_id):
        """Sets the rate_type_id of this Rate.


        :param rate_type_id: The rate_type_id of this Rate.  # noqa: E501
        :type: str
        """

        self._rate_type_id = rate_type_id

    @property
    def service_id(self):
        """Gets the service_id of this Rate.  # noqa: E501


        :return: The service_id of this Rate.  # noqa: E501
        :rtype: Services
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Rate.


        :param service_id: The service_id of this Rate.  # noqa: E501
        :type: Services
        """

        self._service_id = service_id

    @property
    def special_services(self):
        """Gets the special_services of this Rate.  # noqa: E501


        :return: The special_services of this Rate.  # noqa: E501
        :rtype: list[SpecialService]
        """
        return self._special_services

    @special_services.setter
    def special_services(self, special_services):
        """Sets the special_services of this Rate.


        :param special_services: The special_services of this Rate.  # noqa: E501
        :type: list[SpecialService]
        """

        self._special_services = special_services

    @property
    def surcharges(self):
        """Gets the surcharges of this Rate.  # noqa: E501


        :return: The surcharges of this Rate.  # noqa: E501
        :rtype: list[Surcharge]
        """
        return self._surcharges

    @surcharges.setter
    def surcharges(self, surcharges):
        """Sets the surcharges of this Rate.


        :param surcharges: The surcharges of this Rate.  # noqa: E501
        :type: list[Surcharge]
        """

        self._surcharges = surcharges

    @property
    def total_carrier_charge(self):
        """Gets the total_carrier_charge of this Rate.  # noqa: E501


        :return: The total_carrier_charge of this Rate.  # noqa: E501
        :rtype: float
        """
        return self._total_carrier_charge

    @total_carrier_charge.setter
    def total_carrier_charge(self, total_carrier_charge):
        """Sets the total_carrier_charge of this Rate.


        :param total_carrier_charge: The total_carrier_charge of this Rate.  # noqa: E501
        :type: float
        """

        self._total_carrier_charge = total_carrier_charge

    @property
    def total_tax_amount(self):
        """Gets the total_tax_amount of this Rate.  # noqa: E501


        :return: The total_tax_amount of this Rate.  # noqa: E501
        :rtype: float
        """
        return self._total_tax_amount

    @total_tax_amount.setter
    def total_tax_amount(self, total_tax_amount):
        """Sets the total_tax_amount of this Rate.


        :param total_tax_amount: The total_tax_amount of this Rate.  # noqa: E501
        :type: float
        """

        self._total_tax_amount = total_tax_amount

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
        if not isinstance(other, Rate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rate):
            return True

        return self.to_dict() != other.to_dict()