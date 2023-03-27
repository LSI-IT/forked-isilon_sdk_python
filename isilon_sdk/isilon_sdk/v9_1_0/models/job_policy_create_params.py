# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_1_0.models.job_policy import JobPolicy  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.job_policy_interval import JobPolicyInterval  # noqa: F401,E501


class JobPolicyCreateParams(object):
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
        'description': 'str',
        'intervals': 'list[JobPolicyInterval]',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'intervals': 'intervals',
        'name': 'name'
    }

    def __init__(self, description=None, intervals=None, name=None):  # noqa: E501
        """JobPolicyCreateParams - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._intervals = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if intervals is not None:
            self.intervals = intervals
        self.name = name

    @property
    def description(self):
        """Gets the description of this JobPolicyCreateParams.  # noqa: E501

        A helpful human-readable description of the impact policy.  # noqa: E501

        :return: The description of this JobPolicyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobPolicyCreateParams.

        A helpful human-readable description of the impact policy.  # noqa: E501

        :param description: The description of this JobPolicyCreateParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def intervals(self):
        """Gets the intervals of this JobPolicyCreateParams.  # noqa: E501


        :return: The intervals of this JobPolicyCreateParams.  # noqa: E501
        :rtype: list[JobPolicyInterval]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """Sets the intervals of this JobPolicyCreateParams.


        :param intervals: The intervals of this JobPolicyCreateParams.  # noqa: E501
        :type: list[JobPolicyInterval]
        """

        self._intervals = intervals

    @property
    def name(self):
        """Gets the name of this JobPolicyCreateParams.  # noqa: E501

        The name of the impact policy.  # noqa: E501

        :return: The name of this JobPolicyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobPolicyCreateParams.

        The name of the impact policy.  # noqa: E501

        :param name: The name of this JobPolicyCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

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
        if not isinstance(other, JobPolicyCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
