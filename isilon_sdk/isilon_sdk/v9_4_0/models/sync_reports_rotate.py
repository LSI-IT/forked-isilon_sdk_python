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


class SyncReportsRotate(object):
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
        'message': 'str',
        'running': 'bool'
    }

    attribute_map = {
        'message': 'message',
        'running': 'running'
    }

    def __init__(self, message=None, running=None):  # noqa: E501
        """SyncReportsRotate - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._running = None
        self.discriminator = None

        self.message = message
        self.running = running

    @property
    def message(self):
        """Gets the message of this SyncReportsRotate.  # noqa: E501

        A message about the status of the task.  # noqa: E501

        :return: The message of this SyncReportsRotate.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SyncReportsRotate.

        A message about the status of the task.  # noqa: E501

        :param message: The message of this SyncReportsRotate.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def running(self):
        """Gets the running of this SyncReportsRotate.  # noqa: E501

        Whether this task is running or not.  # noqa: E501

        :return: The running of this SyncReportsRotate.  # noqa: E501
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this SyncReportsRotate.

        Whether this task is running or not.  # noqa: E501

        :param running: The running of this SyncReportsRotate.  # noqa: E501
        :type: bool
        """
        if running is None:
            raise ValueError("Invalid value for `running`, must not be `None`")  # noqa: E501

        self._running = running

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
        if not isinstance(other, SyncReportsRotate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
