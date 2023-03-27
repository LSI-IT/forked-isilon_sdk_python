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


class SupportassistPayloadItem(object):
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
        'payload_type': 'str',
        'payload_version': 'str',
        'sub_type': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'payload_type': 'payloadType',
        'payload_version': 'payloadVersion',
        'sub_type': 'subType',
        'timestamp': 'timestamp'
    }

    def __init__(self, payload_type=None, payload_version='1.0', sub_type=None, timestamp='<ISO 8601 UTC format>'):  # noqa: E501
        """SupportassistPayloadItem - a model defined in Swagger"""  # noqa: E501

        self._payload_type = None
        self._payload_version = None
        self._sub_type = None
        self._timestamp = None
        self.discriminator = None

        self.payload_type = payload_type
        if payload_version is not None:
            self.payload_version = payload_version
        if sub_type is not None:
            self.sub_type = sub_type
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def payload_type(self):
        """Gets the payload_type of this SupportassistPayloadItem.  # noqa: E501

        Type of payload request.  # noqa: E501

        :return: The payload_type of this SupportassistPayloadItem.  # noqa: E501
        :rtype: str
        """
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
        """Sets the payload_type of this SupportassistPayloadItem.

        Type of payload request.  # noqa: E501

        :param payload_type: The payload_type of this SupportassistPayloadItem.  # noqa: E501
        :type: str
        """
        if payload_type is None:
            raise ValueError("Invalid value for `payload_type`, must not be `None`")  # noqa: E501
        allowed_values = ["topology", "testConnectivity", "customerContact"]  # noqa: E501
        if payload_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payload_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payload_type, allowed_values)
            )

        self._payload_type = payload_type

    @property
    def payload_version(self):
        """Gets the payload_version of this SupportassistPayloadItem.  # noqa: E501

        Payload version.  # noqa: E501

        :return: The payload_version of this SupportassistPayloadItem.  # noqa: E501
        :rtype: str
        """
        return self._payload_version

    @payload_version.setter
    def payload_version(self, payload_version):
        """Sets the payload_version of this SupportassistPayloadItem.

        Payload version.  # noqa: E501

        :param payload_version: The payload_version of this SupportassistPayloadItem.  # noqa: E501
        :type: str
        """
        if payload_version is not None and len(payload_version) > 255:
            raise ValueError("Invalid value for `payload_version`, length must be less than or equal to `255`")  # noqa: E501
        if payload_version is not None and len(payload_version) < 1:
            raise ValueError("Invalid value for `payload_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._payload_version = payload_version

    @property
    def sub_type(self):
        """Gets the sub_type of this SupportassistPayloadItem.  # noqa: E501

        Payload subtype.  # noqa: E501

        :return: The sub_type of this SupportassistPayloadItem.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this SupportassistPayloadItem.

        Payload subtype.  # noqa: E501

        :param sub_type: The sub_type of this SupportassistPayloadItem.  # noqa: E501
        :type: str
        """
        if sub_type is not None and len(sub_type) > 255:
            raise ValueError("Invalid value for `sub_type`, length must be less than or equal to `255`")  # noqa: E501
        if sub_type is not None and len(sub_type) < 0:
            raise ValueError("Invalid value for `sub_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._sub_type = sub_type

    @property
    def timestamp(self):
        """Gets the timestamp of this SupportassistPayloadItem.  # noqa: E501

        Current Timestamp.  # noqa: E501

        :return: The timestamp of this SupportassistPayloadItem.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SupportassistPayloadItem.

        Current Timestamp.  # noqa: E501

        :param timestamp: The timestamp of this SupportassistPayloadItem.  # noqa: E501
        :type: str
        """
        if timestamp is not None and len(timestamp) > 255:
            raise ValueError("Invalid value for `timestamp`, length must be less than or equal to `255`")  # noqa: E501
        if timestamp is not None and len(timestamp) < 1:
            raise ValueError("Invalid value for `timestamp`, length must be greater than or equal to `1`")  # noqa: E501

        self._timestamp = timestamp

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
        if not isinstance(other, SupportassistPayloadItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other