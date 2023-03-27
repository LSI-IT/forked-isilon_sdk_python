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


class ClusterNodeSled(object):
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
        'is_removeable': 'bool',
        'sled_letter': 'str',
        'sled_state': 'str'
    }

    attribute_map = {
        'is_removeable': 'is_removeable',
        'sled_letter': 'sled_letter',
        'sled_state': 'sled_state'
    }

    def __init__(self, is_removeable=None, sled_letter=None, sled_state=None):  # noqa: E501
        """ClusterNodeSled - a model defined in Swagger"""  # noqa: E501

        self._is_removeable = None
        self._sled_letter = None
        self._sled_state = None
        self.discriminator = None

        self.is_removeable = is_removeable
        self.sled_letter = sled_letter
        self.sled_state = sled_state

    @property
    def is_removeable(self):
        """Gets the is_removeable of this ClusterNodeSled.  # noqa: E501

        Boolean to indicate whether or not the sled is safe to remove.  # noqa: E501

        :return: The is_removeable of this ClusterNodeSled.  # noqa: E501
        :rtype: bool
        """
        return self._is_removeable

    @is_removeable.setter
    def is_removeable(self, is_removeable):
        """Sets the is_removeable of this ClusterNodeSled.

        Boolean to indicate whether or not the sled is safe to remove.  # noqa: E501

        :param is_removeable: The is_removeable of this ClusterNodeSled.  # noqa: E501
        :type: bool
        """
        if is_removeable is None:
            raise ValueError("Invalid value for `is_removeable`, must not be `None`")  # noqa: E501

        self._is_removeable = is_removeable

    @property
    def sled_letter(self):
        """Gets the sled_letter of this ClusterNodeSled.  # noqa: E501

        The sled letter which OneFS uses to refer to this sled in the node.  # noqa: E501

        :return: The sled_letter of this ClusterNodeSled.  # noqa: E501
        :rtype: str
        """
        return self._sled_letter

    @sled_letter.setter
    def sled_letter(self, sled_letter):
        """Sets the sled_letter of this ClusterNodeSled.

        The sled letter which OneFS uses to refer to this sled in the node.  # noqa: E501

        :param sled_letter: The sled_letter of this ClusterNodeSled.  # noqa: E501
        :type: str
        """
        if sled_letter is None:
            raise ValueError("Invalid value for `sled_letter`, must not be `None`")  # noqa: E501
        if sled_letter is not None and len(sled_letter) > 1:
            raise ValueError("Invalid value for `sled_letter`, length must be less than or equal to `1`")  # noqa: E501
        if sled_letter is not None and len(sled_letter) < 1:
            raise ValueError("Invalid value for `sled_letter`, length must be greater than or equal to `1`")  # noqa: E501
        if sled_letter is not None and not re.search('^[a-eA-E]$', sled_letter):  # noqa: E501
            raise ValueError("Invalid value for `sled_letter`, must be a follow pattern or equal to `/^[a-eA-E]$/`")  # noqa: E501

        self._sled_letter = sled_letter

    @property
    def sled_state(self):
        """Gets the sled_state of this ClusterNodeSled.  # noqa: E501

        The state of physical presence of a sled.  # noqa: E501

        :return: The sled_state of this ClusterNodeSled.  # noqa: E501
        :rtype: str
        """
        return self._sled_state

    @sled_state.setter
    def sled_state(self, sled_state):
        """Sets the sled_state of this ClusterNodeSled.

        The state of physical presence of a sled.  # noqa: E501

        :param sled_state: The sled_state of this ClusterNodeSled.  # noqa: E501
        :type: str
        """
        if sled_state is None:
            raise ValueError("Invalid value for `sled_state`, must not be `None`")  # noqa: E501
        allowed_values = ["Present", "Absent", "Unknown"]  # noqa: E501
        if sled_state not in allowed_values:
            raise ValueError(
                "Invalid value for `sled_state` ({0}), must be one of {1}"  # noqa: E501
                .format(sled_state, allowed_values)
            )

        self._sled_state = sled_state

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
        if not isinstance(other, ClusterNodeSled):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
