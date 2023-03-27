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

from isilon_sdk.v9_0_0.models.summary_protocol_stats_protocol_stats_protocol_data_item import SummaryProtocolStatsProtocolStatsProtocolDataItem  # noqa: F401,E501


class SummaryProtocolStatsProtocolStatsProtocol(object):
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
        'data': 'list[SummaryProtocolStatsProtocolStatsProtocolDataItem]',
        'name': 'str'
    }

    attribute_map = {
        'data': 'data',
        'name': 'name'
    }

    def __init__(self, data=None, name=None):  # noqa: E501
        """SummaryProtocolStatsProtocolStatsProtocol - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._name = None
        self.discriminator = None

        self.data = data
        if name is not None:
            self.name = name

    @property
    def data(self):
        """Gets the data of this SummaryProtocolStatsProtocolStatsProtocol.  # noqa: E501


        :return: The data of this SummaryProtocolStatsProtocolStatsProtocol.  # noqa: E501
        :rtype: list[SummaryProtocolStatsProtocolStatsProtocolDataItem]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SummaryProtocolStatsProtocolStatsProtocol.


        :param data: The data of this SummaryProtocolStatsProtocolStatsProtocol.  # noqa: E501
        :type: list[SummaryProtocolStatsProtocolStatsProtocolDataItem]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def name(self):
        """Gets the name of this SummaryProtocolStatsProtocolStatsProtocol.  # noqa: E501

        The name of the protocol.  # noqa: E501

        :return: The name of this SummaryProtocolStatsProtocolStatsProtocol.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SummaryProtocolStatsProtocolStatsProtocol.

        The name of the protocol.  # noqa: E501

        :param name: The name of this SummaryProtocolStatsProtocolStatsProtocol.  # noqa: E501
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
        if not isinstance(other, SummaryProtocolStatsProtocolStatsProtocol):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
