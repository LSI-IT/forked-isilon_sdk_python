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


class SettingsCharacterEncodingsSettings(object):
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
        'current_encoding': 'str',
        'default_encoding': 'str',
        'encodings': 'list[str]'
    }

    attribute_map = {
        'current_encoding': 'current_encoding',
        'default_encoding': 'default_encoding',
        'encodings': 'encodings'
    }

    def __init__(self, current_encoding=None, default_encoding='UTF-8', encodings=None):  # noqa: E501
        """SettingsCharacterEncodingsSettings - a model defined in Swagger"""  # noqa: E501

        self._current_encoding = None
        self._default_encoding = None
        self._encodings = None
        self.discriminator = None

        self.current_encoding = current_encoding
        self.default_encoding = default_encoding
        self.encodings = encodings

    @property
    def current_encoding(self):
        """Gets the current_encoding of this SettingsCharacterEncodingsSettings.  # noqa: E501

        Current filesystem character encoding.  # noqa: E501

        :return: The current_encoding of this SettingsCharacterEncodingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._current_encoding

    @current_encoding.setter
    def current_encoding(self, current_encoding):
        """Sets the current_encoding of this SettingsCharacterEncodingsSettings.

        Current filesystem character encoding.  # noqa: E501

        :param current_encoding: The current_encoding of this SettingsCharacterEncodingsSettings.  # noqa: E501
        :type: str
        """
        if current_encoding is None:
            raise ValueError("Invalid value for `current_encoding`, must not be `None`")  # noqa: E501
        allowed_values = ["Windows-SJIS", "Windows-949", "Windows-1252", "EUC-KR", "EUC-JP", "EUC-JP-MS", "UTF-8-MAC", "UTF-8", "ISO-8859-1 (Latin-1)", "ISO-8859-2 (Latin-2)", "ISO-8859-3 (Latin-3)", "ISO-8859-4 (Latin-4)", "ISO-8859-5 (Cyrillic)", "ISO-8859-6 (Arabic)", "ISO-8859-7 (Greek)", "ISO-8859-8 (Hebrew)", "ISO-8859-9 (Latin-5)", "ISO-8859-10 (Latin-6)", "ISO-8859-13 (Latin-7)", "ISO-8859-14 (Latin-8)", "ISO-8859-15 (Latin-9)", "ISO-8859-16 (Latin-10)"]  # noqa: E501
        if current_encoding not in allowed_values:
            raise ValueError(
                "Invalid value for `current_encoding` ({0}), must be one of {1}"  # noqa: E501
                .format(current_encoding, allowed_values)
            )

        self._current_encoding = current_encoding

    @property
    def default_encoding(self):
        """Gets the default_encoding of this SettingsCharacterEncodingsSettings.  # noqa: E501

        Default filesystem character encoding.  # noqa: E501

        :return: The default_encoding of this SettingsCharacterEncodingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_encoding

    @default_encoding.setter
    def default_encoding(self, default_encoding):
        """Sets the default_encoding of this SettingsCharacterEncodingsSettings.

        Default filesystem character encoding.  # noqa: E501

        :param default_encoding: The default_encoding of this SettingsCharacterEncodingsSettings.  # noqa: E501
        :type: str
        """
        if default_encoding is None:
            raise ValueError("Invalid value for `default_encoding`, must not be `None`")  # noqa: E501
        if default_encoding is not None and len(default_encoding) > 5:
            raise ValueError("Invalid value for `default_encoding`, length must be less than or equal to `5`")  # noqa: E501
        if default_encoding is not None and len(default_encoding) < 5:
            raise ValueError("Invalid value for `default_encoding`, length must be greater than or equal to `5`")  # noqa: E501

        self._default_encoding = default_encoding

    @property
    def encodings(self):
        """Gets the encodings of this SettingsCharacterEncodingsSettings.  # noqa: E501

        A list of supported filesystem character encodings.  # noqa: E501

        :return: The encodings of this SettingsCharacterEncodingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._encodings

    @encodings.setter
    def encodings(self, encodings):
        """Sets the encodings of this SettingsCharacterEncodingsSettings.

        A list of supported filesystem character encodings.  # noqa: E501

        :param encodings: The encodings of this SettingsCharacterEncodingsSettings.  # noqa: E501
        :type: list[str]
        """
        if encodings is None:
            raise ValueError("Invalid value for `encodings`, must not be `None`")  # noqa: E501
        allowed_values = ["Windows-SJIS", "Windows-949", "Windows-1252", "EUC-KR", "EUC-JP", "EUC-JP-MS", "UTF-8-MAC", "UTF-8", "ISO-8859-1 (Latin-1)", "ISO-8859-2 (Latin-2)", "ISO-8859-3 (Latin-3)", "ISO-8859-4 (Latin-4)", "ISO-8859-5 (Cyrillic)", "ISO-8859-6 (Arabic)", "ISO-8859-7 (Greek)", "ISO-8859-8 (Hebrew)", "ISO-8859-9 (Latin-5)", "ISO-8859-10 (Latin-6)", "ISO-8859-13 (Latin-7)", "ISO-8859-14 (Latin-8)", "ISO-8859-15 (Latin-9)", "ISO-8859-16 (Latin-10)"]  # noqa: E501
        if not set(encodings).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `encodings` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(encodings) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._encodings = encodings

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
        if not isinstance(other, SettingsCharacterEncodingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
