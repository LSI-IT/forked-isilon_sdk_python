# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_1_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.auth_id_ntoken_privilege_item import AuthIdNtokenPrivilegeItem  # noqa: F401,E501


class AuthIdNtoken(object):
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
        'additional_id': 'list[AuthAccessAccessItemFileGroup]',
        'gid': 'AuthAccessAccessItemFileGroup',
        'group_sid': 'AuthAccessAccessItemFileGroup',
        'ifs_restricted': 'bool',
        'local_address': 'str',
        'on_disk_group_id': 'AuthAccessAccessItemFileGroup',
        'on_disk_user_id': 'AuthAccessAccessItemFileGroup',
        'privilege': 'list[AuthIdNtokenPrivilegeItem]',
        'protocol': 'int',
        'remote_address': 'str',
        'uid': 'AuthAccessAccessItemFileGroup',
        'user_sid': 'AuthAccessAccessItemFileGroup',
        'zid': 'int',
        'zone_id': 'str'
    }

    attribute_map = {
        'additional_id': 'additional_id',
        'gid': 'gid',
        'group_sid': 'group_sid',
        'ifs_restricted': 'ifs_restricted',
        'local_address': 'local_address',
        'on_disk_group_id': 'on_disk_group_id',
        'on_disk_user_id': 'on_disk_user_id',
        'privilege': 'privilege',
        'protocol': 'protocol',
        'remote_address': 'remote_address',
        'uid': 'uid',
        'user_sid': 'user_sid',
        'zid': 'zid',
        'zone_id': 'zone_id'
    }

    def __init__(self, additional_id=None, gid=None, group_sid=None, ifs_restricted=None, local_address=None, on_disk_group_id=None, on_disk_user_id=None, privilege=None, protocol=None, remote_address=None, uid=None, user_sid=None, zid=None, zone_id=None):  # noqa: E501
        """AuthIdNtoken - a model defined in Swagger"""  # noqa: E501

        self._additional_id = None
        self._gid = None
        self._group_sid = None
        self._ifs_restricted = None
        self._local_address = None
        self._on_disk_group_id = None
        self._on_disk_user_id = None
        self._privilege = None
        self._protocol = None
        self._remote_address = None
        self._uid = None
        self._user_sid = None
        self._zid = None
        self._zone_id = None
        self.discriminator = None

        if additional_id is not None:
            self.additional_id = additional_id
        if gid is not None:
            self.gid = gid
        if group_sid is not None:
            self.group_sid = group_sid
        if ifs_restricted is not None:
            self.ifs_restricted = ifs_restricted
        if local_address is not None:
            self.local_address = local_address
        if on_disk_group_id is not None:
            self.on_disk_group_id = on_disk_group_id
        if on_disk_user_id is not None:
            self.on_disk_user_id = on_disk_user_id
        if privilege is not None:
            self.privilege = privilege
        if protocol is not None:
            self.protocol = protocol
        if remote_address is not None:
            self.remote_address = remote_address
        if uid is not None:
            self.uid = uid
        if user_sid is not None:
            self.user_sid = user_sid
        if zid is not None:
            self.zid = zid
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def additional_id(self):
        """Gets the additional_id of this AuthIdNtoken.  # noqa: E501

        Specifies additional UIDs, GIDs, and SIDs.  # noqa: E501

        :return: The additional_id of this AuthIdNtoken.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._additional_id

    @additional_id.setter
    def additional_id(self, additional_id):
        """Sets the additional_id of this AuthIdNtoken.

        Specifies additional UIDs, GIDs, and SIDs.  # noqa: E501

        :param additional_id: The additional_id of this AuthIdNtoken.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """

        self._additional_id = additional_id

    @property
    def gid(self):
        """Gets the gid of this AuthIdNtoken.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The gid of this AuthIdNtoken.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this AuthIdNtoken.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param gid: The gid of this AuthIdNtoken.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._gid = gid

    @property
    def group_sid(self):
        """Gets the group_sid of this AuthIdNtoken.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The group_sid of this AuthIdNtoken.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._group_sid

    @group_sid.setter
    def group_sid(self, group_sid):
        """Sets the group_sid of this AuthIdNtoken.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param group_sid: The group_sid of this AuthIdNtoken.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._group_sid = group_sid

    @property
    def ifs_restricted(self):
        """Gets the ifs_restricted of this AuthIdNtoken.  # noqa: E501

        Indicates if this user has restricted access to the /ifs file system.  # noqa: E501

        :return: The ifs_restricted of this AuthIdNtoken.  # noqa: E501
        :rtype: bool
        """
        return self._ifs_restricted

    @ifs_restricted.setter
    def ifs_restricted(self, ifs_restricted):
        """Sets the ifs_restricted of this AuthIdNtoken.

        Indicates if this user has restricted access to the /ifs file system.  # noqa: E501

        :param ifs_restricted: The ifs_restricted of this AuthIdNtoken.  # noqa: E501
        :type: bool
        """

        self._ifs_restricted = ifs_restricted

    @property
    def local_address(self):
        """Gets the local_address of this AuthIdNtoken.  # noqa: E501


        :return: The local_address of this AuthIdNtoken.  # noqa: E501
        :rtype: str
        """
        return self._local_address

    @local_address.setter
    def local_address(self, local_address):
        """Sets the local_address of this AuthIdNtoken.


        :param local_address: The local_address of this AuthIdNtoken.  # noqa: E501
        :type: str
        """
        if local_address is not None and len(local_address) > 255:
            raise ValueError("Invalid value for `local_address`, length must be less than or equal to `255`")  # noqa: E501
        if local_address is not None and len(local_address) < 0:
            raise ValueError("Invalid value for `local_address`, length must be greater than or equal to `0`")  # noqa: E501

        self._local_address = local_address

    @property
    def on_disk_group_id(self):
        """Gets the on_disk_group_id of this AuthIdNtoken.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The on_disk_group_id of this AuthIdNtoken.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._on_disk_group_id

    @on_disk_group_id.setter
    def on_disk_group_id(self, on_disk_group_id):
        """Sets the on_disk_group_id of this AuthIdNtoken.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param on_disk_group_id: The on_disk_group_id of this AuthIdNtoken.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._on_disk_group_id = on_disk_group_id

    @property
    def on_disk_user_id(self):
        """Gets the on_disk_user_id of this AuthIdNtoken.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The on_disk_user_id of this AuthIdNtoken.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._on_disk_user_id

    @on_disk_user_id.setter
    def on_disk_user_id(self, on_disk_user_id):
        """Sets the on_disk_user_id of this AuthIdNtoken.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param on_disk_user_id: The on_disk_user_id of this AuthIdNtoken.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._on_disk_user_id = on_disk_user_id

    @property
    def privilege(self):
        """Gets the privilege of this AuthIdNtoken.  # noqa: E501

        Specifies the privileges granted to the currently authenticated user.  # noqa: E501

        :return: The privilege of this AuthIdNtoken.  # noqa: E501
        :rtype: list[AuthIdNtokenPrivilegeItem]
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this AuthIdNtoken.

        Specifies the privileges granted to the currently authenticated user.  # noqa: E501

        :param privilege: The privilege of this AuthIdNtoken.  # noqa: E501
        :type: list[AuthIdNtokenPrivilegeItem]
        """

        self._privilege = privilege

    @property
    def protocol(self):
        """Gets the protocol of this AuthIdNtoken.  # noqa: E501


        :return: The protocol of this AuthIdNtoken.  # noqa: E501
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this AuthIdNtoken.


        :param protocol: The protocol of this AuthIdNtoken.  # noqa: E501
        :type: int
        """
        if protocol is not None and protocol > 128:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must be a value less than or equal to `128`")  # noqa: E501
        if protocol is not None and protocol < 0:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must be a value greater than or equal to `0`")  # noqa: E501

        self._protocol = protocol

    @property
    def remote_address(self):
        """Gets the remote_address of this AuthIdNtoken.  # noqa: E501


        :return: The remote_address of this AuthIdNtoken.  # noqa: E501
        :rtype: str
        """
        return self._remote_address

    @remote_address.setter
    def remote_address(self, remote_address):
        """Sets the remote_address of this AuthIdNtoken.


        :param remote_address: The remote_address of this AuthIdNtoken.  # noqa: E501
        :type: str
        """
        if remote_address is not None and len(remote_address) > 255:
            raise ValueError("Invalid value for `remote_address`, length must be less than or equal to `255`")  # noqa: E501
        if remote_address is not None and len(remote_address) < 0:
            raise ValueError("Invalid value for `remote_address`, length must be greater than or equal to `0`")  # noqa: E501

        self._remote_address = remote_address

    @property
    def uid(self):
        """Gets the uid of this AuthIdNtoken.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The uid of this AuthIdNtoken.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AuthIdNtoken.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param uid: The uid of this AuthIdNtoken.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._uid = uid

    @property
    def user_sid(self):
        """Gets the user_sid of this AuthIdNtoken.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The user_sid of this AuthIdNtoken.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._user_sid

    @user_sid.setter
    def user_sid(self, user_sid):
        """Sets the user_sid of this AuthIdNtoken.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param user_sid: The user_sid of this AuthIdNtoken.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._user_sid = user_sid

    @property
    def zid(self):
        """Gets the zid of this AuthIdNtoken.  # noqa: E501


        :return: The zid of this AuthIdNtoken.  # noqa: E501
        :rtype: int
        """
        return self._zid

    @zid.setter
    def zid(self, zid):
        """Sets the zid of this AuthIdNtoken.


        :param zid: The zid of this AuthIdNtoken.  # noqa: E501
        :type: int
        """
        if zid is not None and zid > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `zid`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if zid is not None and zid < 0:  # noqa: E501
            raise ValueError("Invalid value for `zid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._zid = zid

    @property
    def zone_id(self):
        """Gets the zone_id of this AuthIdNtoken.  # noqa: E501


        :return: The zone_id of this AuthIdNtoken.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this AuthIdNtoken.


        :param zone_id: The zone_id of this AuthIdNtoken.  # noqa: E501
        :type: str
        """
        if zone_id is not None and len(zone_id) > 255:
            raise ValueError("Invalid value for `zone_id`, length must be less than or equal to `255`")  # noqa: E501
        if zone_id is not None and len(zone_id) < 0:
            raise ValueError("Invalid value for `zone_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._zone_id = zone_id

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
        if not isinstance(other, AuthIdNtoken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
