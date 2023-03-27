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


class ChangelistsChangelistDiffRegionsDiffRegion(object):
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
        'byte_count': 'int',
        'region_type': 'str',
        'start_offset': 'int'
    }

    attribute_map = {
        'byte_count': 'byte_count',
        'region_type': 'region_type',
        'start_offset': 'start_offset'
    }

    def __init__(self, byte_count=None, region_type=None, start_offset=None):  # noqa: E501
        """ChangelistsChangelistDiffRegionsDiffRegion - a model defined in Swagger"""  # noqa: E501

        self._byte_count = None
        self._region_type = None
        self._start_offset = None
        self.discriminator = None

        self.byte_count = byte_count
        self.region_type = region_type
        self.start_offset = start_offset

    @property
    def byte_count(self):
        """Gets the byte_count of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501

        Byte count of change region.  # noqa: E501

        :return: The byte_count of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501
        :rtype: int
        """
        return self._byte_count

    @byte_count.setter
    def byte_count(self, byte_count):
        """Sets the byte_count of this ChangelistsChangelistDiffRegionsDiffRegion.

        Byte count of change region.  # noqa: E501

        :param byte_count: The byte_count of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501
        :type: int
        """
        if byte_count is None:
            raise ValueError("Invalid value for `byte_count`, must not be `None`")  # noqa: E501
        if byte_count is not None and byte_count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `byte_count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if byte_count is not None and byte_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `byte_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._byte_count = byte_count

    @property
    def region_type(self):
        """Gets the region_type of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501

        Type of change region.  # noqa: E501

        :return: The region_type of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501
        :rtype: str
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        """Sets the region_type of this ChangelistsChangelistDiffRegionsDiffRegion.

        Type of change region.  # noqa: E501

        :param region_type: The region_type of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501
        :type: str
        """
        if region_type is None:
            raise ValueError("Invalid value for `region_type`, must not be `None`")  # noqa: E501
        allowed_values = ["sparse", "data", "unchanged"]  # noqa: E501
        if region_type not in allowed_values:
            raise ValueError(
                "Invalid value for `region_type` ({0}), must be one of {1}"  # noqa: E501
                .format(region_type, allowed_values)
            )

        self._region_type = region_type

    @property
    def start_offset(self):
        """Gets the start_offset of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501

        Starting byte offset of change region.  # noqa: E501

        :return: The start_offset of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this ChangelistsChangelistDiffRegionsDiffRegion.

        Starting byte offset of change region.  # noqa: E501

        :param start_offset: The start_offset of this ChangelistsChangelistDiffRegionsDiffRegion.  # noqa: E501
        :type: int
        """
        if start_offset is None:
            raise ValueError("Invalid value for `start_offset`, must not be `None`")  # noqa: E501
        if start_offset is not None and start_offset > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `start_offset`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if start_offset is not None and start_offset < 0:  # noqa: E501
            raise ValueError("Invalid value for `start_offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_offset = start_offset

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
        if not isinstance(other, ChangelistsChangelistDiffRegionsDiffRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
