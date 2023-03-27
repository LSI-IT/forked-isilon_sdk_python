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


class CertificateSettingsExtended(object):
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
        'certificate_monitor_enabled': 'bool',
        'certificate_pre_expiration_threshold': 'int',
        'default_https_certificate': 'str'
    }

    attribute_map = {
        'certificate_monitor_enabled': 'certificate_monitor_enabled',
        'certificate_pre_expiration_threshold': 'certificate_pre_expiration_threshold',
        'default_https_certificate': 'default_https_certificate'
    }

    def __init__(self, certificate_monitor_enabled=None, certificate_pre_expiration_threshold=None, default_https_certificate=None):  # noqa: E501
        """CertificateSettingsExtended - a model defined in Swagger"""  # noqa: E501

        self._certificate_monitor_enabled = None
        self._certificate_pre_expiration_threshold = None
        self._default_https_certificate = None
        self.discriminator = None

        if certificate_monitor_enabled is not None:
            self.certificate_monitor_enabled = certificate_monitor_enabled
        if certificate_pre_expiration_threshold is not None:
            self.certificate_pre_expiration_threshold = certificate_pre_expiration_threshold
        if default_https_certificate is not None:
            self.default_https_certificate = default_https_certificate

    @property
    def certificate_monitor_enabled(self):
        """Gets the certificate_monitor_enabled of this CertificateSettingsExtended.  # noqa: E501

        Boolean value indicating whether certificate expiration monitoring is enabled.  # noqa: E501

        :return: The certificate_monitor_enabled of this CertificateSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._certificate_monitor_enabled

    @certificate_monitor_enabled.setter
    def certificate_monitor_enabled(self, certificate_monitor_enabled):
        """Sets the certificate_monitor_enabled of this CertificateSettingsExtended.

        Boolean value indicating whether certificate expiration monitoring is enabled.  # noqa: E501

        :param certificate_monitor_enabled: The certificate_monitor_enabled of this CertificateSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._certificate_monitor_enabled = certificate_monitor_enabled

    @property
    def certificate_pre_expiration_threshold(self):
        """Gets the certificate_pre_expiration_threshold of this CertificateSettingsExtended.  # noqa: E501

        The number of seconds before certificate expiration that the certificate expiration monitor will start raising alerts.  # noqa: E501

        :return: The certificate_pre_expiration_threshold of this CertificateSettingsExtended.  # noqa: E501
        :rtype: int
        """
        return self._certificate_pre_expiration_threshold

    @certificate_pre_expiration_threshold.setter
    def certificate_pre_expiration_threshold(self, certificate_pre_expiration_threshold):
        """Sets the certificate_pre_expiration_threshold of this CertificateSettingsExtended.

        The number of seconds before certificate expiration that the certificate expiration monitor will start raising alerts.  # noqa: E501

        :param certificate_pre_expiration_threshold: The certificate_pre_expiration_threshold of this CertificateSettingsExtended.  # noqa: E501
        :type: int
        """
        if certificate_pre_expiration_threshold is not None and certificate_pre_expiration_threshold > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `certificate_pre_expiration_threshold`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if certificate_pre_expiration_threshold is not None and certificate_pre_expiration_threshold < 0:  # noqa: E501
            raise ValueError("Invalid value for `certificate_pre_expiration_threshold`, must be a value greater than or equal to `0`")  # noqa: E501

        self._certificate_pre_expiration_threshold = certificate_pre_expiration_threshold

    @property
    def default_https_certificate(self):
        """Gets the default_https_certificate of this CertificateSettingsExtended.  # noqa: E501

        ID of the server certificate to be used as the default HTTPS certificate.  # noqa: E501

        :return: The default_https_certificate of this CertificateSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._default_https_certificate

    @default_https_certificate.setter
    def default_https_certificate(self, default_https_certificate):
        """Sets the default_https_certificate of this CertificateSettingsExtended.

        ID of the server certificate to be used as the default HTTPS certificate.  # noqa: E501

        :param default_https_certificate: The default_https_certificate of this CertificateSettingsExtended.  # noqa: E501
        :type: str
        """
        if default_https_certificate is not None and len(default_https_certificate) > 512:
            raise ValueError("Invalid value for `default_https_certificate`, length must be less than or equal to `512`")  # noqa: E501
        if default_https_certificate is not None and len(default_https_certificate) < 1:
            raise ValueError("Invalid value for `default_https_certificate`, length must be greater than or equal to `1`")  # noqa: E501

        self._default_https_certificate = default_https_certificate

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
        if not isinstance(other, CertificateSettingsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
