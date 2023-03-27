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

from isilon_sdk.v9_0_0.models.event_eventlist_event import EventEventlistEvent  # noqa: F401,E501


class EventEventlist(object):
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
        'event_count': 'int',
        'eventgroup_instance': 'str',
        'events': 'list[EventEventlistEvent]',
        'id': 'str'
    }

    attribute_map = {
        'event_count': 'event_count',
        'eventgroup_instance': 'eventgroup_instance',
        'events': 'events',
        'id': 'id'
    }

    def __init__(self, event_count=None, eventgroup_instance=None, events=None, id=None):  # noqa: E501
        """EventEventlist - a model defined in Swagger"""  # noqa: E501

        self._event_count = None
        self._eventgroup_instance = None
        self._events = None
        self._id = None
        self.discriminator = None

        if event_count is not None:
            self.event_count = event_count
        if eventgroup_instance is not None:
            self.eventgroup_instance = eventgroup_instance
        if events is not None:
            self.events = events
        if id is not None:
            self.id = id

    @property
    def event_count(self):
        """Gets the event_count of this EventEventlist.  # noqa: E501

        Number of events linked to this eventgroup.  # noqa: E501

        :return: The event_count of this EventEventlist.  # noqa: E501
        :rtype: int
        """
        return self._event_count

    @event_count.setter
    def event_count(self, event_count):
        """Sets the event_count of this EventEventlist.

        Number of events linked to this eventgroup.  # noqa: E501

        :param event_count: The event_count of this EventEventlist.  # noqa: E501
        :type: int
        """
        if event_count is not None and event_count > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `event_count`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if event_count is not None and event_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `event_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._event_count = event_count

    @property
    def eventgroup_instance(self):
        """Gets the eventgroup_instance of this EventEventlist.  # noqa: E501

        Unique identifier of eventgroup instance.  # noqa: E501

        :return: The eventgroup_instance of this EventEventlist.  # noqa: E501
        :rtype: str
        """
        return self._eventgroup_instance

    @eventgroup_instance.setter
    def eventgroup_instance(self, eventgroup_instance):
        """Sets the eventgroup_instance of this EventEventlist.

        Unique identifier of eventgroup instance.  # noqa: E501

        :param eventgroup_instance: The eventgroup_instance of this EventEventlist.  # noqa: E501
        :type: str
        """
        if eventgroup_instance is not None and len(eventgroup_instance) > 255:
            raise ValueError("Invalid value for `eventgroup_instance`, length must be less than or equal to `255`")  # noqa: E501
        if eventgroup_instance is not None and len(eventgroup_instance) < 0:
            raise ValueError("Invalid value for `eventgroup_instance`, length must be greater than or equal to `0`")  # noqa: E501

        self._eventgroup_instance = eventgroup_instance

    @property
    def events(self):
        """Gets the events of this EventEventlist.  # noqa: E501

        list of all events linked to this eventgroup in chronological order.  # noqa: E501

        :return: The events of this EventEventlist.  # noqa: E501
        :rtype: list[EventEventlistEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this EventEventlist.

        list of all events linked to this eventgroup in chronological order.  # noqa: E501

        :param events: The events of this EventEventlist.  # noqa: E501
        :type: list[EventEventlistEvent]
        """

        self._events = events

    @property
    def id(self):
        """Gets the id of this EventEventlist.  # noqa: E501

        Same as eventgroup_instance.  # noqa: E501

        :return: The id of this EventEventlist.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventEventlist.

        Same as eventgroup_instance.  # noqa: E501

        :param id: The id of this EventEventlist.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

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
        if not isinstance(other, EventEventlist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
