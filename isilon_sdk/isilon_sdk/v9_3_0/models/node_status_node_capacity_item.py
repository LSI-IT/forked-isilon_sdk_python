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


class NodeStatusNodeCapacityItem(object):
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
        'bytes': 'int',
        'count': 'int',
        'type': 'str'
    }

    attribute_map = {
        'bytes': 'bytes',
        'count': 'count',
        'type': 'type'
    }

    def __init__(self, bytes=None, count=None, type=None):  # noqa: E501
        """NodeStatusNodeCapacityItem - a model defined in Swagger"""  # noqa: E501

        self._bytes = None
        self._count = None
        self._type = None
        self.discriminator = None

        if bytes is not None:
            self.bytes = bytes
        if count is not None:
            self.count = count
        if type is not None:
            self.type = type

    @property
    def bytes(self):
        """Gets the bytes of this NodeStatusNodeCapacityItem.  # noqa: E501

        Total device storage bytes.  # noqa: E501

        :return: The bytes of this NodeStatusNodeCapacityItem.  # noqa: E501
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this NodeStatusNodeCapacityItem.

        Total device storage bytes.  # noqa: E501

        :param bytes: The bytes of this NodeStatusNodeCapacityItem.  # noqa: E501
        :type: int
        """
        if bytes is not None and bytes > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `bytes`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if bytes is not None and bytes < 0:  # noqa: E501
            raise ValueError("Invalid value for `bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bytes = bytes

    @property
    def count(self):
        """Gets the count of this NodeStatusNodeCapacityItem.  # noqa: E501

        Total device count.  # noqa: E501

        :return: The count of this NodeStatusNodeCapacityItem.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NodeStatusNodeCapacityItem.

        Total device count.  # noqa: E501

        :param count: The count of this NodeStatusNodeCapacityItem.  # noqa: E501
        :type: int
        """
        if count is not None and count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def type(self):
        """Gets the type of this NodeStatusNodeCapacityItem.  # noqa: E501

        Device type.  # noqa: E501

        :return: The type of this NodeStatusNodeCapacityItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeStatusNodeCapacityItem.

        Device type.  # noqa: E501

        :param type: The type of this NodeStatusNodeCapacityItem.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) > 255:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `255`")  # noqa: E501
        if type is not None and len(type) < 0:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `0`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, NodeStatusNodeCapacityItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other