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

from isilon_sdk.v9_1_0.models.nfs_alias import NfsAlias  # noqa: F401,E501


class NfsAliasCreateParams(object):
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
        'health': 'str',
        'name': 'str',
        'path': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'health': 'health',
        'name': 'name',
        'path': 'path',
        'zone': 'zone'
    }

    def __init__(self, health=None, name=None, path=None, zone=None):  # noqa: E501
        """NfsAliasCreateParams - a model defined in Swagger"""  # noqa: E501

        self._health = None
        self._name = None
        self._path = None
        self._zone = None
        self.discriminator = None

        if health is not None:
            self.health = health
        self.name = name
        self.path = path
        if zone is not None:
            self.zone = zone

    @property
    def health(self):
        """Gets the health of this NfsAliasCreateParams.  # noqa: E501

        Specifies whether the alias is usable.  # noqa: E501

        :return: The health of this NfsAliasCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this NfsAliasCreateParams.

        Specifies whether the alias is usable.  # noqa: E501

        :param health: The health of this NfsAliasCreateParams.  # noqa: E501
        :type: str
        """

        self._health = health

    @property
    def name(self):
        """Gets the name of this NfsAliasCreateParams.  # noqa: E501

        Specifies the name by which the alias can be referenced.  # noqa: E501

        :return: The name of this NfsAliasCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NfsAliasCreateParams.

        Specifies the name by which the alias can be referenced.  # noqa: E501

        :param name: The name of this NfsAliasCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this NfsAliasCreateParams.  # noqa: E501

        Specifies the path to which the alias points.  # noqa: E501

        :return: The path of this NfsAliasCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NfsAliasCreateParams.

        Specifies the path to which the alias points.  # noqa: E501

        :param path: The path of this NfsAliasCreateParams.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def zone(self):
        """Gets the zone of this NfsAliasCreateParams.  # noqa: E501

        Specifies the zone in which the alias is valid.  # noqa: E501

        :return: The zone of this NfsAliasCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this NfsAliasCreateParams.

        Specifies the zone in which the alias is valid.  # noqa: E501

        :param zone: The zone of this NfsAliasCreateParams.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if not isinstance(other, NfsAliasCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
