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

from isilon_sdk.v9_2_1.models.cluster_node_partition import ClusterNodePartition  # noqa: F401,E501


class ClusterNodePartitions(object):
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
        'count': 'int',
        'partitions': 'list[ClusterNodePartition]'
    }

    attribute_map = {
        'count': 'count',
        'partitions': 'partitions'
    }

    def __init__(self, count=None, partitions=None):  # noqa: E501
        """ClusterNodePartitions - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._partitions = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if partitions is not None:
            self.partitions = partitions

    @property
    def count(self):
        """Gets the count of this ClusterNodePartitions.  # noqa: E501

        Count of how many partitions are included.  # noqa: E501

        :return: The count of this ClusterNodePartitions.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ClusterNodePartitions.

        Count of how many partitions are included.  # noqa: E501

        :param count: The count of this ClusterNodePartitions.  # noqa: E501
        :type: int
        """
        if count is not None and count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def partitions(self):
        """Gets the partitions of this ClusterNodePartitions.  # noqa: E501

        Partition information.  # noqa: E501

        :return: The partitions of this ClusterNodePartitions.  # noqa: E501
        :rtype: list[ClusterNodePartition]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ClusterNodePartitions.

        Partition information.  # noqa: E501

        :param partitions: The partitions of this ClusterNodePartitions.  # noqa: E501
        :type: list[ClusterNodePartition]
        """

        self._partitions = partitions

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
        if not isinstance(other, ClusterNodePartitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
