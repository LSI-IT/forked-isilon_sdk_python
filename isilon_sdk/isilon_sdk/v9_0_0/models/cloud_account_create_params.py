# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_0_0.models.cloud_account_credential_provider import CloudAccountCredentialProvider  # noqa: F401,E501


class CloudAccountCreateParams(object):
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
        'account_id': 'str',
        'account_username': 'str',
        'birth_cluster_id': 'str',
        'credential_provider': 'CloudAccountCredentialProvider',
        'enable_ocsp': 'bool',
        'enabled': 'bool',
        'key': 'str',
        'name': 'str',
        'ocsp_responder_url_required': 'bool',
        'proxy': 'str',
        'skip_ssl_validation': 'bool',
        'storage_region': 'str',
        'telemetry_bucket': 'str',
        'type': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_username': 'account_username',
        'birth_cluster_id': 'birth_cluster_id',
        'credential_provider': 'credential_provider',
        'enable_ocsp': 'enable_ocsp',
        'enabled': 'enabled',
        'key': 'key',
        'name': 'name',
        'ocsp_responder_url_required': 'ocsp_responder_url_required',
        'proxy': 'proxy',
        'skip_ssl_validation': 'skip_ssl_validation',
        'storage_region': 'storage_region',
        'telemetry_bucket': 'telemetry_bucket',
        'type': 'type',
        'uri': 'uri'
    }

    def __init__(self, account_id=None, account_username=None, birth_cluster_id=None, credential_provider=None, enable_ocsp=None, enabled=None, key=None, name=None, ocsp_responder_url_required=None, proxy=None, skip_ssl_validation=None, storage_region=None, telemetry_bucket=None, type=None, uri=None):  # noqa: E501
        """CloudAccountCreateParams - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._account_username = None
        self._birth_cluster_id = None
        self._credential_provider = None
        self._enable_ocsp = None
        self._enabled = None
        self._key = None
        self._name = None
        self._ocsp_responder_url_required = None
        self._proxy = None
        self._skip_ssl_validation = None
        self._storage_region = None
        self._telemetry_bucket = None
        self._type = None
        self._uri = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_username is not None:
            self.account_username = account_username
        if birth_cluster_id is not None:
            self.birth_cluster_id = birth_cluster_id
        if credential_provider is not None:
            self.credential_provider = credential_provider
        if enable_ocsp is not None:
            self.enable_ocsp = enable_ocsp
        if enabled is not None:
            self.enabled = enabled
        if key is not None:
            self.key = key
        self.name = name
        if ocsp_responder_url_required is not None:
            self.ocsp_responder_url_required = ocsp_responder_url_required
        if proxy is not None:
            self.proxy = proxy
        if skip_ssl_validation is not None:
            self.skip_ssl_validation = skip_ssl_validation
        if storage_region is not None:
            self.storage_region = storage_region
        if telemetry_bucket is not None:
            self.telemetry_bucket = telemetry_bucket
        self.type = type
        self.uri = uri

    @property
    def account_id(self):
        """Gets the account_id of this CloudAccountCreateParams.  # noqa: E501

        (S3 only) The user id of the S3 account  # noqa: E501

        :return: The account_id of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CloudAccountCreateParams.

        (S3 only) The user id of the S3 account  # noqa: E501

        :param account_id: The account_id of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_username(self):
        """Gets the account_username of this CloudAccountCreateParams.  # noqa: E501

        The username required to authenticate against the cloud service  # noqa: E501

        :return: The account_username of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._account_username

    @account_username.setter
    def account_username(self, account_username):
        """Sets the account_username of this CloudAccountCreateParams.

        The username required to authenticate against the cloud service  # noqa: E501

        :param account_username: The account_username of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """
        if account_username is not None and len(account_username) > 256:
            raise ValueError("Invalid value for `account_username`, length must be less than or equal to `256`")  # noqa: E501
        if account_username is not None and len(account_username) < 0:
            raise ValueError("Invalid value for `account_username`, length must be greater than or equal to `0`")  # noqa: E501

        self._account_username = account_username

    @property
    def birth_cluster_id(self):
        """Gets the birth_cluster_id of this CloudAccountCreateParams.  # noqa: E501

        The guid of the cluster where this account was created  # noqa: E501

        :return: The birth_cluster_id of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """Sets the birth_cluster_id of this CloudAccountCreateParams.

        The guid of the cluster where this account was created  # noqa: E501

        :param birth_cluster_id: The birth_cluster_id of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """
        if birth_cluster_id is not None and len(birth_cluster_id) > 255:
            raise ValueError("Invalid value for `birth_cluster_id`, length must be less than or equal to `255`")  # noqa: E501
        if birth_cluster_id is not None and len(birth_cluster_id) < 0:
            raise ValueError("Invalid value for `birth_cluster_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._birth_cluster_id = birth_cluster_id

    @property
    def credential_provider(self):
        """Gets the credential_provider of this CloudAccountCreateParams.  # noqa: E501

          # noqa: E501

        :return: The credential_provider of this CloudAccountCreateParams.  # noqa: E501
        :rtype: CloudAccountCredentialProvider
        """
        return self._credential_provider

    @credential_provider.setter
    def credential_provider(self, credential_provider):
        """Sets the credential_provider of this CloudAccountCreateParams.

          # noqa: E501

        :param credential_provider: The credential_provider of this CloudAccountCreateParams.  # noqa: E501
        :type: CloudAccountCredentialProvider
        """

        self._credential_provider = credential_provider

    @property
    def enable_ocsp(self):
        """Gets the enable_ocsp of this CloudAccountCreateParams.  # noqa: E501

        (C2S-S3 only) Indicates whether to use OCSP to check the revocation status of the authentication certificate  # noqa: E501

        :return: The enable_ocsp of this CloudAccountCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ocsp

    @enable_ocsp.setter
    def enable_ocsp(self, enable_ocsp):
        """Sets the enable_ocsp of this CloudAccountCreateParams.

        (C2S-S3 only) Indicates whether to use OCSP to check the revocation status of the authentication certificate  # noqa: E501

        :param enable_ocsp: The enable_ocsp of this CloudAccountCreateParams.  # noqa: E501
        :type: bool
        """

        self._enable_ocsp = enable_ocsp

    @property
    def enabled(self):
        """Gets the enabled of this CloudAccountCreateParams.  # noqa: E501

        Whether this account is explicitly enabled or disabled by a user  # noqa: E501

        :return: The enabled of this CloudAccountCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CloudAccountCreateParams.

        Whether this account is explicitly enabled or disabled by a user  # noqa: E501

        :param enabled: The enabled of this CloudAccountCreateParams.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def key(self):
        """Gets the key of this CloudAccountCreateParams.  # noqa: E501

        A valid authentication key for connecting to the cloud  # noqa: E501

        :return: The key of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CloudAccountCreateParams.

        A valid authentication key for connecting to the cloud  # noqa: E501

        :param key: The key of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """
        if key is not None and len(key) > 256:
            raise ValueError("Invalid value for `key`, length must be less than or equal to `256`")  # noqa: E501
        if key is not None and len(key) < 0:
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `0`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this CloudAccountCreateParams.  # noqa: E501

        A unique name for this account  # noqa: E501

        :return: The name of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccountCreateParams.

        A unique name for this account  # noqa: E501

        :param name: The name of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 768:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `768`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def ocsp_responder_url_required(self):
        """Gets the ocsp_responder_url_required of this CloudAccountCreateParams.  # noqa: E501

        (C2S-S3 only) Determines whether a certificate without an OCSP responder URL is considered valid or not  # noqa: E501

        :return: The ocsp_responder_url_required of this CloudAccountCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._ocsp_responder_url_required

    @ocsp_responder_url_required.setter
    def ocsp_responder_url_required(self, ocsp_responder_url_required):
        """Sets the ocsp_responder_url_required of this CloudAccountCreateParams.

        (C2S-S3 only) Determines whether a certificate without an OCSP responder URL is considered valid or not  # noqa: E501

        :param ocsp_responder_url_required: The ocsp_responder_url_required of this CloudAccountCreateParams.  # noqa: E501
        :type: bool
        """

        self._ocsp_responder_url_required = ocsp_responder_url_required

    @property
    def proxy(self):
        """Gets the proxy of this CloudAccountCreateParams.  # noqa: E501

        The id or name of a proxy to be used by this account  # noqa: E501

        :return: The proxy of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CloudAccountCreateParams.

        The id or name of a proxy to be used by this account  # noqa: E501

        :param proxy: The proxy of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def skip_ssl_validation(self):
        """Gets the skip_ssl_validation of this CloudAccountCreateParams.  # noqa: E501

        Indicates whether to skip peer verification of SSL certificates when connecting to the cloud  # noqa: E501

        :return: The skip_ssl_validation of this CloudAccountCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._skip_ssl_validation

    @skip_ssl_validation.setter
    def skip_ssl_validation(self, skip_ssl_validation):
        """Sets the skip_ssl_validation of this CloudAccountCreateParams.

        Indicates whether to skip peer verification of SSL certificates when connecting to the cloud  # noqa: E501

        :param skip_ssl_validation: The skip_ssl_validation of this CloudAccountCreateParams.  # noqa: E501
        :type: bool
        """

        self._skip_ssl_validation = skip_ssl_validation

    @property
    def storage_region(self):
        """Gets the storage_region of this CloudAccountCreateParams.  # noqa: E501

        An appropriate region for the account as defined by the cloud service provider.  For example, faster access times may be gained by referencing a nearby region  # noqa: E501

        :return: The storage_region of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._storage_region

    @storage_region.setter
    def storage_region(self, storage_region):
        """Sets the storage_region of this CloudAccountCreateParams.

        An appropriate region for the account as defined by the cloud service provider.  For example, faster access times may be gained by referencing a nearby region  # noqa: E501

        :param storage_region: The storage_region of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """

        self._storage_region = storage_region

    @property
    def telemetry_bucket(self):
        """Gets the telemetry_bucket of this CloudAccountCreateParams.  # noqa: E501

        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider  # noqa: E501

        :return: The telemetry_bucket of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._telemetry_bucket

    @telemetry_bucket.setter
    def telemetry_bucket(self, telemetry_bucket):
        """Sets the telemetry_bucket of this CloudAccountCreateParams.

        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider  # noqa: E501

        :param telemetry_bucket: The telemetry_bucket of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """
        if telemetry_bucket is not None and len(telemetry_bucket) > 255:
            raise ValueError("Invalid value for `telemetry_bucket`, length must be less than or equal to `255`")  # noqa: E501
        if telemetry_bucket is not None and len(telemetry_bucket) < 0:
            raise ValueError("Invalid value for `telemetry_bucket`, length must be greater than or equal to `0`")  # noqa: E501

        self._telemetry_bucket = telemetry_bucket

    @property
    def type(self):
        """Gets the type of this CloudAccountCreateParams.  # noqa: E501

        The type of cloud protocol required.  E.g., \"isilon\" for Dell EMC PowerScale, \"ecs\" for Dell EMC ECS Appliance, \"virtustream\" for Virtustream Storage Cloud, \"azure\" for Microsoft Azure, \"s3\" for Amazon S3, \"c2s-s3\" for Amazon Commercial Cloud Services S3 and \"google\" for Google Cloud Platform and \"alibaba-cloud\" for Alibaba Cloud  # noqa: E501

        :return: The type of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudAccountCreateParams.

        The type of cloud protocol required.  E.g., \"isilon\" for Dell EMC PowerScale, \"ecs\" for Dell EMC ECS Appliance, \"virtustream\" for Virtustream Storage Cloud, \"azure\" for Microsoft Azure, \"s3\" for Amazon S3, \"c2s-s3\" for Amazon Commercial Cloud Services S3 and \"google\" for Google Cloud Platform and \"alibaba-cloud\" for Alibaba Cloud  # noqa: E501

        :param type: The type of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["isilon", "ecs", "virtustream", "azure", "s3", "c2s-s3", "google", "alibaba-cloud"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this CloudAccountCreateParams.  # noqa: E501

        A valid URI pointing to the location of the cloud storage  # noqa: E501

        :return: The uri of this CloudAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CloudAccountCreateParams.

        A valid URI pointing to the location of the cloud storage  # noqa: E501

        :param uri: The uri of this CloudAccountCreateParams.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501
        if uri is not None and len(uri) > 2048:
            raise ValueError("Invalid value for `uri`, length must be less than or equal to `2048`")  # noqa: E501
        if uri is not None and len(uri) < 0:
            raise ValueError("Invalid value for `uri`, length must be greater than or equal to `0`")  # noqa: E501

        self._uri = uri

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
        if not isinstance(other, CloudAccountCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
