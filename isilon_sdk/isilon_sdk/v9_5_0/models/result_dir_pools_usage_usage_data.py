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


class ResultDirPoolsUsageUsageData(object):
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
        'ads_cnt': 'int',
        'dir_cnt': 'int',
        'file_cnt': 'int',
        'log_size_sum': 'int',
        'log_size_sum_overflow': 'int',
        'name': 'str',
        'other_cnt': 'int',
        'phys_size_sum': 'int'
    }

    attribute_map = {
        'ads_cnt': 'ads_cnt',
        'dir_cnt': 'dir_cnt',
        'file_cnt': 'file_cnt',
        'log_size_sum': 'log_size_sum',
        'log_size_sum_overflow': 'log_size_sum_overflow',
        'name': 'name',
        'other_cnt': 'other_cnt',
        'phys_size_sum': 'phys_size_sum'
    }

    def __init__(self, ads_cnt=None, dir_cnt=None, file_cnt=None, log_size_sum=None, log_size_sum_overflow=None, name=None, other_cnt=None, phys_size_sum=None):  # noqa: E501
        """ResultDirPoolsUsageUsageData - a model defined in Swagger"""  # noqa: E501

        self._ads_cnt = None
        self._dir_cnt = None
        self._file_cnt = None
        self._log_size_sum = None
        self._log_size_sum_overflow = None
        self._name = None
        self._other_cnt = None
        self._phys_size_sum = None
        self.discriminator = None

        if ads_cnt is not None:
            self.ads_cnt = ads_cnt
        if dir_cnt is not None:
            self.dir_cnt = dir_cnt
        if file_cnt is not None:
            self.file_cnt = file_cnt
        if log_size_sum is not None:
            self.log_size_sum = log_size_sum
        if log_size_sum_overflow is not None:
            self.log_size_sum_overflow = log_size_sum_overflow
        if name is not None:
            self.name = name
        if other_cnt is not None:
            self.other_cnt = other_cnt
        if phys_size_sum is not None:
            self.phys_size_sum = phys_size_sum

    @property
    def ads_cnt(self):
        """Gets the ads_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501

        Number of alternate data streams.  # noqa: E501

        :return: The ads_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :rtype: int
        """
        return self._ads_cnt

    @ads_cnt.setter
    def ads_cnt(self, ads_cnt):
        """Sets the ads_cnt of this ResultDirPoolsUsageUsageData.

        Number of alternate data streams.  # noqa: E501

        :param ads_cnt: The ads_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :type: int
        """
        if ads_cnt is not None and ads_cnt > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `ads_cnt`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if ads_cnt is not None and ads_cnt < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `ads_cnt`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._ads_cnt = ads_cnt

    @property
    def dir_cnt(self):
        """Gets the dir_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501

        Number of directories.  # noqa: E501

        :return: The dir_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :rtype: int
        """
        return self._dir_cnt

    @dir_cnt.setter
    def dir_cnt(self, dir_cnt):
        """Sets the dir_cnt of this ResultDirPoolsUsageUsageData.

        Number of directories.  # noqa: E501

        :param dir_cnt: The dir_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :type: int
        """
        if dir_cnt is not None and dir_cnt > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `dir_cnt`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if dir_cnt is not None and dir_cnt < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `dir_cnt`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._dir_cnt = dir_cnt

    @property
    def file_cnt(self):
        """Gets the file_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501

        Number of files.  # noqa: E501

        :return: The file_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :rtype: int
        """
        return self._file_cnt

    @file_cnt.setter
    def file_cnt(self, file_cnt):
        """Sets the file_cnt of this ResultDirPoolsUsageUsageData.

        Number of files.  # noqa: E501

        :param file_cnt: The file_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :type: int
        """
        if file_cnt is not None and file_cnt > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `file_cnt`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if file_cnt is not None and file_cnt < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `file_cnt`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._file_cnt = file_cnt

    @property
    def log_size_sum(self):
        """Gets the log_size_sum of this ResultDirPoolsUsageUsageData.  # noqa: E501

        Logical pool usage by directory in bytes.  # noqa: E501

        :return: The log_size_sum of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :rtype: int
        """
        return self._log_size_sum

    @log_size_sum.setter
    def log_size_sum(self, log_size_sum):
        """Sets the log_size_sum of this ResultDirPoolsUsageUsageData.

        Logical pool usage by directory in bytes.  # noqa: E501

        :param log_size_sum: The log_size_sum of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :type: int
        """
        if log_size_sum is not None and log_size_sum > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `log_size_sum`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if log_size_sum is not None and log_size_sum < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `log_size_sum`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._log_size_sum = log_size_sum

    @property
    def log_size_sum_overflow(self):
        """Gets the log_size_sum_overflow of this ResultDirPoolsUsageUsageData.  # noqa: E501

        Logical size sum of overflow in bytes.  # noqa: E501

        :return: The log_size_sum_overflow of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :rtype: int
        """
        return self._log_size_sum_overflow

    @log_size_sum_overflow.setter
    def log_size_sum_overflow(self, log_size_sum_overflow):
        """Sets the log_size_sum_overflow of this ResultDirPoolsUsageUsageData.

        Logical size sum of overflow in bytes.  # noqa: E501

        :param log_size_sum_overflow: The log_size_sum_overflow of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :type: int
        """
        if log_size_sum_overflow is not None and log_size_sum_overflow > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `log_size_sum_overflow`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if log_size_sum_overflow is not None and log_size_sum_overflow < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `log_size_sum_overflow`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._log_size_sum_overflow = log_size_sum_overflow

    @property
    def name(self):
        """Gets the name of this ResultDirPoolsUsageUsageData.  # noqa: E501

        Name of the storage pool.  # noqa: E501

        :return: The name of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResultDirPoolsUsageUsageData.

        Name of the storage pool.  # noqa: E501

        :param name: The name of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 4096:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `4096`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def other_cnt(self):
        """Gets the other_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501

        Other count.  # noqa: E501

        :return: The other_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :rtype: int
        """
        return self._other_cnt

    @other_cnt.setter
    def other_cnt(self, other_cnt):
        """Sets the other_cnt of this ResultDirPoolsUsageUsageData.

        Other count.  # noqa: E501

        :param other_cnt: The other_cnt of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :type: int
        """
        if other_cnt is not None and other_cnt > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `other_cnt`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if other_cnt is not None and other_cnt < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `other_cnt`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._other_cnt = other_cnt

    @property
    def phys_size_sum(self):
        """Gets the phys_size_sum of this ResultDirPoolsUsageUsageData.  # noqa: E501

        Physical pool usage by directory in bytes.  # noqa: E501

        :return: The phys_size_sum of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :rtype: int
        """
        return self._phys_size_sum

    @phys_size_sum.setter
    def phys_size_sum(self, phys_size_sum):
        """Sets the phys_size_sum of this ResultDirPoolsUsageUsageData.

        Physical pool usage by directory in bytes.  # noqa: E501

        :param phys_size_sum: The phys_size_sum of this ResultDirPoolsUsageUsageData.  # noqa: E501
        :type: int
        """
        if phys_size_sum is not None and phys_size_sum > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `phys_size_sum`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if phys_size_sum is not None and phys_size_sum < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `phys_size_sum`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._phys_size_sum = phys_size_sum

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
        if not isinstance(other, ResultDirPoolsUsageUsageData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
