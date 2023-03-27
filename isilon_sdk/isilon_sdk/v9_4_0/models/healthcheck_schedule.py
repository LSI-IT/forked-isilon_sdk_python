# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HealthcheckSchedule(object):
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
        'checklist': 'list[str]',
        'id': 'str',
        'name': 'str',
        'schedule': 'str'
    }

    attribute_map = {
        'checklist': 'checklist',
        'id': 'id',
        'name': 'name',
        'schedule': 'schedule'
    }

    def __init__(self, checklist=None, id=None, name=None, schedule=None):  # noqa: E501
        """HealthcheckSchedule - a model defined in Swagger"""  # noqa: E501

        self._checklist = None
        self._id = None
        self._name = None
        self._schedule = None
        self.discriminator = None

        if checklist is not None:
            self.checklist = checklist
        if id is not None:
            self.id = id
        self.name = name
        if schedule is not None:
            self.schedule = schedule

    @property
    def checklist(self):
        """Gets the checklist of this HealthcheckSchedule.  # noqa: E501

        Checklists or Items for scheduling.  # noqa: E501

        :return: The checklist of this HealthcheckSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._checklist

    @checklist.setter
    def checklist(self, checklist):
        """Sets the checklist of this HealthcheckSchedule.

        Checklists or Items for scheduling.  # noqa: E501

        :param checklist: The checklist of this HealthcheckSchedule.  # noqa: E501
        :type: list[str]
        """

        self._checklist = checklist

    @property
    def id(self):
        """Gets the id of this HealthcheckSchedule.  # noqa: E501

        The ID of the newly created schedule.  # noqa: E501

        :return: The id of this HealthcheckSchedule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthcheckSchedule.

        The ID of the newly created schedule.  # noqa: E501

        :param id: The id of this HealthcheckSchedule.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this HealthcheckSchedule.  # noqa: E501

        The schedule name.  # noqa: E501

        :return: The name of this HealthcheckSchedule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthcheckSchedule.

        The schedule name.  # noqa: E501

        :param name: The name of this HealthcheckSchedule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def schedule(self):
        """Gets the schedule of this HealthcheckSchedule.  # noqa: E501

        The isi-schedule compatible natural language description of the schedule.  # noqa: E501

        :return: The schedule of this HealthcheckSchedule.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this HealthcheckSchedule.

        The isi-schedule compatible natural language description of the schedule.  # noqa: E501

        :param schedule: The schedule of this HealthcheckSchedule.  # noqa: E501
        :type: str
        """
        if schedule is not None and len(schedule) > 255:
            raise ValueError("Invalid value for `schedule`, length must be less than or equal to `255`")  # noqa: E501
        if schedule is not None and len(schedule) < 0:
            raise ValueError("Invalid value for `schedule`, length must be greater than or equal to `0`")  # noqa: E501

        self._schedule = schedule

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
        if not isinstance(other, HealthcheckSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
