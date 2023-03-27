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


class SnapshotLock(object):
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
        'expires': 'int'
    }

    attribute_map = {
        'expires': 'expires'
    }

    def __init__(self, expires=None):  # noqa: E501
        """SnapshotLock - a model defined in Swagger"""  # noqa: E501

        self._expires = None
        self.discriminator = None

        if expires is not None:
            self.expires = expires

    @property
    def expires(self):
        """Gets the expires of this SnapshotLock.  # noqa: E501

        The Unix Epoch time the snapshot lock will expire and be eligible for automatic deletion.  # noqa: E501

        :return: The expires of this SnapshotLock.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this SnapshotLock.

        The Unix Epoch time the snapshot lock will expire and be eligible for automatic deletion.  # noqa: E501

        :param expires: The expires of this SnapshotLock.  # noqa: E501
        :type: int
        """
        if expires is not None and expires > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `expires`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if expires is not None and expires < 1:  # noqa: E501
            raise ValueError("Invalid value for `expires`, must be a value greater than or equal to `1`")  # noqa: E501

        self._expires = expires

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
        if not isinstance(other, SnapshotLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
