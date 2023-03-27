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

from isilon_sdk.v9_2_1.models.auth_access_access_item_share_effective_user import AuthAccessAccessItemShareEffectiveUser  # noqa: F401,E501
from isilon_sdk.v9_2_1.models.auth_access_access_item_share_share_permissions import AuthAccessAccessItemShareSharePermissions  # noqa: F401,E501


class AuthAccessAccessItemShare(object):
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
        'effective_user': 'AuthAccessAccessItemShareEffectiveUser',
        'share_permissions': 'AuthAccessAccessItemShareSharePermissions'
    }

    attribute_map = {
        'effective_user': 'effective_user',
        'share_permissions': 'share_permissions'
    }

    def __init__(self, effective_user=None, share_permissions=None):  # noqa: E501
        """AuthAccessAccessItemShare - a model defined in Swagger"""  # noqa: E501

        self._effective_user = None
        self._share_permissions = None
        self.discriminator = None

        if effective_user is not None:
            self.effective_user = effective_user
        if share_permissions is not None:
            self.share_permissions = share_permissions

    @property
    def effective_user(self):
        """Gets the effective_user of this AuthAccessAccessItemShare.  # noqa: E501

        Specifies the persona for the user.  # noqa: E501

        :return: The effective_user of this AuthAccessAccessItemShare.  # noqa: E501
        :rtype: AuthAccessAccessItemShareEffectiveUser
        """
        return self._effective_user

    @effective_user.setter
    def effective_user(self, effective_user):
        """Sets the effective_user of this AuthAccessAccessItemShare.

        Specifies the persona for the user.  # noqa: E501

        :param effective_user: The effective_user of this AuthAccessAccessItemShare.  # noqa: E501
        :type: AuthAccessAccessItemShareEffectiveUser
        """

        self._effective_user = effective_user

    @property
    def share_permissions(self):
        """Gets the share_permissions of this AuthAccessAccessItemShare.  # noqa: E501

        Specifies the permissions that the user has on the SHARE.  # noqa: E501

        :return: The share_permissions of this AuthAccessAccessItemShare.  # noqa: E501
        :rtype: AuthAccessAccessItemShareSharePermissions
        """
        return self._share_permissions

    @share_permissions.setter
    def share_permissions(self, share_permissions):
        """Sets the share_permissions of this AuthAccessAccessItemShare.

        Specifies the permissions that the user has on the SHARE.  # noqa: E501

        :param share_permissions: The share_permissions of this AuthAccessAccessItemShare.  # noqa: E501
        :type: AuthAccessAccessItemShareSharePermissions
        """

        self._share_permissions = share_permissions

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
        if not isinstance(other, AuthAccessAccessItemShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
