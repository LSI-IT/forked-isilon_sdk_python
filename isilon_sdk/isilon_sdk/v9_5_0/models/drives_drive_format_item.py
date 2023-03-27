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


class DrivesDriveFormatItem(object):
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
        'purpose': 'str'
    }

    attribute_map = {
        'purpose': 'purpose'
    }

    def __init__(self, purpose=None):  # noqa: E501
        """DrivesDriveFormatItem - a model defined in Swagger"""  # noqa: E501

        self._purpose = None
        self.discriminator = None

        if purpose is not None:
            self.purpose = purpose

    @property
    def purpose(self):
        """Gets the purpose of this DrivesDriveFormatItem.  # noqa: E501

        The purpose to which this drive should be formatted. If not specified, defaults to 'None', which will be automatically purposed based on node configuration and drive type.  # noqa: E501

        :return: The purpose of this DrivesDriveFormatItem.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this DrivesDriveFormatItem.

        The purpose to which this drive should be formatted. If not specified, defaults to 'None', which will be automatically purposed based on node configuration and drive type.  # noqa: E501

        :param purpose: The purpose of this DrivesDriveFormatItem.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

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
        if not isinstance(other, DrivesDriveFormatItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
