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


class NtpServerExtended(object):
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
        'id': 'str',
        'key': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'name': 'name'
    }

    def __init__(self, id=None, key=None, name=None):  # noqa: E501
        """NtpServerExtended - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._key = None
        self._name = None
        self.discriminator = None

        self.id = id
        if key is not None:
            self.key = key
        self.name = name

    @property
    def id(self):
        """Gets the id of this NtpServerExtended.  # noqa: E501

        Field ID.  # noqa: E501

        :return: The id of this NtpServerExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NtpServerExtended.

        Field ID.  # noqa: E501

        :param id: The id of this NtpServerExtended.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def key(self):
        """Gets the key of this NtpServerExtended.  # noqa: E501

        Key value from key_file that maps to this server.  # noqa: E501

        :return: The key of this NtpServerExtended.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NtpServerExtended.

        Key value from key_file that maps to this server.  # noqa: E501

        :param key: The key of this NtpServerExtended.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this NtpServerExtended.  # noqa: E501

        NTP server name.  # noqa: E501

        :return: The name of this NtpServerExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NtpServerExtended.

        NTP server name.  # noqa: E501

        :param name: The name of this NtpServerExtended.  # noqa: E501
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
        if not isinstance(other, NtpServerExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
