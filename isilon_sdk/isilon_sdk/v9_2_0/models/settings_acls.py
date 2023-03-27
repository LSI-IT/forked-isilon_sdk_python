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

from isilon_sdk.v9_2_0.models.settings_acls_acl_policy_settings import SettingsAclsAclPolicySettings  # noqa: F401,E501


class SettingsAcls(object):
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
        'acl_policy_settings': 'SettingsAclsAclPolicySettings'
    }

    attribute_map = {
        'acl_policy_settings': 'acl_policy_settings'
    }

    def __init__(self, acl_policy_settings=None):  # noqa: E501
        """SettingsAcls - a model defined in Swagger"""  # noqa: E501

        self._acl_policy_settings = None
        self.discriminator = None

        if acl_policy_settings is not None:
            self.acl_policy_settings = acl_policy_settings

    @property
    def acl_policy_settings(self):
        """Gets the acl_policy_settings of this SettingsAcls.  # noqa: E501

        ACL policies settings.  # noqa: E501

        :return: The acl_policy_settings of this SettingsAcls.  # noqa: E501
        :rtype: SettingsAclsAclPolicySettings
        """
        return self._acl_policy_settings

    @acl_policy_settings.setter
    def acl_policy_settings(self, acl_policy_settings):
        """Sets the acl_policy_settings of this SettingsAcls.

        ACL policies settings.  # noqa: E501

        :param acl_policy_settings: The acl_policy_settings of this SettingsAcls.  # noqa: E501
        :type: SettingsAclsAclPolicySettings
        """

        self._acl_policy_settings = acl_policy_settings

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
        if not isinstance(other, SettingsAcls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
