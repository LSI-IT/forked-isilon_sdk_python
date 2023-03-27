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

from isilon_sdk.v9_2_0.models.namespace_object import NamespaceObject  # noqa: F401,E501


class NamespaceObjects(object):
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
        'children': 'list[NamespaceObject]',
        'resume': 'str'
    }

    attribute_map = {
        'children': 'children',
        'resume': 'resume'
    }

    def __init__(self, children=None, resume=None):  # noqa: E501
        """NamespaceObjects - a model defined in Swagger"""  # noqa: E501

        self._children = None
        self._resume = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if resume is not None:
            self.resume = resume

    @property
    def children(self):
        """Gets the children of this NamespaceObjects.  # noqa: E501


        :return: The children of this NamespaceObjects.  # noqa: E501
        :rtype: list[NamespaceObject]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this NamespaceObjects.


        :param children: The children of this NamespaceObjects.  # noqa: E501
        :type: list[NamespaceObject]
        """

        self._children = children

    @property
    def resume(self):
        """Gets the resume of this NamespaceObjects.  # noqa: E501


        :return: The resume of this NamespaceObjects.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this NamespaceObjects.


        :param resume: The resume of this NamespaceObjects.  # noqa: E501
        :type: str
        """

        self._resume = resume

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
        if not isinstance(other, NamespaceObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
