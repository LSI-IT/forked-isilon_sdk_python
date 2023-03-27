# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IdResolutionDomainsError(object):
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
        'field': 'str',
        'field_value': 'str',
        'message': 'str'
    }

    attribute_map = {
        'field': 'field',
        'field_value': 'field_value',
        'message': 'message'
    }

    def __init__(self, field=None, field_value=None, message=None):  # noqa: E501
        """IdResolutionDomainsError - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self._field_value = None
        self._message = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if field_value is not None:
            self.field_value = field_value
        if message is not None:
            self.message = message

    @property
    def field(self):
        """Gets the field of this IdResolutionDomainsError.  # noqa: E501

        Identifies the type of id.  # noqa: E501

        :return: The field of this IdResolutionDomainsError.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this IdResolutionDomainsError.

        Identifies the type of id.  # noqa: E501

        :param field: The field of this IdResolutionDomainsError.  # noqa: E501
        :type: str
        """
        if field is not None and len(field) > 255:
            raise ValueError("Invalid value for `field`, length must be less than or equal to `255`")  # noqa: E501
        if field is not None and len(field) < 0:
            raise ValueError("Invalid value for `field`, length must be greater than or equal to `0`")  # noqa: E501

        self._field = field

    @property
    def field_value(self):
        """Gets the field_value of this IdResolutionDomainsError.  # noqa: E501

        A requested id that encountered an error during resolution.  # noqa: E501

        :return: The field_value of this IdResolutionDomainsError.  # noqa: E501
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        """Sets the field_value of this IdResolutionDomainsError.

        A requested id that encountered an error during resolution.  # noqa: E501

        :param field_value: The field_value of this IdResolutionDomainsError.  # noqa: E501
        :type: str
        """
        if field_value is not None and len(field_value) > 255:
            raise ValueError("Invalid value for `field_value`, length must be less than or equal to `255`")  # noqa: E501
        if field_value is not None and len(field_value) < 0:
            raise ValueError("Invalid value for `field_value`, length must be greater than or equal to `0`")  # noqa: E501

        self._field_value = field_value

    @property
    def message(self):
        """Gets the message of this IdResolutionDomainsError.  # noqa: E501

        Error message describes the failed resolution.  # noqa: E501

        :return: The message of this IdResolutionDomainsError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this IdResolutionDomainsError.

        Error message describes the failed resolution.  # noqa: E501

        :param message: The message of this IdResolutionDomainsError.  # noqa: E501
        :type: str
        """
        if message is not None and len(message) > 255:
            raise ValueError("Invalid value for `message`, length must be less than or equal to `255`")  # noqa: E501
        if message is not None and len(message) < 0:
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `0`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, IdResolutionDomainsError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
