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

from isilon_sdk.v9_1_0.models.providers_krb5_krb5_item_extended import ProvidersKrb5Krb5ItemExtended  # noqa: F401,E501


class ProvidersKrb5Extended(object):
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
        'krb5': 'list[ProvidersKrb5Krb5ItemExtended]'
    }

    attribute_map = {
        'krb5': 'krb5'
    }

    def __init__(self, krb5=None):  # noqa: E501
        """ProvidersKrb5Extended - a model defined in Swagger"""  # noqa: E501

        self._krb5 = None
        self.discriminator = None

        if krb5 is not None:
            self.krb5 = krb5

    @property
    def krb5(self):
        """Gets the krb5 of this ProvidersKrb5Extended.  # noqa: E501


        :return: The krb5 of this ProvidersKrb5Extended.  # noqa: E501
        :rtype: list[ProvidersKrb5Krb5ItemExtended]
        """
        return self._krb5

    @krb5.setter
    def krb5(self, krb5):
        """Sets the krb5 of this ProvidersKrb5Extended.


        :param krb5: The krb5 of this ProvidersKrb5Extended.  # noqa: E501
        :type: list[ProvidersKrb5Krb5ItemExtended]
        """

        self._krb5 = krb5

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
        if not isinstance(other, ProvidersKrb5Extended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
