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

from isilon_sdk.v9_4_0.models.debug_stats_describe import DebugStatsDescribe  # noqa: F401,E501


class DebugStatsHandler(object):
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
        'delete': 'DebugStatsDescribe',
        'get': 'DebugStatsDescribe',
        'head': 'DebugStatsDescribe',
        'post': 'DebugStatsDescribe',
        'put': 'DebugStatsDescribe',
        'unsupported': 'DebugStatsDescribe',
        'name': 'str'
    }

    attribute_map = {
        'delete': 'DELETE',
        'get': 'GET',
        'head': 'HEAD',
        'post': 'POST',
        'put': 'PUT',
        'unsupported': 'UNSUPPORTED',
        'name': 'name'
    }

    def __init__(self, delete=None, get=None, head=None, post=None, put=None, unsupported=None, name=None):  # noqa: E501
        """DebugStatsHandler - a model defined in Swagger"""  # noqa: E501

        self._delete = None
        self._get = None
        self._head = None
        self._post = None
        self._put = None
        self._unsupported = None
        self._name = None
        self.discriminator = None

        if delete is not None:
            self.delete = delete
        if get is not None:
            self.get = get
        if head is not None:
            self.head = head
        if post is not None:
            self.post = post
        if put is not None:
            self.put = put
        if unsupported is not None:
            self.unsupported = unsupported
        if name is not None:
            self.name = name

    @property
    def delete(self):
        """Gets the delete of this DebugStatsHandler.  # noqa: E501

        Per-method statistics.  # noqa: E501

        :return: The delete of this DebugStatsHandler.  # noqa: E501
        :rtype: DebugStatsDescribe
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this DebugStatsHandler.

        Per-method statistics.  # noqa: E501

        :param delete: The delete of this DebugStatsHandler.  # noqa: E501
        :type: DebugStatsDescribe
        """

        self._delete = delete

    @property
    def get(self):
        """Gets the get of this DebugStatsHandler.  # noqa: E501

        Per-method statistics.  # noqa: E501

        :return: The get of this DebugStatsHandler.  # noqa: E501
        :rtype: DebugStatsDescribe
        """
        return self._get

    @get.setter
    def get(self, get):
        """Sets the get of this DebugStatsHandler.

        Per-method statistics.  # noqa: E501

        :param get: The get of this DebugStatsHandler.  # noqa: E501
        :type: DebugStatsDescribe
        """

        self._get = get

    @property
    def head(self):
        """Gets the head of this DebugStatsHandler.  # noqa: E501

        Per-method statistics.  # noqa: E501

        :return: The head of this DebugStatsHandler.  # noqa: E501
        :rtype: DebugStatsDescribe
        """
        return self._head

    @head.setter
    def head(self, head):
        """Sets the head of this DebugStatsHandler.

        Per-method statistics.  # noqa: E501

        :param head: The head of this DebugStatsHandler.  # noqa: E501
        :type: DebugStatsDescribe
        """

        self._head = head

    @property
    def post(self):
        """Gets the post of this DebugStatsHandler.  # noqa: E501

        Per-method statistics.  # noqa: E501

        :return: The post of this DebugStatsHandler.  # noqa: E501
        :rtype: DebugStatsDescribe
        """
        return self._post

    @post.setter
    def post(self, post):
        """Sets the post of this DebugStatsHandler.

        Per-method statistics.  # noqa: E501

        :param post: The post of this DebugStatsHandler.  # noqa: E501
        :type: DebugStatsDescribe
        """

        self._post = post

    @property
    def put(self):
        """Gets the put of this DebugStatsHandler.  # noqa: E501

        Per-method statistics.  # noqa: E501

        :return: The put of this DebugStatsHandler.  # noqa: E501
        :rtype: DebugStatsDescribe
        """
        return self._put

    @put.setter
    def put(self, put):
        """Sets the put of this DebugStatsHandler.

        Per-method statistics.  # noqa: E501

        :param put: The put of this DebugStatsHandler.  # noqa: E501
        :type: DebugStatsDescribe
        """

        self._put = put

    @property
    def unsupported(self):
        """Gets the unsupported of this DebugStatsHandler.  # noqa: E501

        Per-method statistics.  # noqa: E501

        :return: The unsupported of this DebugStatsHandler.  # noqa: E501
        :rtype: DebugStatsDescribe
        """
        return self._unsupported

    @unsupported.setter
    def unsupported(self, unsupported):
        """Sets the unsupported of this DebugStatsHandler.

        Per-method statistics.  # noqa: E501

        :param unsupported: The unsupported of this DebugStatsHandler.  # noqa: E501
        :type: DebugStatsDescribe
        """

        self._unsupported = unsupported

    @property
    def name(self):
        """Gets the name of this DebugStatsHandler.  # noqa: E501

        The URI.  # noqa: E501

        :return: The name of this DebugStatsHandler.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DebugStatsHandler.

        The URI.  # noqa: E501

        :param name: The name of this DebugStatsHandler.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, DebugStatsHandler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
