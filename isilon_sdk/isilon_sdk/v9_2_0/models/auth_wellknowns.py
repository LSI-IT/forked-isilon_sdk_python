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

from isilon_sdk.v9_2_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501


class AuthWellknowns(object):
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
        'wellknowns': 'list[AuthAccessAccessItemFileGroup]'
    }

    attribute_map = {
        'wellknowns': 'wellknowns'
    }

    def __init__(self, wellknowns=None):  # noqa: E501
        """AuthWellknowns - a model defined in Swagger"""  # noqa: E501

        self._wellknowns = None
        self.discriminator = None

        if wellknowns is not None:
            self.wellknowns = wellknowns

    @property
    def wellknowns(self):
        """Gets the wellknowns of this AuthWellknowns.  # noqa: E501


        :return: The wellknowns of this AuthWellknowns.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._wellknowns

    @wellknowns.setter
    def wellknowns(self, wellknowns):
        """Sets the wellknowns of this AuthWellknowns.


        :param wellknowns: The wellknowns of this AuthWellknowns.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """

        self._wellknowns = wellknowns

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
        if not isinstance(other, AuthWellknowns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
