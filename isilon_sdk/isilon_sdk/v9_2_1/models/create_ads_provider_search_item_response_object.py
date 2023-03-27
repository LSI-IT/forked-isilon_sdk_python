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

from isilon_sdk.v9_2_1.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501


class CreateAdsProviderSearchItemResponseObject(object):
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
        'description': 'str',
        'display_name': 'str',
        'id': 'AuthAccessAccessItemFileGroup'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'id': 'id'
    }

    def __init__(self, description=None, display_name=None, id=None):  # noqa: E501
        """CreateAdsProviderSearchItemResponseObject - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._display_name = None
        self._id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id

    @property
    def description(self):
        """Gets the description of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501


        :return: The description of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAdsProviderSearchItemResponseObject.


        :param description: The description of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 512:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `512`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501


        :return: The display_name of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateAdsProviderSearchItemResponseObject.


        :param display_name: The display_name of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501
        :type: str
        """
        if display_name is not None and len(display_name) > 255:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `255`")  # noqa: E501
        if display_name is not None and len(display_name) < 0:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The id of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAdsProviderSearchItemResponseObject.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param id: The id of this CreateAdsProviderSearchItemResponseObject.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._id = id

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
        if not isinstance(other, CreateAdsProviderSearchItemResponseObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
