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

from isilon_sdk.v9_3_0.models.groupnet_subnet import GroupnetSubnet  # noqa: F401,E501
from isilon_sdk.v9_3_0.models.subnets_subnet_pool_range import SubnetsSubnetPoolRange  # noqa: F401,E501


class GroupnetSubnetCreateParams(object):
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
        'description': 'str',
        'dsr_addrs': 'list[str]',
        'gateway': 'str',
        'gateway_priority': 'int',
        'mtu': 'int',
        'name': 'str',
        'prefixlen': 'int',
        'sc_service_addrs': 'list[SubnetsSubnetPoolRange]',
        'sc_service_name': 'str',
        'vlan_enabled': 'bool',
        'vlan_id': 'int',
        'addr_family': 'str'
    }

    attribute_map = {
        'description': 'description',
        'dsr_addrs': 'dsr_addrs',
        'gateway': 'gateway',
        'gateway_priority': 'gateway_priority',
        'mtu': 'mtu',
        'name': 'name',
        'prefixlen': 'prefixlen',
        'sc_service_addrs': 'sc_service_addrs',
        'sc_service_name': 'sc_service_name',
        'vlan_enabled': 'vlan_enabled',
        'vlan_id': 'vlan_id',
        'addr_family': 'addr_family'
    }

    def __init__(self, description=None, dsr_addrs=None, gateway=None, gateway_priority=None, mtu=None, name=None, prefixlen=None, sc_service_addrs=None, sc_service_name=None, vlan_enabled=None, vlan_id=None, addr_family=None):  # noqa: E501
        """GroupnetSubnetCreateParams - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._dsr_addrs = None
        self._gateway = None
        self._gateway_priority = None
        self._mtu = None
        self._name = None
        self._prefixlen = None
        self._sc_service_addrs = None
        self._sc_service_name = None
        self._vlan_enabled = None
        self._vlan_id = None
        self._addr_family = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if dsr_addrs is not None:
            self.dsr_addrs = dsr_addrs
        if gateway is not None:
            self.gateway = gateway
        if gateway_priority is not None:
            self.gateway_priority = gateway_priority
        if mtu is not None:
            self.mtu = mtu
        self.name = name
        self.prefixlen = prefixlen
        if sc_service_addrs is not None:
            self.sc_service_addrs = sc_service_addrs
        if sc_service_name is not None:
            self.sc_service_name = sc_service_name
        if vlan_enabled is not None:
            self.vlan_enabled = vlan_enabled
        if vlan_id is not None:
            self.vlan_id = vlan_id
        self.addr_family = addr_family

    @property
    def description(self):
        """Gets the description of this GroupnetSubnetCreateParams.  # noqa: E501

        A description of the subnet.  # noqa: E501

        :return: The description of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupnetSubnetCreateParams.

        A description of the subnet.  # noqa: E501

        :param description: The description of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 128:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def dsr_addrs(self):
        """Gets the dsr_addrs of this GroupnetSubnetCreateParams.  # noqa: E501

        List of Direct Server Return addresses.  # noqa: E501

        :return: The dsr_addrs of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._dsr_addrs

    @dsr_addrs.setter
    def dsr_addrs(self, dsr_addrs):
        """Sets the dsr_addrs of this GroupnetSubnetCreateParams.

        List of Direct Server Return addresses.  # noqa: E501

        :param dsr_addrs: The dsr_addrs of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._dsr_addrs = dsr_addrs

    @property
    def gateway(self):
        """Gets the gateway of this GroupnetSubnetCreateParams.  # noqa: E501

        Gateway IP address.  # noqa: E501

        :return: The gateway of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this GroupnetSubnetCreateParams.

        Gateway IP address.  # noqa: E501

        :param gateway: The gateway of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: str
        """
        if gateway is not None and len(gateway) > 40:
            raise ValueError("Invalid value for `gateway`, length must be less than or equal to `40`")  # noqa: E501
        if gateway is not None and len(gateway) < 1:
            raise ValueError("Invalid value for `gateway`, length must be greater than or equal to `1`")  # noqa: E501

        self._gateway = gateway

    @property
    def gateway_priority(self):
        """Gets the gateway_priority of this GroupnetSubnetCreateParams.  # noqa: E501

        Gateway priority.  # noqa: E501

        :return: The gateway_priority of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._gateway_priority

    @gateway_priority.setter
    def gateway_priority(self, gateway_priority):
        """Sets the gateway_priority of this GroupnetSubnetCreateParams.

        Gateway priority.  # noqa: E501

        :param gateway_priority: The gateway_priority of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: int
        """
        if gateway_priority is not None and gateway_priority > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `gateway_priority`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if gateway_priority is not None and gateway_priority < 1:  # noqa: E501
            raise ValueError("Invalid value for `gateway_priority`, must be a value greater than or equal to `1`")  # noqa: E501

        self._gateway_priority = gateway_priority

    @property
    def mtu(self):
        """Gets the mtu of this GroupnetSubnetCreateParams.  # noqa: E501

        MTU of the subnet.  # noqa: E501

        :return: The mtu of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this GroupnetSubnetCreateParams.

        MTU of the subnet.  # noqa: E501

        :param mtu: The mtu of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: int
        """
        if mtu is not None and mtu > 9000:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must be a value less than or equal to `9000`")  # noqa: E501
        if mtu is not None and mtu < 576:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must be a value greater than or equal to `576`")  # noqa: E501

        self._mtu = mtu

    @property
    def name(self):
        """Gets the name of this GroupnetSubnetCreateParams.  # noqa: E501

        The name of the subnet.  # noqa: E501

        :return: The name of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupnetSubnetCreateParams.

        The name of the subnet.  # noqa: E501

        :param name: The name of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search('^[0-9a-zA-Z_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[0-9a-zA-Z_-]*$/`")  # noqa: E501

        self._name = name

    @property
    def prefixlen(self):
        """Gets the prefixlen of this GroupnetSubnetCreateParams.  # noqa: E501

        Subnet Prefix Length.  # noqa: E501

        :return: The prefixlen of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._prefixlen

    @prefixlen.setter
    def prefixlen(self, prefixlen):
        """Sets the prefixlen of this GroupnetSubnetCreateParams.

        Subnet Prefix Length.  # noqa: E501

        :param prefixlen: The prefixlen of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: int
        """
        if prefixlen is None:
            raise ValueError("Invalid value for `prefixlen`, must not be `None`")  # noqa: E501
        if prefixlen is not None and prefixlen > 128:  # noqa: E501
            raise ValueError("Invalid value for `prefixlen`, must be a value less than or equal to `128`")  # noqa: E501
        if prefixlen is not None and prefixlen < 1:  # noqa: E501
            raise ValueError("Invalid value for `prefixlen`, must be a value greater than or equal to `1`")  # noqa: E501

        self._prefixlen = prefixlen

    @property
    def sc_service_addrs(self):
        """Gets the sc_service_addrs of this GroupnetSubnetCreateParams.  # noqa: E501

        List of IP addresses that SmartConnect listens for DNS requests.  # noqa: E501

        :return: The sc_service_addrs of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: list[SubnetsSubnetPoolRange]
        """
        return self._sc_service_addrs

    @sc_service_addrs.setter
    def sc_service_addrs(self, sc_service_addrs):
        """Sets the sc_service_addrs of this GroupnetSubnetCreateParams.

        List of IP addresses that SmartConnect listens for DNS requests.  # noqa: E501

        :param sc_service_addrs: The sc_service_addrs of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: list[SubnetsSubnetPoolRange]
        """

        self._sc_service_addrs = sc_service_addrs

    @property
    def sc_service_name(self):
        """Gets the sc_service_name of this GroupnetSubnetCreateParams.  # noqa: E501

        Domain Name corresponding to the SmartConnect Service Address.  # noqa: E501

        :return: The sc_service_name of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._sc_service_name

    @sc_service_name.setter
    def sc_service_name(self, sc_service_name):
        """Sets the sc_service_name of this GroupnetSubnetCreateParams.

        Domain Name corresponding to the SmartConnect Service Address.  # noqa: E501

        :param sc_service_name: The sc_service_name of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: str
        """
        if sc_service_name is not None and len(sc_service_name) > 2048:
            raise ValueError("Invalid value for `sc_service_name`, length must be less than or equal to `2048`")  # noqa: E501
        if sc_service_name is not None and len(sc_service_name) < 0:
            raise ValueError("Invalid value for `sc_service_name`, length must be greater than or equal to `0`")  # noqa: E501
        if sc_service_name is not None and not re.search('^$|^[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]*)*$', sc_service_name):  # noqa: E501
            raise ValueError("Invalid value for `sc_service_name`, must be a follow pattern or equal to `/^$|^[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]*)*$/`")  # noqa: E501

        self._sc_service_name = sc_service_name

    @property
    def vlan_enabled(self):
        """Gets the vlan_enabled of this GroupnetSubnetCreateParams.  # noqa: E501

        VLAN tagging enabled or disabled.  # noqa: E501

        :return: The vlan_enabled of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._vlan_enabled

    @vlan_enabled.setter
    def vlan_enabled(self, vlan_enabled):
        """Sets the vlan_enabled of this GroupnetSubnetCreateParams.

        VLAN tagging enabled or disabled.  # noqa: E501

        :param vlan_enabled: The vlan_enabled of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: bool
        """

        self._vlan_enabled = vlan_enabled

    @property
    def vlan_id(self):
        """Gets the vlan_id of this GroupnetSubnetCreateParams.  # noqa: E501

        VLAN ID for all interfaces in the subnet.  # noqa: E501

        :return: The vlan_id of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this GroupnetSubnetCreateParams.

        VLAN ID for all interfaces in the subnet.  # noqa: E501

        :param vlan_id: The vlan_id of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: int
        """
        if vlan_id is not None and vlan_id > 4094:  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must be a value less than or equal to `4094`")  # noqa: E501
        if vlan_id is not None and vlan_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._vlan_id = vlan_id

    @property
    def addr_family(self):
        """Gets the addr_family of this GroupnetSubnetCreateParams.  # noqa: E501

        IP address format.  # noqa: E501

        :return: The addr_family of this GroupnetSubnetCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._addr_family

    @addr_family.setter
    def addr_family(self, addr_family):
        """Sets the addr_family of this GroupnetSubnetCreateParams.

        IP address format.  # noqa: E501

        :param addr_family: The addr_family of this GroupnetSubnetCreateParams.  # noqa: E501
        :type: str
        """
        if addr_family is None:
            raise ValueError("Invalid value for `addr_family`, must not be `None`")  # noqa: E501
        allowed_values = ["ipv4", "ipv6"]  # noqa: E501
        if addr_family not in allowed_values:
            raise ValueError(
                "Invalid value for `addr_family` ({0}), must be one of {1}"  # noqa: E501
                .format(addr_family, allowed_values)
            )

        self._addr_family = addr_family

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
        if not isinstance(other, GroupnetSubnetCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
