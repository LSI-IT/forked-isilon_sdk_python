# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_3_0.models.s3_bucket_acl_item import S3BucketAclItem  # noqa: F401,E501


class S3Bucket(object):
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
        'acl': 'list[S3BucketAclItem]',
        'description': 'str',
        'object_acl_policy': 'str'
    }

    attribute_map = {
        'acl': 'acl',
        'description': 'description',
        'object_acl_policy': 'object_acl_policy'
    }

    def __init__(self, acl=None, description=None, object_acl_policy=None):  # noqa: E501
        """S3Bucket - a model defined in Swagger"""  # noqa: E501

        self._acl = None
        self._description = None
        self._object_acl_policy = None
        self.discriminator = None

        if acl is not None:
            self.acl = acl
        if description is not None:
            self.description = description
        if object_acl_policy is not None:
            self.object_acl_policy = object_acl_policy

    @property
    def acl(self):
        """Gets the acl of this S3Bucket.  # noqa: E501

        Specifies an ordered list of S3 permissions.  # noqa: E501

        :return: The acl of this S3Bucket.  # noqa: E501
        :rtype: list[S3BucketAclItem]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this S3Bucket.

        Specifies an ordered list of S3 permissions.  # noqa: E501

        :param acl: The acl of this S3Bucket.  # noqa: E501
        :type: list[S3BucketAclItem]
        """

        self._acl = acl

    @property
    def description(self):
        """Gets the description of this S3Bucket.  # noqa: E501

        Description for this S3 bucket.  # noqa: E501

        :return: The description of this S3Bucket.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this S3Bucket.

        Description for this S3 bucket.  # noqa: E501

        :param description: The description of this S3Bucket.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 8192:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8192`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def object_acl_policy(self):
        """Gets the object_acl_policy of this S3Bucket.  # noqa: E501

        Set behavior of modifying object acls  # noqa: E501

        :return: The object_acl_policy of this S3Bucket.  # noqa: E501
        :rtype: str
        """
        return self._object_acl_policy

    @object_acl_policy.setter
    def object_acl_policy(self, object_acl_policy):
        """Sets the object_acl_policy of this S3Bucket.

        Set behavior of modifying object acls  # noqa: E501

        :param object_acl_policy: The object_acl_policy of this S3Bucket.  # noqa: E501
        :type: str
        """
        allowed_values = ["replace", "deny"]  # noqa: E501
        if object_acl_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `object_acl_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(object_acl_policy, allowed_values)
            )

        self._object_acl_policy = object_acl_policy

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
        if not isinstance(other, S3Bucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
