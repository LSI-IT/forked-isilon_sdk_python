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


class S3Key(object):
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
        'existing_key_expiry_time': 'int'
    }

    attribute_map = {
        'existing_key_expiry_time': 'existing_key_expiry_time'
    }

    def __init__(self, existing_key_expiry_time=None):  # noqa: E501
        """S3Key - a model defined in Swagger"""  # noqa: E501

        self._existing_key_expiry_time = None
        self.discriminator = None

        if existing_key_expiry_time is not None:
            self.existing_key_expiry_time = existing_key_expiry_time

    @property
    def existing_key_expiry_time(self):
        """Gets the existing_key_expiry_time of this S3Key.  # noqa: E501

        Time from now in minutes that previous secret key will expire.  # noqa: E501

        :return: The existing_key_expiry_time of this S3Key.  # noqa: E501
        :rtype: int
        """
        return self._existing_key_expiry_time

    @existing_key_expiry_time.setter
    def existing_key_expiry_time(self, existing_key_expiry_time):
        """Sets the existing_key_expiry_time of this S3Key.

        Time from now in minutes that previous secret key will expire.  # noqa: E501

        :param existing_key_expiry_time: The existing_key_expiry_time of this S3Key.  # noqa: E501
        :type: int
        """
        if existing_key_expiry_time is not None and existing_key_expiry_time > 1440:  # noqa: E501
            raise ValueError("Invalid value for `existing_key_expiry_time`, must be a value less than or equal to `1440`")  # noqa: E501
        if existing_key_expiry_time is not None and existing_key_expiry_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `existing_key_expiry_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._existing_key_expiry_time = existing_key_expiry_time

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
        if not isinstance(other, S3Key):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
