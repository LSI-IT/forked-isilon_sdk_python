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

from isilon_sdk.v9_0_0.models.job_type import JobType  # noqa: F401,E501


class JobTypeExtended(object):
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
        'enabled': 'bool',
        'policy': 'str',
        'priority': 'int',
        'schedule': 'str',
        'allow_multiple_instances': 'bool',
        'description': 'str',
        'exclusion_set': 'str',
        'hidden': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'policy': 'policy',
        'priority': 'priority',
        'schedule': 'schedule',
        'allow_multiple_instances': 'allow_multiple_instances',
        'description': 'description',
        'exclusion_set': 'exclusion_set',
        'hidden': 'hidden',
        'id': 'id'
    }

    def __init__(self, enabled=None, policy=None, priority=None, schedule=None, allow_multiple_instances=None, description=None, exclusion_set=None, hidden=None, id=None):  # noqa: E501
        """JobTypeExtended - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._policy = None
        self._priority = None
        self._schedule = None
        self._allow_multiple_instances = None
        self._description = None
        self._exclusion_set = None
        self._hidden = None
        self._id = None
        self.discriminator = None

        self.enabled = enabled
        self.policy = policy
        self.priority = priority
        if schedule is not None:
            self.schedule = schedule
        self.allow_multiple_instances = allow_multiple_instances
        self.description = description
        self.exclusion_set = exclusion_set
        self.hidden = hidden
        self.id = id

    @property
    def enabled(self):
        """Gets the enabled of this JobTypeExtended.  # noqa: E501

        Whether the job type is enabled and able to run.  # noqa: E501

        :return: The enabled of this JobTypeExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this JobTypeExtended.

        Whether the job type is enabled and able to run.  # noqa: E501

        :param enabled: The enabled of this JobTypeExtended.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def policy(self):
        """Gets the policy of this JobTypeExtended.  # noqa: E501

        Default impact policy of this job type.  # noqa: E501

        :return: The policy of this JobTypeExtended.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this JobTypeExtended.

        Default impact policy of this job type.  # noqa: E501

        :param policy: The policy of this JobTypeExtended.  # noqa: E501
        :type: str
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def priority(self):
        """Gets the priority of this JobTypeExtended.  # noqa: E501

        Default priority of this job type; lower numbers preempt higher numbers.  # noqa: E501

        :return: The priority of this JobTypeExtended.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JobTypeExtended.

        Default priority of this job type; lower numbers preempt higher numbers.  # noqa: E501

        :param priority: The priority of this JobTypeExtended.  # noqa: E501
        :type: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501
        if priority is not None and priority > 10:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `10`")  # noqa: E501
        if priority is not None and priority < 1:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `1`")  # noqa: E501

        self._priority = priority

    @property
    def schedule(self):
        """Gets the schedule of this JobTypeExtended.  # noqa: E501

        The schedule on which this job type is queued, if any.  # noqa: E501

        :return: The schedule of this JobTypeExtended.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this JobTypeExtended.

        The schedule on which this job type is queued, if any.  # noqa: E501

        :param schedule: The schedule of this JobTypeExtended.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def allow_multiple_instances(self):
        """Gets the allow_multiple_instances of this JobTypeExtended.  # noqa: E501

        Whether multiple instances of this job type may run simultaneously.  # noqa: E501

        :return: The allow_multiple_instances of this JobTypeExtended.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multiple_instances

    @allow_multiple_instances.setter
    def allow_multiple_instances(self, allow_multiple_instances):
        """Sets the allow_multiple_instances of this JobTypeExtended.

        Whether multiple instances of this job type may run simultaneously.  # noqa: E501

        :param allow_multiple_instances: The allow_multiple_instances of this JobTypeExtended.  # noqa: E501
        :type: bool
        """
        if allow_multiple_instances is None:
            raise ValueError("Invalid value for `allow_multiple_instances`, must not be `None`")  # noqa: E501

        self._allow_multiple_instances = allow_multiple_instances

    @property
    def description(self):
        """Gets the description of this JobTypeExtended.  # noqa: E501

        Brief description of the job type.  # noqa: E501

        :return: The description of this JobTypeExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobTypeExtended.

        Brief description of the job type.  # noqa: E501

        :param description: The description of this JobTypeExtended.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def exclusion_set(self):
        """Gets the exclusion_set of this JobTypeExtended.  # noqa: E501

        The set(s) of mutually-exclusive job types to which this job belongs.  No job in this set may run with any other job in this set.  Obsolete; this value will always be an empty string, as exclusion sets are no longer a job type property.  # noqa: E501

        :return: The exclusion_set of this JobTypeExtended.  # noqa: E501
        :rtype: str
        """
        return self._exclusion_set

    @exclusion_set.setter
    def exclusion_set(self, exclusion_set):
        """Sets the exclusion_set of this JobTypeExtended.

        The set(s) of mutually-exclusive job types to which this job belongs.  No job in this set may run with any other job in this set.  Obsolete; this value will always be an empty string, as exclusion sets are no longer a job type property.  # noqa: E501

        :param exclusion_set: The exclusion_set of this JobTypeExtended.  # noqa: E501
        :type: str
        """
        if exclusion_set is None:
            raise ValueError("Invalid value for `exclusion_set`, must not be `None`")  # noqa: E501

        self._exclusion_set = exclusion_set

    @property
    def hidden(self):
        """Gets the hidden of this JobTypeExtended.  # noqa: E501

        Whether this job type is normally visible in the UI.  # noqa: E501

        :return: The hidden of this JobTypeExtended.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this JobTypeExtended.

        Whether this job type is normally visible in the UI.  # noqa: E501

        :param hidden: The hidden of this JobTypeExtended.  # noqa: E501
        :type: bool
        """
        if hidden is None:
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this JobTypeExtended.  # noqa: E501

        Job type ID.  # noqa: E501

        :return: The id of this JobTypeExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobTypeExtended.

        Job type ID.  # noqa: E501

        :param id: The id of this JobTypeExtended.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, JobTypeExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
