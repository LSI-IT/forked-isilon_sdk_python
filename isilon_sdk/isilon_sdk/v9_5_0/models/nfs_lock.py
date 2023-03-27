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


class NfsLock(object):
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
        'client': 'str',
        'client_id': 'int',
        'created': 'int',
        'id': 'str',
        'lin': 'int',
        'lock_type': 'str',
        'path': 'str',
        'range': 'list[int]',
        'version': 'str'
    }

    attribute_map = {
        'client': 'client',
        'client_id': 'client_id',
        'created': 'created',
        'id': 'id',
        'lin': 'lin',
        'lock_type': 'lock_type',
        'path': 'path',
        'range': 'range',
        'version': 'version'
    }

    def __init__(self, client=None, client_id=None, created=None, id=None, lin=None, lock_type=None, path=None, range=None, version=None):  # noqa: E501
        """NfsLock - a model defined in Swagger"""  # noqa: E501

        self._client = None
        self._client_id = None
        self._created = None
        self._id = None
        self._lin = None
        self._lock_type = None
        self._path = None
        self._range = None
        self._version = None
        self.discriminator = None

        if client is not None:
            self.client = client
        if client_id is not None:
            self.client_id = client_id
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if lin is not None:
            self.lin = lin
        if lock_type is not None:
            self.lock_type = lock_type
        if path is not None:
            self.path = path
        if range is not None:
            self.range = range
        if version is not None:
            self.version = version

    @property
    def client(self):
        """Gets the client of this NfsLock.  # noqa: E501

        The client host name, FQDN, or IP.  # noqa: E501

        :return: The client of this NfsLock.  # noqa: E501
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this NfsLock.

        The client host name, FQDN, or IP.  # noqa: E501

        :param client: The client of this NfsLock.  # noqa: E501
        :type: str
        """
        if client is not None and len(client) > 255:
            raise ValueError("Invalid value for `client`, length must be less than or equal to `255`")  # noqa: E501
        if client is not None and len(client) < 1:
            raise ValueError("Invalid value for `client`, length must be greater than or equal to `1`")  # noqa: E501

        self._client = client

    @property
    def client_id(self):
        """Gets the client_id of this NfsLock.  # noqa: E501

        The client ID.  # noqa: E501

        :return: The client_id of this NfsLock.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this NfsLock.

        The client ID.  # noqa: E501

        :param client_id: The client_id of this NfsLock.  # noqa: E501
        :type: int
        """
        if client_id is not None and client_id > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if client_id is not None and client_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._client_id = client_id

    @property
    def created(self):
        """Gets the created of this NfsLock.  # noqa: E501

        Specifies the UNIX Epoch time that the lock was created.  # noqa: E501

        :return: The created of this NfsLock.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NfsLock.

        Specifies the UNIX Epoch time that the lock was created.  # noqa: E501

        :param created: The created of this NfsLock.  # noqa: E501
        :type: int
        """
        if created is not None and created > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `created`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if created is not None and created < 0:  # noqa: E501
            raise ValueError("Invalid value for `created`, must be a value greater than or equal to `0`")  # noqa: E501

        self._created = created

    @property
    def id(self):
        """Gets the id of this NfsLock.  # noqa: E501

        The lock ID.  # noqa: E501

        :return: The id of this NfsLock.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NfsLock.

        The lock ID.  # noqa: E501

        :param id: The id of this NfsLock.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 8192:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `8192`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lin(self):
        """Gets the lin of this NfsLock.  # noqa: E501

        The logical inode number (LIN) of the locked resource.  # noqa: E501

        :return: The lin of this NfsLock.  # noqa: E501
        :rtype: int
        """
        return self._lin

    @lin.setter
    def lin(self, lin):
        """Sets the lin of this NfsLock.

        The logical inode number (LIN) of the locked resource.  # noqa: E501

        :param lin: The lin of this NfsLock.  # noqa: E501
        :type: int
        """
        if lin is not None and lin > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `lin`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if lin is not None and lin < 0:  # noqa: E501
            raise ValueError("Invalid value for `lin`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lin = lin

    @property
    def lock_type(self):
        """Gets the lock_type of this NfsLock.  # noqa: E501

        The type of lock.  # noqa: E501

        :return: The lock_type of this NfsLock.  # noqa: E501
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        """Sets the lock_type of this NfsLock.

        The type of lock.  # noqa: E501

        :param lock_type: The lock_type of this NfsLock.  # noqa: E501
        :type: str
        """
        allowed_values = ["exclusive", "shared", "none"]  # noqa: E501
        if lock_type not in allowed_values:
            raise ValueError(
                "Invalid value for `lock_type` ({0}), must be one of {1}"  # noqa: E501
                .format(lock_type, allowed_values)
            )

        self._lock_type = lock_type

    @property
    def path(self):
        """Gets the path of this NfsLock.  # noqa: E501


        :return: The path of this NfsLock.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NfsLock.


        :param path: The path of this NfsLock.  # noqa: E501
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
    def range(self):
        """Gets the range of this NfsLock.  # noqa: E501

        The byte range within the file that is locked.  # noqa: E501

        :return: The range of this NfsLock.  # noqa: E501
        :rtype: list[int]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this NfsLock.

        The byte range within the file that is locked.  # noqa: E501

        :param range: The range of this NfsLock.  # noqa: E501
        :type: list[int]
        """

        self._range = range

    @property
    def version(self):
        """Gets the version of this NfsLock.  # noqa: E501

        NFS major version: v3 or v4  # noqa: E501

        :return: The version of this NfsLock.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NfsLock.

        NFS major version: v3 or v4  # noqa: E501

        :param version: The version of this NfsLock.  # noqa: E501
        :type: str
        """
        if version is not None and len(version) > 5:
            raise ValueError("Invalid value for `version`, length must be less than or equal to `5`")  # noqa: E501
        if version is not None and len(version) < 2:
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `2`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, NfsLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
