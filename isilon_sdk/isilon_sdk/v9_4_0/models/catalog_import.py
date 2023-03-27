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


class CatalogImport(object):
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
        'file': 'str'
    }

    attribute_map = {
        'file': 'file'
    }

    def __init__(self, file=None):  # noqa: E501
        """CatalogImport - a model defined in Swagger"""  # noqa: E501

        self._file = None
        self.discriminator = None

        self.file = file

    @property
    def file(self):
        """Gets the file of this CatalogImport.  # noqa: E501

        Path of the signed file to import in the catalog  # noqa: E501

        :return: The file of this CatalogImport.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CatalogImport.

        Path of the signed file to import in the catalog  # noqa: E501

        :param file: The file of this CatalogImport.  # noqa: E501
        :type: str
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501
        if file is not None and len(file) > 4096:
            raise ValueError("Invalid value for `file`, length must be less than or equal to `4096`")  # noqa: E501
        if file is not None and len(file) < 3:
            raise ValueError("Invalid value for `file`, length must be greater than or equal to `3`")  # noqa: E501

        self._file = file

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
        if not isinstance(other, CatalogImport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
