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

from isilon_sdk.v9_5_0.models.datamover_account_credentials_cloud_proxy import DatamoverAccountCredentialsCloudProxy  # noqa: F401,E501


class DatamoverAccountCredentialsCloud(object):
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
        'proxy': 'DatamoverAccountCredentialsCloudProxy',
        'secret_key': 'str'
    }

    attribute_map = {
        'access_id': 'access_id',
        'proxy': 'proxy',
        'secret_key': 'secret_key'
    }

    def __init__(self, access_id=None, proxy=None, secret_key=None):  # noqa: E501
        """DatamoverAccountCredentialsCloud - a model defined in Swagger"""  # noqa: E501

        self._access_id = None
        self._proxy = None
        self._secret_key = None
        self.discriminator = None

        if access_id is not None:
            self.access_id = access_id
        if proxy is not None:
            self.proxy = proxy
        if secret_key is not None:
            self.secret_key = secret_key

    @property
    def access_id(self):
        """Gets the access_id of this DatamoverAccountCredentialsCloud.  # noqa: E501

        Access ID  # noqa: E501

        :return: The access_id of this DatamoverAccountCredentialsCloud.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this DatamoverAccountCredentialsCloud.

        Access ID  # noqa: E501

        :param access_id: The access_id of this DatamoverAccountCredentialsCloud.  # noqa: E501
        :type: str
        """
        if access_id is not None and len(access_id) > 255:
            raise ValueError("Invalid value for `access_id`, length must be less than or equal to `255`")  # noqa: E501
        if access_id is not None and len(access_id) < 1:
            raise ValueError("Invalid value for `access_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._access_id = access_id

    @property
    def proxy(self):
        """Gets the proxy of this DatamoverAccountCredentialsCloud.  # noqa: E501

        Proxy information for connection to cloud accounts  # noqa: E501

        :return: The proxy of this DatamoverAccountCredentialsCloud.  # noqa: E501
        :rtype: DatamoverAccountCredentialsCloudProxy
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this DatamoverAccountCredentialsCloud.

        Proxy information for connection to cloud accounts  # noqa: E501

        :param proxy: The proxy of this DatamoverAccountCredentialsCloud.  # noqa: E501
        :type: DatamoverAccountCredentialsCloudProxy
        """

        self._proxy = proxy

    @property
    def secret_key(self):
        """Gets the secret_key of this DatamoverAccountCredentialsCloud.  # noqa: E501

        Secret key  # noqa: E501

        :return: The secret_key of this DatamoverAccountCredentialsCloud.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this DatamoverAccountCredentialsCloud.

        Secret key  # noqa: E501

        :param secret_key: The secret_key of this DatamoverAccountCredentialsCloud.  # noqa: E501
        :type: str
        """
        if secret_key is not None and len(secret_key) > 255:
            raise ValueError("Invalid value for `secret_key`, length must be less than or equal to `255`")  # noqa: E501
        if secret_key is not None and len(secret_key) < 1:
            raise ValueError("Invalid value for `secret_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._secret_key = secret_key

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
        if not isinstance(other, DatamoverAccountCredentialsCloud):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
