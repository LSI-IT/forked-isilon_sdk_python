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

from isilon_sdk.v9_1_0.models.summary_protocol_stats_protocol_stats_network_in import SummaryProtocolStatsProtocolStatsNetworkIn  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.summary_protocol_stats_protocol_stats_network_out import SummaryProtocolStatsProtocolStatsNetworkOut  # noqa: F401,E501


class SummaryProtocolStatsProtocolStatsNetwork(object):
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
        '_in': 'SummaryProtocolStatsProtocolStatsNetworkIn',
        'out': 'SummaryProtocolStatsProtocolStatsNetworkOut'
    }

    attribute_map = {
        '_in': 'in',
        'out': 'out'
    }

    def __init__(self, _in=None, out=None):  # noqa: E501
        """SummaryProtocolStatsProtocolStatsNetwork - a model defined in Swagger"""  # noqa: E501

        self.__in = None
        self._out = None
        self.discriminator = None

        if _in is not None:
            self._in = _in
        if out is not None:
            self.out = out

    @property
    def _in(self):
        """Gets the _in of this SummaryProtocolStatsProtocolStatsNetwork.  # noqa: E501

          # noqa: E501

        :return: The _in of this SummaryProtocolStatsProtocolStatsNetwork.  # noqa: E501
        :rtype: SummaryProtocolStatsProtocolStatsNetworkIn
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this SummaryProtocolStatsProtocolStatsNetwork.

          # noqa: E501

        :param _in: The _in of this SummaryProtocolStatsProtocolStatsNetwork.  # noqa: E501
        :type: SummaryProtocolStatsProtocolStatsNetworkIn
        """

        self.__in = _in

    @property
    def out(self):
        """Gets the out of this SummaryProtocolStatsProtocolStatsNetwork.  # noqa: E501

          # noqa: E501

        :return: The out of this SummaryProtocolStatsProtocolStatsNetwork.  # noqa: E501
        :rtype: SummaryProtocolStatsProtocolStatsNetworkOut
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this SummaryProtocolStatsProtocolStatsNetwork.

          # noqa: E501

        :param out: The out of this SummaryProtocolStatsProtocolStatsNetwork.  # noqa: E501
        :type: SummaryProtocolStatsProtocolStatsNetworkOut
        """

        self._out = out

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
        if not isinstance(other, SummaryProtocolStatsProtocolStatsNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
