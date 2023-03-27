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

from isilon_sdk.v9_3_0.models.node_state_servicelight_extended import NodeStateServicelightExtended  # noqa: F401,E501


class ClusterNodeStateServicelightExtended(object):
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
        'supported': 'bool',
        'valid': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'supported': 'supported',
        'valid': 'valid'
    }

    def __init__(self, enabled=None, supported=None, valid=None):  # noqa: E501
        """ClusterNodeStateServicelightExtended - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._supported = None
        self._valid = None
        self.discriminator = None

        self.enabled = enabled
        if supported is not None:
            self.supported = supported
        if valid is not None:
            self.valid = valid

    @property
    def enabled(self):
        """Gets the enabled of this ClusterNodeStateServicelightExtended.  # noqa: E501

        The node service light state (True = on).  # noqa: E501

        :return: The enabled of this ClusterNodeStateServicelightExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ClusterNodeStateServicelightExtended.

        The node service light state (True = on).  # noqa: E501

        :param enabled: The enabled of this ClusterNodeStateServicelightExtended.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def supported(self):
        """Gets the supported of this ClusterNodeStateServicelightExtended.  # noqa: E501

        This node supports a service light.  # noqa: E501

        :return: The supported of this ClusterNodeStateServicelightExtended.  # noqa: E501
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """Sets the supported of this ClusterNodeStateServicelightExtended.

        This node supports a service light.  # noqa: E501

        :param supported: The supported of this ClusterNodeStateServicelightExtended.  # noqa: E501
        :type: bool
        """

        self._supported = supported

    @property
    def valid(self):
        """Gets the valid of this ClusterNodeStateServicelightExtended.  # noqa: E501

        The node service light state is valid (False = Error).  # noqa: E501

        :return: The valid of this ClusterNodeStateServicelightExtended.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this ClusterNodeStateServicelightExtended.

        The node service light state is valid (False = Error).  # noqa: E501

        :param valid: The valid of this ClusterNodeStateServicelightExtended.  # noqa: E501
        :type: bool
        """

        self._valid = valid

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
        if not isinstance(other, ClusterNodeStateServicelightExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
