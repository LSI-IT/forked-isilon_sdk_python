# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 12
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProvidersSummaryProviderInstanceConnection(object):
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
        'address': 'str',
        'last_used': 'str',
        'server': 'str'
    }

    attribute_map = {
        'address': 'address',
        'last_used': 'last_used',
        'server': 'server'
    }

    def __init__(self, address=None, last_used=None, server=None):  # noqa: E501
        """ProvidersSummaryProviderInstanceConnection - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._last_used = None
        self._server = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if last_used is not None:
            self.last_used = last_used
        if server is not None:
            self.server = server

    @property
    def address(self):
        """Gets the address of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501

        Specifies the IP address of the provider.  # noqa: E501

        :return: The address of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ProvidersSummaryProviderInstanceConnection.

        Specifies the IP address of the provider.  # noqa: E501

        :param address: The address of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501
        :type: str
        """
        if address is not None and len(address) > 255:
            raise ValueError("Invalid value for `address`, length must be less than or equal to `255`")  # noqa: E501
        if address is not None and len(address) < 0:
            raise ValueError("Invalid value for `address`, length must be greater than or equal to `0`")  # noqa: E501

        self._address = address

    @property
    def last_used(self):
        """Gets the last_used of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501

        Specifies the last time the server was contacted.  # noqa: E501

        :return: The last_used of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501
        :rtype: str
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this ProvidersSummaryProviderInstanceConnection.

        Specifies the last time the server was contacted.  # noqa: E501

        :param last_used: The last_used of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501
        :type: str
        """
        if last_used is not None and len(last_used) > 255:
            raise ValueError("Invalid value for `last_used`, length must be less than or equal to `255`")  # noqa: E501
        if last_used is not None and len(last_used) < 0:
            raise ValueError("Invalid value for `last_used`, length must be greater than or equal to `0`")  # noqa: E501

        self._last_used = last_used

    @property
    def server(self):
        """Gets the server of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501

        Specifies the fully qualified domain name of the server.  # noqa: E501

        :return: The server of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ProvidersSummaryProviderInstanceConnection.

        Specifies the fully qualified domain name of the server.  # noqa: E501

        :param server: The server of this ProvidersSummaryProviderInstanceConnection.  # noqa: E501
        :type: str
        """
        if server is not None and len(server) > 255:
            raise ValueError("Invalid value for `server`, length must be less than or equal to `255`")  # noqa: E501
        if server is not None and len(server) < 0:
            raise ValueError("Invalid value for `server`, length must be greater than or equal to `0`")  # noqa: E501

        self._server = server

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
        if not isinstance(other, ProvidersSummaryProviderInstanceConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
