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

from isilon_sdk.v9_4_0.models.result_dir_pools_usage_usage_data import ResultDirPoolsUsageUsageData  # noqa: F401,E501
from isilon_sdk.v9_4_0.models.result_directories_dir_usage import ResultDirectoriesDirUsage  # noqa: F401,E501


class ResultDirPoolsUsage(object):
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
        'begin_time': 'int',
        'dir_depth': 'int',
        'dir_usage': 'ResultDirectoriesDirUsage',
        'storage_pool_type': 'str',
        'usage_data': 'list[ResultDirPoolsUsageUsageData]'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'dir_depth': 'dir_depth',
        'dir_usage': 'dir_usage',
        'storage_pool_type': 'storage_pool_type',
        'usage_data': 'usage_data'
    }

    def __init__(self, begin_time=None, dir_depth=None, dir_usage=None, storage_pool_type=None, usage_data=None):  # noqa: E501
        """ResultDirPoolsUsage - a model defined in Swagger"""  # noqa: E501

        self._begin_time = None
        self._dir_depth = None
        self._dir_usage = None
        self._storage_pool_type = None
        self._usage_data = None
        self.discriminator = None

        self.begin_time = begin_time
        self.dir_depth = dir_depth
        self.dir_usage = dir_usage
        self.storage_pool_type = storage_pool_type
        self.usage_data = usage_data

    @property
    def begin_time(self):
        """Gets the begin_time of this ResultDirPoolsUsage.  # noqa: E501

        Unix Epoch time of start of results collection job.  # noqa: E501

        :return: The begin_time of this ResultDirPoolsUsage.  # noqa: E501
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ResultDirPoolsUsage.

        Unix Epoch time of start of results collection job.  # noqa: E501

        :param begin_time: The begin_time of this ResultDirPoolsUsage.  # noqa: E501
        :type: int
        """
        if begin_time is None:
            raise ValueError("Invalid value for `begin_time`, must not be `None`")  # noqa: E501
        if begin_time is not None and begin_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `begin_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if begin_time is not None and begin_time < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `begin_time`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._begin_time = begin_time

    @property
    def dir_depth(self):
        """Gets the dir_depth of this ResultDirPoolsUsage.  # noqa: E501

        Directory depth.  # noqa: E501

        :return: The dir_depth of this ResultDirPoolsUsage.  # noqa: E501
        :rtype: int
        """
        return self._dir_depth

    @dir_depth.setter
    def dir_depth(self, dir_depth):
        """Sets the dir_depth of this ResultDirPoolsUsage.

        Directory depth.  # noqa: E501

        :param dir_depth: The dir_depth of this ResultDirPoolsUsage.  # noqa: E501
        :type: int
        """
        if dir_depth is None:
            raise ValueError("Invalid value for `dir_depth`, must not be `None`")  # noqa: E501
        if dir_depth is not None and dir_depth > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `dir_depth`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if dir_depth is not None and dir_depth < 0:  # noqa: E501
            raise ValueError("Invalid value for `dir_depth`, must be a value greater than or equal to `0`")  # noqa: E501

        self._dir_depth = dir_depth

    @property
    def dir_usage(self):
        """Gets the dir_usage of this ResultDirPoolsUsage.  # noqa: E501

        Disk usage by the current directory.  # noqa: E501

        :return: The dir_usage of this ResultDirPoolsUsage.  # noqa: E501
        :rtype: ResultDirectoriesDirUsage
        """
        return self._dir_usage

    @dir_usage.setter
    def dir_usage(self, dir_usage):
        """Sets the dir_usage of this ResultDirPoolsUsage.

        Disk usage by the current directory.  # noqa: E501

        :param dir_usage: The dir_usage of this ResultDirPoolsUsage.  # noqa: E501
        :type: ResultDirectoriesDirUsage
        """
        if dir_usage is None:
            raise ValueError("Invalid value for `dir_usage`, must not be `None`")  # noqa: E501

        self._dir_usage = dir_usage

    @property
    def storage_pool_type(self):
        """Gets the storage_pool_type of this ResultDirPoolsUsage.  # noqa: E501

        The type of the storage pool.  # noqa: E501

        :return: The storage_pool_type of this ResultDirPoolsUsage.  # noqa: E501
        :rtype: str
        """
        return self._storage_pool_type

    @storage_pool_type.setter
    def storage_pool_type(self, storage_pool_type):
        """Sets the storage_pool_type of this ResultDirPoolsUsage.

        The type of the storage pool.  # noqa: E501

        :param storage_pool_type: The storage_pool_type of this ResultDirPoolsUsage.  # noqa: E501
        :type: str
        """
        if storage_pool_type is None:
            raise ValueError("Invalid value for `storage_pool_type`, must not be `None`")  # noqa: E501
        allowed_values = ["node_pool"]  # noqa: E501
        if storage_pool_type not in allowed_values:
            raise ValueError(
                "Invalid value for `storage_pool_type` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_pool_type, allowed_values)
            )

        self._storage_pool_type = storage_pool_type

    @property
    def usage_data(self):
        """Gets the usage_data of this ResultDirPoolsUsage.  # noqa: E501

        Disk usage classified by specified storage pool type.  # noqa: E501

        :return: The usage_data of this ResultDirPoolsUsage.  # noqa: E501
        :rtype: list[ResultDirPoolsUsageUsageData]
        """
        return self._usage_data

    @usage_data.setter
    def usage_data(self, usage_data):
        """Sets the usage_data of this ResultDirPoolsUsage.

        Disk usage classified by specified storage pool type.  # noqa: E501

        :param usage_data: The usage_data of this ResultDirPoolsUsage.  # noqa: E501
        :type: list[ResultDirPoolsUsageUsageData]
        """
        if usage_data is None:
            raise ValueError("Invalid value for `usage_data`, must not be `None`")  # noqa: E501

        self._usage_data = usage_data

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
        if not isinstance(other, ResultDirPoolsUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
