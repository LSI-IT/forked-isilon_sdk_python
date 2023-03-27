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

from isilon_sdk.v9_2_0.models.node_internal_ip_address_node import NodeInternalIpAddressNode  # noqa: F401,E501
from isilon_sdk.v9_2_0.models.node_status_cpu_error import NodeStatusCpuError  # noqa: F401,E501


class NodeInternalIpAddress(object):
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
        'errors': 'list[NodeStatusCpuError]',
        'nodes': 'list[NodeInternalIpAddressNode]',
        'total': 'int'
    }

    attribute_map = {
        'errors': 'errors',
        'nodes': 'nodes',
        'total': 'total'
    }

    def __init__(self, errors=None, nodes=None, total=None):  # noqa: E501
        """NodeInternalIpAddress - a model defined in Swagger"""  # noqa: E501

        self._errors = None
        self._nodes = None
        self._total = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if nodes is not None:
            self.nodes = nodes
        if total is not None:
            self.total = total

    @property
    def errors(self):
        """Gets the errors of this NodeInternalIpAddress.  # noqa: E501

        A list of errors encountered by the individual nodes involved in this request, or an empty list if there were no errors.  # noqa: E501

        :return: The errors of this NodeInternalIpAddress.  # noqa: E501
        :rtype: list[NodeStatusCpuError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this NodeInternalIpAddress.

        A list of errors encountered by the individual nodes involved in this request, or an empty list if there were no errors.  # noqa: E501

        :param errors: The errors of this NodeInternalIpAddress.  # noqa: E501
        :type: list[NodeStatusCpuError]
        """

        self._errors = errors

    @property
    def nodes(self):
        """Gets the nodes of this NodeInternalIpAddress.  # noqa: E501

        The responses from the individual nodes involved in this request.  # noqa: E501

        :return: The nodes of this NodeInternalIpAddress.  # noqa: E501
        :rtype: list[NodeInternalIpAddressNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this NodeInternalIpAddress.

        The responses from the individual nodes involved in this request.  # noqa: E501

        :param nodes: The nodes of this NodeInternalIpAddress.  # noqa: E501
        :type: list[NodeInternalIpAddressNode]
        """

        self._nodes = nodes

    @property
    def total(self):
        """Gets the total of this NodeInternalIpAddress.  # noqa: E501

        The total number of nodes responding.  # noqa: E501

        :return: The total of this NodeInternalIpAddress.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NodeInternalIpAddress.

        The total number of nodes responding.  # noqa: E501

        :param total: The total of this NodeInternalIpAddress.  # noqa: E501
        :type: int
        """
        if total is not None and total > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if total is not None and total < 0:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, NodeInternalIpAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
