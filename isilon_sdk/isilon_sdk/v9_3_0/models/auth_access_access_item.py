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

from isilon_sdk.v9_3_0.models.auth_access_access_item_file import AuthAccessAccessItemFile  # noqa: F401,E501
from isilon_sdk.v9_3_0.models.auth_access_access_item_share import AuthAccessAccessItemShare  # noqa: F401,E501
from isilon_sdk.v9_3_0.models.auth_access_access_item_share_effective_user import AuthAccessAccessItemShareEffectiveUser  # noqa: F401,E501


class AuthAccessAccessItem(object):
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
        'file': 'AuthAccessAccessItemFile',
        'id': 'str',
        'share': 'AuthAccessAccessItemShare',
        'user': 'AuthAccessAccessItemShareEffectiveUser'
    }

    attribute_map = {
        'file': 'file',
        'id': 'id',
        'share': 'share',
        'user': 'user'
    }

    def __init__(self, file=None, id=None, share=None, user=None):  # noqa: E501
        """AuthAccessAccessItem - a model defined in Swagger"""  # noqa: E501

        self._file = None
        self._id = None
        self._share = None
        self._user = None
        self.discriminator = None

        if file is not None:
            self.file = file
        if id is not None:
            self.id = id
        if share is not None:
            self.share = share
        if user is not None:
            self.user = user

    @property
    def file(self):
        """Gets the file of this AuthAccessAccessItem.  # noqa: E501

        Specifies properties for access rights.  # noqa: E501

        :return: The file of this AuthAccessAccessItem.  # noqa: E501
        :rtype: AuthAccessAccessItemFile
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this AuthAccessAccessItem.

        Specifies properties for access rights.  # noqa: E501

        :param file: The file of this AuthAccessAccessItem.  # noqa: E501
        :type: AuthAccessAccessItemFile
        """

        self._file = file

    @property
    def id(self):
        """Gets the id of this AuthAccessAccessItem.  # noqa: E501

        Specifies the ID of the user.  # noqa: E501

        :return: The id of this AuthAccessAccessItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthAccessAccessItem.

        Specifies the ID of the user.  # noqa: E501

        :param id: The id of this AuthAccessAccessItem.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def share(self):
        """Gets the share of this AuthAccessAccessItem.  # noqa: E501

        Specifies the permissions that the user has on the share.  # noqa: E501

        :return: The share of this AuthAccessAccessItem.  # noqa: E501
        :rtype: AuthAccessAccessItemShare
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this AuthAccessAccessItem.

        Specifies the permissions that the user has on the share.  # noqa: E501

        :param share: The share of this AuthAccessAccessItem.  # noqa: E501
        :type: AuthAccessAccessItemShare
        """

        self._share = share

    @property
    def user(self):
        """Gets the user of this AuthAccessAccessItem.  # noqa: E501

        Specifies the persona for the user.  # noqa: E501

        :return: The user of this AuthAccessAccessItem.  # noqa: E501
        :rtype: AuthAccessAccessItemShareEffectiveUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AuthAccessAccessItem.

        Specifies the persona for the user.  # noqa: E501

        :param user: The user of this AuthAccessAccessItem.  # noqa: E501
        :type: AuthAccessAccessItemShareEffectiveUser
        """

        self._user = user

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
        if not isinstance(other, AuthAccessAccessItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
