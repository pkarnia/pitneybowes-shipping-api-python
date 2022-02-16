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


class CustomsItem(object):
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
        'description': 'str',
        'h_s_tariff_code': 'str',
        'net_cost_method': 'str',
        'origin_country_code': 'str',
        'origin_state_province': 'str',
        'preference_criterion': 'str',
        'producer_address': 'Address',
        'producer_determination': 'str',
        'producer_id': 'str',
        'quantity': 'int',
        'quantity_uom': 'str',
        'unit_price': 'float',
        'unit_weight': 'ParcelWeight'
    }

    attribute_map = {
        'description': 'description',
        'h_s_tariff_code': 'hSTariffCode',
        'net_cost_method': 'netCostMethod',
        'origin_country_code': 'originCountryCode',
        'origin_state_province': 'originStateProvince',
        'preference_criterion': 'preferenceCriterion',
        'producer_address': 'producerAddress',
        'producer_determination': 'producerDetermination',
        'producer_id': 'producerId',
        'quantity': 'quantity',
        'quantity_uom': 'quantityUOM',
        'unit_price': 'unitPrice',
        'unit_weight': 'unitWeight'
    }

    def __init__(self, description=None, h_s_tariff_code=None, net_cost_method=None, origin_country_code=None, origin_state_province=None, preference_criterion=None, producer_address=None, producer_determination=None, producer_id=None, quantity=None, quantity_uom=None, unit_price=None, unit_weight=None, local_vars_configuration=None):  # noqa: E501
        """CustomsItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._h_s_tariff_code = None
        self._net_cost_method = None
        self._origin_country_code = None
        self._origin_state_province = None
        self._preference_criterion = None
        self._producer_address = None
        self._producer_determination = None
        self._producer_id = None
        self._quantity = None
        self._quantity_uom = None
        self._unit_price = None
        self._unit_weight = None
        self.discriminator = None

        self.description = description
        if h_s_tariff_code is not None:
            self.h_s_tariff_code = h_s_tariff_code
        if net_cost_method is not None:
            self.net_cost_method = net_cost_method
        self.origin_country_code = origin_country_code
        if origin_state_province is not None:
            self.origin_state_province = origin_state_province
        if preference_criterion is not None:
            self.preference_criterion = preference_criterion
        if producer_address is not None:
            self.producer_address = producer_address
        if producer_determination is not None:
            self.producer_determination = producer_determination
        if producer_id is not None:
            self.producer_id = producer_id
        self.quantity = quantity
        if quantity_uom is not None:
            self.quantity_uom = quantity_uom
        self.unit_price = unit_price
        self.unit_weight = unit_weight

    @property
    def description(self):
        """Gets the description of this CustomsItem.  # noqa: E501


        :return: The description of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomsItem.


        :param description: The description of this CustomsItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def h_s_tariff_code(self):
        """Gets the h_s_tariff_code of this CustomsItem.  # noqa: E501


        :return: The h_s_tariff_code of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._h_s_tariff_code

    @h_s_tariff_code.setter
    def h_s_tariff_code(self, h_s_tariff_code):
        """Sets the h_s_tariff_code of this CustomsItem.


        :param h_s_tariff_code: The h_s_tariff_code of this CustomsItem.  # noqa: E501
        :type: str
        """

        self._h_s_tariff_code = h_s_tariff_code

    @property
    def net_cost_method(self):
        """Gets the net_cost_method of this CustomsItem.  # noqa: E501


        :return: The net_cost_method of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._net_cost_method

    @net_cost_method.setter
    def net_cost_method(self, net_cost_method):
        """Sets the net_cost_method of this CustomsItem.


        :param net_cost_method: The net_cost_method of this CustomsItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_NET_COST", "NET_COST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and net_cost_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `net_cost_method` ({0}), must be one of {1}"  # noqa: E501
                .format(net_cost_method, allowed_values)
            )

        self._net_cost_method = net_cost_method

    @property
    def origin_country_code(self):
        """Gets the origin_country_code of this CustomsItem.  # noqa: E501


        :return: The origin_country_code of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._origin_country_code

    @origin_country_code.setter
    def origin_country_code(self, origin_country_code):
        """Sets the origin_country_code of this CustomsItem.


        :param origin_country_code: The origin_country_code of this CustomsItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and origin_country_code is None:  # noqa: E501
            raise ValueError("Invalid value for `origin_country_code`, must not be `None`")  # noqa: E501

        self._origin_country_code = origin_country_code

    @property
    def origin_state_province(self):
        """Gets the origin_state_province of this CustomsItem.  # noqa: E501


        :return: The origin_state_province of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._origin_state_province

    @origin_state_province.setter
    def origin_state_province(self, origin_state_province):
        """Sets the origin_state_province of this CustomsItem.


        :param origin_state_province: The origin_state_province of this CustomsItem.  # noqa: E501
        :type: str
        """

        self._origin_state_province = origin_state_province

    @property
    def preference_criterion(self):
        """Gets the preference_criterion of this CustomsItem.  # noqa: E501


        :return: The preference_criterion of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._preference_criterion

    @preference_criterion.setter
    def preference_criterion(self, preference_criterion):
        """Sets the preference_criterion of this CustomsItem.


        :param preference_criterion: The preference_criterion of this CustomsItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "B", "C", "D", "E", "F"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and preference_criterion not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `preference_criterion` ({0}), must be one of {1}"  # noqa: E501
                .format(preference_criterion, allowed_values)
            )

        self._preference_criterion = preference_criterion

    @property
    def producer_address(self):
        """Gets the producer_address of this CustomsItem.  # noqa: E501


        :return: The producer_address of this CustomsItem.  # noqa: E501
        :rtype: Address
        """
        return self._producer_address

    @producer_address.setter
    def producer_address(self, producer_address):
        """Sets the producer_address of this CustomsItem.


        :param producer_address: The producer_address of this CustomsItem.  # noqa: E501
        :type: Address
        """

        self._producer_address = producer_address

    @property
    def producer_determination(self):
        """Gets the producer_determination of this CustomsItem.  # noqa: E501


        :return: The producer_determination of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._producer_determination

    @producer_determination.setter
    def producer_determination(self, producer_determination):
        """Sets the producer_determination of this CustomsItem.


        :param producer_determination: The producer_determination of this CustomsItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["NO_1", "NO_2", "NO_3", "PD_YES"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and producer_determination not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `producer_determination` ({0}), must be one of {1}"  # noqa: E501
                .format(producer_determination, allowed_values)
            )

        self._producer_determination = producer_determination

    @property
    def producer_id(self):
        """Gets the producer_id of this CustomsItem.  # noqa: E501


        :return: The producer_id of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._producer_id

    @producer_id.setter
    def producer_id(self, producer_id):
        """Sets the producer_id of this CustomsItem.


        :param producer_id: The producer_id of this CustomsItem.  # noqa: E501
        :type: str
        """

        self._producer_id = producer_id

    @property
    def quantity(self):
        """Gets the quantity of this CustomsItem.  # noqa: E501


        :return: The quantity of this CustomsItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CustomsItem.


        :param quantity: The quantity of this CustomsItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def quantity_uom(self):
        """Gets the quantity_uom of this CustomsItem.  # noqa: E501


        :return: The quantity_uom of this CustomsItem.  # noqa: E501
        :rtype: str
        """
        return self._quantity_uom

    @quantity_uom.setter
    def quantity_uom(self, quantity_uom):
        """Sets the quantity_uom of this CustomsItem.


        :param quantity_uom: The quantity_uom of this CustomsItem.  # noqa: E501
        :type: str
        """

        self._quantity_uom = quantity_uom

    @property
    def unit_price(self):
        """Gets the unit_price of this CustomsItem.  # noqa: E501


        :return: The unit_price of this CustomsItem.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this CustomsItem.


        :param unit_price: The unit_price of this CustomsItem.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and unit_price is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

    @property
    def unit_weight(self):
        """Gets the unit_weight of this CustomsItem.  # noqa: E501


        :return: The unit_weight of this CustomsItem.  # noqa: E501
        :rtype: ParcelWeight
        """
        return self._unit_weight

    @unit_weight.setter
    def unit_weight(self, unit_weight):
        """Sets the unit_weight of this CustomsItem.


        :param unit_weight: The unit_weight of this CustomsItem.  # noqa: E501
        :type: ParcelWeight
        """
        if self.local_vars_configuration.client_side_validation and unit_weight is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_weight`, must not be `None`")  # noqa: E501

        self._unit_weight = unit_weight

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
        if not isinstance(other, CustomsItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomsItem):
            return True

        return self.to_dict() != other.to_dict()