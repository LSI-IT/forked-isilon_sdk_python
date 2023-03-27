# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_1_0.models.settings_krb5_defaults_krb5_settings import SettingsKrb5DefaultsKrb5Settings  # noqa: F401,E501


class SettingsKrb5Defaults(object):
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
        'krb5_settings': 'SettingsKrb5DefaultsKrb5Settings'
    }

    attribute_map = {
        'krb5_settings': 'krb5_settings'
    }

    def __init__(self, krb5_settings=None):  # noqa: E501
        """SettingsKrb5Defaults - a model defined in Swagger"""  # noqa: E501

        self._krb5_settings = None
        self.discriminator = None

        if krb5_settings is not None:
            self.krb5_settings = krb5_settings

    @property
    def krb5_settings(self):
        """Gets the krb5_settings of this SettingsKrb5Defaults.  # noqa: E501

        Specifies the properties for the global Kerberos authentication settings.  # noqa: E501

        :return: The krb5_settings of this SettingsKrb5Defaults.  # noqa: E501
        :rtype: SettingsKrb5DefaultsKrb5Settings
        """
        return self._krb5_settings

    @krb5_settings.setter
    def krb5_settings(self, krb5_settings):
        """Sets the krb5_settings of this SettingsKrb5Defaults.

        Specifies the properties for the global Kerberos authentication settings.  # noqa: E501

        :param krb5_settings: The krb5_settings of this SettingsKrb5Defaults.  # noqa: E501
        :type: SettingsKrb5DefaultsKrb5Settings
        """

        self._krb5_settings = krb5_settings

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
        if not isinstance(other, SettingsKrb5Defaults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
