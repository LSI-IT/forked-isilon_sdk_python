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

from isilon_sdk.v9_4_0.models.cluster_node_partition_statfs import ClusterNodePartitionStatfs  # noqa: F401,E501


class ClusterNodePartition(object):
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
        'block_size': 'int',
        'capacity': 'int',
        'component_devices': 'str',
        'mount_point': 'str',
        'percent_used': 'str',
        'statfs': 'ClusterNodePartitionStatfs',
        'used': 'int'
    }

    attribute_map = {
        'block_size': 'block_size',
        'capacity': 'capacity',
        'component_devices': 'component_devices',
        'mount_point': 'mount_point',
        'percent_used': 'percent_used',
        'statfs': 'statfs',
        'used': 'used'
    }

    def __init__(self, block_size=None, capacity=None, component_devices=None, mount_point=None, percent_used=None, statfs=None, used=None):  # noqa: E501
        """ClusterNodePartition - a model defined in Swagger"""  # noqa: E501

        self._block_size = None
        self._capacity = None
        self._component_devices = None
        self._mount_point = None
        self._percent_used = None
        self._statfs = None
        self._used = None
        self.discriminator = None

        if block_size is not None:
            self.block_size = block_size
        if capacity is not None:
            self.capacity = capacity
        if component_devices is not None:
            self.component_devices = component_devices
        if mount_point is not None:
            self.mount_point = mount_point
        if percent_used is not None:
            self.percent_used = percent_used
        if statfs is not None:
            self.statfs = statfs
        if used is not None:
            self.used = used

    @property
    def block_size(self):
        """Gets the block_size of this ClusterNodePartition.  # noqa: E501

        The block size used for the reported partition information.  # noqa: E501

        :return: The block_size of this ClusterNodePartition.  # noqa: E501
        :rtype: int
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """Sets the block_size of this ClusterNodePartition.

        The block size used for the reported partition information.  # noqa: E501

        :param block_size: The block_size of this ClusterNodePartition.  # noqa: E501
        :type: int
        """
        if block_size is not None and block_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `block_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if block_size is not None and block_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `block_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._block_size = block_size

    @property
    def capacity(self):
        """Gets the capacity of this ClusterNodePartition.  # noqa: E501

        Total blocks on this file system partition.  # noqa: E501

        :return: The capacity of this ClusterNodePartition.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ClusterNodePartition.

        Total blocks on this file system partition.  # noqa: E501

        :param capacity: The capacity of this ClusterNodePartition.  # noqa: E501
        :type: int
        """
        if capacity is not None and capacity > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if capacity is not None and capacity < 0:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity = capacity

    @property
    def component_devices(self):
        """Gets the component_devices of this ClusterNodePartition.  # noqa: E501

        Comma separated list of devices used for this file system partition.  # noqa: E501

        :return: The component_devices of this ClusterNodePartition.  # noqa: E501
        :rtype: str
        """
        return self._component_devices

    @component_devices.setter
    def component_devices(self, component_devices):
        """Sets the component_devices of this ClusterNodePartition.

        Comma separated list of devices used for this file system partition.  # noqa: E501

        :param component_devices: The component_devices of this ClusterNodePartition.  # noqa: E501
        :type: str
        """
        if component_devices is not None and len(component_devices) > 255:
            raise ValueError("Invalid value for `component_devices`, length must be less than or equal to `255`")  # noqa: E501
        if component_devices is not None and len(component_devices) < 0:
            raise ValueError("Invalid value for `component_devices`, length must be greater than or equal to `0`")  # noqa: E501

        self._component_devices = component_devices

    @property
    def mount_point(self):
        """Gets the mount_point of this ClusterNodePartition.  # noqa: E501

        Directory on which this partition is mounted.  # noqa: E501

        :return: The mount_point of this ClusterNodePartition.  # noqa: E501
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """Sets the mount_point of this ClusterNodePartition.

        Directory on which this partition is mounted.  # noqa: E501

        :param mount_point: The mount_point of this ClusterNodePartition.  # noqa: E501
        :type: str
        """
        if mount_point is not None and len(mount_point) > 255:
            raise ValueError("Invalid value for `mount_point`, length must be less than or equal to `255`")  # noqa: E501
        if mount_point is not None and len(mount_point) < 0:
            raise ValueError("Invalid value for `mount_point`, length must be greater than or equal to `0`")  # noqa: E501

        self._mount_point = mount_point

    @property
    def percent_used(self):
        """Gets the percent_used of this ClusterNodePartition.  # noqa: E501

        Used blocks on this file system partition, expressed as a percentage.  # noqa: E501

        :return: The percent_used of this ClusterNodePartition.  # noqa: E501
        :rtype: str
        """
        return self._percent_used

    @percent_used.setter
    def percent_used(self, percent_used):
        """Sets the percent_used of this ClusterNodePartition.

        Used blocks on this file system partition, expressed as a percentage.  # noqa: E501

        :param percent_used: The percent_used of this ClusterNodePartition.  # noqa: E501
        :type: str
        """
        if percent_used is not None and len(percent_used) > 255:
            raise ValueError("Invalid value for `percent_used`, length must be less than or equal to `255`")  # noqa: E501
        if percent_used is not None and len(percent_used) < 0:
            raise ValueError("Invalid value for `percent_used`, length must be greater than or equal to `0`")  # noqa: E501

        self._percent_used = percent_used

    @property
    def statfs(self):
        """Gets the statfs of this ClusterNodePartition.  # noqa: E501

        System partition details as provided by statfs(2).  # noqa: E501

        :return: The statfs of this ClusterNodePartition.  # noqa: E501
        :rtype: ClusterNodePartitionStatfs
        """
        return self._statfs

    @statfs.setter
    def statfs(self, statfs):
        """Sets the statfs of this ClusterNodePartition.

        System partition details as provided by statfs(2).  # noqa: E501

        :param statfs: The statfs of this ClusterNodePartition.  # noqa: E501
        :type: ClusterNodePartitionStatfs
        """

        self._statfs = statfs

    @property
    def used(self):
        """Gets the used of this ClusterNodePartition.  # noqa: E501

        Used blocks on this file system partition.  # noqa: E501

        :return: The used of this ClusterNodePartition.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ClusterNodePartition.

        Used blocks on this file system partition.  # noqa: E501

        :param used: The used of this ClusterNodePartition.  # noqa: E501
        :type: int
        """
        if used is not None and used > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `used`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if used is not None and used < 0:  # noqa: E501
            raise ValueError("Invalid value for `used`, must be a value greater than or equal to `0`")  # noqa: E501

        self._used = used

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
        if not isinstance(other, ClusterNodePartition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
