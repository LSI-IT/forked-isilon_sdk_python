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


class ResultTopDirsDir(object):
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
        'path': 'str'
    }

    attribute_map = {
        'atime': 'atime',
        'btime': 'btime',
        'ctime': 'ctime',
        'path': 'path'
    }

    def __init__(self, atime=None, btime=None, ctime=None, path=None):  # noqa: E501
        """ResultTopDirsDir - a model defined in Swagger"""  # noqa: E501

        self._atime = None
        self._btime = None
        self._ctime = None
        self._path = None
        self.discriminator = None

        self.atime = atime
        self.btime = btime
        self.ctime = ctime
        self.path = path

    @property
    def atime(self):
        """Gets the atime of this ResultTopDirsDir.  # noqa: E501

        Directory access time  # noqa: E501

        :return: The atime of this ResultTopDirsDir.  # noqa: E501
        :rtype: int
        """
        return self._atime

    @atime.setter
    def atime(self, atime):
        """Sets the atime of this ResultTopDirsDir.

        Directory access time  # noqa: E501

        :param atime: The atime of this ResultTopDirsDir.  # noqa: E501
        :type: int
        """
        if atime is None:
            raise ValueError("Invalid value for `atime`, must not be `None`")  # noqa: E501

        self._atime = atime

    @property
    def btime(self):
        """Gets the btime of this ResultTopDirsDir.  # noqa: E501

        Directory creation begin time.  # noqa: E501

        :return: The btime of this ResultTopDirsDir.  # noqa: E501
        :rtype: int
        """
        return self._btime

    @btime.setter
    def btime(self, btime):
        """Sets the btime of this ResultTopDirsDir.

        Directory creation begin time.  # noqa: E501

        :param btime: The btime of this ResultTopDirsDir.  # noqa: E501
        :type: int
        """
        if btime is None:
            raise ValueError("Invalid value for `btime`, must not be `None`")  # noqa: E501

        self._btime = btime

    @property
    def ctime(self):
        """Gets the ctime of this ResultTopDirsDir.  # noqa: E501

        Unix inode change time.  # noqa: E501

        :return: The ctime of this ResultTopDirsDir.  # noqa: E501
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this ResultTopDirsDir.

        Unix inode change time.  # noqa: E501

        :param ctime: The ctime of this ResultTopDirsDir.  # noqa: E501
        :type: int
        """
        if ctime is None:
            raise ValueError("Invalid value for `ctime`, must not be `None`")  # noqa: E501

        self._ctime = ctime

    @property
    def path(self):
        """Gets the path of this ResultTopDirsDir.  # noqa: E501

        Relative directory path under /ifs/.  # noqa: E501

        :return: The path of this ResultTopDirsDir.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ResultTopDirsDir.

        Relative directory path under /ifs/.  # noqa: E501

        :param path: The path of this ResultTopDirsDir.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

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
        if not isinstance(other, ResultTopDirsDir):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
