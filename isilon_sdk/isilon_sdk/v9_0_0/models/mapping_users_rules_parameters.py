# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_0_0.models.mapping_users_rules_parameters_default_unix_user import MappingUsersRulesParametersDefaultUnixUser  # noqa: F401,E501


class MappingUsersRulesParameters(object):
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
        'default_unix_user': 'MappingUsersRulesParametersDefaultUnixUser'
    }

    attribute_map = {
        'default_unix_user': 'default_unix_user'
    }

    def __init__(self, default_unix_user=None):  # noqa: E501
        """MappingUsersRulesParameters - a model defined in Swagger"""  # noqa: E501

        self._default_unix_user = None
        self.discriminator = None

        if default_unix_user is not None:
            self.default_unix_user = default_unix_user

    @property
    def default_unix_user(self):
        """Gets the default_unix_user of this MappingUsersRulesParameters.  # noqa: E501

          # noqa: E501

        :return: The default_unix_user of this MappingUsersRulesParameters.  # noqa: E501
        :rtype: MappingUsersRulesParametersDefaultUnixUser
        """
        return self._default_unix_user

    @default_unix_user.setter
    def default_unix_user(self, default_unix_user):
        """Sets the default_unix_user of this MappingUsersRulesParameters.

          # noqa: E501

        :param default_unix_user: The default_unix_user of this MappingUsersRulesParameters.  # noqa: E501
        :type: MappingUsersRulesParametersDefaultUnixUser
        """

        self._default_unix_user = default_unix_user

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
        if not isinstance(other, MappingUsersRulesParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
