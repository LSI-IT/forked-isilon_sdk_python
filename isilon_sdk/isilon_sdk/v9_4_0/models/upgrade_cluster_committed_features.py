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

from isilon_sdk.v9_4_0.models.upgrade_cluster_committed_features_gen_bit import UpgradeClusterCommittedFeaturesGenBit  # noqa: F401,E501


class UpgradeClusterCommittedFeatures(object):
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
        'default_gen': 'int',
        'gen_bits': 'list[UpgradeClusterCommittedFeaturesGenBit]'
    }

    attribute_map = {
        'default_gen': 'default_gen',
        'gen_bits': 'gen_bits'
    }

    def __init__(self, default_gen=None, gen_bits=None):  # noqa: E501
        """UpgradeClusterCommittedFeatures - a model defined in Swagger"""  # noqa: E501

        self._default_gen = None
        self._gen_bits = None
        self.discriminator = None

        if default_gen is not None:
            self.default_gen = default_gen
        if gen_bits is not None:
            self.gen_bits = gen_bits

    @property
    def default_gen(self):
        """Gets the default_gen of this UpgradeClusterCommittedFeatures.  # noqa: E501


        :return: The default_gen of this UpgradeClusterCommittedFeatures.  # noqa: E501
        :rtype: int
        """
        return self._default_gen

    @default_gen.setter
    def default_gen(self, default_gen):
        """Sets the default_gen of this UpgradeClusterCommittedFeatures.


        :param default_gen: The default_gen of this UpgradeClusterCommittedFeatures.  # noqa: E501
        :type: int
        """
        if default_gen is not None and default_gen > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `default_gen`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if default_gen is not None and default_gen < 0:  # noqa: E501
            raise ValueError("Invalid value for `default_gen`, must be a value greater than or equal to `0`")  # noqa: E501

        self._default_gen = default_gen

    @property
    def gen_bits(self):
        """Gets the gen_bits of this UpgradeClusterCommittedFeatures.  # noqa: E501


        :return: The gen_bits of this UpgradeClusterCommittedFeatures.  # noqa: E501
        :rtype: list[UpgradeClusterCommittedFeaturesGenBit]
        """
        return self._gen_bits

    @gen_bits.setter
    def gen_bits(self, gen_bits):
        """Sets the gen_bits of this UpgradeClusterCommittedFeatures.


        :param gen_bits: The gen_bits of this UpgradeClusterCommittedFeatures.  # noqa: E501
        :type: list[UpgradeClusterCommittedFeaturesGenBit]
        """

        self._gen_bits = gen_bits

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
        if not isinstance(other, UpgradeClusterCommittedFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
