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


class ClusterStatfs(object):
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
        'f_bavail': 'int',
        'f_bfree': 'int',
        'f_blocks': 'int',
        'f_bsize': 'int',
        'f_ffree': 'int',
        'f_files': 'int',
        'f_flags': 'int',
        'f_fstypename': 'str',
        'f_iosize': 'int',
        'f_mntfromname': 'str',
        'f_mntonname': 'str',
        'f_namemax': 'int',
        'f_owner': 'int',
        'f_type': 'int',
        'f_version': 'int'
    }

    attribute_map = {
        'f_bavail': 'f_bavail',
        'f_bfree': 'f_bfree',
        'f_blocks': 'f_blocks',
        'f_bsize': 'f_bsize',
        'f_ffree': 'f_ffree',
        'f_files': 'f_files',
        'f_flags': 'f_flags',
        'f_fstypename': 'f_fstypename',
        'f_iosize': 'f_iosize',
        'f_mntfromname': 'f_mntfromname',
        'f_mntonname': 'f_mntonname',
        'f_namemax': 'f_namemax',
        'f_owner': 'f_owner',
        'f_type': 'f_type',
        'f_version': 'f_version'
    }

    def __init__(self, f_bavail=None, f_bfree=None, f_blocks=None, f_bsize=None, f_ffree=None, f_files=None, f_flags=None, f_fstypename=None, f_iosize=None, f_mntfromname=None, f_mntonname=None, f_namemax=None, f_owner=None, f_type=None, f_version=None):  # noqa: E501
        """ClusterStatfs - a model defined in Swagger"""  # noqa: E501

        self._f_bavail = None
        self._f_bfree = None
        self._f_blocks = None
        self._f_bsize = None
        self._f_ffree = None
        self._f_files = None
        self._f_flags = None
        self._f_fstypename = None
        self._f_iosize = None
        self._f_mntfromname = None
        self._f_mntonname = None
        self._f_namemax = None
        self._f_owner = None
        self._f_type = None
        self._f_version = None
        self.discriminator = None

        self.f_bavail = f_bavail
        self.f_bfree = f_bfree
        self.f_blocks = f_blocks
        self.f_bsize = f_bsize
        self.f_ffree = f_ffree
        self.f_files = f_files
        self.f_flags = f_flags
        self.f_fstypename = f_fstypename
        self.f_iosize = f_iosize
        self.f_mntfromname = f_mntfromname
        self.f_mntonname = f_mntonname
        self.f_namemax = f_namemax
        self.f_owner = f_owner
        self.f_type = f_type
        self.f_version = f_version

    @property
    def f_bavail(self):
        """Gets the f_bavail of this ClusterStatfs.  # noqa: E501

        The number of free blocks available to non-superuser.  # noqa: E501

        :return: The f_bavail of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_bavail

    @f_bavail.setter
    def f_bavail(self, f_bavail):
        """Sets the f_bavail of this ClusterStatfs.

        The number of free blocks available to non-superuser.  # noqa: E501

        :param f_bavail: The f_bavail of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_bavail is None:
            raise ValueError("Invalid value for `f_bavail`, must not be `None`")  # noqa: E501

        self._f_bavail = f_bavail

    @property
    def f_bfree(self):
        """Gets the f_bfree of this ClusterStatfs.  # noqa: E501

        The number of free blocks in the filesystem.  # noqa: E501

        :return: The f_bfree of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_bfree

    @f_bfree.setter
    def f_bfree(self, f_bfree):
        """Sets the f_bfree of this ClusterStatfs.

        The number of free blocks in the filesystem.  # noqa: E501

        :param f_bfree: The f_bfree of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_bfree is None:
            raise ValueError("Invalid value for `f_bfree`, must not be `None`")  # noqa: E501

        self._f_bfree = f_bfree

    @property
    def f_blocks(self):
        """Gets the f_blocks of this ClusterStatfs.  # noqa: E501

        The total number of data blocks in the filesystem.  # noqa: E501

        :return: The f_blocks of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_blocks

    @f_blocks.setter
    def f_blocks(self, f_blocks):
        """Sets the f_blocks of this ClusterStatfs.

        The total number of data blocks in the filesystem.  # noqa: E501

        :param f_blocks: The f_blocks of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_blocks is None:
            raise ValueError("Invalid value for `f_blocks`, must not be `None`")  # noqa: E501

        self._f_blocks = f_blocks

    @property
    def f_bsize(self):
        """Gets the f_bsize of this ClusterStatfs.  # noqa: E501

        The filesystem fragment size.  # noqa: E501

        :return: The f_bsize of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_bsize

    @f_bsize.setter
    def f_bsize(self, f_bsize):
        """Sets the f_bsize of this ClusterStatfs.

        The filesystem fragment size.  # noqa: E501

        :param f_bsize: The f_bsize of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_bsize is None:
            raise ValueError("Invalid value for `f_bsize`, must not be `None`")  # noqa: E501

        self._f_bsize = f_bsize

    @property
    def f_ffree(self):
        """Gets the f_ffree of this ClusterStatfs.  # noqa: E501

        The number of free nodes available to non-superuser.  # noqa: E501

        :return: The f_ffree of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_ffree

    @f_ffree.setter
    def f_ffree(self, f_ffree):
        """Sets the f_ffree of this ClusterStatfs.

        The number of free nodes available to non-superuser.  # noqa: E501

        :param f_ffree: The f_ffree of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_ffree is None:
            raise ValueError("Invalid value for `f_ffree`, must not be `None`")  # noqa: E501

        self._f_ffree = f_ffree

    @property
    def f_files(self):
        """Gets the f_files of this ClusterStatfs.  # noqa: E501

        The total number of file nodes in the filesystem.  # noqa: E501

        :return: The f_files of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_files

    @f_files.setter
    def f_files(self, f_files):
        """Sets the f_files of this ClusterStatfs.

        The total number of file nodes in the filesystem.  # noqa: E501

        :param f_files: The f_files of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_files is None:
            raise ValueError("Invalid value for `f_files`, must not be `None`")  # noqa: E501

        self._f_files = f_files

    @property
    def f_flags(self):
        """Gets the f_flags of this ClusterStatfs.  # noqa: E501

        A copy of the mount exported flags.  # noqa: E501

        :return: The f_flags of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_flags

    @f_flags.setter
    def f_flags(self, f_flags):
        """Sets the f_flags of this ClusterStatfs.

        A copy of the mount exported flags.  # noqa: E501

        :param f_flags: The f_flags of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_flags is None:
            raise ValueError("Invalid value for `f_flags`, must not be `None`")  # noqa: E501

        self._f_flags = f_flags

    @property
    def f_fstypename(self):
        """Gets the f_fstypename of this ClusterStatfs.  # noqa: E501

        The filesystem type name.  # noqa: E501

        :return: The f_fstypename of this ClusterStatfs.  # noqa: E501
        :rtype: str
        """
        return self._f_fstypename

    @f_fstypename.setter
    def f_fstypename(self, f_fstypename):
        """Sets the f_fstypename of this ClusterStatfs.

        The filesystem type name.  # noqa: E501

        :param f_fstypename: The f_fstypename of this ClusterStatfs.  # noqa: E501
        :type: str
        """
        if f_fstypename is None:
            raise ValueError("Invalid value for `f_fstypename`, must not be `None`")  # noqa: E501

        self._f_fstypename = f_fstypename

    @property
    def f_iosize(self):
        """Gets the f_iosize of this ClusterStatfs.  # noqa: E501

        The optimal transfer block size.  # noqa: E501

        :return: The f_iosize of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_iosize

    @f_iosize.setter
    def f_iosize(self, f_iosize):
        """Sets the f_iosize of this ClusterStatfs.

        The optimal transfer block size.  # noqa: E501

        :param f_iosize: The f_iosize of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_iosize is None:
            raise ValueError("Invalid value for `f_iosize`, must not be `None`")  # noqa: E501

        self._f_iosize = f_iosize

    @property
    def f_mntfromname(self):
        """Gets the f_mntfromname of this ClusterStatfs.  # noqa: E501

        The name of the mounted filesystem.  # noqa: E501

        :return: The f_mntfromname of this ClusterStatfs.  # noqa: E501
        :rtype: str
        """
        return self._f_mntfromname

    @f_mntfromname.setter
    def f_mntfromname(self, f_mntfromname):
        """Sets the f_mntfromname of this ClusterStatfs.

        The name of the mounted filesystem.  # noqa: E501

        :param f_mntfromname: The f_mntfromname of this ClusterStatfs.  # noqa: E501
        :type: str
        """
        if f_mntfromname is None:
            raise ValueError("Invalid value for `f_mntfromname`, must not be `None`")  # noqa: E501

        self._f_mntfromname = f_mntfromname

    @property
    def f_mntonname(self):
        """Gets the f_mntonname of this ClusterStatfs.  # noqa: E501

        The directory that the filesystem is mounted on.  # noqa: E501

        :return: The f_mntonname of this ClusterStatfs.  # noqa: E501
        :rtype: str
        """
        return self._f_mntonname

    @f_mntonname.setter
    def f_mntonname(self, f_mntonname):
        """Sets the f_mntonname of this ClusterStatfs.

        The directory that the filesystem is mounted on.  # noqa: E501

        :param f_mntonname: The f_mntonname of this ClusterStatfs.  # noqa: E501
        :type: str
        """
        if f_mntonname is None:
            raise ValueError("Invalid value for `f_mntonname`, must not be `None`")  # noqa: E501

        self._f_mntonname = f_mntonname

    @property
    def f_namemax(self):
        """Gets the f_namemax of this ClusterStatfs.  # noqa: E501

        The maximum length of a file name.  # noqa: E501

        :return: The f_namemax of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_namemax

    @f_namemax.setter
    def f_namemax(self, f_namemax):
        """Sets the f_namemax of this ClusterStatfs.

        The maximum length of a file name.  # noqa: E501

        :param f_namemax: The f_namemax of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_namemax is None:
            raise ValueError("Invalid value for `f_namemax`, must not be `None`")  # noqa: E501

        self._f_namemax = f_namemax

    @property
    def f_owner(self):
        """Gets the f_owner of this ClusterStatfs.  # noqa: E501

        The ID of the user that mounted the filesystem.  # noqa: E501

        :return: The f_owner of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_owner

    @f_owner.setter
    def f_owner(self, f_owner):
        """Sets the f_owner of this ClusterStatfs.

        The ID of the user that mounted the filesystem.  # noqa: E501

        :param f_owner: The f_owner of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_owner is None:
            raise ValueError("Invalid value for `f_owner`, must not be `None`")  # noqa: E501

        self._f_owner = f_owner

    @property
    def f_type(self):
        """Gets the f_type of this ClusterStatfs.  # noqa: E501

        The type of the filesystem.  # noqa: E501

        :return: The f_type of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_type

    @f_type.setter
    def f_type(self, f_type):
        """Sets the f_type of this ClusterStatfs.

        The type of the filesystem.  # noqa: E501

        :param f_type: The f_type of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_type is None:
            raise ValueError("Invalid value for `f_type`, must not be `None`")  # noqa: E501

        self._f_type = f_type

    @property
    def f_version(self):
        """Gets the f_version of this ClusterStatfs.  # noqa: E501

        The structure version number.  # noqa: E501

        :return: The f_version of this ClusterStatfs.  # noqa: E501
        :rtype: int
        """
        return self._f_version

    @f_version.setter
    def f_version(self, f_version):
        """Sets the f_version of this ClusterStatfs.

        The structure version number.  # noqa: E501

        :param f_version: The f_version of this ClusterStatfs.  # noqa: E501
        :type: int
        """
        if f_version is None:
            raise ValueError("Invalid value for `f_version`, must not be `None`")  # noqa: E501

        self._f_version = f_version

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
        if not isinstance(other, ClusterStatfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
