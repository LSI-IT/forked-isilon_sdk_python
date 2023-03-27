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

from isilon_sdk.v9_3_0.models.auth_group_object_history_item import AuthGroupObjectHistoryItem  # noqa: F401,E501
from isilon_sdk.v9_3_0.models.mapping_users_lookup_mapping_item_group import MappingUsersLookupMappingItemGroup  # noqa: F401,E501
from isilon_sdk.v9_3_0.models.mapping_users_lookup_mapping_item_privilege import MappingUsersLookupMappingItemPrivilege  # noqa: F401,E501
from isilon_sdk.v9_3_0.models.mapping_users_lookup_mapping_item_user import MappingUsersLookupMappingItemUser  # noqa: F401,E501


class MappingUsersLookupMappingItem(object):
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
        'groups': 'list[MappingUsersLookupMappingItemGroup]',
        'object_history': 'list[AuthGroupObjectHistoryItem]',
        'privileges': 'list[MappingUsersLookupMappingItemPrivilege]',
        'user': 'MappingUsersLookupMappingItemUser',
        'zid': 'int',
        'zone': 'str'
    }

    attribute_map = {
        'groups': 'groups',
        'object_history': 'object_history',
        'privileges': 'privileges',
        'user': 'user',
        'zid': 'zid',
        'zone': 'zone'
    }

    def __init__(self, groups=None, object_history=None, privileges=None, user=None, zid=None, zone=None):  # noqa: E501
        """MappingUsersLookupMappingItem - a model defined in Swagger"""  # noqa: E501

        self._groups = None
        self._object_history = None
        self._privileges = None
        self._user = None
        self._zid = None
        self._zone = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if object_history is not None:
            self.object_history = object_history
        if privileges is not None:
            self.privileges = privileges
        if user is not None:
            self.user = user
        if zid is not None:
            self.zid = zid
        if zone is not None:
            self.zone = zone

    @property
    def groups(self):
        """Gets the groups of this MappingUsersLookupMappingItem.  # noqa: E501


        :return: The groups of this MappingUsersLookupMappingItem.  # noqa: E501
        :rtype: list[MappingUsersLookupMappingItemGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this MappingUsersLookupMappingItem.


        :param groups: The groups of this MappingUsersLookupMappingItem.  # noqa: E501
        :type: list[MappingUsersLookupMappingItemGroup]
        """

        self._groups = groups

    @property
    def object_history(self):
        """Gets the object_history of this MappingUsersLookupMappingItem.  # noqa: E501


        :return: The object_history of this MappingUsersLookupMappingItem.  # noqa: E501
        :rtype: list[AuthGroupObjectHistoryItem]
        """
        return self._object_history

    @object_history.setter
    def object_history(self, object_history):
        """Sets the object_history of this MappingUsersLookupMappingItem.


        :param object_history: The object_history of this MappingUsersLookupMappingItem.  # noqa: E501
        :type: list[AuthGroupObjectHistoryItem]
        """

        self._object_history = object_history

    @property
    def privileges(self):
        """Gets the privileges of this MappingUsersLookupMappingItem.  # noqa: E501


        :return: The privileges of this MappingUsersLookupMappingItem.  # noqa: E501
        :rtype: list[MappingUsersLookupMappingItemPrivilege]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this MappingUsersLookupMappingItem.


        :param privileges: The privileges of this MappingUsersLookupMappingItem.  # noqa: E501
        :type: list[MappingUsersLookupMappingItemPrivilege]
        """

        self._privileges = privileges

    @property
    def user(self):
        """Gets the user of this MappingUsersLookupMappingItem.  # noqa: E501

        Specifies the configuration properties for a user.  # noqa: E501

        :return: The user of this MappingUsersLookupMappingItem.  # noqa: E501
        :rtype: MappingUsersLookupMappingItemUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this MappingUsersLookupMappingItem.

        Specifies the configuration properties for a user.  # noqa: E501

        :param user: The user of this MappingUsersLookupMappingItem.  # noqa: E501
        :type: MappingUsersLookupMappingItemUser
        """

        self._user = user

    @property
    def zid(self):
        """Gets the zid of this MappingUsersLookupMappingItem.  # noqa: E501


        :return: The zid of this MappingUsersLookupMappingItem.  # noqa: E501
        :rtype: int
        """
        return self._zid

    @zid.setter
    def zid(self, zid):
        """Sets the zid of this MappingUsersLookupMappingItem.


        :param zid: The zid of this MappingUsersLookupMappingItem.  # noqa: E501
        :type: int
        """
        if zid is not None and zid > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `zid`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if zid is not None and zid < 0:  # noqa: E501
            raise ValueError("Invalid value for `zid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._zid = zid

    @property
    def zone(self):
        """Gets the zone of this MappingUsersLookupMappingItem.  # noqa: E501


        :return: The zone of this MappingUsersLookupMappingItem.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this MappingUsersLookupMappingItem.


        :param zone: The zone of this MappingUsersLookupMappingItem.  # noqa: E501
        :type: str
        """
        if zone is not None and len(zone) > 255:
            raise ValueError("Invalid value for `zone`, length must be less than or equal to `255`")  # noqa: E501
        if zone is not None and len(zone) < 0:
            raise ValueError("Invalid value for `zone`, length must be greater than or equal to `0`")  # noqa: E501

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
        if not isinstance(other, MappingUsersLookupMappingItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
