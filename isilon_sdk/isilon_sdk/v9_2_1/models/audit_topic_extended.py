# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 12
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_2_1.models.audit_topic import AuditTopic  # noqa: F401,E501


class AuditTopicExtended(object):
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
        'id': 'str',
        'max_cached_messages': 'int',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'max_cached_messages': 'max_cached_messages',
        'name': 'name'
    }

    def __init__(self, id=None, max_cached_messages=None, name=None):  # noqa: E501
        """AuditTopicExtended - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._max_cached_messages = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if max_cached_messages is not None:
            self.max_cached_messages = max_cached_messages
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this AuditTopicExtended.  # noqa: E501

        Specifies the system-provided ID for the audit topic.  # noqa: E501

        :return: The id of this AuditTopicExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditTopicExtended.

        Specifies the system-provided ID for the audit topic.  # noqa: E501

        :param id: The id of this AuditTopicExtended.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def max_cached_messages(self):
        """Gets the max_cached_messages of this AuditTopicExtended.  # noqa: E501

        Specifies the maximum number of messages that can be sent and received at the same time. Messages that are sent and received at the same time can be lost if a system crash occurs. You can prevent message loss by setting this property to 0, which sets audit logs to synchronous.  # noqa: E501

        :return: The max_cached_messages of this AuditTopicExtended.  # noqa: E501
        :rtype: int
        """
        return self._max_cached_messages

    @max_cached_messages.setter
    def max_cached_messages(self, max_cached_messages):
        """Sets the max_cached_messages of this AuditTopicExtended.

        Specifies the maximum number of messages that can be sent and received at the same time. Messages that are sent and received at the same time can be lost if a system crash occurs. You can prevent message loss by setting this property to 0, which sets audit logs to synchronous.  # noqa: E501

        :param max_cached_messages: The max_cached_messages of this AuditTopicExtended.  # noqa: E501
        :type: int
        """
        if max_cached_messages is not None and max_cached_messages > 16384:  # noqa: E501
            raise ValueError("Invalid value for `max_cached_messages`, must be a value less than or equal to `16384`")  # noqa: E501
        if max_cached_messages is not None and max_cached_messages < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_cached_messages`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_cached_messages = max_cached_messages

    @property
    def name(self):
        """Gets the name of this AuditTopicExtended.  # noqa: E501

        Specifies the name of the audit topic.  # noqa: E501

        :return: The name of this AuditTopicExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuditTopicExtended.

        Specifies the name of the audit topic.  # noqa: E501

        :param name: The name of this AuditTopicExtended.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, AuditTopicExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
