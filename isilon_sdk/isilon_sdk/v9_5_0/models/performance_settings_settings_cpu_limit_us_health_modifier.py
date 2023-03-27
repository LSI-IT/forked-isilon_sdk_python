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

from isilon_sdk.v9_5_0.models.performance_settings_settings_cpu_limit_us_health_modifier_impact_high import PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh  # noqa: F401,E501


class PerformanceSettingsSettingsCpuLimitUsHealthModifier(object):
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
        'impact_high': 'PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh',
        'impact_low': 'PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh',
        'impact_medium': 'PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh',
        'impact_unset': 'PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh'
    }

    attribute_map = {
        'impact_high': 'impact_high',
        'impact_low': 'impact_low',
        'impact_medium': 'impact_medium',
        'impact_unset': 'impact_unset'
    }

    def __init__(self, impact_high=None, impact_low=None, impact_medium=None, impact_unset=None):  # noqa: E501
        """PerformanceSettingsSettingsCpuLimitUsHealthModifier - a model defined in Swagger"""  # noqa: E501

        self._impact_high = None
        self._impact_low = None
        self._impact_medium = None
        self._impact_unset = None
        self.discriminator = None

        if impact_high is not None:
            self.impact_high = impact_high
        if impact_low is not None:
            self.impact_low = impact_low
        if impact_medium is not None:
            self.impact_medium = impact_medium
        if impact_unset is not None:
            self.impact_unset = impact_unset

    @property
    def impact_high(self):
        """Gets the impact_high of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501

          # noqa: E501

        :return: The impact_high of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501
        :rtype: PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh
        """
        return self._impact_high

    @impact_high.setter
    def impact_high(self, impact_high):
        """Sets the impact_high of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.

          # noqa: E501

        :param impact_high: The impact_high of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501
        :type: PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh
        """

        self._impact_high = impact_high

    @property
    def impact_low(self):
        """Gets the impact_low of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501

          # noqa: E501

        :return: The impact_low of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501
        :rtype: PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh
        """
        return self._impact_low

    @impact_low.setter
    def impact_low(self, impact_low):
        """Sets the impact_low of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.

          # noqa: E501

        :param impact_low: The impact_low of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501
        :type: PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh
        """

        self._impact_low = impact_low

    @property
    def impact_medium(self):
        """Gets the impact_medium of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501

          # noqa: E501

        :return: The impact_medium of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501
        :rtype: PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh
        """
        return self._impact_medium

    @impact_medium.setter
    def impact_medium(self, impact_medium):
        """Sets the impact_medium of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.

          # noqa: E501

        :param impact_medium: The impact_medium of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501
        :type: PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh
        """

        self._impact_medium = impact_medium

    @property
    def impact_unset(self):
        """Gets the impact_unset of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501

          # noqa: E501

        :return: The impact_unset of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501
        :rtype: PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh
        """
        return self._impact_unset

    @impact_unset.setter
    def impact_unset(self, impact_unset):
        """Sets the impact_unset of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.

          # noqa: E501

        :param impact_unset: The impact_unset of this PerformanceSettingsSettingsCpuLimitUsHealthModifier.  # noqa: E501
        :type: PerformanceSettingsSettingsCpuLimitUsHealthModifierImpactHigh
        """

        self._impact_unset = impact_unset

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
        if not isinstance(other, PerformanceSettingsSettingsCpuLimitUsHealthModifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
