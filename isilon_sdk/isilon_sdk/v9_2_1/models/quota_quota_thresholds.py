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


class QuotaQuotaThresholds(object):
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
        'advisory': 'int',
        'hard': 'int',
        'percent_advisory': 'float',
        'percent_soft': 'float',
        'soft': 'int',
        'soft_grace': 'int'
    }

    attribute_map = {
        'advisory': 'advisory',
        'hard': 'hard',
        'percent_advisory': 'percent_advisory',
        'percent_soft': 'percent_soft',
        'soft': 'soft',
        'soft_grace': 'soft_grace'
    }

    def __init__(self, advisory=None, hard=None, percent_advisory=None, percent_soft=None, soft=None, soft_grace=None):  # noqa: E501
        """QuotaQuotaThresholds - a model defined in Swagger"""  # noqa: E501

        self._advisory = None
        self._hard = None
        self._percent_advisory = None
        self._percent_soft = None
        self._soft = None
        self._soft_grace = None
        self.discriminator = None

        if advisory is not None:
            self.advisory = advisory
        if hard is not None:
            self.hard = hard
        if percent_advisory is not None:
            self.percent_advisory = percent_advisory
        if percent_soft is not None:
            self.percent_soft = percent_soft
        if soft is not None:
            self.soft = soft
        if soft_grace is not None:
            self.soft_grace = soft_grace

    @property
    def advisory(self):
        """Gets the advisory of this QuotaQuotaThresholds.  # noqa: E501

        Usage bytes at which notifications will be sent but writes will not be denied.  # noqa: E501

        :return: The advisory of this QuotaQuotaThresholds.  # noqa: E501
        :rtype: int
        """
        return self._advisory

    @advisory.setter
    def advisory(self, advisory):
        """Sets the advisory of this QuotaQuotaThresholds.

        Usage bytes at which notifications will be sent but writes will not be denied.  # noqa: E501

        :param advisory: The advisory of this QuotaQuotaThresholds.  # noqa: E501
        :type: int
        """
        if advisory is not None and advisory > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `advisory`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if advisory is not None and advisory < 1:  # noqa: E501
            raise ValueError("Invalid value for `advisory`, must be a value greater than or equal to `1`")  # noqa: E501

        self._advisory = advisory

    @property
    def hard(self):
        """Gets the hard of this QuotaQuotaThresholds.  # noqa: E501

        Usage bytes at which further writes will be denied.  # noqa: E501

        :return: The hard of this QuotaQuotaThresholds.  # noqa: E501
        :rtype: int
        """
        return self._hard

    @hard.setter
    def hard(self, hard):
        """Sets the hard of this QuotaQuotaThresholds.

        Usage bytes at which further writes will be denied.  # noqa: E501

        :param hard: The hard of this QuotaQuotaThresholds.  # noqa: E501
        :type: int
        """
        if hard is not None and hard > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `hard`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if hard is not None and hard < 1:  # noqa: E501
            raise ValueError("Invalid value for `hard`, must be a value greater than or equal to `1`")  # noqa: E501

        self._hard = hard

    @property
    def percent_advisory(self):
        """Gets the percent_advisory of this QuotaQuotaThresholds.  # noqa: E501

        Advisory threshold as percent of hard threshold.  # noqa: E501

        :return: The percent_advisory of this QuotaQuotaThresholds.  # noqa: E501
        :rtype: float
        """
        return self._percent_advisory

    @percent_advisory.setter
    def percent_advisory(self, percent_advisory):
        """Sets the percent_advisory of this QuotaQuotaThresholds.

        Advisory threshold as percent of hard threshold.  # noqa: E501

        :param percent_advisory: The percent_advisory of this QuotaQuotaThresholds.  # noqa: E501
        :type: float
        """
        if percent_advisory is not None and percent_advisory > 99.99:  # noqa: E501
            raise ValueError("Invalid value for `percent_advisory`, must be a value less than or equal to `99.99`")  # noqa: E501
        if percent_advisory is not None and percent_advisory < 0.01:  # noqa: E501
            raise ValueError("Invalid value for `percent_advisory`, must be a value greater than or equal to `0.01`")  # noqa: E501

        self._percent_advisory = percent_advisory

    @property
    def percent_soft(self):
        """Gets the percent_soft of this QuotaQuotaThresholds.  # noqa: E501

        Soft threshold as percent of hard threshold.  # noqa: E501

        :return: The percent_soft of this QuotaQuotaThresholds.  # noqa: E501
        :rtype: float
        """
        return self._percent_soft

    @percent_soft.setter
    def percent_soft(self, percent_soft):
        """Sets the percent_soft of this QuotaQuotaThresholds.

        Soft threshold as percent of hard threshold.  # noqa: E501

        :param percent_soft: The percent_soft of this QuotaQuotaThresholds.  # noqa: E501
        :type: float
        """
        if percent_soft is not None and percent_soft > 99.99:  # noqa: E501
            raise ValueError("Invalid value for `percent_soft`, must be a value less than or equal to `99.99`")  # noqa: E501
        if percent_soft is not None and percent_soft < 0.01:  # noqa: E501
            raise ValueError("Invalid value for `percent_soft`, must be a value greater than or equal to `0.01`")  # noqa: E501

        self._percent_soft = percent_soft

    @property
    def soft(self):
        """Gets the soft of this QuotaQuotaThresholds.  # noqa: E501

        Usage bytes at which notifications will be sent and soft grace time will be started.  # noqa: E501

        :return: The soft of this QuotaQuotaThresholds.  # noqa: E501
        :rtype: int
        """
        return self._soft

    @soft.setter
    def soft(self, soft):
        """Sets the soft of this QuotaQuotaThresholds.

        Usage bytes at which notifications will be sent and soft grace time will be started.  # noqa: E501

        :param soft: The soft of this QuotaQuotaThresholds.  # noqa: E501
        :type: int
        """
        if soft is not None and soft > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `soft`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if soft is not None and soft < 1:  # noqa: E501
            raise ValueError("Invalid value for `soft`, must be a value greater than or equal to `1`")  # noqa: E501

        self._soft = soft

    @property
    def soft_grace(self):
        """Gets the soft_grace of this QuotaQuotaThresholds.  # noqa: E501

        Time in seconds after which the soft threshold has been hit before writes will be denied.  # noqa: E501

        :return: The soft_grace of this QuotaQuotaThresholds.  # noqa: E501
        :rtype: int
        """
        return self._soft_grace

    @soft_grace.setter
    def soft_grace(self, soft_grace):
        """Sets the soft_grace of this QuotaQuotaThresholds.

        Time in seconds after which the soft threshold has been hit before writes will be denied.  # noqa: E501

        :param soft_grace: The soft_grace of this QuotaQuotaThresholds.  # noqa: E501
        :type: int
        """
        if soft_grace is not None and soft_grace > 1073741823:  # noqa: E501
            raise ValueError("Invalid value for `soft_grace`, must be a value less than or equal to `1073741823`")  # noqa: E501
        if soft_grace is not None and soft_grace < 1:  # noqa: E501
            raise ValueError("Invalid value for `soft_grace`, must be a value greater than or equal to `1`")  # noqa: E501

        self._soft_grace = soft_grace

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
        if not isinstance(other, QuotaQuotaThresholds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
