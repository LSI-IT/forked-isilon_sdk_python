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


class SettingsKrb5RealmsRealmItem(object):
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
        'admin_server': 'str',
        'default_domain': 'str',
        'id': 'str',
        'is_default_realm': 'bool',
        'is_joined': 'bool',
        'kdc': 'list[str]',
        'realm': 'str'
    }

    attribute_map = {
        'admin_server': 'admin_server',
        'default_domain': 'default_domain',
        'id': 'id',
        'is_default_realm': 'is_default_realm',
        'is_joined': 'is_joined',
        'kdc': 'kdc',
        'realm': 'realm'
    }

    def __init__(self, admin_server=None, default_domain=None, id=None, is_default_realm=None, is_joined=None, kdc=None, realm=None):  # noqa: E501
        """SettingsKrb5RealmsRealmItem - a model defined in Swagger"""  # noqa: E501

        self._admin_server = None
        self._default_domain = None
        self._id = None
        self._is_default_realm = None
        self._is_joined = None
        self._kdc = None
        self._realm = None
        self.discriminator = None

        if admin_server is not None:
            self.admin_server = admin_server
        if default_domain is not None:
            self.default_domain = default_domain
        if id is not None:
            self.id = id
        if is_default_realm is not None:
            self.is_default_realm = is_default_realm
        if is_joined is not None:
            self.is_joined = is_joined
        if kdc is not None:
            self.kdc = kdc
        if realm is not None:
            self.realm = realm

    @property
    def admin_server(self):
        """Gets the admin_server of this SettingsKrb5RealmsRealmItem.  # noqa: E501

        Specifies the administrative server hostname.  # noqa: E501

        :return: The admin_server of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :rtype: str
        """
        return self._admin_server

    @admin_server.setter
    def admin_server(self, admin_server):
        """Sets the admin_server of this SettingsKrb5RealmsRealmItem.

        Specifies the administrative server hostname.  # noqa: E501

        :param admin_server: The admin_server of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :type: str
        """
        if admin_server is not None and len(admin_server) > 255:
            raise ValueError("Invalid value for `admin_server`, length must be less than or equal to `255`")  # noqa: E501
        if admin_server is not None and len(admin_server) < 0:
            raise ValueError("Invalid value for `admin_server`, length must be greater than or equal to `0`")  # noqa: E501

        self._admin_server = admin_server

    @property
    def default_domain(self):
        """Gets the default_domain of this SettingsKrb5RealmsRealmItem.  # noqa: E501

        Specifies the default domain mapped to the realm.  # noqa: E501

        :return: The default_domain of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :rtype: str
        """
        return self._default_domain

    @default_domain.setter
    def default_domain(self, default_domain):
        """Sets the default_domain of this SettingsKrb5RealmsRealmItem.

        Specifies the default domain mapped to the realm.  # noqa: E501

        :param default_domain: The default_domain of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :type: str
        """
        if default_domain is not None and len(default_domain) > 255:
            raise ValueError("Invalid value for `default_domain`, length must be less than or equal to `255`")  # noqa: E501
        if default_domain is not None and len(default_domain) < 0:
            raise ValueError("Invalid value for `default_domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._default_domain = default_domain

    @property
    def id(self):
        """Gets the id of this SettingsKrb5RealmsRealmItem.  # noqa: E501

        ID of realm  # noqa: E501

        :return: The id of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettingsKrb5RealmsRealmItem.

        ID of realm  # noqa: E501

        :param id: The id of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def is_default_realm(self):
        """Gets the is_default_realm of this SettingsKrb5RealmsRealmItem.  # noqa: E501

        If true, indicates that the realm is the default.  # noqa: E501

        :return: The is_default_realm of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_realm

    @is_default_realm.setter
    def is_default_realm(self, is_default_realm):
        """Sets the is_default_realm of this SettingsKrb5RealmsRealmItem.

        If true, indicates that the realm is the default.  # noqa: E501

        :param is_default_realm: The is_default_realm of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :type: bool
        """

        self._is_default_realm = is_default_realm

    @property
    def is_joined(self):
        """Gets the is_joined of this SettingsKrb5RealmsRealmItem.  # noqa: E501

        If true, indicates that the realm is joined.  # noqa: E501

        :return: The is_joined of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_joined

    @is_joined.setter
    def is_joined(self, is_joined):
        """Sets the is_joined of this SettingsKrb5RealmsRealmItem.

        If true, indicates that the realm is joined.  # noqa: E501

        :param is_joined: The is_joined of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :type: bool
        """

        self._is_joined = is_joined

    @property
    def kdc(self):
        """Gets the kdc of this SettingsKrb5RealmsRealmItem.  # noqa: E501

        Specifies the list of KDC hostnames.  # noqa: E501

        :return: The kdc of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._kdc

    @kdc.setter
    def kdc(self, kdc):
        """Sets the kdc of this SettingsKrb5RealmsRealmItem.

        Specifies the list of KDC hostnames.  # noqa: E501

        :param kdc: The kdc of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :type: list[str]
        """

        self._kdc = kdc

    @property
    def realm(self):
        """Gets the realm of this SettingsKrb5RealmsRealmItem.  # noqa: E501

        Specifies the name of the realm.  # noqa: E501

        :return: The realm of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this SettingsKrb5RealmsRealmItem.

        Specifies the name of the realm.  # noqa: E501

        :param realm: The realm of this SettingsKrb5RealmsRealmItem.  # noqa: E501
        :type: str
        """
        if realm is not None and len(realm) > 255:
            raise ValueError("Invalid value for `realm`, length must be less than or equal to `255`")  # noqa: E501
        if realm is not None and len(realm) < 0:
            raise ValueError("Invalid value for `realm`, length must be greater than or equal to `0`")  # noqa: E501

        self._realm = realm

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
        if not isinstance(other, SettingsKrb5RealmsRealmItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
