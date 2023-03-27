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

from isilon_sdk.v9_1_0.models.snapshot_alias_extended import SnapshotAliasExtended  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.snapshot_aliases import SnapshotAliases  # noqa: F401,E501


class SnapshotAliasesExtended(object):
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
        'aliases': 'list[SnapshotAliasExtended]',
        'resume': 'str',
        'total': 'int'
    }

    attribute_map = {
        'aliases': 'aliases',
        'resume': 'resume',
        'total': 'total'
    }

    def __init__(self, aliases=None, resume=None, total=None):  # noqa: E501
        """SnapshotAliasesExtended - a model defined in Swagger"""  # noqa: E501

        self._aliases = None
        self._resume = None
        self._total = None
        self.discriminator = None

        if aliases is not None:
            self.aliases = aliases
        if resume is not None:
            self.resume = resume
        if total is not None:
            self.total = total

    @property
    def aliases(self):
        """Gets the aliases of this SnapshotAliasesExtended.  # noqa: E501


        :return: The aliases of this SnapshotAliasesExtended.  # noqa: E501
        :rtype: list[SnapshotAliasExtended]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this SnapshotAliasesExtended.


        :param aliases: The aliases of this SnapshotAliasesExtended.  # noqa: E501
        :type: list[SnapshotAliasExtended]
        """

        self._aliases = aliases

    @property
    def resume(self):
        """Gets the resume of this SnapshotAliasesExtended.  # noqa: E501

        Resume token value to use in subsequent calls for continuation.  # noqa: E501

        :return: The resume of this SnapshotAliasesExtended.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this SnapshotAliasesExtended.

        Resume token value to use in subsequent calls for continuation.  # noqa: E501

        :param resume: The resume of this SnapshotAliasesExtended.  # noqa: E501
        :type: str
        """

        self._resume = resume

    @property
    def total(self):
        """Gets the total of this SnapshotAliasesExtended.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The total of this SnapshotAliasesExtended.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SnapshotAliasesExtended.

        Total number of items available.  # noqa: E501

        :param total: The total of this SnapshotAliasesExtended.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, SnapshotAliasesExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
