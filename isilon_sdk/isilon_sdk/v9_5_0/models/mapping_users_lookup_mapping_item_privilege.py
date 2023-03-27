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


class MappingUsersLookupMappingItemPrivilege(object):
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
        'id': 'str',
        'name': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'read_only': 'read_only'
    }

    def __init__(self, id=None, name=None, read_only=None):  # noqa: E501
        """MappingUsersLookupMappingItemPrivilege - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._read_only = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if read_only is not None:
            self.read_only = read_only

    @property
    def id(self):
        """Gets the id of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501

        Specifies the ID of the privilege.  # noqa: E501

        :return: The id of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MappingUsersLookupMappingItemPrivilege.

        Specifies the ID of the privilege.  # noqa: E501

        :param id: The id of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501

        Specifies the name of the privilege.  # noqa: E501

        :return: The name of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MappingUsersLookupMappingItemPrivilege.

        Specifies the name of the privilege.  # noqa: E501

        :param name: The name of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def read_only(self):
        """Gets the read_only of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501

        True, if the privilege is read-only.  # noqa: E501

        :return: The read_only of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this MappingUsersLookupMappingItemPrivilege.

        True, if the privilege is read-only.  # noqa: E501

        :param read_only: The read_only of this MappingUsersLookupMappingItemPrivilege.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, MappingUsersLookupMappingItemPrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
