# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ConfigNode(object):
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
        'id': 'int',
        'ip_addr': 'str',
        'lnn': 'int',
        'remote_ipmi_capable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'ip_addr': 'ip_addr',
        'lnn': 'lnn',
        'remote_ipmi_capable': 'remote_ipmi_capable'
    }

    def __init__(self, id=None, ip_addr=None, lnn=None, remote_ipmi_capable=None):  # noqa: E501
        """ConfigNode - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._ip_addr = None
        self._lnn = None
        self._remote_ipmi_capable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.ip_addr = ip_addr
        if lnn is not None:
            self.lnn = lnn
        if remote_ipmi_capable is not None:
            self.remote_ipmi_capable = remote_ipmi_capable

    @property
    def id(self):
        """Gets the id of this ConfigNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this ConfigNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this ConfigNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def ip_addr(self):
        """Gets the ip_addr of this ConfigNode.  # noqa: E501

        IPv4 address in the format: xxx.xxx.xxx.xxx  # noqa: E501

        :return: The ip_addr of this ConfigNode.  # noqa: E501
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this ConfigNode.

        IPv4 address in the format: xxx.xxx.xxx.xxx  # noqa: E501

        :param ip_addr: The ip_addr of this ConfigNode.  # noqa: E501
        :type: str
        """
        if ip_addr is None:
            raise ValueError("Invalid value for `ip_addr`, must not be `None`")  # noqa: E501
        if ip_addr is not None and len(ip_addr) > 45:
            raise ValueError("Invalid value for `ip_addr`, length must be less than or equal to `45`")  # noqa: E501
        if ip_addr is not None and len(ip_addr) < 2:
            raise ValueError("Invalid value for `ip_addr`, length must be greater than or equal to `2`")  # noqa: E501
        if ip_addr is not None and not re.search('^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$', ip_addr):  # noqa: E501
            raise ValueError("Invalid value for `ip_addr`, must be a follow pattern or equal to `/^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$/`")  # noqa: E501

        self._ip_addr = ip_addr

    @property
    def lnn(self):
        """Gets the lnn of this ConfigNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this ConfigNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this ConfigNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this ConfigNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def remote_ipmi_capable(self):
        """Gets the remote_ipmi_capable of this ConfigNode.  # noqa: E501

        True if the node supports the Remote IPMI Management feature  # noqa: E501

        :return: The remote_ipmi_capable of this ConfigNode.  # noqa: E501
        :rtype: bool
        """
        return self._remote_ipmi_capable

    @remote_ipmi_capable.setter
    def remote_ipmi_capable(self, remote_ipmi_capable):
        """Sets the remote_ipmi_capable of this ConfigNode.

        True if the node supports the Remote IPMI Management feature  # noqa: E501

        :param remote_ipmi_capable: The remote_ipmi_capable of this ConfigNode.  # noqa: E501
        :type: bool
        """

        self._remote_ipmi_capable = remote_ipmi_capable

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
        if not isinstance(other, ConfigNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
