# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_4_0.models.snapshot_pending_pending_item import SnapshotPendingPendingItem  # noqa: F401,E501


class SnapshotPending(object):
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
        'pending': 'list[SnapshotPendingPendingItem]',
        'resume': 'str'
    }

    attribute_map = {
        'pending': 'pending',
        'resume': 'resume'
    }

    def __init__(self, pending=None, resume=None):  # noqa: E501
        """SnapshotPending - a model defined in Swagger"""  # noqa: E501

        self._pending = None
        self._resume = None
        self.discriminator = None

        if pending is not None:
            self.pending = pending
        if resume is not None:
            self.resume = resume

    @property
    def pending(self):
        """Gets the pending of this SnapshotPending.  # noqa: E501


        :return: The pending of this SnapshotPending.  # noqa: E501
        :rtype: list[SnapshotPendingPendingItem]
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this SnapshotPending.


        :param pending: The pending of this SnapshotPending.  # noqa: E501
        :type: list[SnapshotPendingPendingItem]
        """

        self._pending = pending

    @property
    def resume(self):
        """Gets the resume of this SnapshotPending.  # noqa: E501

        Resume token value to use in subsequent calls for continuation.  # noqa: E501

        :return: The resume of this SnapshotPending.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this SnapshotPending.

        Resume token value to use in subsequent calls for continuation.  # noqa: E501

        :param resume: The resume of this SnapshotPending.  # noqa: E501
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
        if not isinstance(other, SnapshotPending):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
