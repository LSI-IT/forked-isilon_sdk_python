# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CertificateServerIdParams(object):
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
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, description=None, name=None):  # noqa: E501
        """CertificateServerIdParams - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this CertificateServerIdParams.  # noqa: E501

        Description field associated with a certificate provided for administrative convenience.  # noqa: E501

        :return: The description of this CertificateServerIdParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CertificateServerIdParams.

        Description field associated with a certificate provided for administrative convenience.  # noqa: E501

        :param description: The description of this CertificateServerIdParams.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 2048:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `2048`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this CertificateServerIdParams.  # noqa: E501

        Administrator specified name identifier.  # noqa: E501

        :return: The name of this CertificateServerIdParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificateServerIdParams.

        Administrator specified name identifier.  # noqa: E501

        :param name: The name of this CertificateServerIdParams.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501
        if name is not None and not re.search('^[a-zA-Z0-9_-]*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9_-]*$/`")  # noqa: E501

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
        if not isinstance(other, CertificateServerIdParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other