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

from isilon_sdk.v9_3_0.models.changelist_entry import ChangelistEntry  # noqa: F401,E501


class ChangelistEntriesExtended(object):
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
        'entries': 'list[ChangelistEntry]',
        'resume': 'str'
    }

    attribute_map = {
        'entries': 'entries',
        'resume': 'resume'
    }

    def __init__(self, entries=None, resume=None):  # noqa: E501
        """ChangelistEntriesExtended - a model defined in Swagger"""  # noqa: E501

        self._entries = None
        self._resume = None
        self.discriminator = None

        if entries is not None:
            self.entries = entries
        if resume is not None:
            self.resume = resume

    @property
    def entries(self):
        """Gets the entries of this ChangelistEntriesExtended.  # noqa: E501


        :return: The entries of this ChangelistEntriesExtended.  # noqa: E501
        :rtype: list[ChangelistEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this ChangelistEntriesExtended.


        :param entries: The entries of this ChangelistEntriesExtended.  # noqa: E501
        :type: list[ChangelistEntry]
        """

        self._entries = entries

    @property
    def resume(self):
        """Gets the resume of this ChangelistEntriesExtended.  # noqa: E501

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :return: The resume of this ChangelistEntriesExtended.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this ChangelistEntriesExtended.

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :param resume: The resume of this ChangelistEntriesExtended.  # noqa: E501
        :type: str
        """
        if resume is not None and len(resume) > 8192:
            raise ValueError("Invalid value for `resume`, length must be less than or equal to `8192`")  # noqa: E501
        if resume is not None and len(resume) < 0:
            raise ValueError("Invalid value for `resume`, length must be greater than or equal to `0`")  # noqa: E501

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
        if not isinstance(other, ChangelistEntriesExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
