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


class NetworkExternalExtended(object):
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
        'ipv6_auto_config_enabled': 'bool',
        'sbr': 'bool',
        'sc_rebalance_delay': 'int',
        'tcp_ports': 'list[int]'
    }

    attribute_map = {
        'ipv6_auto_config_enabled': 'ipv6_auto_config_enabled',
        'sbr': 'sbr',
        'sc_rebalance_delay': 'sc_rebalance_delay',
        'tcp_ports': 'tcp_ports'
    }

    def __init__(self, ipv6_auto_config_enabled=None, sbr=None, sc_rebalance_delay=None, tcp_ports=None):  # noqa: E501
        """NetworkExternalExtended - a model defined in Swagger"""  # noqa: E501

        self._ipv6_auto_config_enabled = None
        self._sbr = None
        self._sc_rebalance_delay = None
        self._tcp_ports = None
        self.discriminator = None

        if ipv6_auto_config_enabled is not None:
            self.ipv6_auto_config_enabled = ipv6_auto_config_enabled
        if sbr is not None:
            self.sbr = sbr
        if sc_rebalance_delay is not None:
            self.sc_rebalance_delay = sc_rebalance_delay
        if tcp_ports is not None:
            self.tcp_ports = tcp_ports

    @property
    def ipv6_auto_config_enabled(self):
        """Gets the ipv6_auto_config_enabled of this NetworkExternalExtended.  # noqa: E501

        True if rtsold daemon is enabled.  When set to false, the rtsold service is disabled, and IPv6 auto configuration is disabled  # noqa: E501

        :return: The ipv6_auto_config_enabled of this NetworkExternalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._ipv6_auto_config_enabled

    @ipv6_auto_config_enabled.setter
    def ipv6_auto_config_enabled(self, ipv6_auto_config_enabled):
        """Sets the ipv6_auto_config_enabled of this NetworkExternalExtended.

        True if rtsold daemon is enabled.  When set to false, the rtsold service is disabled, and IPv6 auto configuration is disabled  # noqa: E501

        :param ipv6_auto_config_enabled: The ipv6_auto_config_enabled of this NetworkExternalExtended.  # noqa: E501
        :type: bool
        """

        self._ipv6_auto_config_enabled = ipv6_auto_config_enabled

    @property
    def sbr(self):
        """Gets the sbr of this NetworkExternalExtended.  # noqa: E501

        Enable or disable Source Based Routing (Defaults to false)  # noqa: E501

        :return: The sbr of this NetworkExternalExtended.  # noqa: E501
        :rtype: bool
        """
        return self._sbr

    @sbr.setter
    def sbr(self, sbr):
        """Sets the sbr of this NetworkExternalExtended.

        Enable or disable Source Based Routing (Defaults to false)  # noqa: E501

        :param sbr: The sbr of this NetworkExternalExtended.  # noqa: E501
        :type: bool
        """

        self._sbr = sbr

    @property
    def sc_rebalance_delay(self):
        """Gets the sc_rebalance_delay of this NetworkExternalExtended.  # noqa: E501

        Delay in seconds for IP rebalance.  # noqa: E501

        :return: The sc_rebalance_delay of this NetworkExternalExtended.  # noqa: E501
        :rtype: int
        """
        return self._sc_rebalance_delay

    @sc_rebalance_delay.setter
    def sc_rebalance_delay(self, sc_rebalance_delay):
        """Sets the sc_rebalance_delay of this NetworkExternalExtended.

        Delay in seconds for IP rebalance.  # noqa: E501

        :param sc_rebalance_delay: The sc_rebalance_delay of this NetworkExternalExtended.  # noqa: E501
        :type: int
        """
        if sc_rebalance_delay is not None and sc_rebalance_delay > 10:  # noqa: E501
            raise ValueError("Invalid value for `sc_rebalance_delay`, must be a value less than or equal to `10`")  # noqa: E501
        if sc_rebalance_delay is not None and sc_rebalance_delay < 0:  # noqa: E501
            raise ValueError("Invalid value for `sc_rebalance_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sc_rebalance_delay = sc_rebalance_delay

    @property
    def tcp_ports(self):
        """Gets the tcp_ports of this NetworkExternalExtended.  # noqa: E501

        List of client TCP ports.  # noqa: E501

        :return: The tcp_ports of this NetworkExternalExtended.  # noqa: E501
        :rtype: list[int]
        """
        return self._tcp_ports

    @tcp_ports.setter
    def tcp_ports(self, tcp_ports):
        """Sets the tcp_ports of this NetworkExternalExtended.

        List of client TCP ports.  # noqa: E501

        :param tcp_ports: The tcp_ports of this NetworkExternalExtended.  # noqa: E501
        :type: list[int]
        """

        self._tcp_ports = tcp_ports

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
        if not isinstance(other, NetworkExternalExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
