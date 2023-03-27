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

from isilon_sdk.v9_3_0.models.healthcheck_checklist_item_thresholds import HealthcheckChecklistItemThresholds  # noqa: F401,E501


class HealthcheckEvaluationOverride(object):
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
        'freshness': 'int',
        'id': 'str',
        'pass_status': 'str',
        'thresholds': 'HealthcheckChecklistItemThresholds'
    }

    attribute_map = {
        'freshness': 'freshness',
        'id': 'id',
        'pass_status': 'pass_status',
        'thresholds': 'thresholds'
    }

    def __init__(self, freshness=None, id=None, pass_status=None, thresholds=None):  # noqa: E501
        """HealthcheckEvaluationOverride - a model defined in Swagger"""  # noqa: E501

        self._freshness = None
        self._id = None
        self._pass_status = None
        self._thresholds = None
        self.discriminator = None

        if freshness is not None:
            self.freshness = freshness
        if id is not None:
            self.id = id
        if pass_status is not None:
            self.pass_status = pass_status
        if thresholds is not None:
            self.thresholds = thresholds

    @property
    def freshness(self):
        """Gets the freshness of this HealthcheckEvaluationOverride.  # noqa: E501

        Optional freshness override  # noqa: E501

        :return: The freshness of this HealthcheckEvaluationOverride.  # noqa: E501
        :rtype: int
        """
        return self._freshness

    @freshness.setter
    def freshness(self, freshness):
        """Sets the freshness of this HealthcheckEvaluationOverride.

        Optional freshness override  # noqa: E501

        :param freshness: The freshness of this HealthcheckEvaluationOverride.  # noqa: E501
        :type: int
        """
        if freshness is not None and freshness > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `freshness`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if freshness is not None and freshness < 0:  # noqa: E501
            raise ValueError("Invalid value for `freshness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._freshness = freshness

    @property
    def id(self):
        """Gets the id of this HealthcheckEvaluationOverride.  # noqa: E501

        Id of Item to which override applies  # noqa: E501

        :return: The id of this HealthcheckEvaluationOverride.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthcheckEvaluationOverride.

        Id of Item to which override applies  # noqa: E501

        :param id: The id of this HealthcheckEvaluationOverride.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def pass_status(self):
        """Gets the pass_status of this HealthcheckEvaluationOverride.  # noqa: E501

        Optional pass status override  # noqa: E501

        :return: The pass_status of this HealthcheckEvaluationOverride.  # noqa: E501
        :rtype: str
        """
        return self._pass_status

    @pass_status.setter
    def pass_status(self, pass_status):
        """Sets the pass_status of this HealthcheckEvaluationOverride.

        Optional pass status override  # noqa: E501

        :param pass_status: The pass_status of this HealthcheckEvaluationOverride.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "EMERGENCY"]  # noqa: E501
        if pass_status not in allowed_values:
            raise ValueError(
                "Invalid value for `pass_status` ({0}), must be one of {1}"  # noqa: E501
                .format(pass_status, allowed_values)
            )

        self._pass_status = pass_status

    @property
    def thresholds(self):
        """Gets the thresholds of this HealthcheckEvaluationOverride.  # noqa: E501

        Overrides for status thresholds  # noqa: E501

        :return: The thresholds of this HealthcheckEvaluationOverride.  # noqa: E501
        :rtype: HealthcheckChecklistItemThresholds
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this HealthcheckEvaluationOverride.

        Overrides for status thresholds  # noqa: E501

        :param thresholds: The thresholds of this HealthcheckEvaluationOverride.  # noqa: E501
        :type: HealthcheckChecklistItemThresholds
        """

        self._thresholds = thresholds

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
        if not isinstance(other, HealthcheckEvaluationOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
