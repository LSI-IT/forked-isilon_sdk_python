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


class NameLin(object):
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
        'atime': 'int',
        'btime': 'int',
        'ctime': 'int',
        'flags': 'int',
        'gid': 'int',
        'lin': 'int',
        'link_count': 'int',
        'logical_size': 'int',
        'max_snapid': 'int',
        'min_snapid': 'int',
        'mode': 'int',
        'mtime': 'int',
        'name': 'str',
        'parent_lin': 'int',
        'path': 'str',
        'physical_size': 'int',
        'uid': 'int'
    }

    attribute_map = {
        'atime': 'atime',
        'btime': 'btime',
        'ctime': 'ctime',
        'flags': 'flags',
        'gid': 'gid',
        'lin': 'lin',
        'link_count': 'link_count',
        'logical_size': 'logical_size',
        'max_snapid': 'max_snapid',
        'min_snapid': 'min_snapid',
        'mode': 'mode',
        'mtime': 'mtime',
        'name': 'name',
        'parent_lin': 'parent_lin',
        'path': 'path',
        'physical_size': 'physical_size',
        'uid': 'uid'
    }

    def __init__(self, atime=None, btime=None, ctime=None, flags=None, gid=None, lin=None, link_count=None, logical_size=None, max_snapid=None, min_snapid=None, mode=None, mtime=None, name=None, parent_lin=None, path=None, physical_size=None, uid=None):  # noqa: E501
        """NameLin - a model defined in Swagger"""  # noqa: E501

        self._atime = None
        self._btime = None
        self._ctime = None
        self._flags = None
        self._gid = None
        self._lin = None
        self._link_count = None
        self._logical_size = None
        self._max_snapid = None
        self._min_snapid = None
        self._mode = None
        self._mtime = None
        self._name = None
        self._parent_lin = None
        self._path = None
        self._physical_size = None
        self._uid = None
        self.discriminator = None

        self.atime = atime
        self.btime = btime
        self.ctime = ctime
        self.flags = flags
        self.gid = gid
        self.lin = lin
        self.link_count = link_count
        self.logical_size = logical_size
        self.max_snapid = max_snapid
        self.min_snapid = min_snapid
        self.mode = mode
        self.mtime = mtime
        self.name = name
        self.parent_lin = parent_lin
        if path is not None:
            self.path = path
        self.physical_size = physical_size
        self.uid = uid

    @property
    def atime(self):
        """Gets the atime of this NameLin.  # noqa: E501

        The Unix epoch time of the file access.  # noqa: E501

        :return: The atime of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """Sets the atime of this NameLin.

        The Unix epoch time of the file access.  # noqa: E501

        :param atime: The atime of this NameLin.  # noqa: E501
        :type: int
        """
        if atime is None:
            raise ValueError("Invalid value for `atime`, must not be `None`")  # noqa: E501
        if atime is not None and atime > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `atime`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if atime is not None and atime < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `atime`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._atime = atime

    @property
    def btime(self):
        """Gets the btime of this NameLin.  # noqa: E501

        The Unix epoch time of the file birth.  # noqa: E501

        :return: The btime of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._btime

    @btime.setter
    def btime(self, btime):
        """Sets the btime of this NameLin.

        The Unix epoch time of the file birth.  # noqa: E501

        :param btime: The btime of this NameLin.  # noqa: E501
        :type: int
        """
        if btime is None:
            raise ValueError("Invalid value for `btime`, must not be `None`")  # noqa: E501
        if btime is not None and btime > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `btime`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if btime is not None and btime < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `btime`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._btime = btime

    @property
    def ctime(self):
        """Gets the ctime of this NameLin.  # noqa: E501

        The Unix epoch time of the file creation.  # noqa: E501

        :return: The ctime of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this NameLin.

        The Unix epoch time of the file creation.  # noqa: E501

        :param ctime: The ctime of this NameLin.  # noqa: E501
        :type: int
        """
        if ctime is None:
            raise ValueError("Invalid value for `ctime`, must not be `None`")  # noqa: E501
        if ctime is not None and ctime > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `ctime`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if ctime is not None and ctime < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `ctime`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._ctime = ctime

    @property
    def flags(self):
        """Gets the flags of this NameLin.  # noqa: E501

        Bitmap of flags representing file or directory attributes.  # noqa: E501

        :return: The flags of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this NameLin.

        Bitmap of flags representing file or directory attributes.  # noqa: E501

        :param flags: The flags of this NameLin.  # noqa: E501
        :type: int
        """
        if flags is None:
            raise ValueError("Invalid value for `flags`, must not be `None`")  # noqa: E501
        if flags is not None and flags > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `flags`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if flags is not None and flags < 1:  # noqa: E501
            raise ValueError("Invalid value for `flags`, must be a value greater than or equal to `1`")  # noqa: E501

        self._flags = flags

    @property
    def gid(self):
        """Gets the gid of this NameLin.  # noqa: E501

        Group ID of the file.  # noqa: E501

        :return: The gid of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this NameLin.

        Group ID of the file.  # noqa: E501

        :param gid: The gid of this NameLin.  # noqa: E501
        :type: int
        """
        if gid is None:
            raise ValueError("Invalid value for `gid`, must not be `None`")  # noqa: E501
        if gid is not None and gid > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if gid is not None and gid < 0:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gid = gid

    @property
    def lin(self):
        """Gets the lin of this NameLin.  # noqa: E501

        Logical Inode Number of file or directory.  # noqa: E501

        :return: The lin of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._lin

    @lin.setter
    def lin(self, lin):
        """Sets the lin of this NameLin.

        Logical Inode Number of file or directory.  # noqa: E501

        :param lin: The lin of this NameLin.  # noqa: E501
        :type: int
        """
        if lin is None:
            raise ValueError("Invalid value for `lin`, must not be `None`")  # noqa: E501
        if lin is not None and lin > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `lin`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if lin is not None and lin < 0:  # noqa: E501
            raise ValueError("Invalid value for `lin`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lin = lin

    @property
    def link_count(self):
        """Gets the link_count of this NameLin.  # noqa: E501

        Link count of file.  # noqa: E501

        :return: The link_count of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._link_count

    @link_count.setter
    def link_count(self, link_count):
        """Sets the link_count of this NameLin.

        Link count of file.  # noqa: E501

        :param link_count: The link_count of this NameLin.  # noqa: E501
        :type: int
        """
        if link_count is None:
            raise ValueError("Invalid value for `link_count`, must not be `None`")  # noqa: E501
        if link_count is not None and link_count > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `link_count`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if link_count is not None and link_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `link_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._link_count = link_count

    @property
    def logical_size(self):
        """Gets the logical_size of this NameLin.  # noqa: E501

        Logical file size in bytes.  # noqa: E501

        :return: The logical_size of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._logical_size

    @logical_size.setter
    def logical_size(self, logical_size):
        """Sets the logical_size of this NameLin.

        Logical file size in bytes.  # noqa: E501

        :param logical_size: The logical_size of this NameLin.  # noqa: E501
        :type: int
        """
        if logical_size is None:
            raise ValueError("Invalid value for `logical_size`, must not be `None`")  # noqa: E501
        if logical_size is not None and logical_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `logical_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if logical_size is not None and logical_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `logical_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._logical_size = logical_size

    @property
    def max_snapid(self):
        """Gets the max_snapid of this NameLin.  # noqa: E501

        Maximum Snapshot ID for file.  # noqa: E501

        :return: The max_snapid of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._max_snapid

    @max_snapid.setter
    def max_snapid(self, max_snapid):
        """Sets the max_snapid of this NameLin.

        Maximum Snapshot ID for file.  # noqa: E501

        :param max_snapid: The max_snapid of this NameLin.  # noqa: E501
        :type: int
        """
        if max_snapid is None:
            raise ValueError("Invalid value for `max_snapid`, must not be `None`")  # noqa: E501
        if max_snapid is not None and max_snapid > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `max_snapid`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if max_snapid is not None and max_snapid < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_snapid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_snapid = max_snapid

    @property
    def min_snapid(self):
        """Gets the min_snapid of this NameLin.  # noqa: E501

        Minimum Snapshot ID for file.  # noqa: E501

        :return: The min_snapid of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._min_snapid

    @min_snapid.setter
    def min_snapid(self, min_snapid):
        """Sets the min_snapid of this NameLin.

        Minimum Snapshot ID for file.  # noqa: E501

        :param min_snapid: The min_snapid of this NameLin.  # noqa: E501
        :type: int
        """
        if min_snapid is None:
            raise ValueError("Invalid value for `min_snapid`, must not be `None`")  # noqa: E501
        if min_snapid is not None and min_snapid > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `min_snapid`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if min_snapid is not None and min_snapid < 0:  # noqa: E501
            raise ValueError("Invalid value for `min_snapid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_snapid = min_snapid

    @property
    def mode(self):
        """Gets the mode of this NameLin.  # noqa: E501

        Mode bits (Unix file permissions) on the file.  # noqa: E501

        :return: The mode of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this NameLin.

        Mode bits (Unix file permissions) on the file.  # noqa: E501

        :param mode: The mode of this NameLin.  # noqa: E501
        :type: int
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501
        if mode is not None and mode > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `mode`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if mode is not None and mode < 0:  # noqa: E501
            raise ValueError("Invalid value for `mode`, must be a value greater than or equal to `0`")  # noqa: E501

        self._mode = mode

    @property
    def mtime(self):
        """Gets the mtime of this NameLin.  # noqa: E501

        The Unix epoch time of the file modification.  # noqa: E501

        :return: The mtime of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """Sets the mtime of this NameLin.

        The Unix epoch time of the file modification.  # noqa: E501

        :param mtime: The mtime of this NameLin.  # noqa: E501
        :type: int
        """
        if mtime is None:
            raise ValueError("Invalid value for `mtime`, must not be `None`")  # noqa: E501
        if mtime is not None and mtime > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `mtime`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if mtime is not None and mtime < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `mtime`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._mtime = mtime

    @property
    def name(self):
        """Gets the name of this NameLin.  # noqa: E501

        Name of file or directory.  # noqa: E501

        :return: The name of this NameLin.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NameLin.

        Name of file or directory.  # noqa: E501

        :param name: The name of this NameLin.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def parent_lin(self):
        """Gets the parent_lin of this NameLin.  # noqa: E501

        Parent Logical Inode Number of file or directory.  # noqa: E501

        :return: The parent_lin of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._parent_lin

    @parent_lin.setter
    def parent_lin(self, parent_lin):
        """Sets the parent_lin of this NameLin.

        Parent Logical Inode Number of file or directory.  # noqa: E501

        :param parent_lin: The parent_lin of this NameLin.  # noqa: E501
        :type: int
        """
        if parent_lin is None:
            raise ValueError("Invalid value for `parent_lin`, must not be `None`")  # noqa: E501
        if parent_lin is not None and parent_lin > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `parent_lin`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if parent_lin is not None and parent_lin < 0:  # noqa: E501
            raise ValueError("Invalid value for `parent_lin`, must be a value greater than or equal to `0`")  # noqa: E501

        self._parent_lin = parent_lin

    @property
    def path(self):
        """Gets the path of this NameLin.  # noqa: E501

        Path of file or directory.  # noqa: E501

        :return: The path of this NameLin.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NameLin.

        Path of file or directory.  # noqa: E501

        :param path: The path of this NameLin.  # noqa: E501
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
    def physical_size(self):
        """Gets the physical_size of this NameLin.  # noqa: E501

        Physical file size in bytes.  # noqa: E501

        :return: The physical_size of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._physical_size

    @physical_size.setter
    def physical_size(self, physical_size):
        """Sets the physical_size of this NameLin.

        Physical file size in bytes.  # noqa: E501

        :param physical_size: The physical_size of this NameLin.  # noqa: E501
        :type: int
        """
        if physical_size is None:
            raise ValueError("Invalid value for `physical_size`, must not be `None`")  # noqa: E501
        if physical_size is not None and physical_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `physical_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if physical_size is not None and physical_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `physical_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._physical_size = physical_size

    @property
    def uid(self):
        """Gets the uid of this NameLin.  # noqa: E501

        User ID of the file.  # noqa: E501

        :return: The uid of this NameLin.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this NameLin.

        User ID of the file.  # noqa: E501

        :param uid: The uid of this NameLin.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        if uid is not None and uid > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if uid is not None and uid < 0:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uid = uid

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
        if not isinstance(other, NameLin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
