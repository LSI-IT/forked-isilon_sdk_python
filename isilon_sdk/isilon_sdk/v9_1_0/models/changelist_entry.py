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

from isilon_sdk.v9_1_0.models.changelist_entry_atime import ChangelistEntryAtime  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.changelists_changelist_diff_regions_diff_region import ChangelistsChangelistDiffRegionsDiffRegion  # noqa: F401,E501


class ChangelistEntry(object):
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
        'atime': 'ChangelistEntryAtime',
        'btime': 'ChangelistEntryAtime',
        'change_types': 'list[str]',
        'ctime': 'ChangelistEntryAtime',
        'data_pool': 'int',
        'diff_regions': 'list[ChangelistsChangelistDiffRegionsDiffRegion]',
        'file_type': 'str',
        'gid': 'int',
        'id': 'str',
        'lin': 'int',
        'metadata_pool': 'int',
        'mtime': 'ChangelistEntryAtime',
        'num_diff_regions': 'int',
        'parent_lin': 'int',
        'path': 'str',
        'physical_size': 'int',
        'size': 'int',
        'uid': 'int',
        'user_flags': 'list[str]'
    }

    attribute_map = {
        'atime': 'atime',
        'btime': 'btime',
        'change_types': 'change_types',
        'ctime': 'ctime',
        'data_pool': 'data_pool',
        'diff_regions': 'diff_regions',
        'file_type': 'file_type',
        'gid': 'gid',
        'id': 'id',
        'lin': 'lin',
        'metadata_pool': 'metadata_pool',
        'mtime': 'mtime',
        'num_diff_regions': 'num_diff_regions',
        'parent_lin': 'parent_lin',
        'path': 'path',
        'physical_size': 'physical_size',
        'size': 'size',
        'uid': 'uid',
        'user_flags': 'user_flags'
    }

    def __init__(self, atime=None, btime=None, change_types=None, ctime=None, data_pool=None, diff_regions=None, file_type=None, gid=None, id=None, lin=None, metadata_pool=None, mtime=None, num_diff_regions=None, parent_lin=None, path=None, physical_size=None, size=None, uid=None, user_flags=None):  # noqa: E501
        """ChangelistEntry - a model defined in Swagger"""  # noqa: E501

        self._atime = None
        self._btime = None
        self._change_types = None
        self._ctime = None
        self._data_pool = None
        self._diff_regions = None
        self._file_type = None
        self._gid = None
        self._id = None
        self._lin = None
        self._metadata_pool = None
        self._mtime = None
        self._num_diff_regions = None
        self._parent_lin = None
        self._path = None
        self._physical_size = None
        self._size = None
        self._uid = None
        self._user_flags = None
        self.discriminator = None

        if atime is not None:
            self.atime = atime
        if btime is not None:
            self.btime = btime
        if change_types is not None:
            self.change_types = change_types
        if ctime is not None:
            self.ctime = ctime
        self.data_pool = data_pool
        if diff_regions is not None:
            self.diff_regions = diff_regions
        self.file_type = file_type
        self.gid = gid
        self.id = id
        self.lin = lin
        self.metadata_pool = metadata_pool
        if mtime is not None:
            self.mtime = mtime
        if num_diff_regions is not None:
            self.num_diff_regions = num_diff_regions
        self.parent_lin = parent_lin
        self.path = path
        self.physical_size = physical_size
        self.size = size
        self.uid = uid
        if user_flags is not None:
            self.user_flags = user_flags

    @property
    def atime(self):
        """Gets the atime of this ChangelistEntry.  # noqa: E501

          # noqa: E501

        :return: The atime of this ChangelistEntry.  # noqa: E501
        :rtype: ChangelistEntryAtime
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """Sets the atime of this ChangelistEntry.

          # noqa: E501

        :param atime: The atime of this ChangelistEntry.  # noqa: E501
        :type: ChangelistEntryAtime
        """

        self._atime = atime

    @property
    def btime(self):
        """Gets the btime of this ChangelistEntry.  # noqa: E501

          # noqa: E501

        :return: The btime of this ChangelistEntry.  # noqa: E501
        :rtype: ChangelistEntryAtime
        """
        return self._btime

    @btime.setter
    def btime(self, btime):
        """Sets the btime of this ChangelistEntry.

          # noqa: E501

        :param btime: The btime of this ChangelistEntry.  # noqa: E501
        :type: ChangelistEntryAtime
        """

        self._btime = btime

    @property
    def change_types(self):
        """Gets the change_types of this ChangelistEntry.  # noqa: E501

        The types of change for this entry.  # noqa: E501

        :return: The change_types of this ChangelistEntry.  # noqa: E501
        :rtype: list[str]
        """
        return self._change_types

    @change_types.setter
    def change_types(self, change_types):
        """Sets the change_types of this ChangelistEntry.

        The types of change for this entry.  # noqa: E501

        :param change_types: The change_types of this ChangelistEntry.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ENTRY_MODIFIED", "ENTRY_ADDED", "ENTRY_REMOVED", "ENTRY_PATH_CHANGED", "ENTRY_HAS_ADS", "ENTRY_ADS", "ENTRY_HAS_HARDLINKS", "ENTRY_PARENT_REMOVED", "ENTRY_PATH_LOOKUP_REQ", "ENTRY_WORM_COMMITTED"]  # noqa: E501
        if not set(change_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `change_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(change_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._change_types = change_types

    @property
    def ctime(self):
        """Gets the ctime of this ChangelistEntry.  # noqa: E501

          # noqa: E501

        :return: The ctime of this ChangelistEntry.  # noqa: E501
        :rtype: ChangelistEntryAtime
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this ChangelistEntry.

          # noqa: E501

        :param ctime: The ctime of this ChangelistEntry.  # noqa: E501
        :type: ChangelistEntryAtime
        """

        self._ctime = ctime

    @property
    def data_pool(self):
        """Gets the data_pool of this ChangelistEntry.  # noqa: E501

        The data disk pool ID of the file associated with the entry.  # noqa: E501

        :return: The data_pool of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._data_pool

    @data_pool.setter
    def data_pool(self, data_pool):
        """Sets the data_pool of this ChangelistEntry.

        The data disk pool ID of the file associated with the entry.  # noqa: E501

        :param data_pool: The data_pool of this ChangelistEntry.  # noqa: E501
        :type: int
        """
        if data_pool is None:
            raise ValueError("Invalid value for `data_pool`, must not be `None`")  # noqa: E501
        if data_pool is not None and data_pool > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `data_pool`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if data_pool is not None and data_pool < 0:  # noqa: E501
            raise ValueError("Invalid value for `data_pool`, must be a value greater than or equal to `0`")  # noqa: E501

        self._data_pool = data_pool

    @property
    def diff_regions(self):
        """Gets the diff_regions of this ChangelistEntry.  # noqa: E501

        Changed regions of the file  # noqa: E501

        :return: The diff_regions of this ChangelistEntry.  # noqa: E501
        :rtype: list[ChangelistsChangelistDiffRegionsDiffRegion]
        """
        return self._diff_regions

    @diff_regions.setter
    def diff_regions(self, diff_regions):
        """Sets the diff_regions of this ChangelistEntry.

        Changed regions of the file  # noqa: E501

        :param diff_regions: The diff_regions of this ChangelistEntry.  # noqa: E501
        :type: list[ChangelistsChangelistDiffRegionsDiffRegion]
        """

        self._diff_regions = diff_regions

    @property
    def file_type(self):
        """Gets the file_type of this ChangelistEntry.  # noqa: E501

        Type of file.  # noqa: E501

        :return: The file_type of this ChangelistEntry.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ChangelistEntry.

        Type of file.  # noqa: E501

        :param file_type: The file_type of this ChangelistEntry.  # noqa: E501
        :type: str
        """
        if file_type is None:
            raise ValueError("Invalid value for `file_type`, must not be `None`")  # noqa: E501
        allowed_values = ["(REMOVED)", "regular", "directory", "symlink", "fifo", "socket", "char device", "block device", "unknown"]  # noqa: E501
        if file_type not in allowed_values:
            raise ValueError(
                "Invalid value for `file_type` ({0}), must be one of {1}"  # noqa: E501
                .format(file_type, allowed_values)
            )

        self._file_type = file_type

    @property
    def gid(self):
        """Gets the gid of this ChangelistEntry.  # noqa: E501

        The Group ID defined flags of the file associated with the entry.  # noqa: E501

        :return: The gid of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this ChangelistEntry.

        The Group ID defined flags of the file associated with the entry.  # noqa: E501

        :param gid: The gid of this ChangelistEntry.  # noqa: E501
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
    def id(self):
        """Gets the id of this ChangelistEntry.  # noqa: E501

        The ID of the changelist entry.  # noqa: E501

        :return: The id of this ChangelistEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangelistEntry.

        The ID of the changelist entry.  # noqa: E501

        :param id: The id of this ChangelistEntry.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 20:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `20`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def lin(self):
        """Gets the lin of this ChangelistEntry.  # noqa: E501

        The LIN number of the file associated with the entry.  # noqa: E501

        :return: The lin of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._lin

    @lin.setter
    def lin(self, lin):
        """Sets the lin of this ChangelistEntry.

        The LIN number of the file associated with the entry.  # noqa: E501

        :param lin: The lin of this ChangelistEntry.  # noqa: E501
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
    def metadata_pool(self):
        """Gets the metadata_pool of this ChangelistEntry.  # noqa: E501

        The metadata disk pool ID of the file associated with the entry.  # noqa: E501

        :return: The metadata_pool of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._metadata_pool

    @metadata_pool.setter
    def metadata_pool(self, metadata_pool):
        """Sets the metadata_pool of this ChangelistEntry.

        The metadata disk pool ID of the file associated with the entry.  # noqa: E501

        :param metadata_pool: The metadata_pool of this ChangelistEntry.  # noqa: E501
        :type: int
        """
        if metadata_pool is None:
            raise ValueError("Invalid value for `metadata_pool`, must not be `None`")  # noqa: E501
        if metadata_pool is not None and metadata_pool > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `metadata_pool`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if metadata_pool is not None and metadata_pool < 0:  # noqa: E501
            raise ValueError("Invalid value for `metadata_pool`, must be a value greater than or equal to `0`")  # noqa: E501

        self._metadata_pool = metadata_pool

    @property
    def mtime(self):
        """Gets the mtime of this ChangelistEntry.  # noqa: E501

          # noqa: E501

        :return: The mtime of this ChangelistEntry.  # noqa: E501
        :rtype: ChangelistEntryAtime
        """
        return self._mtime

    @mtime.setter
    def mtime(self, mtime):
        """Sets the mtime of this ChangelistEntry.

          # noqa: E501

        :param mtime: The mtime of this ChangelistEntry.  # noqa: E501
        :type: ChangelistEntryAtime
        """

        self._mtime = mtime

    @property
    def num_diff_regions(self):
        """Gets the num_diff_regions of this ChangelistEntry.  # noqa: E501

        Number of changed regions stored in the diff_regions array. A value of 4294967295 indicates that diff_regions contains a truncated list of changed regions, and a full list must be obtained from another handler.  # noqa: E501

        :return: The num_diff_regions of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._num_diff_regions

    @num_diff_regions.setter
    def num_diff_regions(self, num_diff_regions):
        """Sets the num_diff_regions of this ChangelistEntry.

        Number of changed regions stored in the diff_regions array. A value of 4294967295 indicates that diff_regions contains a truncated list of changed regions, and a full list must be obtained from another handler.  # noqa: E501

        :param num_diff_regions: The num_diff_regions of this ChangelistEntry.  # noqa: E501
        :type: int
        """
        if num_diff_regions is not None and num_diff_regions > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `num_diff_regions`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if num_diff_regions is not None and num_diff_regions < 1:  # noqa: E501
            raise ValueError("Invalid value for `num_diff_regions`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_diff_regions = num_diff_regions

    @property
    def parent_lin(self):
        """Gets the parent_lin of this ChangelistEntry.  # noqa: E501

        The Parent LIN number of the file associated with the entry.  # noqa: E501

        :return: The parent_lin of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._parent_lin

    @parent_lin.setter
    def parent_lin(self, parent_lin):
        """Sets the parent_lin of this ChangelistEntry.

        The Parent LIN number of the file associated with the entry.  # noqa: E501

        :param parent_lin: The parent_lin of this ChangelistEntry.  # noqa: E501
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
        """Gets the path of this ChangelistEntry.  # noqa: E501

        The relative path to the file associated with the entry.  # noqa: E501

        :return: The path of this ChangelistEntry.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ChangelistEntry.

        The relative path to the file associated with the entry.  # noqa: E501

        :param path: The path of this ChangelistEntry.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if path is not None and len(path) > 4096:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if path is not None and len(path) < 0:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `0`")  # noqa: E501

        self._path = path

    @property
    def physical_size(self):
        """Gets the physical_size of this ChangelistEntry.  # noqa: E501

        The physical size of the file associated with the entry.  # noqa: E501

        :return: The physical_size of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._physical_size

    @physical_size.setter
    def physical_size(self, physical_size):
        """Sets the physical_size of this ChangelistEntry.

        The physical size of the file associated with the entry.  # noqa: E501

        :param physical_size: The physical_size of this ChangelistEntry.  # noqa: E501
        :type: int
        """
        if physical_size is None:
            raise ValueError("Invalid value for `physical_size`, must not be `None`")  # noqa: E501
        if physical_size is not None and physical_size > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `physical_size`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if physical_size is not None and physical_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `physical_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._physical_size = physical_size

    @property
    def size(self):
        """Gets the size of this ChangelistEntry.  # noqa: E501

        The size of the file associated with the entry.  # noqa: E501

        :return: The size of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ChangelistEntry.

        The size of the file associated with the entry.  # noqa: E501

        :param size: The size of this ChangelistEntry.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        if size is not None and size > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if size is not None and size < 0:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def uid(self):
        """Gets the uid of this ChangelistEntry.  # noqa: E501

        The User ID flags of the file associated with the entry.  # noqa: E501

        :return: The uid of this ChangelistEntry.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ChangelistEntry.

        The User ID flags of the file associated with the entry.  # noqa: E501

        :param uid: The uid of this ChangelistEntry.  # noqa: E501
        :type: int
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501
        if uid is not None and uid > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if uid is not None and uid < 0:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uid = uid

    @property
    def user_flags(self):
        """Gets the user_flags of this ChangelistEntry.  # noqa: E501

        The user defined flags of the file associated with the entry.  # noqa: E501

        :return: The user_flags of this ChangelistEntry.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_flags

    @user_flags.setter
    def user_flags(self, user_flags):
        """Sets the user_flags of this ChangelistEntry.

        The user defined flags of the file associated with the entry.  # noqa: E501

        :param user_flags: The user_flags of this ChangelistEntry.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["sappnd", "arch", "schg", "sunlnk", "snapshot", "uappnd", "uarch", "hidden", "uchg", "nodump", "uunlnk", "offline", "opaque", "rdonly", "reparse", "sparse", "system", "inherit", "writecache", "wcinherit", "noindex", "ssmartlinked", "noscow", "scachedsmartlink", "shasntfsacl", "shasntfsog", "sparentsupgraded", "sbackupsparse", "ads", "hasads", "wcendurant"]  # noqa: E501
        if not set(user_flags).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `user_flags` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(user_flags) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._user_flags = user_flags

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
        if not isinstance(other, ChangelistEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
