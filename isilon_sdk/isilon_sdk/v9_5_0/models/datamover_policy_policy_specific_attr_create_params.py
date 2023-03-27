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

from isilon_sdk.v9_5_0.models.datamover_policy_policy_specific_attr import DatamoverPolicyPolicySpecificAttr  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.datamover_policy_policy_specific_attr_copy_policy import DatamoverPolicyPolicySpecificAttrCopyPolicy  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.datamover_policy_policy_specific_attr_creation_policy import DatamoverPolicyPolicySpecificAttrCreationPolicy  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.datamover_policy_policy_specific_attr_expiration_policy import DatamoverPolicyPolicySpecificAttrExpirationPolicy  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.datamover_policy_policy_specific_attr_repeat_copy_policy import DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy  # noqa: F401,E501


class DatamoverPolicyPolicySpecificAttrCreateParams(object):
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
        'copy_policy': 'DatamoverPolicyPolicySpecificAttrCopyPolicy',
        'creation_policy': 'DatamoverPolicyPolicySpecificAttrCreationPolicy',
        'expiration_policy': 'DatamoverPolicyPolicySpecificAttrExpirationPolicy',
        'policy_type': 'str',
        'repeat_copy_policy': 'DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy'
    }

    attribute_map = {
        'copy_policy': 'copy_policy',
        'creation_policy': 'creation_policy',
        'expiration_policy': 'expiration_policy',
        'policy_type': 'policy_type',
        'repeat_copy_policy': 'repeat_copy_policy'
    }

    def __init__(self, copy_policy=None, creation_policy=None, expiration_policy=None, policy_type=None, repeat_copy_policy=None):  # noqa: E501
        """DatamoverPolicyPolicySpecificAttrCreateParams - a model defined in Swagger"""  # noqa: E501

        self._copy_policy = None
        self._creation_policy = None
        self._expiration_policy = None
        self._policy_type = None
        self._repeat_copy_policy = None
        self.discriminator = None

        if copy_policy is not None:
            self.copy_policy = copy_policy
        if creation_policy is not None:
            self.creation_policy = creation_policy
        if expiration_policy is not None:
            self.expiration_policy = expiration_policy
        self.policy_type = policy_type
        if repeat_copy_policy is not None:
            self.repeat_copy_policy = repeat_copy_policy

    @property
    def copy_policy(self):
        """Gets the copy_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501

          # noqa: E501

        :return: The copy_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :rtype: DatamoverPolicyPolicySpecificAttrCopyPolicy
        """
        return self._copy_policy

    @copy_policy.setter
    def copy_policy(self, copy_policy):
        """Sets the copy_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.

          # noqa: E501

        :param copy_policy: The copy_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :type: DatamoverPolicyPolicySpecificAttrCopyPolicy
        """

        self._copy_policy = copy_policy

    @property
    def creation_policy(self):
        """Gets the creation_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501

        Fields specific to dataset creation.  # noqa: E501

        :return: The creation_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :rtype: DatamoverPolicyPolicySpecificAttrCreationPolicy
        """
        return self._creation_policy

    @creation_policy.setter
    def creation_policy(self, creation_policy):
        """Sets the creation_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.

        Fields specific to dataset creation.  # noqa: E501

        :param creation_policy: The creation_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :type: DatamoverPolicyPolicySpecificAttrCreationPolicy
        """

        self._creation_policy = creation_policy

    @property
    def expiration_policy(self):
        """Gets the expiration_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501

        Fields specific to dataset retention policy.  # noqa: E501

        :return: The expiration_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :rtype: DatamoverPolicyPolicySpecificAttrExpirationPolicy
        """
        return self._expiration_policy

    @expiration_policy.setter
    def expiration_policy(self, expiration_policy):
        """Sets the expiration_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.

        Fields specific to dataset retention policy.  # noqa: E501

        :param expiration_policy: The expiration_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :type: DatamoverPolicyPolicySpecificAttrExpirationPolicy
        """

        self._expiration_policy = expiration_policy

    @property
    def policy_type(self):
        """Gets the policy_type of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501

        The type of policy - Creation, Expiration, Copy, Repeat-Copy.  # noqa: E501

        :return: The policy_type of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this DatamoverPolicyPolicySpecificAttrCreateParams.

        The type of policy - Creation, Expiration, Copy, Repeat-Copy.  # noqa: E501

        :param policy_type: The policy_type of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :type: str
        """
        if policy_type is None:
            raise ValueError("Invalid value for `policy_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CREATION", "EXPIRATION", "COPY", "REPEAT_COPY"]  # noqa: E501
        if policy_type not in allowed_values:
            raise ValueError(
                "Invalid value for `policy_type` ({0}), must be one of {1}"  # noqa: E501
                .format(policy_type, allowed_values)
            )

        self._policy_type = policy_type

    @property
    def repeat_copy_policy(self):
        """Gets the repeat_copy_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501

          # noqa: E501

        :return: The repeat_copy_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :rtype: DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy
        """
        return self._repeat_copy_policy

    @repeat_copy_policy.setter
    def repeat_copy_policy(self, repeat_copy_policy):
        """Sets the repeat_copy_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.

          # noqa: E501

        :param repeat_copy_policy: The repeat_copy_policy of this DatamoverPolicyPolicySpecificAttrCreateParams.  # noqa: E501
        :type: DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy
        """

        self._repeat_copy_policy = repeat_copy_policy

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
        if not isinstance(other, DatamoverPolicyPolicySpecificAttrCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other