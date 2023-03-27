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

from isilon_sdk.v9_1_0.models.nodetype_assess_nodetype_from_nodepool_item import NodetypeAssessNodetypeFromNodepoolItem  # noqa: F401,E501


class NodetypeAssessNodetype(object):
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
        'from_nodepool': 'list[NodetypeAssessNodetypeFromNodepoolItem]',
        'to_nodepool': 'list[NodetypeAssessNodetypeFromNodepoolItem]'
    }

    attribute_map = {
        'from_nodepool': 'from_nodepool',
        'to_nodepool': 'to_nodepool'
    }

    def __init__(self, from_nodepool=None, to_nodepool=None):  # noqa: E501
        """NodetypeAssessNodetype - a model defined in Swagger"""  # noqa: E501

        self._from_nodepool = None
        self._to_nodepool = None
        self.discriminator = None

        self.from_nodepool = from_nodepool
        self.to_nodepool = to_nodepool

    @property
    def from_nodepool(self):
        """Gets the from_nodepool of this NodetypeAssessNodetype.  # noqa: E501

        Pools assessed for removing nodetype.  # noqa: E501

        :return: The from_nodepool of this NodetypeAssessNodetype.  # noqa: E501
        :rtype: list[NodetypeAssessNodetypeFromNodepoolItem]
        """
        return self._from_nodepool

    @from_nodepool.setter
    def from_nodepool(self, from_nodepool):
        """Sets the from_nodepool of this NodetypeAssessNodetype.

        Pools assessed for removing nodetype.  # noqa: E501

        :param from_nodepool: The from_nodepool of this NodetypeAssessNodetype.  # noqa: E501
        :type: list[NodetypeAssessNodetypeFromNodepoolItem]
        """
        if from_nodepool is None:
            raise ValueError("Invalid value for `from_nodepool`, must not be `None`")  # noqa: E501

        self._from_nodepool = from_nodepool

    @property
    def to_nodepool(self):
        """Gets the to_nodepool of this NodetypeAssessNodetype.  # noqa: E501

        Pools assessed for adding nodetype.  # noqa: E501

        :return: The to_nodepool of this NodetypeAssessNodetype.  # noqa: E501
        :rtype: list[NodetypeAssessNodetypeFromNodepoolItem]
        """
        return self._to_nodepool

    @to_nodepool.setter
    def to_nodepool(self, to_nodepool):
        """Sets the to_nodepool of this NodetypeAssessNodetype.

        Pools assessed for adding nodetype.  # noqa: E501

        :param to_nodepool: The to_nodepool of this NodetypeAssessNodetype.  # noqa: E501
        :type: list[NodetypeAssessNodetypeFromNodepoolItem]
        """
        if to_nodepool is None:
            raise ValueError("Invalid value for `to_nodepool`, must not be `None`")  # noqa: E501

        self._to_nodepool = to_nodepool

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
        if not isinstance(other, NodetypeAssessNodetype):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
