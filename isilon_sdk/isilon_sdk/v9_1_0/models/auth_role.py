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

from isilon_sdk.v9_1_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.auth_id_ntoken_privilege_item import AuthIdNtokenPrivilegeItem  # noqa: F401,E501


class AuthRole(object):
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
        'description': 'str',
        'members': 'list[AuthAccessAccessItemFileGroup]',
        'name': 'str',
        'privileges': 'list[AuthIdNtokenPrivilegeItem]'
    }

    attribute_map = {
        'description': 'description',
        'members': 'members',
        'name': 'name',
        'privileges': 'privileges'
    }

    def __init__(self, description=None, members=None, name=None, privileges=None):  # noqa: E501
        """AuthRole - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._members = None
        self._name = None
        self._privileges = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if members is not None:
            self.members = members
        if name is not None:
            self.name = name
        if privileges is not None:
            self.privileges = privileges

    @property
    def description(self):
        """Gets the description of this AuthRole.  # noqa: E501

        Specifies the description of the role.  # noqa: E501

        :return: The description of this AuthRole.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuthRole.

        Specifies the description of the role.  # noqa: E501

        :param description: The description of this AuthRole.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def members(self):
        """Gets the members of this AuthRole.  # noqa: E501

        Specifies the users or groups that have this role.  # noqa: E501

        :return: The members of this AuthRole.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this AuthRole.

        Specifies the users or groups that have this role.  # noqa: E501

        :param members: The members of this AuthRole.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """

        self._members = members

    @property
    def name(self):
        """Gets the name of this AuthRole.  # noqa: E501

        Specifies the name of the role.  # noqa: E501

        :return: The name of this AuthRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthRole.

        Specifies the name of the role.  # noqa: E501

        :param name: The name of this AuthRole.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501
        if name is not None and not re.search('^[^   ](.*[^   ])*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[^   ](.*[^   ])*$/`")  # noqa: E501

        self._name = name

    @property
    def privileges(self):
        """Gets the privileges of this AuthRole.  # noqa: E501

        Specifies the privileges granted by this role.  # noqa: E501

        :return: The privileges of this AuthRole.  # noqa: E501
        :rtype: list[AuthIdNtokenPrivilegeItem]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this AuthRole.

        Specifies the privileges granted by this role.  # noqa: E501

        :param privileges: The privileges of this AuthRole.  # noqa: E501
        :type: list[AuthIdNtokenPrivilegeItem]
        """

        self._privileges = privileges

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
        if not isinstance(other, AuthRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
