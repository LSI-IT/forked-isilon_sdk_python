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


class DedupeReport(object):
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
        'phase': 'int',
        'results': 'str',
        'time': 'int'
    }

    attribute_map = {
        'phase': 'phase',
        'results': 'results',
        'time': 'time'
    }

    def __init__(self, phase=None, results=None, time=None):  # noqa: E501
        """DedupeReport - a model defined in Swagger"""  # noqa: E501

        self._phase = None
        self._results = None
        self._time = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if results is not None:
            self.results = results
        if time is not None:
            self.time = time

    @property
    def phase(self):
        """Gets the phase of this DedupeReport.  # noqa: E501

        The phase of the job this report was generated for.  # noqa: E501

        :return: The phase of this DedupeReport.  # noqa: E501
        :rtype: int
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this DedupeReport.

        The phase of the job this report was generated for.  # noqa: E501

        :param phase: The phase of this DedupeReport.  # noqa: E501
        :type: int
        """

        self._phase = phase

    @property
    def results(self):
        """Gets the results of this DedupeReport.  # noqa: E501

        The report results.  # noqa: E501

        :return: The results of this DedupeReport.  # noqa: E501
        :rtype: str
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DedupeReport.

        The report results.  # noqa: E501

        :param results: The results of this DedupeReport.  # noqa: E501
        :type: str
        """

        self._results = results

    @property
    def time(self):
        """Gets the time of this DedupeReport.  # noqa: E501

        The time this report was generated in Unix epoch seconds.  # noqa: E501

        :return: The time of this DedupeReport.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this DedupeReport.

        The time this report was generated in Unix epoch seconds.  # noqa: E501

        :param time: The time of this DedupeReport.  # noqa: E501
        :type: int
        """

        self._time = time

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
        if not isinstance(other, DedupeReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
