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

from isilon_sdk.v9_5_0.models.cluster_services_node_service import ClusterServicesNodeService  # noqa: F401,E501


class ClusterServicesNode(object):
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
        'devid': 'int',
        'lnn': 'int',
        'services': 'list[ClusterServicesNodeService]'
    }

    attribute_map = {
        'devid': 'devid',
        'lnn': 'lnn',
        'services': 'services'
    }

    def __init__(self, devid=None, lnn=None, services=None):  # noqa: E501
        """ClusterServicesNode - a model defined in Swagger"""  # noqa: E501

        self._devid = None
        self._lnn = None
        self._services = None
        self.discriminator = None

        self.devid = devid
        if lnn is not None:
            self.lnn = lnn
        if services is not None:
            self.services = services

    @property
    def devid(self):
        """Gets the devid of this ClusterServicesNode.  # noqa: E501

        Device ID.  # noqa: E501

        :return: The devid of this ClusterServicesNode.  # noqa: E501
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """Sets the devid of this ClusterServicesNode.

        Device ID.  # noqa: E501

        :param devid: The devid of this ClusterServicesNode.  # noqa: E501
        :type: int
        """
        if devid is None:
            raise ValueError("Invalid value for `devid`, must not be `None`")  # noqa: E501
        if devid is not None and devid > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `devid`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if devid is not None and devid < 0:  # noqa: E501
            raise ValueError("Invalid value for `devid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._devid = devid

    @property
    def lnn(self):
        """Gets the lnn of this ClusterServicesNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this ClusterServicesNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this ClusterServicesNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this ClusterServicesNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def services(self):
        """Gets the services of this ClusterServicesNode.  # noqa: E501

        List of the services on the node.  # noqa: E501

        :return: The services of this ClusterServicesNode.  # noqa: E501
        :rtype: list[ClusterServicesNodeService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this ClusterServicesNode.

        List of the services on the node.  # noqa: E501

        :param services: The services of this ClusterServicesNode.  # noqa: E501
        :type: list[ClusterServicesNodeService]
        """

        self._services = services

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
        if not isinstance(other, ClusterServicesNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
