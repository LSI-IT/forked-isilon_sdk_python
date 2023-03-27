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


class ZoneUser(object):
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
        'sid': 'str',
        'uid': 'int',
        'username': 'str'
    }

    attribute_map = {
        'sid': 'sid',
        'uid': 'uid',
        'username': 'username'
    }

    def __init__(self, sid=None, uid=None, username=None):  # noqa: E501
        """ZoneUser - a model defined in Swagger"""  # noqa: E501

        self._sid = None
        self._uid = None
        self._username = None
        self.discriminator = None

        if sid is not None:
            self.sid = sid
        if uid is not None:
            self.uid = uid
        if username is not None:
            self.username = username

    @property
    def sid(self):
        """Gets the sid of this ZoneUser.  # noqa: E501

        Specifies a security identifier.  # noqa: E501

        :return: The sid of this ZoneUser.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this ZoneUser.

        Specifies a security identifier.  # noqa: E501

        :param sid: The sid of this ZoneUser.  # noqa: E501
        :type: str
        """
        if sid is not None and len(sid) > 255:
            raise ValueError("Invalid value for `sid`, length must be less than or equal to `255`")  # noqa: E501
        if sid is not None and len(sid) < 0:
            raise ValueError("Invalid value for `sid`, length must be greater than or equal to `0`")  # noqa: E501

        self._sid = sid

    @property
    def uid(self):
        """Gets the uid of this ZoneUser.  # noqa: E501

        Specifies a numeric user identifier.  # noqa: E501

        :return: The uid of this ZoneUser.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ZoneUser.

        Specifies a numeric user identifier.  # noqa: E501

        :param uid: The uid of this ZoneUser.  # noqa: E501
        :type: int
        """
        if uid is not None and uid > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if uid is not None and uid < 0:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uid = uid

    @property
    def username(self):
        """Gets the username of this ZoneUser.  # noqa: E501

        The username associated with the sid/uid.  # noqa: E501

        :return: The username of this ZoneUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ZoneUser.

        The username associated with the sid/uid.  # noqa: E501

        :param username: The username of this ZoneUser.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 255:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if username is not None and len(username) < 0:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `0`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, ZoneUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
