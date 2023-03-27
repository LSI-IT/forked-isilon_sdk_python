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

from isilon_sdk.v9_2_1.models.storagepool_status_unhealthy_item_affected_item import StoragepoolStatusUnhealthyItemAffectedItem  # noqa: F401,E501
from isilon_sdk.v9_2_1.models.storagepool_status_unhealthy_item_diskpool import StoragepoolStatusUnhealthyItemDiskpool  # noqa: F401,E501


class StoragepoolStatusUnhealthyItem(object):
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
        'affected': 'list[StoragepoolStatusUnhealthyItemAffectedItem]',
        'diskpool': 'StoragepoolStatusUnhealthyItemDiskpool',
        'health_flags': 'list[str]'
    }

    attribute_map = {
        'affected': 'affected',
        'diskpool': 'diskpool',
        'health_flags': 'health_flags'
    }

    def __init__(self, affected=None, diskpool=None, health_flags=None):  # noqa: E501
        """StoragepoolStatusUnhealthyItem - a model defined in Swagger"""  # noqa: E501

        self._affected = None
        self._diskpool = None
        self._health_flags = None
        self.discriminator = None

        self.affected = affected
        if diskpool is not None:
            self.diskpool = diskpool
        if health_flags is not None:
            self.health_flags = health_flags

    @property
    def affected(self):
        """Gets the affected of this StoragepoolStatusUnhealthyItem.  # noqa: E501

        The affected nodes and/or drives.  # noqa: E501

        :return: The affected of this StoragepoolStatusUnhealthyItem.  # noqa: E501
        :rtype: list[StoragepoolStatusUnhealthyItemAffectedItem]
        """
        return self._affected

    @affected.setter
    def affected(self, affected):
        """Sets the affected of this StoragepoolStatusUnhealthyItem.

        The affected nodes and/or drives.  # noqa: E501

        :param affected: The affected of this StoragepoolStatusUnhealthyItem.  # noqa: E501
        :type: list[StoragepoolStatusUnhealthyItemAffectedItem]
        """
        if affected is None:
            raise ValueError("Invalid value for `affected`, must not be `None`")  # noqa: E501

        self._affected = affected

    @property
    def diskpool(self):
        """Gets the diskpool of this StoragepoolStatusUnhealthyItem.  # noqa: E501

          # noqa: E501

        :return: The diskpool of this StoragepoolStatusUnhealthyItem.  # noqa: E501
        :rtype: StoragepoolStatusUnhealthyItemDiskpool
        """
        return self._diskpool

    @diskpool.setter
    def diskpool(self, diskpool):
        """Sets the diskpool of this StoragepoolStatusUnhealthyItem.

          # noqa: E501

        :param diskpool: The diskpool of this StoragepoolStatusUnhealthyItem.  # noqa: E501
        :type: StoragepoolStatusUnhealthyItemDiskpool
        """

        self._diskpool = diskpool

    @property
    def health_flags(self):
        """Gets the health_flags of this StoragepoolStatusUnhealthyItem.  # noqa: E501

        An array of containing any health issues with this pool.  If the pool is healthy, the list is empty.  # noqa: E501

        :return: The health_flags of this StoragepoolStatusUnhealthyItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._health_flags

    @health_flags.setter
    def health_flags(self, health_flags):
        """Sets the health_flags of this StoragepoolStatusUnhealthyItem.

        An array of containing any health issues with this pool.  If the pool is healthy, the list is empty.  # noqa: E501

        :param health_flags: The health_flags of this StoragepoolStatusUnhealthyItem.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["underprovisioned", "missing_drives", "devices_down", "devices_smartfailed", "waiting_repair"]  # noqa: E501
        if not set(health_flags).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `health_flags` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(health_flags) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._health_flags = health_flags

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
        if not isinstance(other, StoragepoolStatusUnhealthyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other