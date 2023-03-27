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


class StatisticsKeyPolicy(object):
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
        'interval': 'int',
        'persistent': 'bool',
        'retention': 'int'
    }

    attribute_map = {
        'interval': 'interval',
        'persistent': 'persistent',
        'retention': 'retention'
    }

    def __init__(self, interval=None, persistent=None, retention=None):  # noqa: E501
        """StatisticsKeyPolicy - a model defined in Swagger"""  # noqa: E501

        self._interval = None
        self._persistent = None
        self._retention = None
        self.discriminator = None

        self.interval = interval
        self.persistent = persistent
        self.retention = retention

    @property
    def interval(self):
        """Gets the interval of this StatisticsKeyPolicy.  # noqa: E501

        Time between samples in seconds.  # noqa: E501

        :return: The interval of this StatisticsKeyPolicy.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this StatisticsKeyPolicy.

        Time between samples in seconds.  # noqa: E501

        :param interval: The interval of this StatisticsKeyPolicy.  # noqa: E501
        :type: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def persistent(self):
        """Gets the persistent of this StatisticsKeyPolicy.  # noqa: E501

        If true, history is persisted.  # noqa: E501

        :return: The persistent of this StatisticsKeyPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._persistent

    @persistent.setter
    def persistent(self, persistent):
        """Sets the persistent of this StatisticsKeyPolicy.

        If true, history is persisted.  # noqa: E501

        :param persistent: The persistent of this StatisticsKeyPolicy.  # noqa: E501
        :type: bool
        """
        if persistent is None:
            raise ValueError("Invalid value for `persistent`, must not be `None`")  # noqa: E501

        self._persistent = persistent

    @property
    def retention(self):
        """Gets the retention of this StatisticsKeyPolicy.  # noqa: E501

        Time in seconds to keep data.  # noqa: E501

        :return: The retention of this StatisticsKeyPolicy.  # noqa: E501
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this StatisticsKeyPolicy.

        Time in seconds to keep data.  # noqa: E501

        :param retention: The retention of this StatisticsKeyPolicy.  # noqa: E501
        :type: int
        """
        if retention is None:
            raise ValueError("Invalid value for `retention`, must not be `None`")  # noqa: E501

        self._retention = retention

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
        if not isinstance(other, StatisticsKeyPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
