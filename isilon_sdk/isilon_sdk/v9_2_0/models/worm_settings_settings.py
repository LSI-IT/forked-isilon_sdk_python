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


class WormSettingsSettings(object):
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
        'cdate': 'int'
    }

    attribute_map = {
        'cdate': 'cdate'
    }

    def __init__(self, cdate=None):  # noqa: E501
        """WormSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._cdate = None
        self.discriminator = None

        if cdate is not None:
            self.cdate = cdate

    @property
    def cdate(self):
        """Gets the cdate of this WormSettingsSettings.  # noqa: E501

        Specifies the current time of the SmartLock compliance clock in Unix Epoch seconds. If the compliance clock is not set, this value is null. A PUT request will set the compliance clock date to the current system time. The cluster must be in compliance mode to set the compliance clock.  # noqa: E501

        :return: The cdate of this WormSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._cdate

    @cdate.setter
    def cdate(self, cdate):
        """Sets the cdate of this WormSettingsSettings.

        Specifies the current time of the SmartLock compliance clock in Unix Epoch seconds. If the compliance clock is not set, this value is null. A PUT request will set the compliance clock date to the current system time. The cluster must be in compliance mode to set the compliance clock.  # noqa: E501

        :param cdate: The cdate of this WormSettingsSettings.  # noqa: E501
        :type: int
        """

        self._cdate = cdate

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
        if not isinstance(other, WormSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other