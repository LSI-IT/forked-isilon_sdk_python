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


class CreateS3KeyResponseKeys(object):
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
        'access_id': 'str',
        'old_key_expiry': 'int',
        'old_key_timestamp': 'int',
        'old_secret_key': 'str',
        'secret_key': 'str',
        'secret_key_timestamp': 'int'
    }

    attribute_map = {
        'access_id': 'access_id',
        'old_key_expiry': 'old_key_expiry',
        'old_key_timestamp': 'old_key_timestamp',
        'old_secret_key': 'old_secret_key',
        'secret_key': 'secret_key',
        'secret_key_timestamp': 'secret_key_timestamp'
    }

    def __init__(self, access_id=None, old_key_expiry=None, old_key_timestamp=None, old_secret_key=None, secret_key=None, secret_key_timestamp=None):  # noqa: E501
        """CreateS3KeyResponseKeys - a model defined in Swagger"""  # noqa: E501

        self._access_id = None
        self._old_key_expiry = None
        self._old_key_timestamp = None
        self._old_secret_key = None
        self._secret_key = None
        self._secret_key_timestamp = None
        self.discriminator = None

        if access_id is not None:
            self.access_id = access_id
        if old_key_expiry is not None:
            self.old_key_expiry = old_key_expiry
        if old_key_timestamp is not None:
            self.old_key_timestamp = old_key_timestamp
        if old_secret_key is not None:
            self.old_secret_key = old_secret_key
        if secret_key is not None:
            self.secret_key = secret_key
        if secret_key_timestamp is not None:
            self.secret_key_timestamp = secret_key_timestamp

    @property
    def access_id(self):
        """Gets the access_id of this CreateS3KeyResponseKeys.  # noqa: E501

        S3 Access ID  # noqa: E501

        :return: The access_id of this CreateS3KeyResponseKeys.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this CreateS3KeyResponseKeys.

        S3 Access ID  # noqa: E501

        :param access_id: The access_id of this CreateS3KeyResponseKeys.  # noqa: E501
        :type: str
        """
        if access_id is not None and len(access_id) > 272:
            raise ValueError("Invalid value for `access_id`, length must be less than or equal to `272`")  # noqa: E501
        if access_id is not None and len(access_id) < 9:
            raise ValueError("Invalid value for `access_id`, length must be greater than or equal to `9`")  # noqa: E501

        self._access_id = access_id

    @property
    def old_key_expiry(self):
        """Gets the old_key_expiry of this CreateS3KeyResponseKeys.  # noqa: E501

        Time that previous secret key will expire, in format YYYY-MM-DD HH:MM:SS  # noqa: E501

        :return: The old_key_expiry of this CreateS3KeyResponseKeys.  # noqa: E501
        :rtype: int
        """
        return self._old_key_expiry

    @old_key_expiry.setter
    def old_key_expiry(self, old_key_expiry):
        """Sets the old_key_expiry of this CreateS3KeyResponseKeys.

        Time that previous secret key will expire, in format YYYY-MM-DD HH:MM:SS  # noqa: E501

        :param old_key_expiry: The old_key_expiry of this CreateS3KeyResponseKeys.  # noqa: E501
        :type: int
        """

        self._old_key_expiry = old_key_expiry

    @property
    def old_key_timestamp(self):
        """Gets the old_key_timestamp of this CreateS3KeyResponseKeys.  # noqa: E501

        Time that previous secret key was created, in format YYYY-MM-DD HH:MM:SS  # noqa: E501

        :return: The old_key_timestamp of this CreateS3KeyResponseKeys.  # noqa: E501
        :rtype: int
        """
        return self._old_key_timestamp

    @old_key_timestamp.setter
    def old_key_timestamp(self, old_key_timestamp):
        """Sets the old_key_timestamp of this CreateS3KeyResponseKeys.

        Time that previous secret key was created, in format YYYY-MM-DD HH:MM:SS  # noqa: E501

        :param old_key_timestamp: The old_key_timestamp of this CreateS3KeyResponseKeys.  # noqa: E501
        :type: int
        """

        self._old_key_timestamp = old_key_timestamp

    @property
    def old_secret_key(self):
        """Gets the old_secret_key of this CreateS3KeyResponseKeys.  # noqa: E501

        Previous secret key  # noqa: E501

        :return: The old_secret_key of this CreateS3KeyResponseKeys.  # noqa: E501
        :rtype: str
        """
        return self._old_secret_key

    @old_secret_key.setter
    def old_secret_key(self, old_secret_key):
        """Sets the old_secret_key of this CreateS3KeyResponseKeys.

        Previous secret key  # noqa: E501

        :param old_secret_key: The old_secret_key of this CreateS3KeyResponseKeys.  # noqa: E501
        :type: str
        """
        if old_secret_key is not None and len(old_secret_key) > 255:
            raise ValueError("Invalid value for `old_secret_key`, length must be less than or equal to `255`")  # noqa: E501
        if old_secret_key is not None and len(old_secret_key) < 1:
            raise ValueError("Invalid value for `old_secret_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._old_secret_key = old_secret_key

    @property
    def secret_key(self):
        """Gets the secret_key of this CreateS3KeyResponseKeys.  # noqa: E501

        Secret key  # noqa: E501

        :return: The secret_key of this CreateS3KeyResponseKeys.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this CreateS3KeyResponseKeys.

        Secret key  # noqa: E501

        :param secret_key: The secret_key of this CreateS3KeyResponseKeys.  # noqa: E501
        :type: str
        """
        if secret_key is not None and len(secret_key) > 255:
            raise ValueError("Invalid value for `secret_key`, length must be less than or equal to `255`")  # noqa: E501
        if secret_key is not None and len(secret_key) < 1:
            raise ValueError("Invalid value for `secret_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._secret_key = secret_key

    @property
    def secret_key_timestamp(self):
        """Gets the secret_key_timestamp of this CreateS3KeyResponseKeys.  # noqa: E501

        Time that secret key was created, in format YYYY-MM-DD HH:MM:SS  # noqa: E501

        :return: The secret_key_timestamp of this CreateS3KeyResponseKeys.  # noqa: E501
        :rtype: int
        """
        return self._secret_key_timestamp

    @secret_key_timestamp.setter
    def secret_key_timestamp(self, secret_key_timestamp):
        """Sets the secret_key_timestamp of this CreateS3KeyResponseKeys.

        Time that secret key was created, in format YYYY-MM-DD HH:MM:SS  # noqa: E501

        :param secret_key_timestamp: The secret_key_timestamp of this CreateS3KeyResponseKeys.  # noqa: E501
        :type: int
        """

        self._secret_key_timestamp = secret_key_timestamp

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
        if not isinstance(other, CreateS3KeyResponseKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
