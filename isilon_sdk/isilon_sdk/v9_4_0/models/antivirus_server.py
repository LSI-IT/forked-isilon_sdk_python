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


class AntivirusServer(object):
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
        'description': 'str',
        'enabled': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'url': 'url'
    }

    def __init__(self, description=None, enabled=None, url=None):  # noqa: E501
        """AntivirusServer - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._enabled = None
        self._url = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if url is not None:
            self.url = url

    @property
    def description(self):
        """Gets the description of this AntivirusServer.  # noqa: E501

        A description for the server.  # noqa: E501

        :return: The description of this AntivirusServer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AntivirusServer.

        A description for the server.  # noqa: E501

        :param description: The description of this AntivirusServer.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this AntivirusServer.  # noqa: E501

        Whether the server is enabled.  # noqa: E501

        :return: The enabled of this AntivirusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AntivirusServer.

        Whether the server is enabled.  # noqa: E501

        :param enabled: The enabled of this AntivirusServer.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def url(self):
        """Gets the url of this AntivirusServer.  # noqa: E501

        The icap url for the server.  This should have a format of: icap://host.domain:port/path  # noqa: E501

        :return: The url of this AntivirusServer.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AntivirusServer.

        The icap url for the server.  This should have a format of: icap://host.domain:port/path  # noqa: E501

        :param url: The url of this AntivirusServer.  # noqa: E501
        :type: str
        """
        if url is not None and len(url) > 2048:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `2048`")  # noqa: E501
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, AntivirusServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
