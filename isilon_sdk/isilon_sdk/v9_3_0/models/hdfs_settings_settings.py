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


class HdfsSettingsSettings(object):
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
        'ambari_metrics_collector': 'str',
        'ambari_namenode': 'str',
        'ambari_server': 'str',
        'authentication_mode': 'str',
        'data_transfer_cipher': 'str',
        'default_block_size': 'int',
        'default_checksum_type': 'str',
        'hadoop_version_3_or_later': 'bool',
        'hdfs_acl_enabled': 'bool',
        'odp_version': 'str',
        'root_directory': 'str',
        'service': 'bool',
        'webhdfs_enabled': 'bool'
    }

    attribute_map = {
        'ambari_metrics_collector': 'ambari_metrics_collector',
        'ambari_namenode': 'ambari_namenode',
        'ambari_server': 'ambari_server',
        'authentication_mode': 'authentication_mode',
        'data_transfer_cipher': 'data_transfer_cipher',
        'default_block_size': 'default_block_size',
        'default_checksum_type': 'default_checksum_type',
        'hadoop_version_3_or_later': 'hadoop_version_3_or_later',
        'hdfs_acl_enabled': 'hdfs_acl_enabled',
        'odp_version': 'odp_version',
        'root_directory': 'root_directory',
        'service': 'service',
        'webhdfs_enabled': 'webhdfs_enabled'
    }

    def __init__(self, ambari_metrics_collector=None, ambari_namenode=None, ambari_server=None, authentication_mode=None, data_transfer_cipher=None, default_block_size=None, default_checksum_type=None, hadoop_version_3_or_later=None, hdfs_acl_enabled=None, odp_version=None, root_directory=None, service=None, webhdfs_enabled=None):  # noqa: E501
        """HdfsSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._ambari_metrics_collector = None
        self._ambari_namenode = None
        self._ambari_server = None
        self._authentication_mode = None
        self._data_transfer_cipher = None
        self._default_block_size = None
        self._default_checksum_type = None
        self._hadoop_version_3_or_later = None
        self._hdfs_acl_enabled = None
        self._odp_version = None
        self._root_directory = None
        self._service = None
        self._webhdfs_enabled = None
        self.discriminator = None

        if ambari_metrics_collector is not None:
            self.ambari_metrics_collector = ambari_metrics_collector
        if ambari_namenode is not None:
            self.ambari_namenode = ambari_namenode
        if ambari_server is not None:
            self.ambari_server = ambari_server
        if authentication_mode is not None:
            self.authentication_mode = authentication_mode
        if data_transfer_cipher is not None:
            self.data_transfer_cipher = data_transfer_cipher
        if default_block_size is not None:
            self.default_block_size = default_block_size
        if default_checksum_type is not None:
            self.default_checksum_type = default_checksum_type
        if hadoop_version_3_or_later is not None:
            self.hadoop_version_3_or_later = hadoop_version_3_or_later
        if hdfs_acl_enabled is not None:
            self.hdfs_acl_enabled = hdfs_acl_enabled
        if odp_version is not None:
            self.odp_version = odp_version
        if root_directory is not None:
            self.root_directory = root_directory
        if service is not None:
            self.service = service
        if webhdfs_enabled is not None:
            self.webhdfs_enabled = webhdfs_enabled

    @property
    def ambari_metrics_collector(self):
        """Gets the ambari_metrics_collector of this HdfsSettingsSettings.  # noqa: E501

        Ambari metrics collector.  # noqa: E501

        :return: The ambari_metrics_collector of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ambari_metrics_collector

    @ambari_metrics_collector.setter
    def ambari_metrics_collector(self, ambari_metrics_collector):
        """Sets the ambari_metrics_collector of this HdfsSettingsSettings.

        Ambari metrics collector.  # noqa: E501

        :param ambari_metrics_collector: The ambari_metrics_collector of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        if ambari_metrics_collector is not None and len(ambari_metrics_collector) > 2048:
            raise ValueError("Invalid value for `ambari_metrics_collector`, length must be less than or equal to `2048`")  # noqa: E501
        if ambari_metrics_collector is not None and len(ambari_metrics_collector) < 0:
            raise ValueError("Invalid value for `ambari_metrics_collector`, length must be greater than or equal to `0`")  # noqa: E501

        self._ambari_metrics_collector = ambari_metrics_collector

    @property
    def ambari_namenode(self):
        """Gets the ambari_namenode of this HdfsSettingsSettings.  # noqa: E501

        NameNode of Ambari server.  # noqa: E501

        :return: The ambari_namenode of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ambari_namenode

    @ambari_namenode.setter
    def ambari_namenode(self, ambari_namenode):
        """Sets the ambari_namenode of this HdfsSettingsSettings.

        NameNode of Ambari server.  # noqa: E501

        :param ambari_namenode: The ambari_namenode of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        if ambari_namenode is not None and len(ambari_namenode) > 2048:
            raise ValueError("Invalid value for `ambari_namenode`, length must be less than or equal to `2048`")  # noqa: E501
        if ambari_namenode is not None and len(ambari_namenode) < 0:
            raise ValueError("Invalid value for `ambari_namenode`, length must be greater than or equal to `0`")  # noqa: E501

        self._ambari_namenode = ambari_namenode

    @property
    def ambari_server(self):
        """Gets the ambari_server of this HdfsSettingsSettings.  # noqa: E501

        Ambari server  # noqa: E501

        :return: The ambari_server of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ambari_server

    @ambari_server.setter
    def ambari_server(self, ambari_server):
        """Sets the ambari_server of this HdfsSettingsSettings.

        Ambari server  # noqa: E501

        :param ambari_server: The ambari_server of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        if ambari_server is not None and len(ambari_server) > 2048:
            raise ValueError("Invalid value for `ambari_server`, length must be less than or equal to `2048`")  # noqa: E501
        if ambari_server is not None and len(ambari_server) < 0:
            raise ValueError("Invalid value for `ambari_server`, length must be greater than or equal to `0`")  # noqa: E501

        self._ambari_server = ambari_server

    @property
    def authentication_mode(self):
        """Gets the authentication_mode of this HdfsSettingsSettings.  # noqa: E501

        Type of authentication for HDFS protocol.  # noqa: E501

        :return: The authentication_mode of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._authentication_mode

    @authentication_mode.setter
    def authentication_mode(self, authentication_mode):
        """Sets the authentication_mode of this HdfsSettingsSettings.

        Type of authentication for HDFS protocol.  # noqa: E501

        :param authentication_mode: The authentication_mode of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["simple_only", "kerberos_only"]  # noqa: E501
        if authentication_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_mode, allowed_values)
            )

        self._authentication_mode = authentication_mode

    @property
    def data_transfer_cipher(self):
        """Gets the data_transfer_cipher of this HdfsSettingsSettings.  # noqa: E501

        Encryption algorithm to use for data transfer (if any).  # noqa: E501

        :return: The data_transfer_cipher of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._data_transfer_cipher

    @data_transfer_cipher.setter
    def data_transfer_cipher(self, data_transfer_cipher):
        """Sets the data_transfer_cipher of this HdfsSettingsSettings.

        Encryption algorithm to use for data transfer (if any).  # noqa: E501

        :param data_transfer_cipher: The data_transfer_cipher of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "aes_128_ctr", "aes_192_ctr", "aes_256_ctr"]  # noqa: E501
        if data_transfer_cipher not in allowed_values:
            raise ValueError(
                "Invalid value for `data_transfer_cipher` ({0}), must be one of {1}"  # noqa: E501
                .format(data_transfer_cipher, allowed_values)
            )

        self._data_transfer_cipher = data_transfer_cipher

    @property
    def default_block_size(self):
        """Gets the default_block_size of this HdfsSettingsSettings.  # noqa: E501

        Block size (size=2**value) reported by HDFS server.  # noqa: E501

        :return: The default_block_size of this HdfsSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._default_block_size

    @default_block_size.setter
    def default_block_size(self, default_block_size):
        """Sets the default_block_size of this HdfsSettingsSettings.

        Block size (size=2**value) reported by HDFS server.  # noqa: E501

        :param default_block_size: The default_block_size of this HdfsSettingsSettings.  # noqa: E501
        :type: int
        """
        if default_block_size is not None and default_block_size > 65535:  # noqa: E501
            raise ValueError("Invalid value for `default_block_size`, must be a value less than or equal to `65535`")  # noqa: E501
        if default_block_size is not None and default_block_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `default_block_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._default_block_size = default_block_size

    @property
    def default_checksum_type(self):
        """Gets the default_checksum_type of this HdfsSettingsSettings.  # noqa: E501

        Checksum type reported by HDFS server.  # noqa: E501

        :return: The default_checksum_type of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_checksum_type

    @default_checksum_type.setter
    def default_checksum_type(self, default_checksum_type):
        """Sets the default_checksum_type of this HdfsSettingsSettings.

        Checksum type reported by HDFS server.  # noqa: E501

        :param default_checksum_type: The default_checksum_type of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "crc32", "crc32c"]  # noqa: E501
        if default_checksum_type not in allowed_values:
            raise ValueError(
                "Invalid value for `default_checksum_type` ({0}), must be one of {1}"  # noqa: E501
                .format(default_checksum_type, allowed_values)
            )

        self._default_checksum_type = default_checksum_type

    @property
    def hadoop_version_3_or_later(self):
        """Gets the hadoop_version_3_or_later of this HdfsSettingsSettings.  # noqa: E501

        Hadoop client version is 3 or later.  # noqa: E501

        :return: The hadoop_version_3_or_later of this HdfsSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._hadoop_version_3_or_later

    @hadoop_version_3_or_later.setter
    def hadoop_version_3_or_later(self, hadoop_version_3_or_later):
        """Sets the hadoop_version_3_or_later of this HdfsSettingsSettings.

        Hadoop client version is 3 or later.  # noqa: E501

        :param hadoop_version_3_or_later: The hadoop_version_3_or_later of this HdfsSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._hadoop_version_3_or_later = hadoop_version_3_or_later

    @property
    def hdfs_acl_enabled(self):
        """Gets the hdfs_acl_enabled of this HdfsSettingsSettings.  # noqa: E501

        Enable HDFS ACL on the zone  # noqa: E501

        :return: The hdfs_acl_enabled of this HdfsSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._hdfs_acl_enabled

    @hdfs_acl_enabled.setter
    def hdfs_acl_enabled(self, hdfs_acl_enabled):
        """Sets the hdfs_acl_enabled of this HdfsSettingsSettings.

        Enable HDFS ACL on the zone  # noqa: E501

        :param hdfs_acl_enabled: The hdfs_acl_enabled of this HdfsSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._hdfs_acl_enabled = hdfs_acl_enabled

    @property
    def odp_version(self):
        """Gets the odp_version of this HdfsSettingsSettings.  # noqa: E501

        ODP stack repository version number.  # noqa: E501

        :return: The odp_version of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._odp_version

    @odp_version.setter
    def odp_version(self, odp_version):
        """Sets the odp_version of this HdfsSettingsSettings.

        ODP stack repository version number.  # noqa: E501

        :param odp_version: The odp_version of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        if odp_version is not None and len(odp_version) > 255:
            raise ValueError("Invalid value for `odp_version`, length must be less than or equal to `255`")  # noqa: E501
        if odp_version is not None and len(odp_version) < 0:
            raise ValueError("Invalid value for `odp_version`, length must be greater than or equal to `0`")  # noqa: E501

        self._odp_version = odp_version

    @property
    def root_directory(self):
        """Gets the root_directory of this HdfsSettingsSettings.  # noqa: E501


        :return: The root_directory of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._root_directory

    @root_directory.setter
    def root_directory(self, root_directory):
        """Sets the root_directory of this HdfsSettingsSettings.


        :param root_directory: The root_directory of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        if root_directory is not None and len(root_directory) > 4096:
            raise ValueError("Invalid value for `root_directory`, length must be less than or equal to `4096`")  # noqa: E501
        if root_directory is not None and len(root_directory) < 4:
            raise ValueError("Invalid value for `root_directory`, length must be greater than or equal to `4`")  # noqa: E501
        if root_directory is not None and not re.search('^\/ifs$|^\/ifs\/', root_directory):  # noqa: E501
            raise ValueError("Invalid value for `root_directory`, must be a follow pattern or equal to `/^\/ifs$|^\/ifs\//`")  # noqa: E501

        self._root_directory = root_directory

    @property
    def service(self):
        """Gets the service of this HdfsSettingsSettings.  # noqa: E501

        Enable or disable the HDFS service.  # noqa: E501

        :return: The service of this HdfsSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this HdfsSettingsSettings.

        Enable or disable the HDFS service.  # noqa: E501

        :param service: The service of this HdfsSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._service = service

    @property
    def webhdfs_enabled(self):
        """Gets the webhdfs_enabled of this HdfsSettingsSettings.  # noqa: E501

        Enable or disable WebHDFS.  # noqa: E501

        :return: The webhdfs_enabled of this HdfsSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._webhdfs_enabled

    @webhdfs_enabled.setter
    def webhdfs_enabled(self, webhdfs_enabled):
        """Sets the webhdfs_enabled of this HdfsSettingsSettings.

        Enable or disable WebHDFS.  # noqa: E501

        :param webhdfs_enabled: The webhdfs_enabled of this HdfsSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._webhdfs_enabled = webhdfs_enabled

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
        if not isinstance(other, HdfsSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
