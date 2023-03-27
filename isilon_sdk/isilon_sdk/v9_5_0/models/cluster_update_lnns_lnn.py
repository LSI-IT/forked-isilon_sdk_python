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


class ClusterUpdateLnnsLnn(object):
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
        'current_lnn': 'int',
        'new_lnn': 'int'
    }

    attribute_map = {
        'current_lnn': 'current_lnn',
        'new_lnn': 'new_lnn'
    }

    def __init__(self, current_lnn=None, new_lnn=None):  # noqa: E501
        """ClusterUpdateLnnsLnn - a model defined in Swagger"""  # noqa: E501

        self._current_lnn = None
        self._new_lnn = None
        self.discriminator = None

        if current_lnn is not None:
            self.current_lnn = current_lnn
        if new_lnn is not None:
            self.new_lnn = new_lnn

    @property
    def current_lnn(self):
        """Gets the current_lnn of this ClusterUpdateLnnsLnn.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The current_lnn of this ClusterUpdateLnnsLnn.  # noqa: E501
        :rtype: int
        """
        return self._current_lnn

    @current_lnn.setter
    def current_lnn(self, current_lnn):
        """Sets the current_lnn of this ClusterUpdateLnnsLnn.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param current_lnn: The current_lnn of this ClusterUpdateLnnsLnn.  # noqa: E501
        :type: int
        """
        if current_lnn is not None and current_lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `current_lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if current_lnn is not None and current_lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `current_lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._current_lnn = current_lnn

    @property
    def new_lnn(self):
        """Gets the new_lnn of this ClusterUpdateLnnsLnn.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The new_lnn of this ClusterUpdateLnnsLnn.  # noqa: E501
        :rtype: int
        """
        return self._new_lnn

    @new_lnn.setter
    def new_lnn(self, new_lnn):
        """Sets the new_lnn of this ClusterUpdateLnnsLnn.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param new_lnn: The new_lnn of this ClusterUpdateLnnsLnn.  # noqa: E501
        :type: int
        """
        if new_lnn is not None and new_lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `new_lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if new_lnn is not None and new_lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `new_lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._new_lnn = new_lnn

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
        if not isinstance(other, ClusterUpdateLnnsLnn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other