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

from isilon_sdk.v9_4_0.models.cluster_identity_logon_extended import ClusterIdentityLogonExtended  # noqa: F401,E501


class ClusterIdentityExtended(object):
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
        'description': 'str',
        'logon': 'ClusterIdentityLogonExtended',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'logon': 'logon',
        'name': 'name'
    }

    def __init__(self, description=None, logon=None, name=None):  # noqa: E501
        """ClusterIdentityExtended - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._logon = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if logon is not None:
            self.logon = logon
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this ClusterIdentityExtended.  # noqa: E501

        A description of the cluster.  # noqa: E501

        :return: The description of this ClusterIdentityExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterIdentityExtended.

        A description of the cluster.  # noqa: E501

        :param description: The description of this ClusterIdentityExtended.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def logon(self):
        """Gets the logon of this ClusterIdentityExtended.  # noqa: E501

        The information displayed when a user logs in to the cluster.  # noqa: E501

        :return: The logon of this ClusterIdentityExtended.  # noqa: E501
        :rtype: ClusterIdentityLogonExtended
        """
        return self._logon

    @logon.setter
    def logon(self, logon):
        """Sets the logon of this ClusterIdentityExtended.

        The information displayed when a user logs in to the cluster.  # noqa: E501

        :param logon: The logon of this ClusterIdentityExtended.  # noqa: E501
        :type: ClusterIdentityLogonExtended
        """

        self._logon = logon

    @property
    def name(self):
        """Gets the name of this ClusterIdentityExtended.  # noqa: E501

        The name of the cluster.  # noqa: E501

        :return: The name of this ClusterIdentityExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterIdentityExtended.

        The name of the cluster.  # noqa: E501

        :param name: The name of this ClusterIdentityExtended.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, ClusterIdentityExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
