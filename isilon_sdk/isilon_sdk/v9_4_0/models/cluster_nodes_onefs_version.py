# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClusterNodesOnefsVersion(object):
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
        'bugfix': 'int',
        'maintenance': 'int',
        'major': 'int',
        'minor': 'int',
        'version': 'str'
    }

    attribute_map = {
        'bugfix': 'bugfix',
        'maintenance': 'maintenance',
        'major': 'major',
        'minor': 'minor',
        'version': 'version'
    }

    def __init__(self, bugfix=None, maintenance=None, major=None, minor=None, version=None):  # noqa: E501
        """ClusterNodesOnefsVersion - a model defined in Swagger"""  # noqa: E501

        self._bugfix = None
        self._maintenance = None
        self._major = None
        self._minor = None
        self._version = None
        self.discriminator = None

        if bugfix is not None:
            self.bugfix = bugfix
        if maintenance is not None:
            self.maintenance = maintenance
        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if version is not None:
            self.version = version

    @property
    def bugfix(self):
        """Gets the bugfix of this ClusterNodesOnefsVersion.  # noqa: E501


        :return: The bugfix of this ClusterNodesOnefsVersion.  # noqa: E501
        :rtype: int
        """
        return self._bugfix

    @bugfix.setter
    def bugfix(self, bugfix):
        """Sets the bugfix of this ClusterNodesOnefsVersion.


        :param bugfix: The bugfix of this ClusterNodesOnefsVersion.  # noqa: E501
        :type: int
        """
        if bugfix is not None and bugfix > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `bugfix`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if bugfix is not None and bugfix < 0:  # noqa: E501
            raise ValueError("Invalid value for `bugfix`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bugfix = bugfix

    @property
    def maintenance(self):
        """Gets the maintenance of this ClusterNodesOnefsVersion.  # noqa: E501


        :return: The maintenance of this ClusterNodesOnefsVersion.  # noqa: E501
        :rtype: int
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """Sets the maintenance of this ClusterNodesOnefsVersion.


        :param maintenance: The maintenance of this ClusterNodesOnefsVersion.  # noqa: E501
        :type: int
        """
        if maintenance is not None and maintenance > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `maintenance`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if maintenance is not None and maintenance < 0:  # noqa: E501
            raise ValueError("Invalid value for `maintenance`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maintenance = maintenance

    @property
    def major(self):
        """Gets the major of this ClusterNodesOnefsVersion.  # noqa: E501


        :return: The major of this ClusterNodesOnefsVersion.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this ClusterNodesOnefsVersion.


        :param major: The major of this ClusterNodesOnefsVersion.  # noqa: E501
        :type: int
        """
        if major is not None and major > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `major`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if major is not None and major < 0:  # noqa: E501
            raise ValueError("Invalid value for `major`, must be a value greater than or equal to `0`")  # noqa: E501

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this ClusterNodesOnefsVersion.  # noqa: E501


        :return: The minor of this ClusterNodesOnefsVersion.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this ClusterNodesOnefsVersion.


        :param minor: The minor of this ClusterNodesOnefsVersion.  # noqa: E501
        :type: int
        """
        if minor is not None and minor > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `minor`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if minor is not None and minor < 0:  # noqa: E501
            raise ValueError("Invalid value for `minor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._minor = minor

    @property
    def version(self):
        """Gets the version of this ClusterNodesOnefsVersion.  # noqa: E501

        Hex representation of the OneFS version integer.  # noqa: E501

        :return: The version of this ClusterNodesOnefsVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterNodesOnefsVersion.

        Hex representation of the OneFS version integer.  # noqa: E501

        :param version: The version of this ClusterNodesOnefsVersion.  # noqa: E501
        :type: str
        """
        if version is not None and len(version) > 128:
            raise ValueError("Invalid value for `version`, length must be less than or equal to `128`")  # noqa: E501
        if version is not None and len(version) < 1:
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

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
        if not isinstance(other, ClusterNodesOnefsVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
