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

from isilon_sdk.v9_5_0.models.s3_settings_zone_settings import S3SettingsZoneSettings  # noqa: F401,E501


class S3SettingsZone(object):
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
        'settings': 'S3SettingsZoneSettings'
    }

    attribute_map = {
        'settings': 'settings'
    }

    def __init__(self, settings=None):  # noqa: E501
        """S3SettingsZone - a model defined in Swagger"""  # noqa: E501

        self._settings = None
        self.discriminator = None

        self.settings = settings

    @property
    def settings(self):
        """Gets the settings of this S3SettingsZone.  # noqa: E501

          # noqa: E501

        :return: The settings of this S3SettingsZone.  # noqa: E501
        :rtype: S3SettingsZoneSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this S3SettingsZone.

          # noqa: E501

        :param settings: The settings of this S3SettingsZone.  # noqa: E501
        :type: S3SettingsZoneSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

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
        if not isinstance(other, S3SettingsZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
