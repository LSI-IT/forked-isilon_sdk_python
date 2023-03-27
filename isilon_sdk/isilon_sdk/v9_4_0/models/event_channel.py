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

from isilon_sdk.v9_4_0.models.event_channel_parameters import EventChannelParameters  # noqa: F401,E501


class EventChannel(object):
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
        'allowed_nodes': 'list[int]',
        'enabled': 'bool',
        'excluded_nodes': 'list[int]',
        'parameters': 'EventChannelParameters',
        'system': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'allowed_nodes': 'allowed_nodes',
        'enabled': 'enabled',
        'excluded_nodes': 'excluded_nodes',
        'parameters': 'parameters',
        'system': 'system',
        'type': 'type'
    }

    def __init__(self, allowed_nodes=None, enabled=None, excluded_nodes=None, parameters=None, system=None, type=None):  # noqa: E501
        """EventChannel - a model defined in Swagger"""  # noqa: E501

        self._allowed_nodes = None
        self._enabled = None
        self._excluded_nodes = None
        self._parameters = None
        self._system = None
        self._type = None
        self.discriminator = None

        if allowed_nodes is not None:
            self.allowed_nodes = allowed_nodes
        if enabled is not None:
            self.enabled = enabled
        if excluded_nodes is not None:
            self.excluded_nodes = excluded_nodes
        if parameters is not None:
            self.parameters = parameters
        if system is not None:
            self.system = system
        if type is not None:
            self.type = type

    @property
    def allowed_nodes(self):
        """Gets the allowed_nodes of this EventChannel.  # noqa: E501

        Nodes (LNNs) that can be masters for this channel.  # noqa: E501

        :return: The allowed_nodes of this EventChannel.  # noqa: E501
        :rtype: list[int]
        """
        return self._allowed_nodes

    @allowed_nodes.setter
    def allowed_nodes(self, allowed_nodes):
        """Sets the allowed_nodes of this EventChannel.

        Nodes (LNNs) that can be masters for this channel.  # noqa: E501

        :param allowed_nodes: The allowed_nodes of this EventChannel.  # noqa: E501
        :type: list[int]
        """

        self._allowed_nodes = allowed_nodes

    @property
    def enabled(self):
        """Gets the enabled of this EventChannel.  # noqa: E501

        Channel is to be used or not.  # noqa: E501

        :return: The enabled of this EventChannel.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this EventChannel.

        Channel is to be used or not.  # noqa: E501

        :param enabled: The enabled of this EventChannel.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def excluded_nodes(self):
        """Gets the excluded_nodes of this EventChannel.  # noqa: E501

        Nodes (LNNs) that can NOT be the masters for this channel.  # noqa: E501

        :return: The excluded_nodes of this EventChannel.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_nodes

    @excluded_nodes.setter
    def excluded_nodes(self, excluded_nodes):
        """Sets the excluded_nodes of this EventChannel.

        Nodes (LNNs) that can NOT be the masters for this channel.  # noqa: E501

        :param excluded_nodes: The excluded_nodes of this EventChannel.  # noqa: E501
        :type: list[int]
        """

        self._excluded_nodes = excluded_nodes

    @property
    def parameters(self):
        """Gets the parameters of this EventChannel.  # noqa: E501

        Parameters to be used for an smtp channel.  # noqa: E501

        :return: The parameters of this EventChannel.  # noqa: E501
        :rtype: EventChannelParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this EventChannel.

        Parameters to be used for an smtp channel.  # noqa: E501

        :param parameters: The parameters of this EventChannel.  # noqa: E501
        :type: EventChannelParameters
        """

        self._parameters = parameters

    @property
    def system(self):
        """Gets the system of this EventChannel.  # noqa: E501

        Channel is a pre-defined system channel.  # noqa: E501

        :return: The system of this EventChannel.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this EventChannel.

        Channel is a pre-defined system channel.  # noqa: E501

        :param system: The system of this EventChannel.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def type(self):
        """Gets the type of this EventChannel.  # noqa: E501

        The mechanism used by the channel.  # noqa: E501

        :return: The type of this EventChannel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventChannel.

        The mechanism used by the channel.  # noqa: E501

        :param type: The type of this EventChannel.  # noqa: E501
        :type: str
        """
        allowed_values = ["connectemc", "smtp", "snmp", "heartbeat"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, EventChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
