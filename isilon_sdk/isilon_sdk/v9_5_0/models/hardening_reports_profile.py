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

from isilon_sdk.v9_5_0.models.hardening_reports_profile_cluster_wide import HardeningReportsProfileClusterWide  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.hardening_reports_profile_node import HardeningReportsProfileNode  # noqa: F401,E501


class HardeningReportsProfile(object):
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
        'applied': 'bool',
        'cluster_wide': 'HardeningReportsProfileClusterWide',
        'name': 'str',
        'nodes': 'list[HardeningReportsProfileNode]'
    }

    attribute_map = {
        'applied': 'applied',
        'cluster_wide': 'cluster_wide',
        'name': 'name',
        'nodes': 'nodes'
    }

    def __init__(self, applied=None, cluster_wide=None, name=None, nodes=None):  # noqa: E501
        """HardeningReportsProfile - a model defined in Swagger"""  # noqa: E501

        self._applied = None
        self._cluster_wide = None
        self._name = None
        self._nodes = None
        self.discriminator = None

        if applied is not None:
            self.applied = applied
        if cluster_wide is not None:
            self.cluster_wide = cluster_wide
        if name is not None:
            self.name = name
        if nodes is not None:
            self.nodes = nodes

    @property
    def applied(self):
        """Gets the applied of this HardeningReportsProfile.  # noqa: E501


        :return: The applied of this HardeningReportsProfile.  # noqa: E501
        :rtype: bool
        """
        return self._applied

    @applied.setter
    def applied(self, applied):
        """Sets the applied of this HardeningReportsProfile.


        :param applied: The applied of this HardeningReportsProfile.  # noqa: E501
        :type: bool
        """

        self._applied = applied

    @property
    def cluster_wide(self):
        """Gets the cluster_wide of this HardeningReportsProfile.  # noqa: E501

        Report for cluster wide rules.  # noqa: E501

        :return: The cluster_wide of this HardeningReportsProfile.  # noqa: E501
        :rtype: HardeningReportsProfileClusterWide
        """
        return self._cluster_wide

    @cluster_wide.setter
    def cluster_wide(self, cluster_wide):
        """Sets the cluster_wide of this HardeningReportsProfile.

        Report for cluster wide rules.  # noqa: E501

        :param cluster_wide: The cluster_wide of this HardeningReportsProfile.  # noqa: E501
        :type: HardeningReportsProfileClusterWide
        """

        self._cluster_wide = cluster_wide

    @property
    def name(self):
        """Gets the name of this HardeningReportsProfile.  # noqa: E501


        :return: The name of this HardeningReportsProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HardeningReportsProfile.


        :param name: The name of this HardeningReportsProfile.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def nodes(self):
        """Gets the nodes of this HardeningReportsProfile.  # noqa: E501

        List of reports for each node.  # noqa: E501

        :return: The nodes of this HardeningReportsProfile.  # noqa: E501
        :rtype: list[HardeningReportsProfileNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this HardeningReportsProfile.

        List of reports for each node.  # noqa: E501

        :param nodes: The nodes of this HardeningReportsProfile.  # noqa: E501
        :type: list[HardeningReportsProfileNode]
        """

        self._nodes = nodes

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
        if not isinstance(other, HardeningReportsProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
