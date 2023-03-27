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

from isilon_sdk.v9_5_0.models.http_service import HttpService  # noqa: F401,E501


class HttpServiceExtended(object):
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
        'enabled': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'id': 'id'
    }

    def __init__(self, enabled=None, id=None):  # noqa: E501
        """HttpServiceExtended - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id

    @property
    def enabled(self):
        """Gets the enabled of this HttpServiceExtended.  # noqa: E501

        A True value indicates the service is currently enabled on the cluster.  # noqa: E501

        :return: The enabled of this HttpServiceExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this HttpServiceExtended.

        A True value indicates the service is currently enabled on the cluster.  # noqa: E501

        :param enabled: The enabled of this HttpServiceExtended.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this HttpServiceExtended.  # noqa: E501

        A string used to identify the service.  # noqa: E501

        :return: The id of this HttpServiceExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HttpServiceExtended.

        A string used to identify the service.  # noqa: E501

        :param id: The id of this HttpServiceExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["PowerScaleUI", "Platform-API-External", "RAN", "SWIFT", "RemoteService"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"  # noqa: E501
                .format(id, allowed_values)
            )

        self._id = id

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
        if not isinstance(other, HttpServiceExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
