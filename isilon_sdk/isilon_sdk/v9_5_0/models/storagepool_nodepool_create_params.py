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

from isilon_sdk.v9_5_0.models.storagepool_nodepool import StoragepoolNodepool  # noqa: F401,E501


class StoragepoolNodepoolCreateParams(object):
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
        'assess': 'bool',
        'l3': 'bool',
        'lnns': 'list[int]',
        'name': 'str',
        'node_type_ids': 'list[int]',
        'protection_policy': 'str',
        'tier': 'str',
        'transfer_limit_pct': 'int',
        'transfer_limit_state': 'str'
    }

    attribute_map = {
        'assess': 'assess',
        'l3': 'l3',
        'lnns': 'lnns',
        'name': 'name',
        'node_type_ids': 'node_type_ids',
        'protection_policy': 'protection_policy',
        'tier': 'tier',
        'transfer_limit_pct': 'transfer_limit_pct',
        'transfer_limit_state': 'transfer_limit_state'
    }

    def __init__(self, assess=None, l3=None, lnns=None, name=None, node_type_ids=None, protection_policy=None, tier=None, transfer_limit_pct=None, transfer_limit_state=None):  # noqa: E501
        """StoragepoolNodepoolCreateParams - a model defined in Swagger"""  # noqa: E501

        self._assess = None
        self._l3 = None
        self._lnns = None
        self._name = None
        self._node_type_ids = None
        self._protection_policy = None
        self._tier = None
        self._transfer_limit_pct = None
        self._transfer_limit_state = None
        self.discriminator = None

        if assess is not None:
            self.assess = assess
        if l3 is not None:
            self.l3 = l3
        self.lnns = lnns
        self.name = name
        if node_type_ids is not None:
            self.node_type_ids = node_type_ids
        if protection_policy is not None:
            self.protection_policy = protection_policy
        if tier is not None:
            self.tier = tier
        if transfer_limit_pct is not None:
            self.transfer_limit_pct = transfer_limit_pct
        if transfer_limit_state is not None:
            self.transfer_limit_state = transfer_limit_state

    @property
    def assess(self):
        """Gets the assess of this StoragepoolNodepoolCreateParams.  # noqa: E501

        Test that the action is possible  # noqa: E501

        :return: The assess of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._assess

    @assess.setter
    def assess(self, assess):
        """Sets the assess of this StoragepoolNodepoolCreateParams.

        Test that the action is possible  # noqa: E501

        :param assess: The assess of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: bool
        """

        self._assess = assess

    @property
    def l3(self):
        """Gets the l3 of this StoragepoolNodepoolCreateParams.  # noqa: E501

        Use SSDs in this node pool for L3 cache.  # noqa: E501

        :return: The l3 of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this StoragepoolNodepoolCreateParams.

        Use SSDs in this node pool for L3 cache.  # noqa: E501

        :param l3: The l3 of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: bool
        """

        self._l3 = l3

    @property
    def lnns(self):
        """Gets the lnns of this StoragepoolNodepoolCreateParams.  # noqa: E501

        The node membership change requested for this node pool.  # noqa: E501

        :return: The lnns of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._lnns

    @lnns.setter
    def lnns(self, lnns):
        """Sets the lnns of this StoragepoolNodepoolCreateParams.

        The node membership change requested for this node pool.  # noqa: E501

        :param lnns: The lnns of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: list[int]
        """
        if lnns is None:
            raise ValueError("Invalid value for `lnns`, must not be `None`")  # noqa: E501

        self._lnns = lnns

    @property
    def name(self):
        """Gets the name of this StoragepoolNodepoolCreateParams.  # noqa: E501

        The node pool name.  # noqa: E501

        :return: The name of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoragepoolNodepoolCreateParams.

        The node pool name.  # noqa: E501

        :param name: The name of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def node_type_ids(self):
        """Gets the node_type_ids of this StoragepoolNodepoolCreateParams.  # noqa: E501

        The node types that are part of this pool.  # noqa: E501

        :return: The node_type_ids of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._node_type_ids

    @node_type_ids.setter
    def node_type_ids(self, node_type_ids):
        """Sets the node_type_ids of this StoragepoolNodepoolCreateParams.

        The node types that are part of this pool.  # noqa: E501

        :param node_type_ids: The node_type_ids of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: list[int]
        """

        self._node_type_ids = node_type_ids

    @property
    def protection_policy(self):
        """Gets the protection_policy of this StoragepoolNodepoolCreateParams.  # noqa: E501

        The node pool protection policy.  # noqa: E501

        :return: The protection_policy of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this StoragepoolNodepoolCreateParams.

        The node pool protection policy.  # noqa: E501

        :param protection_policy: The protection_policy of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: str
        """
        if protection_policy is not None and len(protection_policy) > 255:
            raise ValueError("Invalid value for `protection_policy`, length must be less than or equal to `255`")  # noqa: E501
        if protection_policy is not None and len(protection_policy) < 1:
            raise ValueError("Invalid value for `protection_policy`, length must be greater than or equal to `1`")  # noqa: E501

        self._protection_policy = protection_policy

    @property
    def tier(self):
        """Gets the tier of this StoragepoolNodepoolCreateParams.  # noqa: E501

        The name or ID of the node pool's tier, if it is in a tier.  # noqa: E501

        :return: The tier of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this StoragepoolNodepoolCreateParams.

        The name or ID of the node pool's tier, if it is in a tier.  # noqa: E501

        :param tier: The tier of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: str
        """

        self._tier = tier

    @property
    def transfer_limit_pct(self):
        """Gets the transfer_limit_pct of this StoragepoolNodepoolCreateParams.  # noqa: E501

        Stop moving files to this nodepool when this limit is met  # noqa: E501

        :return: The transfer_limit_pct of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._transfer_limit_pct

    @transfer_limit_pct.setter
    def transfer_limit_pct(self, transfer_limit_pct):
        """Sets the transfer_limit_pct of this StoragepoolNodepoolCreateParams.

        Stop moving files to this nodepool when this limit is met  # noqa: E501

        :param transfer_limit_pct: The transfer_limit_pct of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: int
        """
        if transfer_limit_pct is not None and transfer_limit_pct > 100:  # noqa: E501
            raise ValueError("Invalid value for `transfer_limit_pct`, must be a value less than or equal to `100`")  # noqa: E501
        if transfer_limit_pct is not None and transfer_limit_pct < 0:  # noqa: E501
            raise ValueError("Invalid value for `transfer_limit_pct`, must be a value greater than or equal to `0`")  # noqa: E501

        self._transfer_limit_pct = transfer_limit_pct

    @property
    def transfer_limit_state(self):
        """Gets the transfer_limit_state of this StoragepoolNodepoolCreateParams.  # noqa: E501

        How the transfer limit value is being applied  # noqa: E501

        :return: The transfer_limit_state of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._transfer_limit_state

    @transfer_limit_state.setter
    def transfer_limit_state(self, transfer_limit_state):
        """Sets the transfer_limit_state of this StoragepoolNodepoolCreateParams.

        How the transfer limit value is being applied  # noqa: E501

        :param transfer_limit_state: The transfer_limit_state of this StoragepoolNodepoolCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["disabled", "default"]  # noqa: E501
        if transfer_limit_state not in allowed_values:
            raise ValueError(
                "Invalid value for `transfer_limit_state` ({0}), must be one of {1}"  # noqa: E501
                .format(transfer_limit_state, allowed_values)
            )

        self._transfer_limit_state = transfer_limit_state

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
        if not isinstance(other, StoragepoolNodepoolCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
