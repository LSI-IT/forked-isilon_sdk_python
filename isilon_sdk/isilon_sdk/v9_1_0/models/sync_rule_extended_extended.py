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

from isilon_sdk.v9_1_0.models.sync_rule_schedule import SyncRuleSchedule  # noqa: F401,E501


class SyncRuleExtendedExtended(object):
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
        'enabled': 'bool',
        'id': 'str',
        'limit': 'int',
        'schedule': 'SyncRuleSchedule',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'id': 'id',
        'limit': 'limit',
        'schedule': 'schedule',
        'type': 'type'
    }

    def __init__(self, description=None, enabled=None, id=None, limit=None, schedule=None, type=None):  # noqa: E501
        """SyncRuleExtendedExtended - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._enabled = None
        self._id = None
        self._limit = None
        self._schedule = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if schedule is not None:
            self.schedule = schedule
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this SyncRuleExtendedExtended.  # noqa: E501

        User-entered description of this performance rule.  # noqa: E501

        :return: The description of this SyncRuleExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SyncRuleExtendedExtended.

        User-entered description of this performance rule.  # noqa: E501

        :param description: The description of this SyncRuleExtendedExtended.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this SyncRuleExtendedExtended.  # noqa: E501

        Whether this performance rule is currently in effect during its specified intervals.  # noqa: E501

        :return: The enabled of this SyncRuleExtendedExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SyncRuleExtendedExtended.

        Whether this performance rule is currently in effect during its specified intervals.  # noqa: E501

        :param enabled: The enabled of this SyncRuleExtendedExtended.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this SyncRuleExtendedExtended.  # noqa: E501

        The system ID given to this performance rule.  # noqa: E501

        :return: The id of this SyncRuleExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SyncRuleExtendedExtended.

        The system ID given to this performance rule.  # noqa: E501

        :param id: The id of this SyncRuleExtendedExtended.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def limit(self):
        """Gets the limit of this SyncRuleExtendedExtended.  # noqa: E501

        Amount the specified system resource type is limited by this rule.  Units are kb/s for bandwidth, files/s for file-count, processing percentage used for cpu, or percentage of maximum available workers.  # noqa: E501

        :return: The limit of this SyncRuleExtendedExtended.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SyncRuleExtendedExtended.

        Amount the specified system resource type is limited by this rule.  Units are kb/s for bandwidth, files/s for file-count, processing percentage used for cpu, or percentage of maximum available workers.  # noqa: E501

        :param limit: The limit of this SyncRuleExtendedExtended.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def schedule(self):
        """Gets the schedule of this SyncRuleExtendedExtended.  # noqa: E501

        A schedule defining when during a week this performance rule is in effect.  If unspecified or null, the schedule will always be in effect.  # noqa: E501

        :return: The schedule of this SyncRuleExtendedExtended.  # noqa: E501
        :rtype: SyncRuleSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this SyncRuleExtendedExtended.

        A schedule defining when during a week this performance rule is in effect.  If unspecified or null, the schedule will always be in effect.  # noqa: E501

        :param schedule: The schedule of this SyncRuleExtendedExtended.  # noqa: E501
        :type: SyncRuleSchedule
        """

        self._schedule = schedule

    @property
    def type(self):
        """Gets the type of this SyncRuleExtendedExtended.  # noqa: E501

        The type of system resource this rule limits.  # noqa: E501

        :return: The type of this SyncRuleExtendedExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SyncRuleExtendedExtended.

        The type of system resource this rule limits.  # noqa: E501

        :param type: The type of this SyncRuleExtendedExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["bandwidth", "file_count", "cpu", "worker"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, SyncRuleExtendedExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
