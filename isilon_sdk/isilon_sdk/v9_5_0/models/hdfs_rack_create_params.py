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

from isilon_sdk.v9_5_0.models.hdfs_rack import HdfsRack  # noqa: F401,E501


class HdfsRackCreateParams(object):
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
        'client_ip_ranges': 'list[str]',
        'ip_pools': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'client_ip_ranges': 'client_ip_ranges',
        'ip_pools': 'ip_pools',
        'name': 'name'
    }

    def __init__(self, client_ip_ranges=None, ip_pools=None, name=None):  # noqa: E501
        """HdfsRackCreateParams - a model defined in Swagger"""  # noqa: E501

        self._client_ip_ranges = None
        self._ip_pools = None
        self._name = None
        self.discriminator = None

        if client_ip_ranges is not None:
            self.client_ip_ranges = client_ip_ranges
        if ip_pools is not None:
            self.ip_pools = ip_pools
        self.name = name

    @property
    def client_ip_ranges(self):
        """Gets the client_ip_ranges of this HdfsRackCreateParams.  # noqa: E501

        Array of IP ranges. Clients from one of these IP ranges are served by corresponding nodes from ip_pools array.  # noqa: E501

        :return: The client_ip_ranges of this HdfsRackCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_ip_ranges

    @client_ip_ranges.setter
    def client_ip_ranges(self, client_ip_ranges):
        """Sets the client_ip_ranges of this HdfsRackCreateParams.

        Array of IP ranges. Clients from one of these IP ranges are served by corresponding nodes from ip_pools array.  # noqa: E501

        :param client_ip_ranges: The client_ip_ranges of this HdfsRackCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._client_ip_ranges = client_ip_ranges

    @property
    def ip_pools(self):
        """Gets the ip_pools of this HdfsRackCreateParams.  # noqa: E501

        Array of IP pool names to use for serving clients from client_ip_ranges.  # noqa: E501

        :return: The ip_pools of this HdfsRackCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_pools

    @ip_pools.setter
    def ip_pools(self, ip_pools):
        """Sets the ip_pools of this HdfsRackCreateParams.

        Array of IP pool names to use for serving clients from client_ip_ranges.  # noqa: E501

        :param ip_pools: The ip_pools of this HdfsRackCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._ip_pools = ip_pools

    @property
    def name(self):
        """Gets the name of this HdfsRackCreateParams.  # noqa: E501

        Name of the rack  # noqa: E501

        :return: The name of this HdfsRackCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HdfsRackCreateParams.

        Name of the rack  # noqa: E501

        :param name: The name of this HdfsRackCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, HdfsRackCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
