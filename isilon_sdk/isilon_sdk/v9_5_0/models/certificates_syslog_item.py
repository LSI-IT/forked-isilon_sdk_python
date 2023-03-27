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


class CertificatesSyslogItem(object):
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
        'certificate_key_password': 'str',
        'certificate_key_path': 'str',
        'certificate_path': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'certificate_key_password': 'certificate_key_password',
        'certificate_key_path': 'certificate_key_path',
        'certificate_path': 'certificate_path',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, certificate_key_password=None, certificate_key_path=None, certificate_path=None, description=None, name=None):  # noqa: E501
        """CertificatesSyslogItem - a model defined in Swagger"""  # noqa: E501

        self._certificate_key_password = None
        self._certificate_key_path = None
        self._certificate_path = None
        self._description = None
        self._name = None
        self.discriminator = None

        if certificate_key_password is not None:
            self.certificate_key_password = certificate_key_password
        self.certificate_key_path = certificate_key_path
        self.certificate_path = certificate_path
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def certificate_key_password(self):
        """Gets the certificate_key_password of this CertificatesSyslogItem.  # noqa: E501

        Optional private key password.   # noqa: E501

        :return: The certificate_key_password of this CertificatesSyslogItem.  # noqa: E501
        :rtype: str
        """
        return self._certificate_key_password

    @certificate_key_password.setter
    def certificate_key_password(self, certificate_key_password):
        """Sets the certificate_key_password of this CertificatesSyslogItem.

        Optional private key password.   # noqa: E501

        :param certificate_key_password: The certificate_key_password of this CertificatesSyslogItem.  # noqa: E501
        :type: str
        """
        if certificate_key_password is not None and len(certificate_key_password) > 256:
            raise ValueError("Invalid value for `certificate_key_password`, length must be less than or equal to `256`")  # noqa: E501
        if certificate_key_password is not None and len(certificate_key_password) < 1:
            raise ValueError("Invalid value for `certificate_key_password`, length must be greater than or equal to `1`")  # noqa: E501

        self._certificate_key_password = certificate_key_password

    @property
    def certificate_key_path(self):
        """Gets the certificate_key_path of this CertificatesSyslogItem.  # noqa: E501

        Local path to the certificate key that is to be imported.  # noqa: E501

        :return: The certificate_key_path of this CertificatesSyslogItem.  # noqa: E501
        :rtype: str
        """
        return self._certificate_key_path

    @certificate_key_path.setter
    def certificate_key_path(self, certificate_key_path):
        """Sets the certificate_key_path of this CertificatesSyslogItem.

        Local path to the certificate key that is to be imported.  # noqa: E501

        :param certificate_key_path: The certificate_key_path of this CertificatesSyslogItem.  # noqa: E501
        :type: str
        """
        if certificate_key_path is None:
            raise ValueError("Invalid value for `certificate_key_path`, must not be `None`")  # noqa: E501
        if certificate_key_path is not None and len(certificate_key_path) > 1024:
            raise ValueError("Invalid value for `certificate_key_path`, length must be less than or equal to `1024`")  # noqa: E501
        if certificate_key_path is not None and len(certificate_key_path) < 1:
            raise ValueError("Invalid value for `certificate_key_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._certificate_key_path = certificate_key_path

    @property
    def certificate_path(self):
        """Gets the certificate_path of this CertificatesSyslogItem.  # noqa: E501

        Local path to the certificate that is to be imported.  # noqa: E501

        :return: The certificate_path of this CertificatesSyslogItem.  # noqa: E501
        :rtype: str
        """
        return self._certificate_path

    @certificate_path.setter
    def certificate_path(self, certificate_path):
        """Sets the certificate_path of this CertificatesSyslogItem.

        Local path to the certificate that is to be imported.  # noqa: E501

        :param certificate_path: The certificate_path of this CertificatesSyslogItem.  # noqa: E501
        :type: str
        """
        if certificate_path is None:
            raise ValueError("Invalid value for `certificate_path`, must not be `None`")  # noqa: E501
        if certificate_path is not None and len(certificate_path) > 1024:
            raise ValueError("Invalid value for `certificate_path`, length must be less than or equal to `1024`")  # noqa: E501
        if certificate_path is not None and len(certificate_path) < 1:
            raise ValueError("Invalid value for `certificate_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._certificate_path = certificate_path

    @property
    def description(self):
        """Gets the description of this CertificatesSyslogItem.  # noqa: E501

        Description field associated with a certificate provided for administrative convenience.  # noqa: E501

        :return: The description of this CertificatesSyslogItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CertificatesSyslogItem.

        Description field associated with a certificate provided for administrative convenience.  # noqa: E501

        :param description: The description of this CertificatesSyslogItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 2048:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `2048`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this CertificatesSyslogItem.  # noqa: E501

        Administrator specified name identifier.  # noqa: E501

        :return: The name of this CertificatesSyslogItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CertificatesSyslogItem.

        Administrator specified name identifier.  # noqa: E501

        :param name: The name of this CertificatesSyslogItem.  # noqa: E501
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
        if not isinstance(other, CertificatesSyslogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
