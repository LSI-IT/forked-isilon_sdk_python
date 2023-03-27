# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 16
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_5_0.models.license_generate_hardware_item import LicenseGenerateHardwareItem  # noqa: F401,E501


class LicenseGenerate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'activated_license_list': 'list[str]',
        'activation': 'str',
        'hardware': 'list[LicenseGenerateHardwareItem]',
        'not_activated_license_list': 'list[str]'
    }

    attribute_map = {
        'activated_license_list': 'activated_license_list',
        'activation': 'activation',
        'hardware': 'hardware',
        'not_activated_license_list': 'not_activated_license_list'
    }

    def __init__(self, activated_license_list=None, activation=None, hardware=None, not_activated_license_list=None):  # noqa: E501
        """LicenseGenerate - a model defined in Swagger"""  # noqa: E501

        self._activated_license_list = None
        self._activation = None
        self._hardware = None
        self._not_activated_license_list = None
        self.discriminator = None

        if activated_license_list is not None:
            self.activated_license_list = activated_license_list
        if activation is not None:
            self.activation = activation
        if hardware is not None:
            self.hardware = hardware
        if not_activated_license_list is not None:
            self.not_activated_license_list = not_activated_license_list

    @property
    def activated_license_list(self):
        """Gets the activated_license_list of this LicenseGenerate.  # noqa: E501

        Array of licenses included in activation file.  # noqa: E501

        :return: The activated_license_list of this LicenseGenerate.  # noqa: E501
        :rtype: list[str]
        """
        return self._activated_license_list

    @activated_license_list.setter
    def activated_license_list(self, activated_license_list):
        """Sets the activated_license_list of this LicenseGenerate.

        Array of licenses included in activation file.  # noqa: E501

        :param activated_license_list: The activated_license_list of this LicenseGenerate.  # noqa: E501
        :type: list[str]
        """

        self._activated_license_list = activated_license_list

    @property
    def activation(self):
        """Gets the activation of this LicenseGenerate.  # noqa: E501

        Contents of licensing activation file.  # noqa: E501

        :return: The activation of this LicenseGenerate.  # noqa: E501
        :rtype: str
        """
        return self._activation

    @activation.setter
    def activation(self, activation):
        """Sets the activation of this LicenseGenerate.

        Contents of licensing activation file.  # noqa: E501

        :param activation: The activation of this LicenseGenerate.  # noqa: E501
        :type: str
        """
        if activation is not None and len(activation) > 2147483647:
            raise ValueError("Invalid value for `activation`, length must be less than or equal to `2147483647`")  # noqa: E501
        if activation is not None and len(activation) < 1:
            raise ValueError("Invalid value for `activation`, length must be greater than or equal to `1`")  # noqa: E501
        if activation is not None and not re.search('.+', activation):  # noqa: E501
            raise ValueError("Invalid value for `activation`, must be a follow pattern or equal to `/.+/`")  # noqa: E501

        self._activation = activation

    @property
    def hardware(self):
        """Gets the hardware of this LicenseGenerate.  # noqa: E501

        Array of licenses included in activation file.  # noqa: E501

        :return: The hardware of this LicenseGenerate.  # noqa: E501
        :rtype: list[LicenseGenerateHardwareItem]
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this LicenseGenerate.

        Array of licenses included in activation file.  # noqa: E501

        :param hardware: The hardware of this LicenseGenerate.  # noqa: E501
        :type: list[LicenseGenerateHardwareItem]
        """

        self._hardware = hardware

    @property
    def not_activated_license_list(self):
        """Gets the not_activated_license_list of this LicenseGenerate.  # noqa: E501

        An array of licenses not included in activation file.  # noqa: E501

        :return: The not_activated_license_list of this LicenseGenerate.  # noqa: E501
        :rtype: list[str]
        """
        return self._not_activated_license_list

    @not_activated_license_list.setter
    def not_activated_license_list(self, not_activated_license_list):
        """Sets the not_activated_license_list of this LicenseGenerate.

        An array of licenses not included in activation file.  # noqa: E501

        :param not_activated_license_list: The not_activated_license_list of this LicenseGenerate.  # noqa: E501
        :type: list[str]
        """

        self._not_activated_license_list = not_activated_license_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, LicenseGenerate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
