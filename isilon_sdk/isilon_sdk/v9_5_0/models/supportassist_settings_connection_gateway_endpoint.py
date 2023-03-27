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


class SupportassistSettingsConnectionGatewayEndpoint(object):
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
        'enabled': 'bool',
        'host': 'str',
        'port': 'int',
        'priority': 'int',
        'use_proxy': 'bool',
        'validate_ssl': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'host': 'host',
        'port': 'port',
        'priority': 'priority',
        'use_proxy': 'use_proxy',
        'validate_ssl': 'validate_ssl'
    }

    def __init__(self, enabled=True, host=None, port=None, priority=None, use_proxy=False, validate_ssl=False):  # noqa: E501
        """SupportassistSettingsConnectionGatewayEndpoint - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._host = None
        self._port = None
        self._priority = None
        self._use_proxy = None
        self._validate_ssl = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        self.host = host
        if port is not None:
            self.port = port
        if priority is not None:
            self.priority = priority
        if use_proxy is not None:
            self.use_proxy = use_proxy
        if validate_ssl is not None:
            self.validate_ssl = validate_ssl

    @property
    def enabled(self):
        """Gets the enabled of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501

        Whether this gateway is enabled/disabled  # noqa: E501

        :return: The enabled of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SupportassistSettingsConnectionGatewayEndpoint.

        Whether this gateway is enabled/disabled  # noqa: E501

        :param enabled: The enabled of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def host(self):
        """Gets the host of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501

        Gateway hostname or IPv4 address  # noqa: E501

        :return: The host of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SupportassistSettingsConnectionGatewayEndpoint.

        Gateway hostname or IPv4 address  # noqa: E501

        :param host: The host of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501
        if host is not None and len(host) > 255:
            raise ValueError("Invalid value for `host`, length must be less than or equal to `255`")  # noqa: E501
        if host is not None and len(host) < 0:
            raise ValueError("Invalid value for `host`, length must be greater than or equal to `0`")  # noqa: E501
        if host is not None and not re.search('(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$)', host):  # noqa: E501
            raise ValueError("Invalid value for `host`, must be a follow pattern or equal to `/(^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$|^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$)/`")  # noqa: E501

        self._host = host

    @property
    def port(self):
        """Gets the port of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501

        Gateway port  # noqa: E501

        :return: The port of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SupportassistSettingsConnectionGatewayEndpoint.

        Gateway port  # noqa: E501

        :param port: The port of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :type: int
        """
        if port is not None and port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if port is not None and port < 1:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

    @property
    def priority(self):
        """Gets the priority of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501

        Gateway's priority  # noqa: E501

        :return: The priority of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this SupportassistSettingsConnectionGatewayEndpoint.

        Gateway's priority  # noqa: E501

        :param priority: The priority of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :type: int
        """
        if priority is not None and priority > 4:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `4`")  # noqa: E501
        if priority is not None and priority < 1:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `1`")  # noqa: E501

        self._priority = priority

    @property
    def use_proxy(self):
        """Gets the use_proxy of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501

        Whether to use Proxy for this gateway  # noqa: E501

        :return: The use_proxy of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :rtype: bool
        """
        return self._use_proxy

    @use_proxy.setter
    def use_proxy(self, use_proxy):
        """Sets the use_proxy of this SupportassistSettingsConnectionGatewayEndpoint.

        Whether to use Proxy for this gateway  # noqa: E501

        :param use_proxy: The use_proxy of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :type: bool
        """

        self._use_proxy = use_proxy

    @property
    def validate_ssl(self):
        """Gets the validate_ssl of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501

        Whether to validate SSL for this gateway  # noqa: E501

        :return: The validate_ssl of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :rtype: bool
        """
        return self._validate_ssl

    @validate_ssl.setter
    def validate_ssl(self, validate_ssl):
        """Sets the validate_ssl of this SupportassistSettingsConnectionGatewayEndpoint.

        Whether to validate SSL for this gateway  # noqa: E501

        :param validate_ssl: The validate_ssl of this SupportassistSettingsConnectionGatewayEndpoint.  # noqa: E501
        :type: bool
        """

        self._validate_ssl = validate_ssl

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
        if not isinstance(other, SupportassistSettingsConnectionGatewayEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other