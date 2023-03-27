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

from isilon_sdk.v9_5_0.models.firewall_policy import FirewallPolicy  # noqa: F401,E501


class FirewallPolicyExtended(object):
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
        'default_action': 'str',
        'description': 'str',
        'max_rules': 'int',
        'name': 'str',
        'pools': 'list[str]',
        'subnets': 'list[str]',
        'id': 'str',
        'rules': 'list[str]'
    }

    attribute_map = {
        'default_action': 'default_action',
        'description': 'description',
        'max_rules': 'max_rules',
        'name': 'name',
        'pools': 'pools',
        'subnets': 'subnets',
        'id': 'id',
        'rules': 'rules'
    }

    def __init__(self, default_action=None, description=None, max_rules=None, name=None, pools=None, subnets=None, id=None, rules=None):  # noqa: E501
        """FirewallPolicyExtended - a model defined in Swagger"""  # noqa: E501

        self._default_action = None
        self._description = None
        self._max_rules = None
        self._name = None
        self._pools = None
        self._subnets = None
        self._id = None
        self._rules = None
        self.discriminator = None

        if default_action is not None:
            self.default_action = default_action
        if description is not None:
            self.description = description
        if max_rules is not None:
            self.max_rules = max_rules
        if name is not None:
            self.name = name
        if pools is not None:
            self.pools = pools
        if subnets is not None:
            self.subnets = subnets
        if id is not None:
            self.id = id
        if rules is not None:
            self.rules = rules

    @property
    def default_action(self):
        """Gets the default_action of this FirewallPolicyExtended.  # noqa: E501

        Policy default action  # noqa: E501

        :return: The default_action of this FirewallPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._default_action

    @default_action.setter
    def default_action(self, default_action):
        """Sets the default_action of this FirewallPolicyExtended.

        Policy default action  # noqa: E501

        :param default_action: The default_action of this FirewallPolicyExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow", "deny"]  # noqa: E501
        if default_action not in allowed_values:
            raise ValueError(
                "Invalid value for `default_action` ({0}), must be one of {1}"  # noqa: E501
                .format(default_action, allowed_values)
            )

        self._default_action = default_action

    @property
    def description(self):
        """Gets the description of this FirewallPolicyExtended.  # noqa: E501

        A description of the firewall policy.  # noqa: E501

        :return: The description of this FirewallPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FirewallPolicyExtended.

        A description of the firewall policy.  # noqa: E501

        :param description: The description of this FirewallPolicyExtended.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def max_rules(self):
        """Gets the max_rules of this FirewallPolicyExtended.  # noqa: E501

        Maximum rule counts in one policy  # noqa: E501

        :return: The max_rules of this FirewallPolicyExtended.  # noqa: E501
        :rtype: int
        """
        return self._max_rules

    @max_rules.setter
    def max_rules(self, max_rules):
        """Sets the max_rules of this FirewallPolicyExtended.

        Maximum rule counts in one policy  # noqa: E501

        :param max_rules: The max_rules of this FirewallPolicyExtended.  # noqa: E501
        :type: int
        """
        if max_rules is not None and max_rules > 200:  # noqa: E501
            raise ValueError("Invalid value for `max_rules`, must be a value less than or equal to `200`")  # noqa: E501
        if max_rules is not None and max_rules < 100:  # noqa: E501
            raise ValueError("Invalid value for `max_rules`, must be a value greater than or equal to `100`")  # noqa: E501

        self._max_rules = max_rules

    @property
    def name(self):
        """Gets the name of this FirewallPolicyExtended.  # noqa: E501

        The name of the firewall policy.  # noqa: E501

        :return: The name of this FirewallPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FirewallPolicyExtended.

        The name of the firewall policy.  # noqa: E501

        :param name: The name of this FirewallPolicyExtended.  # noqa: E501
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
    def pools(self):
        """Gets the pools of this FirewallPolicyExtended.  # noqa: E501

        List of Network Pools this policy is currently applied to.  # noqa: E501

        :return: The pools of this FirewallPolicyExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this FirewallPolicyExtended.

        List of Network Pools this policy is currently applied to.  # noqa: E501

        :param pools: The pools of this FirewallPolicyExtended.  # noqa: E501
        :type: list[str]
        """

        self._pools = pools

    @property
    def subnets(self):
        """Gets the subnets of this FirewallPolicyExtended.  # noqa: E501

        List of Network Subnets this policy is currently applied for SSIP service.  # noqa: E501

        :return: The subnets of this FirewallPolicyExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this FirewallPolicyExtended.

        List of Network Subnets this policy is currently applied for SSIP service.  # noqa: E501

        :param subnets: The subnets of this FirewallPolicyExtended.  # noqa: E501
        :type: list[str]
        """

        self._subnets = subnets

    @property
    def id(self):
        """Gets the id of this FirewallPolicyExtended.  # noqa: E501

        Unique firewall policy ID.  # noqa: E501

        :return: The id of this FirewallPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirewallPolicyExtended.

        Unique firewall policy ID.  # noqa: E501

        :param id: The id of this FirewallPolicyExtended.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 32:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `32`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501
        if id is not None and not re.search('^[0-9a-zA-Z_-]*$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[0-9a-zA-Z_-]*$/`")  # noqa: E501

        self._id = id

    @property
    def rules(self):
        """Gets the rules of this FirewallPolicyExtended.  # noqa: E501

        Name of the rules inside policy.  # noqa: E501

        :return: The rules of this FirewallPolicyExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this FirewallPolicyExtended.

        Name of the rules inside policy.  # noqa: E501

        :param rules: The rules of this FirewallPolicyExtended.  # noqa: E501
        :type: list[str]
        """

        self._rules = rules

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
        if not isinstance(other, FirewallPolicyExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
