# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EventMaintenanceExtended(object):
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
        'maintenance': 'bool',
        'prune': 'int'
    }

    attribute_map = {
        'maintenance': 'maintenance',
        'prune': 'prune'
    }

    def __init__(self, maintenance=None, prune=None):  # noqa: E501
        """EventMaintenanceExtended - a model defined in Swagger"""  # noqa: E501

        self._maintenance = None
        self._prune = None
        self.discriminator = None

        if maintenance is not None:
            self.maintenance = maintenance
        if prune is not None:
            self.prune = prune

    @property
    def maintenance(self):
        """Gets the maintenance of this EventMaintenanceExtended.  # noqa: E501

        Indicates if maintenance mode is enabled.  # noqa: E501

        :return: The maintenance of this EventMaintenanceExtended.  # noqa: E501
        :rtype: bool
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """Sets the maintenance of this EventMaintenanceExtended.

        Indicates if maintenance mode is enabled.  # noqa: E501

        :param maintenance: The maintenance of this EventMaintenanceExtended.  # noqa: E501
        :type: bool
        """

        self._maintenance = maintenance

    @property
    def prune(self):
        """Gets the prune of this EventMaintenanceExtended.  # noqa: E501

        Removes all maintenance mode history that is greater than set number of days.  # noqa: E501

        :return: The prune of this EventMaintenanceExtended.  # noqa: E501
        :rtype: int
        """
        return self._prune

    @prune.setter
    def prune(self, prune):
        """Sets the prune of this EventMaintenanceExtended.

        Removes all maintenance mode history that is greater than set number of days.  # noqa: E501

        :param prune: The prune of this EventMaintenanceExtended.  # noqa: E501
        :type: int
        """
        if prune is not None and prune > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `prune`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if prune is not None and prune < 0:  # noqa: E501
            raise ValueError("Invalid value for `prune`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prune = prune

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
        if not isinstance(other, EventMaintenanceExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
