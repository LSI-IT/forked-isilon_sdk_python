# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_0_0.models.job_recent_recent_job import JobRecentRecentJob  # noqa: F401,E501


class JobRecent(object):
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
        'recent_jobs': 'list[JobRecentRecentJob]',
        'total': 'int'
    }

    attribute_map = {
        'recent_jobs': 'recent_jobs',
        'total': 'total'
    }

    def __init__(self, recent_jobs=None, total=None):  # noqa: E501
        """JobRecent - a model defined in Swagger"""  # noqa: E501

        self._recent_jobs = None
        self._total = None
        self.discriminator = None

        if recent_jobs is not None:
            self.recent_jobs = recent_jobs
        if total is not None:
            self.total = total

    @property
    def recent_jobs(self):
        """Gets the recent_jobs of this JobRecent.  # noqa: E501


        :return: The recent_jobs of this JobRecent.  # noqa: E501
        :rtype: list[JobRecentRecentJob]
        """
        return self._recent_jobs

    @recent_jobs.setter
    def recent_jobs(self, recent_jobs):
        """Sets the recent_jobs of this JobRecent.


        :param recent_jobs: The recent_jobs of this JobRecent.  # noqa: E501
        :type: list[JobRecentRecentJob]
        """

        self._recent_jobs = recent_jobs

    @property
    def total(self):
        """Gets the total of this JobRecent.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The total of this JobRecent.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this JobRecent.

        Total number of items available.  # noqa: E501

        :param total: The total of this JobRecent.  # noqa: E501
        :type: int
        """
        if total is not None and total > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if total is not None and total < 0:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, JobRecent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
