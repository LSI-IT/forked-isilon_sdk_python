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


class S3SettingsGlobalSettings(object):
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
        'http_port': 'int',
        'https_only': 'bool',
        'https_port': 'int',
        'service': 'bool'
    }

    attribute_map = {
        'http_port': 'http_port',
        'https_only': 'https_only',
        'https_port': 'https_port',
        'service': 'service'
    }

    def __init__(self, http_port=None, https_only=None, https_port=None, service=None):  # noqa: E501
        """S3SettingsGlobalSettings - a model defined in Swagger"""  # noqa: E501

        self._http_port = None
        self._https_only = None
        self._https_port = None
        self._service = None
        self.discriminator = None

        if http_port is not None:
            self.http_port = http_port
        if https_only is not None:
            self.https_only = https_only
        if https_port is not None:
            self.https_port = https_port
        if service is not None:
            self.service = service

    @property
    def http_port(self):
        """Gets the http_port of this S3SettingsGlobalSettings.  # noqa: E501

        The port on which to listen for HTTP S3 requests.  # noqa: E501

        :return: The http_port of this S3SettingsGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this S3SettingsGlobalSettings.

        The port on which to listen for HTTP S3 requests.  # noqa: E501

        :param http_port: The http_port of this S3SettingsGlobalSettings.  # noqa: E501
        :type: int
        """
        if http_port is not None and http_port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `http_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if http_port is not None and http_port < 1024:  # noqa: E501
            raise ValueError("Invalid value for `http_port`, must be a value greater than or equal to `1024`")  # noqa: E501

        self._http_port = http_port

    @property
    def https_only(self):
        """Gets the https_only of this S3SettingsGlobalSettings.  # noqa: E501

        Indicates whether S3 service will accept only HTTPS request, or both HTTPS and HTTP.  # noqa: E501

        :return: The https_only of this S3SettingsGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._https_only

    @https_only.setter
    def https_only(self, https_only):
        """Sets the https_only of this S3SettingsGlobalSettings.

        Indicates whether S3 service will accept only HTTPS request, or both HTTPS and HTTP.  # noqa: E501

        :param https_only: The https_only of this S3SettingsGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._https_only = https_only

    @property
    def https_port(self):
        """Gets the https_port of this S3SettingsGlobalSettings.  # noqa: E501

        The port on which to listen for HTTPS S3 requests.  # noqa: E501

        :return: The https_port of this S3SettingsGlobalSettings.  # noqa: E501
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this S3SettingsGlobalSettings.

        The port on which to listen for HTTPS S3 requests.  # noqa: E501

        :param https_port: The https_port of this S3SettingsGlobalSettings.  # noqa: E501
        :type: int
        """
        if https_port is not None and https_port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `https_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if https_port is not None and https_port < 1024:  # noqa: E501
            raise ValueError("Invalid value for `https_port`, must be a value greater than or equal to `1024`")  # noqa: E501

        self._https_port = https_port

    @property
    def service(self):
        """Gets the service of this S3SettingsGlobalSettings.  # noqa: E501

        True if the S3 service is enabled.  When set to false, the S3 service is disabled.  # noqa: E501

        :return: The service of this S3SettingsGlobalSettings.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this S3SettingsGlobalSettings.

        True if the S3 service is enabled.  When set to false, the S3 service is disabled.  # noqa: E501

        :param service: The service of this S3SettingsGlobalSettings.  # noqa: E501
        :type: bool
        """

        self._service = service

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
        if not isinstance(other, S3SettingsGlobalSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
