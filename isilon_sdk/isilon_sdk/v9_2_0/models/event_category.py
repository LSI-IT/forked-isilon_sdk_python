# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 12
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EventCategory(object):
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
        'id': 'str',
        'id_name': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'id_name': 'id_name',
        'name': 'name'
    }

    def __init__(self, id=None, id_name=None, name=None):  # noqa: E501
        """EventCategory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._id_name = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if id_name is not None:
            self.id_name = id_name
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this EventCategory.  # noqa: E501

        Numeric identifier of eventgroup category.  # noqa: E501

        :return: The id of this EventCategory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventCategory.

        Numeric identifier of eventgroup category.  # noqa: E501

        :param id: The id of this EventCategory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def id_name(self):
        """Gets the id_name of this EventCategory.  # noqa: E501

        Name of category.  # noqa: E501

        :return: The id_name of this EventCategory.  # noqa: E501
        :rtype: str
        """
        return self._id_name

    @id_name.setter
    def id_name(self, id_name):
        """Sets the id_name of this EventCategory.

        Name of category.  # noqa: E501

        :param id_name: The id_name of this EventCategory.  # noqa: E501
        :type: str
        """

        self._id_name = id_name

    @property
    def name(self):
        """Gets the name of this EventCategory.  # noqa: E501

        Description of category.  # noqa: E501

        :return: The name of this EventCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventCategory.

        Description of category.  # noqa: E501

        :param name: The name of this EventCategory.  # noqa: E501
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
        if not isinstance(other, EventCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
