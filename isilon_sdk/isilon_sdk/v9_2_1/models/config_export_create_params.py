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


class ConfigExportCreateParams(object):
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
        'components': 'str'
    }

    attribute_map = {
        'components': 'components'
    }

    def __init__(self, components=None):  # noqa: E501
        """ConfigExportCreateParams - a model defined in Swagger"""  # noqa: E501

        self._components = None
        self.discriminator = None

        if components is not None:
            self.components = components

    @property
    def components(self):
        """Gets the components of this ConfigExportCreateParams.  # noqa: E501

        Specifies the components which will be exported.  # noqa: E501

        :return: The components of this ConfigExportCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ConfigExportCreateParams.

        Specifies the components which will be exported.  # noqa: E501

        :param components: The components of this ConfigExportCreateParams.  # noqa: E501
        :type: str
        """
        if components is not None and len(components) > 8192:
            raise ValueError("Invalid value for `components`, length must be less than or equal to `8192`")  # noqa: E501
        if components is not None and len(components) < 1:
            raise ValueError("Invalid value for `components`, length must be greater than or equal to `1`")  # noqa: E501

        self._components = components

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
        if not isinstance(other, ConfigExportCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
