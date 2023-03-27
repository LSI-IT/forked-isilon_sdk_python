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

from isilon_sdk.v9_4_0.models.cluster_node_sensor_value import ClusterNodeSensorValue  # noqa: F401,E501


class ClusterNodeSensor(object):
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
        'count': 'int',
        'name': 'str',
        'values': 'list[ClusterNodeSensorValue]'
    }

    attribute_map = {
        'count': 'count',
        'name': 'name',
        'values': 'values'
    }

    def __init__(self, count=None, name=None, values=None):  # noqa: E501
        """ClusterNodeSensor - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._name = None
        self._values = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if name is not None:
            self.name = name
        if values is not None:
            self.values = values

    @property
    def count(self):
        """Gets the count of this ClusterNodeSensor.  # noqa: E501

        The count of values in this sensor group.  # noqa: E501

        :return: The count of this ClusterNodeSensor.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ClusterNodeSensor.

        The count of values in this sensor group.  # noqa: E501

        :param count: The count of this ClusterNodeSensor.  # noqa: E501
        :type: int
        """
        if count is not None and count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def name(self):
        """Gets the name of this ClusterNodeSensor.  # noqa: E501

        The name of this sensor group.  # noqa: E501

        :return: The name of this ClusterNodeSensor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterNodeSensor.

        The name of this sensor group.  # noqa: E501

        :param name: The name of this ClusterNodeSensor.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def values(self):
        """Gets the values of this ClusterNodeSensor.  # noqa: E501

        The list of specific sensor value info in this sensor group.  # noqa: E501

        :return: The values of this ClusterNodeSensor.  # noqa: E501
        :rtype: list[ClusterNodeSensorValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ClusterNodeSensor.

        The list of specific sensor value info in this sensor group.  # noqa: E501

        :param values: The values of this ClusterNodeSensor.  # noqa: E501
        :type: list[ClusterNodeSensorValue]
        """

        self._values = values

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
        if not isinstance(other, ClusterNodeSensor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
