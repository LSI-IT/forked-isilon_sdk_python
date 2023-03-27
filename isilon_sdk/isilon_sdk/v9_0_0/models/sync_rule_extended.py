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

from isilon_sdk.v9_0_0.models.sync_rule import SyncRule  # noqa: F401,E501
from isilon_sdk.v9_0_0.models.sync_rule_schedule import SyncRuleSchedule  # noqa: F401,E501


class SyncRuleExtended(object):
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
        'limit': 'int',
        'schedule': 'SyncRuleSchedule',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'limit': 'limit',
        'schedule': 'schedule',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, description=None, enabled=None, limit=None, schedule=None, id=None, type=None):  # noqa: E501
        """SyncRuleExtended - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._enabled = None
        self._limit = None
        self._schedule = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.description = description
        self.enabled = enabled
        self.limit = limit
        if schedule is not None:
            self.schedule = schedule
        self.id = id
        self.type = type

    @property
    def description(self):
        """Gets the description of this SyncRuleExtended.  # noqa: E501

        User-entered description of this performance rule.  # noqa: E501

        :return: The description of this SyncRuleExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SyncRuleExtended.

        User-entered description of this performance rule.  # noqa: E501

        :param description: The description of this SyncRuleExtended.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this SyncRuleExtended.  # noqa: E501

        Whether this performance rule is currently in effect during its specified intervals.  # noqa: E501

        :return: The enabled of this SyncRuleExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SyncRuleExtended.

        Whether this performance rule is currently in effect during its specified intervals.  # noqa: E501

        :param enabled: The enabled of this SyncRuleExtended.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def limit(self):
        """Gets the limit of this SyncRuleExtended.  # noqa: E501

        Amount the specified system resource type is limited by this rule.  Units are kb/s for bandwidth, files/s for file-count, processing percentage used for cpu, or percentage of maximum available workers.  # noqa: E501

        :return: The limit of this SyncRuleExtended.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SyncRuleExtended.

        Amount the specified system resource type is limited by this rule.  Units are kb/s for bandwidth, files/s for file-count, processing percentage used for cpu, or percentage of maximum available workers.  # noqa: E501

        :param limit: The limit of this SyncRuleExtended.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def schedule(self):
        """Gets the schedule of this SyncRuleExtended.  # noqa: E501

        A schedule defining when during a week this performance rule is in effect.  If unspecified or null, the schedule will always be in effect.  # noqa: E501

        :return: The schedule of this SyncRuleExtended.  # noqa: E501
        :rtype: SyncRuleSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this SyncRuleExtended.

        A schedule defining when during a week this performance rule is in effect.  If unspecified or null, the schedule will always be in effect.  # noqa: E501

        :param schedule: The schedule of this SyncRuleExtended.  # noqa: E501
        :type: SyncRuleSchedule
        """

        self._schedule = schedule

    @property
    def id(self):
        """Gets the id of this SyncRuleExtended.  # noqa: E501

        The system ID given to this performance rule.  # noqa: E501

        :return: The id of this SyncRuleExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SyncRuleExtended.

        The system ID given to this performance rule.  # noqa: E501

        :param id: The id of this SyncRuleExtended.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this SyncRuleExtended.  # noqa: E501

        The type of system resource this rule limits.  # noqa: E501

        :return: The type of this SyncRuleExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SyncRuleExtended.

        The type of system resource this rule limits.  # noqa: E501

        :param type: The type of this SyncRuleExtended.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
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
        if not isinstance(other, SyncRuleExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
