# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SummaryProtocolStatsProtocolStatsCpu(object):
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
        'idle': 'float',
        'system': 'float',
        'user': 'float'
    }

    attribute_map = {
        'idle': 'idle',
        'system': 'system',
        'user': 'user'
    }

    def __init__(self, idle=None, system=None, user=None):  # noqa: E501
        """SummaryProtocolStatsProtocolStatsCpu - a model defined in Swagger"""  # noqa: E501

        self._idle = None
        self._system = None
        self._user = None
        self.discriminator = None

        self.idle = idle
        self.system = system
        self.user = user

    @property
    def idle(self):
        """Gets the idle of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501

        Percentage of CPU idle time  # noqa: E501

        :return: The idle of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501
        :rtype: float
        """
        return self._idle

    @idle.setter
    def idle(self, idle):
        """Sets the idle of this SummaryProtocolStatsProtocolStatsCpu.

        Percentage of CPU idle time  # noqa: E501

        :param idle: The idle of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501
        :type: float
        """
        if idle is None:
            raise ValueError("Invalid value for `idle`, must not be `None`")  # noqa: E501

        self._idle = idle

    @property
    def system(self):
        """Gets the system of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501

        Percentage of CPU consumed by the system  # noqa: E501

        :return: The system of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501
        :rtype: float
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this SummaryProtocolStatsProtocolStatsCpu.

        Percentage of CPU consumed by the system  # noqa: E501

        :param system: The system of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501
        :type: float
        """
        if system is None:
            raise ValueError("Invalid value for `system`, must not be `None`")  # noqa: E501

        self._system = system

    @property
    def user(self):
        """Gets the user of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501

        Percentage of CPU consumed by user activities  # noqa: E501

        :return: The user of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501
        :rtype: float
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SummaryProtocolStatsProtocolStatsCpu.

        Percentage of CPU consumed by user activities  # noqa: E501

        :param user: The user of this SummaryProtocolStatsProtocolStatsCpu.  # noqa: E501
        :type: float
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, SummaryProtocolStatsProtocolStatsCpu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
