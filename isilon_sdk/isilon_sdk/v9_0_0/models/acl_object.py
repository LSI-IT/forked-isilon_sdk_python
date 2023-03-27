# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_0_0.models.member_object import MemberObject  # noqa: F401,E501


class AclObject(object):
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
        'accessrights': 'list[str]',
        'accesstype': 'str',
        'inherit_flags': 'list[str]',
        'op': 'str',
        'trustee': 'MemberObject'
    }

    attribute_map = {
        'accessrights': 'accessrights',
        'accesstype': 'accesstype',
        'inherit_flags': 'inherit_flags',
        'op': 'op',
        'trustee': 'trustee'
    }

    def __init__(self, accessrights=None, accesstype=None, inherit_flags=None, op=None, trustee=None):  # noqa: E501
        """AclObject - a model defined in Swagger"""  # noqa: E501

        self._accessrights = None
        self._accesstype = None
        self._inherit_flags = None
        self._op = None
        self._trustee = None
        self.discriminator = None

        if accessrights is not None:
            self.accessrights = accessrights
        if accesstype is not None:
            self.accesstype = accesstype
        if inherit_flags is not None:
            self.inherit_flags = inherit_flags
        if op is not None:
            self.op = op
        if trustee is not None:
            self.trustee = trustee

    @property
    def accessrights(self):
        """Gets the accessrights of this AclObject.  # noqa: E501


        :return: The accessrights of this AclObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._accessrights

    @accessrights.setter
    def accessrights(self, accessrights):
        """Sets the accessrights of this AclObject.


        :param accessrights: The accessrights of this AclObject.  # noqa: E501
        :type: list[str]
        """

        self._accessrights = accessrights

    @property
    def accesstype(self):
        """Gets the accesstype of this AclObject.  # noqa: E501


        :return: The accesstype of this AclObject.  # noqa: E501
        :rtype: str
        """
        return self._accesstype

    @accesstype.setter
    def accesstype(self, accesstype):
        """Sets the accesstype of this AclObject.


        :param accesstype: The accesstype of this AclObject.  # noqa: E501
        :type: str
        """

        self._accesstype = accesstype

    @property
    def inherit_flags(self):
        """Gets the inherit_flags of this AclObject.  # noqa: E501


        :return: The inherit_flags of this AclObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._inherit_flags

    @inherit_flags.setter
    def inherit_flags(self, inherit_flags):
        """Sets the inherit_flags of this AclObject.


        :param inherit_flags: The inherit_flags of this AclObject.  # noqa: E501
        :type: list[str]
        """

        self._inherit_flags = inherit_flags

    @property
    def op(self):
        """Gets the op of this AclObject.  # noqa: E501


        :return: The op of this AclObject.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this AclObject.


        :param op: The op of this AclObject.  # noqa: E501
        :type: str
        """

        self._op = op

    @property
    def trustee(self):
        """Gets the trustee of this AclObject.  # noqa: E501


        :return: The trustee of this AclObject.  # noqa: E501
        :rtype: MemberObject
        """
        return self._trustee

    @trustee.setter
    def trustee(self, trustee):
        """Sets the trustee of this AclObject.


        :param trustee: The trustee of this AclObject.  # noqa: E501
        :type: MemberObject
        """

        self._trustee = trustee

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
        if not isinstance(other, AclObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
