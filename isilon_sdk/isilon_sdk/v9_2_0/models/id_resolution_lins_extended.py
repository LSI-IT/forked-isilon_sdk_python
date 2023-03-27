# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 12
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_2_0.models.id_resolution_domains_error import IdResolutionDomainsError  # noqa: F401,E501
from isilon_sdk.v9_2_0.models.id_resolution_lins import IdResolutionLins  # noqa: F401,E501
from isilon_sdk.v9_2_0.models.id_resolution_lins_path import IdResolutionLinsPath  # noqa: F401,E501


class IdResolutionLinsExtended(object):
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
        'paths': 'list[IdResolutionLinsPath]',
        'errors': 'list[IdResolutionDomainsError]',
        'resume': 'str',
        'total': 'int'
    }

    attribute_map = {
        'paths': 'paths',
        'errors': 'errors',
        'resume': 'resume',
        'total': 'total'
    }

    def __init__(self, paths=None, errors=None, resume=None, total=None):  # noqa: E501
        """IdResolutionLinsExtended - a model defined in Swagger"""  # noqa: E501

        self._paths = None
        self._errors = None
        self._resume = None
        self._total = None
        self.discriminator = None

        if paths is not None:
            self.paths = paths
        if errors is not None:
            self.errors = errors
        if resume is not None:
            self.resume = resume
        if total is not None:
            self.total = total

    @property
    def paths(self):
        """Gets the paths of this IdResolutionLinsExtended.  # noqa: E501


        :return: The paths of this IdResolutionLinsExtended.  # noqa: E501
        :rtype: list[IdResolutionLinsPath]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this IdResolutionLinsExtended.


        :param paths: The paths of this IdResolutionLinsExtended.  # noqa: E501
        :type: list[IdResolutionLinsPath]
        """

        self._paths = paths

    @property
    def errors(self):
        """Gets the errors of this IdResolutionLinsExtended.  # noqa: E501

        A list of id resolution errors that occurred during the bulk resolution. This list is included with a successful response.  # noqa: E501

        :return: The errors of this IdResolutionLinsExtended.  # noqa: E501
        :rtype: list[IdResolutionDomainsError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this IdResolutionLinsExtended.

        A list of id resolution errors that occurred during the bulk resolution. This list is included with a successful response.  # noqa: E501

        :param errors: The errors of this IdResolutionLinsExtended.  # noqa: E501
        :type: list[IdResolutionDomainsError]
        """

        self._errors = errors

    @property
    def resume(self):
        """Gets the resume of this IdResolutionLinsExtended.  # noqa: E501

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :return: The resume of this IdResolutionLinsExtended.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this IdResolutionLinsExtended.

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :param resume: The resume of this IdResolutionLinsExtended.  # noqa: E501
        :type: str
        """
        if resume is not None and len(resume) > 8192:
            raise ValueError("Invalid value for `resume`, length must be less than or equal to `8192`")  # noqa: E501
        if resume is not None and len(resume) < 0:
            raise ValueError("Invalid value for `resume`, length must be greater than or equal to `0`")  # noqa: E501

        self._resume = resume

    @property
    def total(self):
        """Gets the total of this IdResolutionLinsExtended.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The total of this IdResolutionLinsExtended.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this IdResolutionLinsExtended.

        Total number of items available.  # noqa: E501

        :param total: The total of this IdResolutionLinsExtended.  # noqa: E501
        :type: int
        """
        if total is not None and total > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if total is not None and total < 0:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, IdResolutionLinsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
