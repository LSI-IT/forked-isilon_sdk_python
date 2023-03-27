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

from isilon_sdk.v9_2_1.models.config_network_network_range import ConfigNetworkNetworkRange  # noqa: F401,E501


class ConfigNetworkNetwork(object):
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
        'gateway': 'str',
        'prefixlen': 'int',
        'ranges': 'list[ConfigNetworkNetworkRange]'
    }

    attribute_map = {
        'gateway': 'gateway',
        'prefixlen': 'prefixlen',
        'ranges': 'ranges'
    }

    def __init__(self, gateway=None, prefixlen=None, ranges=None):  # noqa: E501
        """ConfigNetworkNetwork - a model defined in Swagger"""  # noqa: E501

        self._gateway = None
        self._prefixlen = None
        self._ranges = None
        self.discriminator = None

        if gateway is not None:
            self.gateway = gateway
        if prefixlen is not None:
            self.prefixlen = prefixlen
        if ranges is not None:
            self.ranges = ranges

    @property
    def gateway(self):
        """Gets the gateway of this ConfigNetworkNetwork.  # noqa: E501

        IPv4 address in the format: xxx.xxx.xxx.xxx  # noqa: E501

        :return: The gateway of this ConfigNetworkNetwork.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this ConfigNetworkNetwork.

        IPv4 address in the format: xxx.xxx.xxx.xxx  # noqa: E501

        :param gateway: The gateway of this ConfigNetworkNetwork.  # noqa: E501
        :type: str
        """
        if gateway is not None and len(gateway) > 45:
            raise ValueError("Invalid value for `gateway`, length must be less than or equal to `45`")  # noqa: E501
        if gateway is not None and len(gateway) < 2:
            raise ValueError("Invalid value for `gateway`, length must be greater than or equal to `2`")  # noqa: E501
        if gateway is not None and not re.search('^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$', gateway):  # noqa: E501
            raise ValueError("Invalid value for `gateway`, must be a follow pattern or equal to `/^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$/`")  # noqa: E501

        self._gateway = gateway

    @property
    def prefixlen(self):
        """Gets the prefixlen of this ConfigNetworkNetwork.  # noqa: E501

        Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask.  # noqa: E501

        :return: The prefixlen of this ConfigNetworkNetwork.  # noqa: E501
        :rtype: int
        """
        return self._prefixlen

    @prefixlen.setter
    def prefixlen(self, prefixlen):
        """Sets the prefixlen of this ConfigNetworkNetwork.

        Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask.  # noqa: E501

        :param prefixlen: The prefixlen of this ConfigNetworkNetwork.  # noqa: E501
        :type: int
        """
        if prefixlen is not None and prefixlen > 32:  # noqa: E501
            raise ValueError("Invalid value for `prefixlen`, must be a value less than or equal to `32`")  # noqa: E501
        if prefixlen is not None and prefixlen < 0:  # noqa: E501
            raise ValueError("Invalid value for `prefixlen`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prefixlen = prefixlen

    @property
    def ranges(self):
        """Gets the ranges of this ConfigNetworkNetwork.  # noqa: E501

        List of IP address ranges.  # noqa: E501

        :return: The ranges of this ConfigNetworkNetwork.  # noqa: E501
        :rtype: list[ConfigNetworkNetworkRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """Sets the ranges of this ConfigNetworkNetwork.

        List of IP address ranges.  # noqa: E501

        :param ranges: The ranges of this ConfigNetworkNetwork.  # noqa: E501
        :type: list[ConfigNetworkNetworkRange]
        """

        self._ranges = ranges

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
        if not isinstance(other, ConfigNetworkNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
