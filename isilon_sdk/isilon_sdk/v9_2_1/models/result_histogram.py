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

from isilon_sdk.v9_2_1.models.result_histogram_histogram_item import ResultHistogramHistogramItem  # noqa: F401,E501


class ResultHistogram(object):
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
        'atime_enabled': 'bool',
        'attribute_count': 'int',
        'begin_time': 'int',
        'histogram': 'list[ResultHistogramHistogramItem]'
    }

    attribute_map = {
        'atime_enabled': 'atime_enabled',
        'attribute_count': 'attribute_count',
        'begin_time': 'begin_time',
        'histogram': 'histogram'
    }

    def __init__(self, atime_enabled=None, attribute_count=None, begin_time=None, histogram=None):  # noqa: E501
        """ResultHistogram - a model defined in Swagger"""  # noqa: E501

        self._atime_enabled = None
        self._attribute_count = None
        self._begin_time = None
        self._histogram = None
        self.discriminator = None

        self.atime_enabled = atime_enabled
        self.attribute_count = attribute_count
        self.begin_time = begin_time
        self.histogram = histogram

    @property
    def atime_enabled(self):
        """Gets the atime_enabled of this ResultHistogram.  # noqa: E501

        Access time enabled.  # noqa: E501

        :return: The atime_enabled of this ResultHistogram.  # noqa: E501
        :rtype: bool
        """
        return self._atime_enabled

    @atime_enabled.setter
    def atime_enabled(self, atime_enabled):
        """Sets the atime_enabled of this ResultHistogram.

        Access time enabled.  # noqa: E501

        :param atime_enabled: The atime_enabled of this ResultHistogram.  # noqa: E501
        :type: bool
        """
        if atime_enabled is None:
            raise ValueError("Invalid value for `atime_enabled`, must not be `None`")  # noqa: E501

        self._atime_enabled = atime_enabled

    @property
    def attribute_count(self):
        """Gets the attribute_count of this ResultHistogram.  # noqa: E501

        User attribute count.  # noqa: E501

        :return: The attribute_count of this ResultHistogram.  # noqa: E501
        :rtype: int
        """
        return self._attribute_count

    @attribute_count.setter
    def attribute_count(self, attribute_count):
        """Sets the attribute_count of this ResultHistogram.

        User attribute count.  # noqa: E501

        :param attribute_count: The attribute_count of this ResultHistogram.  # noqa: E501
        :type: int
        """
        if attribute_count is None:
            raise ValueError("Invalid value for `attribute_count`, must not be `None`")  # noqa: E501

        self._attribute_count = attribute_count

    @property
    def begin_time(self):
        """Gets the begin_time of this ResultHistogram.  # noqa: E501

        Unix Epoch time of start of results collection job.  # noqa: E501

        :return: The begin_time of this ResultHistogram.  # noqa: E501
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ResultHistogram.

        Unix Epoch time of start of results collection job.  # noqa: E501

        :param begin_time: The begin_time of this ResultHistogram.  # noqa: E501
        :type: int
        """
        if begin_time is None:
            raise ValueError("Invalid value for `begin_time`, must not be `None`")  # noqa: E501

        self._begin_time = begin_time

    @property
    def histogram(self):
        """Gets the histogram of this ResultHistogram.  # noqa: E501

        Histogram data of specified file count parameter.  # noqa: E501

        :return: The histogram of this ResultHistogram.  # noqa: E501
        :rtype: list[ResultHistogramHistogramItem]
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """Sets the histogram of this ResultHistogram.

        Histogram data of specified file count parameter.  # noqa: E501

        :param histogram: The histogram of this ResultHistogram.  # noqa: E501
        :type: list[ResultHistogramHistogramItem]
        """
        if histogram is None:
            raise ValueError("Invalid value for `histogram`, must not be `None`")  # noqa: E501

        self._histogram = histogram

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
        if not isinstance(other, ResultHistogram):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
