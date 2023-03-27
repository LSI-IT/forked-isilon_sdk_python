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


class DedupeSettingsSettings(object):
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
        'assess_paths': 'list[str]',
        'dedupe_schedule': 'str',
        'paths': 'list[str]'
    }

    attribute_map = {
        'assess_paths': 'assess_paths',
        'dedupe_schedule': 'dedupe_schedule',
        'paths': 'paths'
    }

    def __init__(self, assess_paths=None, dedupe_schedule=None, paths=None):  # noqa: E501
        """DedupeSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._assess_paths = None
        self._dedupe_schedule = None
        self._paths = None
        self.discriminator = None

        if assess_paths is not None:
            self.assess_paths = assess_paths
        if dedupe_schedule is not None:
            self.dedupe_schedule = dedupe_schedule
        if paths is not None:
            self.paths = paths

    @property
    def assess_paths(self):
        """Gets the assess_paths of this DedupeSettingsSettings.  # noqa: E501

        The paths that will be assessed.  # noqa: E501

        :return: The assess_paths of this DedupeSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._assess_paths

    @assess_paths.setter
    def assess_paths(self, assess_paths):
        """Sets the assess_paths of this DedupeSettingsSettings.

        The paths that will be assessed.  # noqa: E501

        :param assess_paths: The assess_paths of this DedupeSettingsSettings.  # noqa: E501
        :type: list[str]
        """

        self._assess_paths = assess_paths

    @property
    def dedupe_schedule(self):
        """Gets the dedupe_schedule of this DedupeSettingsSettings.  # noqa: E501

        The schedule for the dedupe job.  # noqa: E501

        :return: The dedupe_schedule of this DedupeSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._dedupe_schedule

    @dedupe_schedule.setter
    def dedupe_schedule(self, dedupe_schedule):
        """Sets the dedupe_schedule of this DedupeSettingsSettings.

        The schedule for the dedupe job.  # noqa: E501

        :param dedupe_schedule: The dedupe_schedule of this DedupeSettingsSettings.  # noqa: E501
        :type: str
        """

        self._dedupe_schedule = dedupe_schedule

    @property
    def paths(self):
        """Gets the paths of this DedupeSettingsSettings.  # noqa: E501

        The paths that will be deduped.  # noqa: E501

        :return: The paths of this DedupeSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this DedupeSettingsSettings.

        The paths that will be deduped.  # noqa: E501

        :param paths: The paths of this DedupeSettingsSettings.  # noqa: E501
        :type: list[str]
        """

        self._paths = paths

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
        if not isinstance(other, DedupeSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
