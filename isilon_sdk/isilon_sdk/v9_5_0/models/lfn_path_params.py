# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 16
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LfnPathParams(object):
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
        'max_bytes': 'int',
        'max_chars': 'int',
        'path': 'str',
        'policy': 'str'
    }

    attribute_map = {
        'max_bytes': 'max_bytes',
        'max_chars': 'max_chars',
        'path': 'path',
        'policy': 'policy'
    }

    def __init__(self, max_bytes=None, max_chars=None, path=None, policy=None):  # noqa: E501
        """LfnPathParams - a model defined in Swagger"""  # noqa: E501

        self._max_bytes = None
        self._max_chars = None
        self._path = None
        self._policy = None
        self.discriminator = None

        if max_bytes is not None:
            self.max_bytes = max_bytes
        if max_chars is not None:
            self.max_chars = max_chars
        if path is not None:
            self.path = path
        if policy is not None:
            self.policy = policy

    @property
    def max_bytes(self):
        """Gets the max_bytes of this LfnPathParams.  # noqa: E501

        Specifies the maximum number of bytes the UTF-8 encoded filename can have. This may be more than the character limit as a single character could require up to 4 bytes to be encoded.  # noqa: E501

        :return: The max_bytes of this LfnPathParams.  # noqa: E501
        :rtype: int
        """
        return self._max_bytes

    @max_bytes.setter
    def max_bytes(self, max_bytes):
        """Sets the max_bytes of this LfnPathParams.

        Specifies the maximum number of bytes the UTF-8 encoded filename can have. This may be more than the character limit as a single character could require up to 4 bytes to be encoded.  # noqa: E501

        :param max_bytes: The max_bytes of this LfnPathParams.  # noqa: E501
        :type: int
        """
        if max_bytes is not None and max_bytes > 1024:  # noqa: E501
            raise ValueError("Invalid value for `max_bytes`, must be a value less than or equal to `1024`")  # noqa: E501
        if max_bytes is not None and max_bytes < 255:  # noqa: E501
            raise ValueError("Invalid value for `max_bytes`, must be a value greater than or equal to `255`")  # noqa: E501

        self._max_bytes = max_bytes

    @property
    def max_chars(self):
        """Gets the max_chars of this LfnPathParams.  # noqa: E501

        Specifies the maximum number of characters a filename can have. Each character will require between 1 and 4 bytes to encode.  # noqa: E501

        :return: The max_chars of this LfnPathParams.  # noqa: E501
        :rtype: int
        """
        return self._max_chars

    @max_chars.setter
    def max_chars(self, max_chars):
        """Sets the max_chars of this LfnPathParams.

        Specifies the maximum number of characters a filename can have. Each character will require between 1 and 4 bytes to encode.  # noqa: E501

        :param max_chars: The max_chars of this LfnPathParams.  # noqa: E501
        :type: int
        """
        if max_chars is not None and max_chars > 1024:  # noqa: E501
            raise ValueError("Invalid value for `max_chars`, must be a value less than or equal to `1024`")  # noqa: E501
        if max_chars is not None and max_chars < 255:  # noqa: E501
            raise ValueError("Invalid value for `max_chars`, must be a value greater than or equal to `255`")  # noqa: E501

        self._max_chars = max_chars

    @property
    def path(self):
        """Gets the path of this LfnPathParams.  # noqa: E501


        :return: The path of this LfnPathParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LfnPathParams.


        :param path: The path of this LfnPathParams.  # noqa: E501
        :type: str
        """
        if path is not None and len(path) > 4096:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if path is not None and len(path) < 4:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `4`")  # noqa: E501
        if path is not None and not re.search('^\/ifs$|^\/ifs\/', path):  # noqa: E501
            raise ValueError("Invalid value for `path`, must be a follow pattern or equal to `/^\/ifs$|^\/ifs\//`")  # noqa: E501

        self._path = path

    @property
    def policy(self):
        """Gets the policy of this LfnPathParams.  # noqa: E501

        Specifies the name length policy for bytes and chars.  # noqa: E501

        :return: The policy of this LfnPathParams.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this LfnPathParams.

        Specifies the name length policy for bytes and chars.  # noqa: E501

        :param policy: The policy of this LfnPathParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["restricted", "full", "custom"]  # noqa: E501
        if policy not in allowed_values:
            raise ValueError(
                "Invalid value for `policy` ({0}), must be one of {1}"  # noqa: E501
                .format(policy, allowed_values)
            )

        self._policy = policy

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
        if not isinstance(other, LfnPathParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
