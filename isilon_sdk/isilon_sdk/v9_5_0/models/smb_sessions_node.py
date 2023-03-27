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

from isilon_sdk.v9_5_0.models.protocols_smb_sessions_session import ProtocolsSmbSessionsSession  # noqa: F401,E501


class SmbSessionsNode(object):
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
        'id': 'int',
        'lnn': 'int',
        'resume': 'str',
        'sessions': 'list[ProtocolsSmbSessionsSession]',
        'total': 'int'
    }

    attribute_map = {
        'id': 'id',
        'lnn': 'lnn',
        'resume': 'resume',
        'sessions': 'sessions',
        'total': 'total'
    }

    def __init__(self, id=None, lnn=None, resume=None, sessions=None, total=None):  # noqa: E501
        """SmbSessionsNode - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._lnn = None
        self._resume = None
        self._sessions = None
        self._total = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if resume is not None:
            self.resume = resume
        if sessions is not None:
            self.sessions = sessions
        if total is not None:
            self.total = total

    @property
    def id(self):
        """Gets the id of this SmbSessionsNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this SmbSessionsNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmbSessionsNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this SmbSessionsNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this SmbSessionsNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this SmbSessionsNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this SmbSessionsNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this SmbSessionsNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def resume(self):
        """Gets the resume of this SmbSessionsNode.  # noqa: E501

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :return: The resume of this SmbSessionsNode.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this SmbSessionsNode.

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :param resume: The resume of this SmbSessionsNode.  # noqa: E501
        :type: str
        """
        if resume is not None and len(resume) > 8192:
            raise ValueError("Invalid value for `resume`, length must be less than or equal to `8192`")  # noqa: E501
        if resume is not None and len(resume) < 0:
            raise ValueError("Invalid value for `resume`, length must be greater than or equal to `0`")  # noqa: E501

        self._resume = resume

    @property
    def sessions(self):
        """Gets the sessions of this SmbSessionsNode.  # noqa: E501

        A list of open SMB sessions on node.  # noqa: E501

        :return: The sessions of this SmbSessionsNode.  # noqa: E501
        :rtype: list[ProtocolsSmbSessionsSession]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        """Sets the sessions of this SmbSessionsNode.

        A list of open SMB sessions on node.  # noqa: E501

        :param sessions: The sessions of this SmbSessionsNode.  # noqa: E501
        :type: list[ProtocolsSmbSessionsSession]
        """

        self._sessions = sessions

    @property
    def total(self):
        """Gets the total of this SmbSessionsNode.  # noqa: E501

        The number of sessions returned.  # noqa: E501

        :return: The total of this SmbSessionsNode.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SmbSessionsNode.

        The number of sessions returned.  # noqa: E501

        :param total: The total of this SmbSessionsNode.  # noqa: E501
        :type: int
        """
        if total is not None and total > 65535:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value less than or equal to `65535`")  # noqa: E501
        if total is not None and total < 0:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, SmbSessionsNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
