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


class CloudSettingsSettingsSleepTimeoutArchive(object):
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
        'recovery_with_tasks': 'float',
        'recovery_without_tasks': 'float',
        'with_tasks': 'float',
        'without_tasks': 'float'
    }

    attribute_map = {
        'recovery_with_tasks': 'recovery_with_tasks',
        'recovery_without_tasks': 'recovery_without_tasks',
        'with_tasks': 'with_tasks',
        'without_tasks': 'without_tasks'
    }

    def __init__(self, recovery_with_tasks=None, recovery_without_tasks=None, with_tasks=None, without_tasks=None):  # noqa: E501
        """CloudSettingsSettingsSleepTimeoutArchive - a model defined in Swagger"""  # noqa: E501

        self._recovery_with_tasks = None
        self._recovery_without_tasks = None
        self._with_tasks = None
        self._without_tasks = None
        self.discriminator = None

        if recovery_with_tasks is not None:
            self.recovery_with_tasks = recovery_with_tasks
        if recovery_without_tasks is not None:
            self.recovery_without_tasks = recovery_without_tasks
        if with_tasks is not None:
            self.with_tasks = with_tasks
        if without_tasks is not None:
            self.without_tasks = without_tasks

    @property
    def recovery_with_tasks(self):
        """Gets the recovery_with_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501

        Sleep timeout for a recovery thread with pending tasks  # noqa: E501

        :return: The recovery_with_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501
        :rtype: float
        """
        return self._recovery_with_tasks

    @recovery_with_tasks.setter
    def recovery_with_tasks(self, recovery_with_tasks):
        """Sets the recovery_with_tasks of this CloudSettingsSettingsSleepTimeoutArchive.

        Sleep timeout for a recovery thread with pending tasks  # noqa: E501

        :param recovery_with_tasks: The recovery_with_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501
        :type: float
        """

        self._recovery_with_tasks = recovery_with_tasks

    @property
    def recovery_without_tasks(self):
        """Gets the recovery_without_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501

        Sleep timeout for a recovery thread without pending tasks  # noqa: E501

        :return: The recovery_without_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501
        :rtype: float
        """
        return self._recovery_without_tasks

    @recovery_without_tasks.setter
    def recovery_without_tasks(self, recovery_without_tasks):
        """Sets the recovery_without_tasks of this CloudSettingsSettingsSleepTimeoutArchive.

        Sleep timeout for a recovery thread without pending tasks  # noqa: E501

        :param recovery_without_tasks: The recovery_without_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501
        :type: float
        """

        self._recovery_without_tasks = recovery_without_tasks

    @property
    def with_tasks(self):
        """Gets the with_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501

        Sleep timeout for a non-recovery thread with pending tasks  # noqa: E501

        :return: The with_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501
        :rtype: float
        """
        return self._with_tasks

    @with_tasks.setter
    def with_tasks(self, with_tasks):
        """Sets the with_tasks of this CloudSettingsSettingsSleepTimeoutArchive.

        Sleep timeout for a non-recovery thread with pending tasks  # noqa: E501

        :param with_tasks: The with_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501
        :type: float
        """

        self._with_tasks = with_tasks

    @property
    def without_tasks(self):
        """Gets the without_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501

        Sleep timeout for a non-recovery thread without pending tasks  # noqa: E501

        :return: The without_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501
        :rtype: float
        """
        return self._without_tasks

    @without_tasks.setter
    def without_tasks(self, without_tasks):
        """Sets the without_tasks of this CloudSettingsSettingsSleepTimeoutArchive.

        Sleep timeout for a non-recovery thread without pending tasks  # noqa: E501

        :param without_tasks: The without_tasks of this CloudSettingsSettingsSleepTimeoutArchive.  # noqa: E501
        :type: float
        """

        self._without_tasks = without_tasks

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
        if not isinstance(other, CloudSettingsSettingsSleepTimeoutArchive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
