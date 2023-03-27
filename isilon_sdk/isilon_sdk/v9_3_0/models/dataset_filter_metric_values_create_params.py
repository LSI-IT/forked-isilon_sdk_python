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


class DatasetFilterMetricValuesCreateParams(object):
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
        'export_id': 'float',
        'groupname': 'str',
        'local_address': 'str',
        'path': 'str',
        'protocol': 'str',
        'remote_address': 'str',
        'share_name': 'str',
        'username': 'str',
        'zone_name': 'str'
    }

    attribute_map = {
        'export_id': 'export_id',
        'groupname': 'groupname',
        'local_address': 'local_address',
        'path': 'path',
        'protocol': 'protocol',
        'remote_address': 'remote_address',
        'share_name': 'share_name',
        'username': 'username',
        'zone_name': 'zone_name'
    }

    def __init__(self, export_id=None, groupname=None, local_address=None, path=None, protocol=None, remote_address=None, share_name=None, username=None, zone_name=None):  # noqa: E501
        """DatasetFilterMetricValuesCreateParams - a model defined in Swagger"""  # noqa: E501

        self._export_id = None
        self._groupname = None
        self._local_address = None
        self._path = None
        self._protocol = None
        self._remote_address = None
        self._share_name = None
        self._username = None
        self._zone_name = None
        self.discriminator = None

        if export_id is not None:
            self.export_id = export_id
        if groupname is not None:
            self.groupname = groupname
        if local_address is not None:
            self.local_address = local_address
        if path is not None:
            self.path = path
        if protocol is not None:
            self.protocol = protocol
        if remote_address is not None:
            self.remote_address = remote_address
        if share_name is not None:
            self.share_name = share_name
        if username is not None:
            self.username = username
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def export_id(self):
        """Gets the export_id of this DatasetFilterMetricValuesCreateParams.  # noqa: E501

        NFS export ID  # noqa: E501

        :return: The export_id of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: float
        """
        return self._export_id

    @export_id.setter
    def export_id(self, export_id):
        """Sets the export_id of this DatasetFilterMetricValuesCreateParams.

        NFS export ID  # noqa: E501

        :param export_id: The export_id of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: float
        """
        if export_id is not None and export_id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `export_id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if export_id is not None and export_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `export_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._export_id = export_id

    @property
    def groupname(self):
        """Gets the groupname of this DatasetFilterMetricValuesCreateParams.  # noqa: E501

        groupname  # noqa: E501

        :return: The groupname of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname):
        """Sets the groupname of this DatasetFilterMetricValuesCreateParams.

        groupname  # noqa: E501

        :param groupname: The groupname of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: str
        """
        if groupname is not None and len(groupname) > 255:
            raise ValueError("Invalid value for `groupname`, length must be less than or equal to `255`")  # noqa: E501
        if groupname is not None and len(groupname) < 1:
            raise ValueError("Invalid value for `groupname`, length must be greater than or equal to `1`")  # noqa: E501

        self._groupname = groupname

    @property
    def local_address(self):
        """Gets the local_address of this DatasetFilterMetricValuesCreateParams.  # noqa: E501

        Local IPv4, IPv6 address, address range, or subnet.  # noqa: E501

        :return: The local_address of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._local_address

    @local_address.setter
    def local_address(self, local_address):
        """Sets the local_address of this DatasetFilterMetricValuesCreateParams.

        Local IPv4, IPv6 address, address range, or subnet.  # noqa: E501

        :param local_address: The local_address of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: str
        """
        if local_address is not None and len(local_address) > 91:
            raise ValueError("Invalid value for `local_address`, length must be less than or equal to `91`")  # noqa: E501
        if local_address is not None and len(local_address) < 1:
            raise ValueError("Invalid value for `local_address`, length must be greater than or equal to `1`")  # noqa: E501
        if local_address is not None and not re.search('^[0-9a-fA-F:.\/-]*$', local_address):  # noqa: E501
            raise ValueError("Invalid value for `local_address`, must be a follow pattern or equal to `/^[0-9a-fA-F:.\/-]*$/`")  # noqa: E501

        self._local_address = local_address

    @property
    def path(self):
        """Gets the path of this DatasetFilterMetricValuesCreateParams.  # noqa: E501


        :return: The path of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DatasetFilterMetricValuesCreateParams.


        :param path: The path of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: str
        """
        if path is not None and len(path) > 4096:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if path is not None and len(path) < 4:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `4`")  # noqa: E501
        if path is not None and not re.search('^\/ifs$|^\/ifs\/', path):  # noqa: E501
            raise ValueError("Invalid value for `path`, must be a follow pattern or equal to `/^\/ifs$|^\/ifs\//`")  # noqa: E501

        self._path = path

    @property
    def protocol(self):
        """Gets the protocol of this DatasetFilterMetricValuesCreateParams.  # noqa: E501

        The protocol used for the request  # noqa: E501

        :return: The protocol of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DatasetFilterMetricValuesCreateParams.

        The protocol used for the request  # noqa: E501

        :param protocol: The protocol of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def remote_address(self):
        """Gets the remote_address of this DatasetFilterMetricValuesCreateParams.  # noqa: E501

        Client IPv4 or IPv6 address, address range, or subnet.  # noqa: E501

        :return: The remote_address of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._remote_address

    @remote_address.setter
    def remote_address(self, remote_address):
        """Sets the remote_address of this DatasetFilterMetricValuesCreateParams.

        Client IPv4 or IPv6 address, address range, or subnet.  # noqa: E501

        :param remote_address: The remote_address of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: str
        """
        if remote_address is not None and len(remote_address) > 91:
            raise ValueError("Invalid value for `remote_address`, length must be less than or equal to `91`")  # noqa: E501
        if remote_address is not None and len(remote_address) < 1:
            raise ValueError("Invalid value for `remote_address`, length must be greater than or equal to `1`")  # noqa: E501
        if remote_address is not None and not re.search('^[0-9a-fA-F:.\/-]*$', remote_address):  # noqa: E501
            raise ValueError("Invalid value for `remote_address`, must be a follow pattern or equal to `/^[0-9a-fA-F:.\/-]*$/`")  # noqa: E501

        self._remote_address = remote_address

    @property
    def share_name(self):
        """Gets the share_name of this DatasetFilterMetricValuesCreateParams.  # noqa: E501

        SMB share name  # noqa: E501

        :return: The share_name of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._share_name

    @share_name.setter
    def share_name(self, share_name):
        """Sets the share_name of this DatasetFilterMetricValuesCreateParams.

        SMB share name  # noqa: E501

        :param share_name: The share_name of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: str
        """
        if share_name is not None and len(share_name) > 320:
            raise ValueError("Invalid value for `share_name`, length must be less than or equal to `320`")  # noqa: E501
        if share_name is not None and len(share_name) < 1:
            raise ValueError("Invalid value for `share_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._share_name = share_name

    @property
    def username(self):
        """Gets the username of this DatasetFilterMetricValuesCreateParams.  # noqa: E501

        username  # noqa: E501

        :return: The username of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DatasetFilterMetricValuesCreateParams.

        username  # noqa: E501

        :param username: The username of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 255:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def zone_name(self):
        """Gets the zone_name of this DatasetFilterMetricValuesCreateParams.  # noqa: E501

        The zone name  # noqa: E501

        :return: The zone_name of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this DatasetFilterMetricValuesCreateParams.

        The zone name  # noqa: E501

        :param zone_name: The zone_name of this DatasetFilterMetricValuesCreateParams.  # noqa: E501
        :type: str
        """
        if zone_name is not None and len(zone_name) > 255:
            raise ValueError("Invalid value for `zone_name`, length must be less than or equal to `255`")  # noqa: E501
        if zone_name is not None and len(zone_name) < 1:
            raise ValueError("Invalid value for `zone_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._zone_name = zone_name

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
        if not isinstance(other, DatasetFilterMetricValuesCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
