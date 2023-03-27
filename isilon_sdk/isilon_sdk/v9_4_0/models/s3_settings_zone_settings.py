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


class S3SettingsZoneSettings(object):
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
        'base_domain': 'str',
        'bucket_directory_create_mode': 'int',
        'object_acl_policy': 'str',
        'root_path': 'str',
        'use_md5_for_etag': 'bool',
        'validate_content_md5': 'bool'
    }

    attribute_map = {
        'base_domain': 'base_domain',
        'bucket_directory_create_mode': 'bucket_directory_create_mode',
        'object_acl_policy': 'object_acl_policy',
        'root_path': 'root_path',
        'use_md5_for_etag': 'use_md5_for_etag',
        'validate_content_md5': 'validate_content_md5'
    }

    def __init__(self, base_domain=None, bucket_directory_create_mode=None, object_acl_policy=None, root_path=None, use_md5_for_etag=None, validate_content_md5=None):  # noqa: E501
        """S3SettingsZoneSettings - a model defined in Swagger"""  # noqa: E501

        self._base_domain = None
        self._bucket_directory_create_mode = None
        self._object_acl_policy = None
        self._root_path = None
        self._use_md5_for_etag = None
        self._validate_content_md5 = None
        self.discriminator = None

        if base_domain is not None:
            self.base_domain = base_domain
        if bucket_directory_create_mode is not None:
            self.bucket_directory_create_mode = bucket_directory_create_mode
        if object_acl_policy is not None:
            self.object_acl_policy = object_acl_policy
        if root_path is not None:
            self.root_path = root_path
        if use_md5_for_etag is not None:
            self.use_md5_for_etag = use_md5_for_etag
        if validate_content_md5 is not None:
            self.validate_content_md5 = validate_content_md5

    @property
    def base_domain(self):
        """Gets the base_domain of this S3SettingsZoneSettings.  # noqa: E501

        Specifies the S3 base domain name.  # noqa: E501

        :return: The base_domain of this S3SettingsZoneSettings.  # noqa: E501
        :rtype: str
        """
        return self._base_domain

    @base_domain.setter
    def base_domain(self, base_domain):
        """Sets the base_domain of this S3SettingsZoneSettings.

        Specifies the S3 base domain name.  # noqa: E501

        :param base_domain: The base_domain of this S3SettingsZoneSettings.  # noqa: E501
        :type: str
        """
        if base_domain is not None and len(base_domain) > 255:
            raise ValueError("Invalid value for `base_domain`, length must be less than or equal to `255`")  # noqa: E501
        if base_domain is not None and len(base_domain) < 0:
            raise ValueError("Invalid value for `base_domain`, length must be greater than or equal to `0`")  # noqa: E501
        if base_domain is not None and not re.search('^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$', base_domain):  # noqa: E501
            raise ValueError("Invalid value for `base_domain`, must be a follow pattern or equal to `/^$|^((([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])(\\.([a-zA-Z0-9_][a-zA-Z0-9-]{0,61})?[a-zA-Z0-9])*)$/`")  # noqa: E501

        self._base_domain = base_domain

    @property
    def bucket_directory_create_mode(self):
        """Gets the bucket_directory_create_mode of this S3SettingsZoneSettings.  # noqa: E501

        Create bucket directory with this permission mode  # noqa: E501

        :return: The bucket_directory_create_mode of this S3SettingsZoneSettings.  # noqa: E501
        :rtype: int
        """
        return self._bucket_directory_create_mode

    @bucket_directory_create_mode.setter
    def bucket_directory_create_mode(self, bucket_directory_create_mode):
        """Sets the bucket_directory_create_mode of this S3SettingsZoneSettings.

        Create bucket directory with this permission mode  # noqa: E501

        :param bucket_directory_create_mode: The bucket_directory_create_mode of this S3SettingsZoneSettings.  # noqa: E501
        :type: int
        """
        if bucket_directory_create_mode is not None and bucket_directory_create_mode > 511:  # noqa: E501
            raise ValueError("Invalid value for `bucket_directory_create_mode`, must be a value less than or equal to `511`")  # noqa: E501
        if bucket_directory_create_mode is not None and bucket_directory_create_mode < 0:  # noqa: E501
            raise ValueError("Invalid value for `bucket_directory_create_mode`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bucket_directory_create_mode = bucket_directory_create_mode

    @property
    def object_acl_policy(self):
        """Gets the object_acl_policy of this S3SettingsZoneSettings.  # noqa: E501

        Default object ACL policy for S3 Buckets.  # noqa: E501

        :return: The object_acl_policy of this S3SettingsZoneSettings.  # noqa: E501
        :rtype: str
        """
        return self._object_acl_policy

    @object_acl_policy.setter
    def object_acl_policy(self, object_acl_policy):
        """Sets the object_acl_policy of this S3SettingsZoneSettings.

        Default object ACL policy for S3 Buckets.  # noqa: E501

        :param object_acl_policy: The object_acl_policy of this S3SettingsZoneSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["replace", "deny"]  # noqa: E501
        if object_acl_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `object_acl_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(object_acl_policy, allowed_values)
            )

        self._object_acl_policy = object_acl_policy

    @property
    def root_path(self):
        """Gets the root_path of this S3SettingsZoneSettings.  # noqa: E501

        Specifies the S3 bucket root path.  # noqa: E501

        :return: The root_path of this S3SettingsZoneSettings.  # noqa: E501
        :rtype: str
        """
        return self._root_path

    @root_path.setter
    def root_path(self, root_path):
        """Sets the root_path of this S3SettingsZoneSettings.

        Specifies the S3 bucket root path.  # noqa: E501

        :param root_path: The root_path of this S3SettingsZoneSettings.  # noqa: E501
        :type: str
        """
        if root_path is not None and len(root_path) > 4096:
            raise ValueError("Invalid value for `root_path`, length must be less than or equal to `4096`")  # noqa: E501
        if root_path is not None and len(root_path) < 1:
            raise ValueError("Invalid value for `root_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._root_path = root_path

    @property
    def use_md5_for_etag(self):
        """Gets the use_md5_for_etag of this S3SettingsZoneSettings.  # noqa: E501

        Use MD5 for Etag on upload  # noqa: E501

        :return: The use_md5_for_etag of this S3SettingsZoneSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_md5_for_etag

    @use_md5_for_etag.setter
    def use_md5_for_etag(self, use_md5_for_etag):
        """Sets the use_md5_for_etag of this S3SettingsZoneSettings.

        Use MD5 for Etag on upload  # noqa: E501

        :param use_md5_for_etag: The use_md5_for_etag of this S3SettingsZoneSettings.  # noqa: E501
        :type: bool
        """

        self._use_md5_for_etag = use_md5_for_etag

    @property
    def validate_content_md5(self):
        """Gets the validate_content_md5 of this S3SettingsZoneSettings.  # noqa: E501

        Validate given Content-MD5  # noqa: E501

        :return: The validate_content_md5 of this S3SettingsZoneSettings.  # noqa: E501
        :rtype: bool
        """
        return self._validate_content_md5

    @validate_content_md5.setter
    def validate_content_md5(self, validate_content_md5):
        """Sets the validate_content_md5 of this S3SettingsZoneSettings.

        Validate given Content-MD5  # noqa: E501

        :param validate_content_md5: The validate_content_md5 of this S3SettingsZoneSettings.  # noqa: E501
        :type: bool
        """

        self._validate_content_md5 = validate_content_md5

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
        if not isinstance(other, S3SettingsZoneSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
