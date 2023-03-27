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

from isilon_sdk.v9_2_1.models.namespace_metadata_attrs import NamespaceMetadataAttrs  # noqa: F401,E501


class NamespaceMetadata(object):
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
        'action': 'str',
        'attrs': 'list[NamespaceMetadataAttrs]'
    }

    attribute_map = {
        'action': 'action',
        'attrs': 'attrs'
    }

    def __init__(self, action=None, attrs=None):  # noqa: E501
        """NamespaceMetadata - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._attrs = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if attrs is not None:
            self.attrs = attrs

    @property
    def action(self):
        """Gets the action of this NamespaceMetadata.  # noqa: E501


        :return: The action of this NamespaceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NamespaceMetadata.


        :param action: The action of this NamespaceMetadata.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def attrs(self):
        """Gets the attrs of this NamespaceMetadata.  # noqa: E501


        :return: The attrs of this NamespaceMetadata.  # noqa: E501
        :rtype: list[NamespaceMetadataAttrs]
        """
        return self._attrs

    @attrs.setter
    def attrs(self, attrs):
        """Sets the attrs of this NamespaceMetadata.


        :param attrs: The attrs of this NamespaceMetadata.  # noqa: E501
        :type: list[NamespaceMetadataAttrs]
        """

        self._attrs = attrs

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
        if not isinstance(other, NamespaceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
