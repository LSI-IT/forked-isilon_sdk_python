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

from isilon_sdk.v9_5_0.models.policies_policy_rule_dst_ports import PoliciesPolicyRuleDstPorts  # noqa: F401,E501


class PoliciesPolicyRule(object):
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
        'action': 'str',
        'description': 'str',
        'dst_ports': 'PoliciesPolicyRuleDstPorts',
        'index': 'int',
        'name': 'str',
        'protocol': 'str',
        'src_networks': 'list[str]',
        'src_ports': 'PoliciesPolicyRuleDstPorts'
    }

    attribute_map = {
        'action': 'action',
        'description': 'description',
        'dst_ports': 'dst_ports',
        'index': 'index',
        'name': 'name',
        'protocol': 'protocol',
        'src_networks': 'src_networks',
        'src_ports': 'src_ports'
    }

    def __init__(self, action=None, description=None, dst_ports=None, index=None, name=None, protocol=None, src_networks=None, src_ports=None):  # noqa: E501
        """PoliciesPolicyRule - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._description = None
        self._dst_ports = None
        self._index = None
        self._name = None
        self._protocol = None
        self._src_networks = None
        self._src_ports = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        if dst_ports is not None:
            self.dst_ports = dst_ports
        if index is not None:
            self.index = index
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if src_networks is not None:
            self.src_networks = src_networks
        if src_ports is not None:
            self.src_ports = src_ports

    @property
    def action(self):
        """Gets the action of this PoliciesPolicyRule.  # noqa: E501

        Rule action  # noqa: E501

        :return: The action of this PoliciesPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PoliciesPolicyRule.

        Rule action  # noqa: E501

        :param action: The action of this PoliciesPolicyRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow", "deny", "reject"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def description(self):
        """Gets the description of this PoliciesPolicyRule.  # noqa: E501

        A description of the firewall rule.  # noqa: E501

        :return: The description of this PoliciesPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PoliciesPolicyRule.

        A description of the firewall rule.  # noqa: E501

        :param description: The description of this PoliciesPolicyRule.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def dst_ports(self):
        """Gets the dst_ports of this PoliciesPolicyRule.  # noqa: E501

        Customer specified protocols or OneFS default services's protocols for destination control  # noqa: E501

        :return: The dst_ports of this PoliciesPolicyRule.  # noqa: E501
        :rtype: PoliciesPolicyRuleDstPorts
        """
        return self._dst_ports

    @dst_ports.setter
    def dst_ports(self, dst_ports):
        """Sets the dst_ports of this PoliciesPolicyRule.

        Customer specified protocols or OneFS default services's protocols for destination control  # noqa: E501

        :param dst_ports: The dst_ports of this PoliciesPolicyRule.  # noqa: E501
        :type: PoliciesPolicyRuleDstPorts
        """

        self._dst_ports = dst_ports

    @property
    def index(self):
        """Gets the index of this PoliciesPolicyRule.  # noqa: E501

        Firewall rule index in policy  # noqa: E501

        :return: The index of this PoliciesPolicyRule.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this PoliciesPolicyRule.

        Firewall rule index in policy  # noqa: E501

        :param index: The index of this PoliciesPolicyRule.  # noqa: E501
        :type: int
        """
        if index is not None and index > 200:  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value less than or equal to `200`")  # noqa: E501
        if index is not None and index < 1:  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value greater than or equal to `1`")  # noqa: E501

        self._index = index

    @property
    def name(self):
        """Gets the name of this PoliciesPolicyRule.  # noqa: E501

        The name of the firewall rule.  # noqa: E501

        :return: The name of this PoliciesPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PoliciesPolicyRule.

        The name of the firewall rule.  # noqa: E501

        :param name: The name of this PoliciesPolicyRule.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search('^[0-9a-zA-Z_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[0-9a-zA-Z_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this PoliciesPolicyRule.  # noqa: E501

        Firewall rule set on protocol  # noqa: E501

        :return: The protocol of this PoliciesPolicyRule.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PoliciesPolicyRule.

        Firewall rule set on protocol  # noqa: E501

        :param protocol: The protocol of this PoliciesPolicyRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALL", "TCP", "UDP", "ICMP", "ICMP6"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def src_networks(self):
        """Gets the src_networks of this PoliciesPolicyRule.  # noqa: E501

        Source Networks  # noqa: E501

        :return: The src_networks of this PoliciesPolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._src_networks

    @src_networks.setter
    def src_networks(self, src_networks):
        """Sets the src_networks of this PoliciesPolicyRule.

        Source Networks  # noqa: E501

        :param src_networks: The src_networks of this PoliciesPolicyRule.  # noqa: E501
        :type: list[str]
        """

        self._src_networks = src_networks

    @property
    def src_ports(self):
        """Gets the src_ports of this PoliciesPolicyRule.  # noqa: E501

        Customer specified protocols or OneFS default services's protocols for source control  # noqa: E501

        :return: The src_ports of this PoliciesPolicyRule.  # noqa: E501
        :rtype: PoliciesPolicyRuleDstPorts
        """
        return self._src_ports

    @src_ports.setter
    def src_ports(self, src_ports):
        """Sets the src_ports of this PoliciesPolicyRule.

        Customer specified protocols or OneFS default services's protocols for source control  # noqa: E501

        :param src_ports: The src_ports of this PoliciesPolicyRule.  # noqa: E501
        :type: PoliciesPolicyRuleDstPorts
        """

        self._src_ports = src_ports

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
        if not isinstance(other, PoliciesPolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
