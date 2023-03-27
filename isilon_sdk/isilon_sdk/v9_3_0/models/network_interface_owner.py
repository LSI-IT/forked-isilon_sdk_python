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


class NetworkInterfaceOwner(object):
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
        'access_zone': 'str',
        'groupnet': 'str',
        'id': 'str',
        'ip_addrs': 'list[str]',
        'pool': 'str',
        'subnet': 'str',
        'type': 'str',
        'vlan_id': 'int'
    }

    attribute_map = {
        'access_zone': 'access_zone',
        'groupnet': 'groupnet',
        'id': 'id',
        'ip_addrs': 'ip_addrs',
        'pool': 'pool',
        'subnet': 'subnet',
        'type': 'type',
        'vlan_id': 'vlan_id'
    }

    def __init__(self, access_zone=None, groupnet=None, id=None, ip_addrs=None, pool=None, subnet=None, type=None, vlan_id=None):  # noqa: E501
        """NetworkInterfaceOwner - a model defined in Swagger"""  # noqa: E501

        self._access_zone = None
        self._groupnet = None
        self._id = None
        self._ip_addrs = None
        self._pool = None
        self._subnet = None
        self._type = None
        self._vlan_id = None
        self.discriminator = None

        if access_zone is not None:
            self.access_zone = access_zone
        if groupnet is not None:
            self.groupnet = groupnet
        if id is not None:
            self.id = id
        if ip_addrs is not None:
            self.ip_addrs = ip_addrs
        if pool is not None:
            self.pool = pool
        if subnet is not None:
            self.subnet = subnet
        if type is not None:
            self.type = type
        if vlan_id is not None:
            self.vlan_id = vlan_id

    @property
    def access_zone(self):
        """Gets the access_zone of this NetworkInterfaceOwner.  # noqa: E501

        Name of configured Access Zone.  # noqa: E501

        :return: The access_zone of this NetworkInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._access_zone

    @access_zone.setter
    def access_zone(self, access_zone):
        """Sets the access_zone of this NetworkInterfaceOwner.

        Name of configured Access Zone.  # noqa: E501

        :param access_zone: The access_zone of this NetworkInterfaceOwner.  # noqa: E501
        :type: str
        """
        if access_zone is not None and len(access_zone) > 255:
            raise ValueError("Invalid value for `access_zone`, length must be less than or equal to `255`")  # noqa: E501
        if access_zone is not None and len(access_zone) < 0:
            raise ValueError("Invalid value for `access_zone`, length must be greater than or equal to `0`")  # noqa: E501

        self._access_zone = access_zone

    @property
    def groupnet(self):
        """Gets the groupnet of this NetworkInterfaceOwner.  # noqa: E501


        :return: The groupnet of this NetworkInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """Sets the groupnet of this NetworkInterfaceOwner.


        :param groupnet: The groupnet of this NetworkInterfaceOwner.  # noqa: E501
        :type: str
        """
        if groupnet is not None and len(groupnet) > 32:
            raise ValueError("Invalid value for `groupnet`, length must be less than or equal to `32`")  # noqa: E501
        if groupnet is not None and len(groupnet) < 1:
            raise ValueError("Invalid value for `groupnet`, length must be greater than or equal to `1`")  # noqa: E501

        self._groupnet = groupnet

    @property
    def id(self):
        """Gets the id of this NetworkInterfaceOwner.  # noqa: E501

        The id of the owner. The concatenation of the groupnet, subnet, and pool fields as relevant.  # noqa: E501

        :return: The id of this NetworkInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkInterfaceOwner.

        The id of the owner. The concatenation of the groupnet, subnet, and pool fields as relevant.  # noqa: E501

        :param id: The id of this NetworkInterfaceOwner.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 98:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `98`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def ip_addrs(self):
        """Gets the ip_addrs of this NetworkInterfaceOwner.  # noqa: E501

        List of IPs on this interface in the pool  # noqa: E501

        :return: The ip_addrs of this NetworkInterfaceOwner.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addrs

    @ip_addrs.setter
    def ip_addrs(self, ip_addrs):
        """Sets the ip_addrs of this NetworkInterfaceOwner.

        List of IPs on this interface in the pool  # noqa: E501

        :param ip_addrs: The ip_addrs of this NetworkInterfaceOwner.  # noqa: E501
        :type: list[str]
        """

        self._ip_addrs = ip_addrs

    @property
    def pool(self):
        """Gets the pool of this NetworkInterfaceOwner.  # noqa: E501


        :return: The pool of this NetworkInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this NetworkInterfaceOwner.


        :param pool: The pool of this NetworkInterfaceOwner.  # noqa: E501
        :type: str
        """
        if pool is not None and len(pool) > 32:
            raise ValueError("Invalid value for `pool`, length must be less than or equal to `32`")  # noqa: E501
        if pool is not None and len(pool) < 0:
            raise ValueError("Invalid value for `pool`, length must be greater than or equal to `0`")  # noqa: E501

        self._pool = pool

    @property
    def subnet(self):
        """Gets the subnet of this NetworkInterfaceOwner.  # noqa: E501


        :return: The subnet of this NetworkInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this NetworkInterfaceOwner.


        :param subnet: The subnet of this NetworkInterfaceOwner.  # noqa: E501
        :type: str
        """
        if subnet is not None and len(subnet) > 32:
            raise ValueError("Invalid value for `subnet`, length must be less than or equal to `32`")  # noqa: E501
        if subnet is not None and len(subnet) < 1:
            raise ValueError("Invalid value for `subnet`, length must be greater than or equal to `1`")  # noqa: E501

        self._subnet = subnet

    @property
    def type(self):
        """Gets the type of this NetworkInterfaceOwner.  # noqa: E501

        Specifies the type of network addresses that this interface owner contains.  # noqa: E501

        :return: The type of this NetworkInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkInterfaceOwner.

        Specifies the type of network addresses that this interface owner contains.  # noqa: E501

        :param type: The type of this NetworkInterfaceOwner.  # noqa: E501
        :type: str
        """
        allowed_values = ["static", "dynamic", "smartconnect_service", "ipv6_link_local", "internal"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def vlan_id(self):
        """Gets the vlan_id of this NetworkInterfaceOwner.  # noqa: E501


        :return: The vlan_id of this NetworkInterfaceOwner.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this NetworkInterfaceOwner.


        :param vlan_id: The vlan_id of this NetworkInterfaceOwner.  # noqa: E501
        :type: int
        """
        if vlan_id is not None and vlan_id > 4094:  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must be a value less than or equal to `4094`")  # noqa: E501
        if vlan_id is not None and vlan_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._vlan_id = vlan_id

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
        if not isinstance(other, NetworkInterfaceOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
