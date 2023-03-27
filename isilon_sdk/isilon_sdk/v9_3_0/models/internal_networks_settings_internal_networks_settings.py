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

from isilon_sdk.v9_3_0.models.internal_networks_settings_internal_networks_settings_network_item import InternalNetworksSettingsInternalNetworksSettingsNetworkItem  # noqa: F401,E501


class InternalNetworksSettingsInternalNetworksSettings(object):
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
        'network': 'list[InternalNetworksSettingsInternalNetworksSettingsNetworkItem]'
    }

    attribute_map = {
        'network': 'network'
    }

    def __init__(self, network=None):  # noqa: E501
        """InternalNetworksSettingsInternalNetworksSettings - a model defined in Swagger"""  # noqa: E501

        self._network = None
        self.discriminator = None

        if network is not None:
            self.network = network

    @property
    def network(self):
        """Gets the network of this InternalNetworksSettingsInternalNetworksSettings.  # noqa: E501


        :return: The network of this InternalNetworksSettingsInternalNetworksSettings.  # noqa: E501
        :rtype: list[InternalNetworksSettingsInternalNetworksSettingsNetworkItem]
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this InternalNetworksSettingsInternalNetworksSettings.


        :param network: The network of this InternalNetworksSettingsInternalNetworksSettings.  # noqa: E501
        :type: list[InternalNetworksSettingsInternalNetworksSettingsNetworkItem]
        """

        self._network = network

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
        if not isinstance(other, InternalNetworksSettingsInternalNetworksSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
