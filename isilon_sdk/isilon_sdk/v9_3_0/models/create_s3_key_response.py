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

from isilon_sdk.v9_3_0.models.create_s3_key_response_keys import CreateS3KeyResponseKeys  # noqa: F401,E501


class CreateS3KeyResponse(object):
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
        'keys': 'CreateS3KeyResponseKeys'
    }

    attribute_map = {
        'keys': 'keys'
    }

    def __init__(self, keys=None):  # noqa: E501
        """CreateS3KeyResponse - a model defined in Swagger"""  # noqa: E501

        self._keys = None
        self.discriminator = None

        self.keys = keys

    @property
    def keys(self):
        """Gets the keys of this CreateS3KeyResponse.  # noqa: E501

          # noqa: E501

        :return: The keys of this CreateS3KeyResponse.  # noqa: E501
        :rtype: CreateS3KeyResponseKeys
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this CreateS3KeyResponse.

          # noqa: E501

        :param keys: The keys of this CreateS3KeyResponse.  # noqa: E501
        :type: CreateS3KeyResponseKeys
        """
        if keys is None:
            raise ValueError("Invalid value for `keys`, must not be `None`")  # noqa: E501

        self._keys = keys

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
        if not isinstance(other, CreateS3KeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
