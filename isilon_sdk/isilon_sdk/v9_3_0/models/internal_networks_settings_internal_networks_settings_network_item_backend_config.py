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


class InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig(object):
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
        'fabric_monitoring': 'str',
        'shared_backend': 'bool'
    }

    attribute_map = {
        'fabric_monitoring': 'fabric_monitoring',
        'shared_backend': 'shared_backend'
    }

    def __init__(self, fabric_monitoring=None, shared_backend=None):  # noqa: E501
        """InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig - a model defined in Swagger"""  # noqa: E501

        self._fabric_monitoring = None
        self._shared_backend = None
        self.discriminator = None

        self.fabric_monitoring = fabric_monitoring
        if shared_backend is not None:
            self.shared_backend = shared_backend

    @property
    def fabric_monitoring(self):
        """Gets the fabric_monitoring of this InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig.  # noqa: E501

        Represents if backend fabric monitoring is enabled or disabled.  # noqa: E501

        :return: The fabric_monitoring of this InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig.  # noqa: E501
        :rtype: str
        """
        return self._fabric_monitoring

    @fabric_monitoring.setter
    def fabric_monitoring(self, fabric_monitoring):
        """Sets the fabric_monitoring of this InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig.

        Represents if backend fabric monitoring is enabled or disabled.  # noqa: E501

        :param fabric_monitoring: The fabric_monitoring of this InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig.  # noqa: E501
        :type: str
        """
        if fabric_monitoring is None:
            raise ValueError("Invalid value for `fabric_monitoring`, must not be `None`")  # noqa: E501
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if fabric_monitoring not in allowed_values:
            raise ValueError(
                "Invalid value for `fabric_monitoring` ({0}), must be one of {1}"  # noqa: E501
                .format(fabric_monitoring, allowed_values)
            )

        self._fabric_monitoring = fabric_monitoring

    @property
    def shared_backend(self):
        """Gets the shared_backend of this InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig.  # noqa: E501

        Represents if backend network is shared among multiple OneFS clusters.  # noqa: E501

        :return: The shared_backend of this InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig.  # noqa: E501
        :rtype: bool
        """
        return self._shared_backend

    @shared_backend.setter
    def shared_backend(self, shared_backend):
        """Sets the shared_backend of this InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig.

        Represents if backend network is shared among multiple OneFS clusters.  # noqa: E501

        :param shared_backend: The shared_backend of this InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig.  # noqa: E501
        :type: bool
        """

        self._shared_backend = shared_backend

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
        if not isinstance(other, InternalNetworksSettingsInternalNetworksSettingsNetworkItemBackendConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
