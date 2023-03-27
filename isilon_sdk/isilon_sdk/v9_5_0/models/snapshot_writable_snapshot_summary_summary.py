# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 16
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SnapshotWritableSnapshotSummarySummary(object):
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
        'active_count': 'int',
        'active_phys_size': 'int',
        'count': 'int',
        'deleting_count': 'int',
        'deleting_phys_size': 'int',
        'phys_size': 'int'
    }

    attribute_map = {
        'active_count': 'active_count',
        'active_phys_size': 'active_phys_size',
        'count': 'count',
        'deleting_count': 'deleting_count',
        'deleting_phys_size': 'deleting_phys_size',
        'phys_size': 'phys_size'
    }

    def __init__(self, active_count=None, active_phys_size=None, count=None, deleting_count=None, deleting_phys_size=None, phys_size=None):  # noqa: E501
        """SnapshotWritableSnapshotSummarySummary - a model defined in Swagger"""  # noqa: E501

        self._active_count = None
        self._active_phys_size = None
        self._count = None
        self._deleting_count = None
        self._deleting_phys_size = None
        self._phys_size = None
        self.discriminator = None

        if active_count is not None:
            self.active_count = active_count
        if active_phys_size is not None:
            self.active_phys_size = active_phys_size
        if count is not None:
            self.count = count
        if deleting_count is not None:
            self.deleting_count = deleting_count
        if deleting_phys_size is not None:
            self.deleting_phys_size = deleting_phys_size
        if phys_size is not None:
            self.phys_size = phys_size

    @property
    def active_count(self):
        """Gets the active_count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501

        Total number of active writable snapshots.  # noqa: E501

        :return: The active_count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._active_count

    @active_count.setter
    def active_count(self, active_count):
        """Sets the active_count of this SnapshotWritableSnapshotSummarySummary.

        Total number of active writable snapshots.  # noqa: E501

        :param active_count: The active_count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :type: int
        """
        if active_count is not None and active_count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `active_count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if active_count is not None and active_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `active_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._active_count = active_count

    @property
    def active_phys_size(self):
        """Gets the active_phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501

        Sum of storage in bytes used by active writable snapshots.  # noqa: E501

        :return: The active_phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._active_phys_size

    @active_phys_size.setter
    def active_phys_size(self, active_phys_size):
        """Sets the active_phys_size of this SnapshotWritableSnapshotSummarySummary.

        Sum of storage in bytes used by active writable snapshots.  # noqa: E501

        :param active_phys_size: The active_phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :type: int
        """
        if active_phys_size is not None and active_phys_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `active_phys_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if active_phys_size is not None and active_phys_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `active_phys_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._active_phys_size = active_phys_size

    @property
    def count(self):
        """Gets the count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501

        Total number of writable snapshots.  # noqa: E501

        :return: The count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SnapshotWritableSnapshotSummarySummary.

        Total number of writable snapshots.  # noqa: E501

        :param count: The count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :type: int
        """
        if count is not None and count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def deleting_count(self):
        """Gets the deleting_count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501

        Total number of delete-pending writable snapshots.  # noqa: E501

        :return: The deleting_count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._deleting_count

    @deleting_count.setter
    def deleting_count(self, deleting_count):
        """Sets the deleting_count of this SnapshotWritableSnapshotSummarySummary.

        Total number of delete-pending writable snapshots.  # noqa: E501

        :param deleting_count: The deleting_count of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :type: int
        """
        if deleting_count is not None and deleting_count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `deleting_count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if deleting_count is not None and deleting_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `deleting_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._deleting_count = deleting_count

    @property
    def deleting_phys_size(self):
        """Gets the deleting_phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501

        Sum of storage in bytes used by delete-pending writable snapshots.  # noqa: E501

        :return: The deleting_phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._deleting_phys_size

    @deleting_phys_size.setter
    def deleting_phys_size(self, deleting_phys_size):
        """Sets the deleting_phys_size of this SnapshotWritableSnapshotSummarySummary.

        Sum of storage in bytes used by delete-pending writable snapshots.  # noqa: E501

        :param deleting_phys_size: The deleting_phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :type: int
        """
        if deleting_phys_size is not None and deleting_phys_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `deleting_phys_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if deleting_phys_size is not None and deleting_phys_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `deleting_phys_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._deleting_phys_size = deleting_phys_size

    @property
    def phys_size(self):
        """Gets the phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501

        Sum of storage in bytes used by all writable snapshots.  # noqa: E501

        :return: The phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :rtype: int
        """
        return self._phys_size

    @phys_size.setter
    def phys_size(self, phys_size):
        """Sets the phys_size of this SnapshotWritableSnapshotSummarySummary.

        Sum of storage in bytes used by all writable snapshots.  # noqa: E501

        :param phys_size: The phys_size of this SnapshotWritableSnapshotSummarySummary.  # noqa: E501
        :type: int
        """
        if phys_size is not None and phys_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `phys_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if phys_size is not None and phys_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `phys_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._phys_size = phys_size

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
        if not isinstance(other, SnapshotWritableSnapshotSummarySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other