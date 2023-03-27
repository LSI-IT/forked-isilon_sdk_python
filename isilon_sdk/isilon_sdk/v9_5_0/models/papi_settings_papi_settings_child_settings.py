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


class PapiSettingsPapiSettingsChildSettings(object):
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
        'child_limit': 'int',
        'child_limit_ceiling': 'int',
        'child_limit_extension': 'int',
        'child_limit_floor': 'int'
    }

    attribute_map = {
        'child_limit': 'child_limit',
        'child_limit_ceiling': 'child_limit_ceiling',
        'child_limit_extension': 'child_limit_extension',
        'child_limit_floor': 'child_limit_floor'
    }

    def __init__(self, child_limit=None, child_limit_ceiling=None, child_limit_extension=None, child_limit_floor=None):  # noqa: E501
        """PapiSettingsPapiSettingsChildSettings - a model defined in Swagger"""  # noqa: E501

        self._child_limit = None
        self._child_limit_ceiling = None
        self._child_limit_extension = None
        self._child_limit_floor = None
        self.discriminator = None

        if child_limit is not None:
            self.child_limit = child_limit
        if child_limit_ceiling is not None:
            self.child_limit_ceiling = child_limit_ceiling
        if child_limit_extension is not None:
            self.child_limit_extension = child_limit_extension
        if child_limit_floor is not None:
            self.child_limit_floor = child_limit_floor

    @property
    def child_limit(self):
        """Gets the child_limit of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501

        The number of PAPI requests that can be processed concurrently.  # noqa: E501

        :return: The child_limit of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501
        :rtype: int
        """
        return self._child_limit

    @child_limit.setter
    def child_limit(self, child_limit):
        """Sets the child_limit of this PapiSettingsPapiSettingsChildSettings.

        The number of PAPI requests that can be processed concurrently.  # noqa: E501

        :param child_limit: The child_limit of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501
        :type: int
        """
        if child_limit is not None and child_limit > 65535:  # noqa: E501
            raise ValueError("Invalid value for `child_limit`, must be a value less than or equal to `65535`")  # noqa: E501
        if child_limit is not None and child_limit < 2:  # noqa: E501
            raise ValueError("Invalid value for `child_limit`, must be a value greater than or equal to `2`")  # noqa: E501

        self._child_limit = child_limit

    @property
    def child_limit_ceiling(self):
        """Gets the child_limit_ceiling of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501

        Max value of child_limit that can be controlled.  # noqa: E501

        :return: The child_limit_ceiling of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501
        :rtype: int
        """
        return self._child_limit_ceiling

    @child_limit_ceiling.setter
    def child_limit_ceiling(self, child_limit_ceiling):
        """Sets the child_limit_ceiling of this PapiSettingsPapiSettingsChildSettings.

        Max value of child_limit that can be controlled.  # noqa: E501

        :param child_limit_ceiling: The child_limit_ceiling of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501
        :type: int
        """
        if child_limit_ceiling is not None and child_limit_ceiling > 65535:  # noqa: E501
            raise ValueError("Invalid value for `child_limit_ceiling`, must be a value less than or equal to `65535`")  # noqa: E501
        if child_limit_ceiling is not None and child_limit_ceiling < 2:  # noqa: E501
            raise ValueError("Invalid value for `child_limit_ceiling`, must be a value greater than or equal to `2`")  # noqa: E501

        self._child_limit_ceiling = child_limit_ceiling

    @property
    def child_limit_extension(self):
        """Gets the child_limit_extension of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501

        Extends the child limit for serving the URIs.  # noqa: E501

        :return: The child_limit_extension of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501
        :rtype: int
        """
        return self._child_limit_extension

    @child_limit_extension.setter
    def child_limit_extension(self, child_limit_extension):
        """Sets the child_limit_extension of this PapiSettingsPapiSettingsChildSettings.

        Extends the child limit for serving the URIs.  # noqa: E501

        :param child_limit_extension: The child_limit_extension of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501
        :type: int
        """
        if child_limit_extension is not None and child_limit_extension > 65535:  # noqa: E501
            raise ValueError("Invalid value for `child_limit_extension`, must be a value less than or equal to `65535`")  # noqa: E501
        if child_limit_extension is not None and child_limit_extension < 0:  # noqa: E501
            raise ValueError("Invalid value for `child_limit_extension`, must be a value greater than or equal to `0`")  # noqa: E501

        self._child_limit_extension = child_limit_extension

    @property
    def child_limit_floor(self):
        """Gets the child_limit_floor of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501

        Min value of child_limit that can be controlled.  # noqa: E501

        :return: The child_limit_floor of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501
        :rtype: int
        """
        return self._child_limit_floor

    @child_limit_floor.setter
    def child_limit_floor(self, child_limit_floor):
        """Sets the child_limit_floor of this PapiSettingsPapiSettingsChildSettings.

        Min value of child_limit that can be controlled.  # noqa: E501

        :param child_limit_floor: The child_limit_floor of this PapiSettingsPapiSettingsChildSettings.  # noqa: E501
        :type: int
        """
        if child_limit_floor is not None and child_limit_floor > 65535:  # noqa: E501
            raise ValueError("Invalid value for `child_limit_floor`, must be a value less than or equal to `65535`")  # noqa: E501
        if child_limit_floor is not None and child_limit_floor < 2:  # noqa: E501
            raise ValueError("Invalid value for `child_limit_floor`, must be a value greater than or equal to `2`")  # noqa: E501

        self._child_limit_floor = child_limit_floor

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
        if not isinstance(other, PapiSettingsPapiSettingsChildSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
