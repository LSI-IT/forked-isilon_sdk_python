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


class SettingsKrb5DefaultsKrb5Settings(object):
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
        'allow_weak_crypto': 'bool',
        'always_send_preauth': 'bool',
        'default_realm': 'str',
        'dns_lookup_kdc': 'bool',
        'dns_lookup_realm': 'bool'
    }

    attribute_map = {
        'allow_weak_crypto': 'allow_weak_crypto',
        'always_send_preauth': 'always_send_preauth',
        'default_realm': 'default_realm',
        'dns_lookup_kdc': 'dns_lookup_kdc',
        'dns_lookup_realm': 'dns_lookup_realm'
    }

    def __init__(self, allow_weak_crypto=None, always_send_preauth=None, default_realm=None, dns_lookup_kdc=None, dns_lookup_realm=None):  # noqa: E501
        """SettingsKrb5DefaultsKrb5Settings - a model defined in Swagger"""  # noqa: E501

        self._allow_weak_crypto = None
        self._always_send_preauth = None
        self._default_realm = None
        self._dns_lookup_kdc = None
        self._dns_lookup_realm = None
        self.discriminator = None

        if allow_weak_crypto is not None:
            self.allow_weak_crypto = allow_weak_crypto
        if always_send_preauth is not None:
            self.always_send_preauth = always_send_preauth
        if default_realm is not None:
            self.default_realm = default_realm
        if dns_lookup_kdc is not None:
            self.dns_lookup_kdc = dns_lookup_kdc
        if dns_lookup_realm is not None:
            self.dns_lookup_realm = dns_lookup_realm

    @property
    def allow_weak_crypto(self):
        """Gets the allow_weak_crypto of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501

        If true, allow the use of DES encryption  # noqa: E501

        :return: The allow_weak_crypto of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_weak_crypto

    @allow_weak_crypto.setter
    def allow_weak_crypto(self, allow_weak_crypto):
        """Sets the allow_weak_crypto of this SettingsKrb5DefaultsKrb5Settings.

        If true, allow the use of DES encryption  # noqa: E501

        :param allow_weak_crypto: The allow_weak_crypto of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :type: bool
        """

        self._allow_weak_crypto = allow_weak_crypto

    @property
    def always_send_preauth(self):
        """Gets the always_send_preauth of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501

        If true, always attempts to preauthenticate to the domain controller.  # noqa: E501

        :return: The always_send_preauth of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :rtype: bool
        """
        return self._always_send_preauth

    @always_send_preauth.setter
    def always_send_preauth(self, always_send_preauth):
        """Sets the always_send_preauth of this SettingsKrb5DefaultsKrb5Settings.

        If true, always attempts to preauthenticate to the domain controller.  # noqa: E501

        :param always_send_preauth: The always_send_preauth of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :type: bool
        """

        self._always_send_preauth = always_send_preauth

    @property
    def default_realm(self):
        """Gets the default_realm of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501

        Specifies the realm for unqualified names.  # noqa: E501

        :return: The default_realm of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :rtype: str
        """
        return self._default_realm

    @default_realm.setter
    def default_realm(self, default_realm):
        """Sets the default_realm of this SettingsKrb5DefaultsKrb5Settings.

        Specifies the realm for unqualified names.  # noqa: E501

        :param default_realm: The default_realm of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :type: str
        """
        if default_realm is not None and len(default_realm) > 255:
            raise ValueError("Invalid value for `default_realm`, length must be less than or equal to `255`")  # noqa: E501
        if default_realm is not None and len(default_realm) < 0:
            raise ValueError("Invalid value for `default_realm`, length must be greater than or equal to `0`")  # noqa: E501

        self._default_realm = default_realm

    @property
    def dns_lookup_kdc(self):
        """Gets the dns_lookup_kdc of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501

        If true, find KDCs through the DNS.  # noqa: E501

        :return: The dns_lookup_kdc of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :rtype: bool
        """
        return self._dns_lookup_kdc

    @dns_lookup_kdc.setter
    def dns_lookup_kdc(self, dns_lookup_kdc):
        """Sets the dns_lookup_kdc of this SettingsKrb5DefaultsKrb5Settings.

        If true, find KDCs through the DNS.  # noqa: E501

        :param dns_lookup_kdc: The dns_lookup_kdc of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :type: bool
        """

        self._dns_lookup_kdc = dns_lookup_kdc

    @property
    def dns_lookup_realm(self):
        """Gets the dns_lookup_realm of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501

        If true, find realm names through the DNS.  # noqa: E501

        :return: The dns_lookup_realm of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :rtype: bool
        """
        return self._dns_lookup_realm

    @dns_lookup_realm.setter
    def dns_lookup_realm(self, dns_lookup_realm):
        """Sets the dns_lookup_realm of this SettingsKrb5DefaultsKrb5Settings.

        If true, find realm names through the DNS.  # noqa: E501

        :param dns_lookup_realm: The dns_lookup_realm of this SettingsKrb5DefaultsKrb5Settings.  # noqa: E501
        :type: bool
        """

        self._dns_lookup_realm = dns_lookup_realm

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
        if not isinstance(other, SettingsKrb5DefaultsKrb5Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
