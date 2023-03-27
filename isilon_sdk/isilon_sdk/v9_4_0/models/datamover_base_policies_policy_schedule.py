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


class DatamoverBasePoliciesPolicySchedule(object):
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
        'date_times': 'list[str]',
        'recurrence': 'list[str]',
        'start_time': 'str'
    }

    attribute_map = {
        'date_times': 'date_times',
        'recurrence': 'recurrence',
        'start_time': 'start_time'
    }

    def __init__(self, date_times=None, recurrence=None, start_time=None):  # noqa: E501
        """DatamoverBasePoliciesPolicySchedule - a model defined in Swagger"""  # noqa: E501

        self._date_times = None
        self._recurrence = None
        self._start_time = None
        self.discriminator = None

        if date_times is not None:
            self.date_times = date_times
        if recurrence is not None:
            self.recurrence = recurrence
        if start_time is not None:
            self.start_time = start_time

    @property
    def date_times(self):
        """Gets the date_times of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501

        The specific date/times at which this policy should run regardless of the start_time and recurrence.  # noqa: E501

        :return: The date_times of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._date_times

    @date_times.setter
    def date_times(self, date_times):
        """Sets the date_times of this DatamoverBasePoliciesPolicySchedule.

        The specific date/times at which this policy should run regardless of the start_time and recurrence.  # noqa: E501

        :param date_times: The date_times of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501
        :type: list[str]
        """

        self._date_times = date_times

    @property
    def recurrence(self):
        """Gets the recurrence of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501

        The cron expression to represent a repetitive schedule for the policy w.r.t. start_time.  # noqa: E501

        :return: The recurrence of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._recurrence

    @recurrence.setter
    def recurrence(self, recurrence):
        """Sets the recurrence of this DatamoverBasePoliciesPolicySchedule.

        The cron expression to represent a repetitive schedule for the policy w.r.t. start_time.  # noqa: E501

        :param recurrence: The recurrence of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501
        :type: list[str]
        """

        self._recurrence = recurrence

    @property
    def start_time(self):
        """Gets the start_time of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501

        The date/time of the first run of the policy. It should be in 'yyyy-mm-dd hh:mn:ss' format, where year range is 2001-2099.  # noqa: E501

        :return: The start_time of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DatamoverBasePoliciesPolicySchedule.

        The date/time of the first run of the policy. It should be in 'yyyy-mm-dd hh:mn:ss' format, where year range is 2001-2099.  # noqa: E501

        :param start_time: The start_time of this DatamoverBasePoliciesPolicySchedule.  # noqa: E501
        :type: str
        """
        if start_time is not None and len(start_time) > 19:
            raise ValueError("Invalid value for `start_time`, length must be less than or equal to `19`")  # noqa: E501
        if start_time is not None and len(start_time) < 0:
            raise ValueError("Invalid value for `start_time`, length must be greater than or equal to `0`")  # noqa: E501

        self._start_time = start_time

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
        if not isinstance(other, DatamoverBasePoliciesPolicySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other