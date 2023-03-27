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


class PoolsPoolStatusSettingsNodeInterfaceStatus(object):
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
        'total': 'int',
        'usable': 'int'
    }

    attribute_map = {
        'total': 'total',
        'usable': 'usable'
    }

    def __init__(self, total=None, usable=None):  # noqa: E501
        """PoolsPoolStatusSettingsNodeInterfaceStatus - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._usable = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if usable is not None:
            self.usable = usable

    @property
    def total(self):
        """Gets the total of this PoolsPoolStatusSettingsNodeInterfaceStatus.  # noqa: E501

        The number of interfaces on the node that are configured within this Network Pool  # noqa: E501

        :return: The total of this PoolsPoolStatusSettingsNodeInterfaceStatus.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PoolsPoolStatusSettingsNodeInterfaceStatus.

        The number of interfaces on the node that are configured within this Network Pool  # noqa: E501

        :param total: The total of this PoolsPoolStatusSettingsNodeInterfaceStatus.  # noqa: E501
        :type: int
        """
        if total is not None and total > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if total is not None and total < 0:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

    @property
    def usable(self):
        """Gets the usable of this PoolsPoolStatusSettingsNodeInterfaceStatus.  # noqa: E501

        The number of interfaces on the node that are configured within this Network Pool and are currently usable to SmartConnect.  # noqa: E501

        :return: The usable of this PoolsPoolStatusSettingsNodeInterfaceStatus.  # noqa: E501
        :rtype: int
        """
        return self._usable

    @usable.setter
    def usable(self, usable):
        """Sets the usable of this PoolsPoolStatusSettingsNodeInterfaceStatus.

        The number of interfaces on the node that are configured within this Network Pool and are currently usable to SmartConnect.  # noqa: E501

        :param usable: The usable of this PoolsPoolStatusSettingsNodeInterfaceStatus.  # noqa: E501
        :type: int
        """
        if usable is not None and usable > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `usable`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if usable is not None and usable < 0:  # noqa: E501
            raise ValueError("Invalid value for `usable`, must be a value greater than or equal to `0`")  # noqa: E501

        self._usable = usable

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
        if not isinstance(other, PoolsPoolStatusSettingsNodeInterfaceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
