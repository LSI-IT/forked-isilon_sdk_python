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


class QuotaQuotaThresholdsExtended(object):
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
        'advisory_exceeded': 'bool',
        'advisory_last_exceeded': 'int',
        'hard': 'int',
        'hard_exceeded': 'bool',
        'hard_last_exceeded': 'int',
        'percent_advisory': 'float',
        'percent_soft': 'float',
        'soft': 'int',
        'soft_exceeded': 'bool',
        'soft_grace': 'int',
        'soft_last_exceeded': 'int'
    }

    attribute_map = {
        'advisory': 'advisory',
        'advisory_exceeded': 'advisory_exceeded',
        'advisory_last_exceeded': 'advisory_last_exceeded',
        'hard': 'hard',
        'hard_exceeded': 'hard_exceeded',
        'hard_last_exceeded': 'hard_last_exceeded',
        'percent_advisory': 'percent_advisory',
        'percent_soft': 'percent_soft',
        'soft': 'soft',
        'soft_exceeded': 'soft_exceeded',
        'soft_grace': 'soft_grace',
        'soft_last_exceeded': 'soft_last_exceeded'
    }

    def __init__(self, advisory=None, advisory_exceeded=None, advisory_last_exceeded=None, hard=None, hard_exceeded=None, hard_last_exceeded=None, percent_advisory=None, percent_soft=None, soft=None, soft_exceeded=None, soft_grace=None, soft_last_exceeded=None):  # noqa: E501
        """QuotaQuotaThresholdsExtended - a model defined in Swagger"""  # noqa: E501

        self._advisory = None
        self._advisory_exceeded = None
        self._advisory_last_exceeded = None
        self._hard = None
        self._hard_exceeded = None
        self._hard_last_exceeded = None
        self._percent_advisory = None
        self._percent_soft = None
        self._soft = None
        self._soft_exceeded = None
        self._soft_grace = None
        self._soft_last_exceeded = None
        self.discriminator = None

        if advisory is not None:
            self.advisory = advisory
        if advisory_exceeded is not None:
            self.advisory_exceeded = advisory_exceeded
        if advisory_last_exceeded is not None:
            self.advisory_last_exceeded = advisory_last_exceeded
        if hard is not None:
            self.hard = hard
        if hard_exceeded is not None:
            self.hard_exceeded = hard_exceeded
        if hard_last_exceeded is not None:
            self.hard_last_exceeded = hard_last_exceeded
        if percent_advisory is not None:
            self.percent_advisory = percent_advisory
        if percent_soft is not None:
            self.percent_soft = percent_soft
        if soft is not None:
            self.soft = soft
        if soft_exceeded is not None:
            self.soft_exceeded = soft_exceeded
        if soft_grace is not None:
            self.soft_grace = soft_grace
        if soft_last_exceeded is not None:
            self.soft_last_exceeded = soft_last_exceeded

    @property
    def advisory(self):
        """Gets the advisory of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Usage bytes at which notifications will be sent but writes will not be denied.  # noqa: E501

        :return: The advisory of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: int
        """
        return self._advisory

    @advisory.setter
    def advisory(self, advisory):
        """Sets the advisory of this QuotaQuotaThresholdsExtended.

        Usage bytes at which notifications will be sent but writes will not be denied.  # noqa: E501

        :param advisory: The advisory of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: int
        """
        if advisory is not None and advisory < 1:  # noqa: E501
            raise ValueError("Invalid value for `advisory`, must be a value greater than or equal to `1`")  # noqa: E501

        self._advisory = advisory

    @property
    def advisory_exceeded(self):
        """Gets the advisory_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501

        True if the advisory threshold has been hit.  # noqa: E501

        :return: The advisory_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._advisory_exceeded

    @advisory_exceeded.setter
    def advisory_exceeded(self, advisory_exceeded):
        """Sets the advisory_exceeded of this QuotaQuotaThresholdsExtended.

        True if the advisory threshold has been hit.  # noqa: E501

        :param advisory_exceeded: The advisory_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: bool
        """

        self._advisory_exceeded = advisory_exceeded

    @property
    def advisory_last_exceeded(self):
        """Gets the advisory_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Time at which advisory threshold was hit.  # noqa: E501

        :return: The advisory_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: int
        """
        return self._advisory_last_exceeded

    @advisory_last_exceeded.setter
    def advisory_last_exceeded(self, advisory_last_exceeded):
        """Sets the advisory_last_exceeded of this QuotaQuotaThresholdsExtended.

        Time at which advisory threshold was hit.  # noqa: E501

        :param advisory_last_exceeded: The advisory_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: int
        """

        self._advisory_last_exceeded = advisory_last_exceeded

    @property
    def hard(self):
        """Gets the hard of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Usage bytes at which further writes will be denied.  # noqa: E501

        :return: The hard of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: int
        """
        return self._hard

    @hard.setter
    def hard(self, hard):
        """Sets the hard of this QuotaQuotaThresholdsExtended.

        Usage bytes at which further writes will be denied.  # noqa: E501

        :param hard: The hard of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: int
        """
        if hard is not None and hard < 1:  # noqa: E501
            raise ValueError("Invalid value for `hard`, must be a value greater than or equal to `1`")  # noqa: E501

        self._hard = hard

    @property
    def hard_exceeded(self):
        """Gets the hard_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501

        True if the hard threshold has been hit.  # noqa: E501

        :return: The hard_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._hard_exceeded

    @hard_exceeded.setter
    def hard_exceeded(self, hard_exceeded):
        """Sets the hard_exceeded of this QuotaQuotaThresholdsExtended.

        True if the hard threshold has been hit.  # noqa: E501

        :param hard_exceeded: The hard_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: bool
        """

        self._hard_exceeded = hard_exceeded

    @property
    def hard_last_exceeded(self):
        """Gets the hard_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Time at which hard threshold was hit.  # noqa: E501

        :return: The hard_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: int
        """
        return self._hard_last_exceeded

    @hard_last_exceeded.setter
    def hard_last_exceeded(self, hard_last_exceeded):
        """Sets the hard_last_exceeded of this QuotaQuotaThresholdsExtended.

        Time at which hard threshold was hit.  # noqa: E501

        :param hard_last_exceeded: The hard_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: int
        """

        self._hard_last_exceeded = hard_last_exceeded

    @property
    def percent_advisory(self):
        """Gets the percent_advisory of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Advisory threshold as percent of hard threshold. Usage bytes at which notifications will be sent but writes will not be denied.  # noqa: E501

        :return: The percent_advisory of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: float
        """
        return self._percent_advisory

    @percent_advisory.setter
    def percent_advisory(self, percent_advisory):
        """Sets the percent_advisory of this QuotaQuotaThresholdsExtended.

        Advisory threshold as percent of hard threshold. Usage bytes at which notifications will be sent but writes will not be denied.  # noqa: E501

        :param percent_advisory: The percent_advisory of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: float
        """
        if percent_advisory is not None and percent_advisory > 99.99:  # noqa: E501
            raise ValueError("Invalid value for `percent_advisory`, must be a value less than or equal to `99.99`")  # noqa: E501
        if percent_advisory is not None and percent_advisory < 0.01:  # noqa: E501
            raise ValueError("Invalid value for `percent_advisory`, must be a value greater than or equal to `0.01`")  # noqa: E501

        self._percent_advisory = percent_advisory

    @property
    def percent_soft(self):
        """Gets the percent_soft of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Soft threshold as percent of hard threshold. Usage bytes at which notifications will be sent and soft grace time will be started.  # noqa: E501

        :return: The percent_soft of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: float
        """
        return self._percent_soft

    @percent_soft.setter
    def percent_soft(self, percent_soft):
        """Sets the percent_soft of this QuotaQuotaThresholdsExtended.

        Soft threshold as percent of hard threshold. Usage bytes at which notifications will be sent and soft grace time will be started.  # noqa: E501

        :param percent_soft: The percent_soft of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: float
        """
        if percent_soft is not None and percent_soft > 99.99:  # noqa: E501
            raise ValueError("Invalid value for `percent_soft`, must be a value less than or equal to `99.99`")  # noqa: E501
        if percent_soft is not None and percent_soft < 0.01:  # noqa: E501
            raise ValueError("Invalid value for `percent_soft`, must be a value greater than or equal to `0.01`")  # noqa: E501

        self._percent_soft = percent_soft

    @property
    def soft(self):
        """Gets the soft of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Usage bytes at which notifications will be sent and soft grace time will be started.  # noqa: E501

        :return: The soft of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: int
        """
        return self._soft

    @soft.setter
    def soft(self, soft):
        """Sets the soft of this QuotaQuotaThresholdsExtended.

        Usage bytes at which notifications will be sent and soft grace time will be started.  # noqa: E501

        :param soft: The soft of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: int
        """
        if soft is not None and soft < 1:  # noqa: E501
            raise ValueError("Invalid value for `soft`, must be a value greater than or equal to `1`")  # noqa: E501

        self._soft = soft

    @property
    def soft_exceeded(self):
        """Gets the soft_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501

        True if the soft threshold has been hit.  # noqa: E501

        :return: The soft_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._soft_exceeded

    @soft_exceeded.setter
    def soft_exceeded(self, soft_exceeded):
        """Sets the soft_exceeded of this QuotaQuotaThresholdsExtended.

        True if the soft threshold has been hit.  # noqa: E501

        :param soft_exceeded: The soft_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: bool
        """

        self._soft_exceeded = soft_exceeded

    @property
    def soft_grace(self):
        """Gets the soft_grace of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Time in seconds after which the soft threshold has been hit before writes will be denied.  # noqa: E501

        :return: The soft_grace of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: int
        """
        return self._soft_grace

    @soft_grace.setter
    def soft_grace(self, soft_grace):
        """Sets the soft_grace of this QuotaQuotaThresholdsExtended.

        Time in seconds after which the soft threshold has been hit before writes will be denied.  # noqa: E501

        :param soft_grace: The soft_grace of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: int
        """
        if soft_grace is not None and soft_grace < 1:  # noqa: E501
            raise ValueError("Invalid value for `soft_grace`, must be a value greater than or equal to `1`")  # noqa: E501

        self._soft_grace = soft_grace

    @property
    def soft_last_exceeded(self):
        """Gets the soft_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501

        Time at which soft threshold was hit  # noqa: E501

        :return: The soft_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :rtype: int
        """
        return self._soft_last_exceeded

    @soft_last_exceeded.setter
    def soft_last_exceeded(self, soft_last_exceeded):
        """Sets the soft_last_exceeded of this QuotaQuotaThresholdsExtended.

        Time at which soft threshold was hit  # noqa: E501

        :param soft_last_exceeded: The soft_last_exceeded of this QuotaQuotaThresholdsExtended.  # noqa: E501
        :type: int
        """

        self._soft_last_exceeded = soft_last_exceeded

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
        if not isinstance(other, QuotaQuotaThresholdsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
