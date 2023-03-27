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


class SubnetsSubnetPoolRange(object):
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
        'high': 'str',
        'low': 'str'
    }

    attribute_map = {
        'high': 'high',
        'low': 'low'
    }

    def __init__(self, high=None, low=None):  # noqa: E501
        """SubnetsSubnetPoolRange - a model defined in Swagger"""  # noqa: E501

        self._high = None
        self._low = None
        self.discriminator = None

        self.high = high
        self.low = low

    @property
    def high(self):
        """Gets the high of this SubnetsSubnetPoolRange.  # noqa: E501

        High IP  # noqa: E501

        :return: The high of this SubnetsSubnetPoolRange.  # noqa: E501
        :rtype: str
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this SubnetsSubnetPoolRange.

        High IP  # noqa: E501

        :param high: The high of this SubnetsSubnetPoolRange.  # noqa: E501
        :type: str
        """
        if high is None:
            raise ValueError("Invalid value for `high`, must not be `None`")  # noqa: E501
        if high is not None and len(high) > 40:
            raise ValueError("Invalid value for `high`, length must be less than or equal to `40`")  # noqa: E501
        if high is not None and len(high) < 1:
            raise ValueError("Invalid value for `high`, length must be greater than or equal to `1`")  # noqa: E501
        if high is not None and not re.search('(^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)', high):  # noqa: E501
            raise ValueError("Invalid value for `high`, must be a follow pattern or equal to `/(^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)/`")  # noqa: E501

        self._high = high

    @property
    def low(self):
        """Gets the low of this SubnetsSubnetPoolRange.  # noqa: E501

        Low IP  # noqa: E501

        :return: The low of this SubnetsSubnetPoolRange.  # noqa: E501
        :rtype: str
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this SubnetsSubnetPoolRange.

        Low IP  # noqa: E501

        :param low: The low of this SubnetsSubnetPoolRange.  # noqa: E501
        :type: str
        """
        if low is None:
            raise ValueError("Invalid value for `low`, must not be `None`")  # noqa: E501
        if low is not None and len(low) > 40:
            raise ValueError("Invalid value for `low`, length must be less than or equal to `40`")  # noqa: E501
        if low is not None and len(low) < 1:
            raise ValueError("Invalid value for `low`, length must be greater than or equal to `1`")  # noqa: E501
        if low is not None and not re.search('(^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)', low):  # noqa: E501
            raise ValueError("Invalid value for `low`, must be a follow pattern or equal to `/(^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5}::([0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){0,5})?$|^[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7}$)/`")  # noqa: E501

        self._low = low

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
        if not isinstance(other, SubnetsSubnetPoolRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
