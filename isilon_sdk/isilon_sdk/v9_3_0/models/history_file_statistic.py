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


class HistoryFileStatistic(object):
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
        'allocated': 'int',
        'id': 'str',
        'limit': 'int',
        'name': 'str',
        'timestamp': 'int',
        'total': 'int'
    }

    attribute_map = {
        'allocated': 'allocated',
        'id': 'id',
        'limit': 'limit',
        'name': 'name',
        'timestamp': 'timestamp',
        'total': 'total'
    }

    def __init__(self, allocated=None, id=None, limit=None, name=None, timestamp=None, total=None):  # noqa: E501
        """HistoryFileStatistic - a model defined in Swagger"""  # noqa: E501

        self._allocated = None
        self._id = None
        self._limit = None
        self._name = None
        self._timestamp = None
        self._total = None
        self.discriminator = None

        self.allocated = allocated
        self.id = id
        self.limit = limit
        if name is not None:
            self.name = name
        self.timestamp = timestamp
        self.total = total

    @property
    def allocated(self):
        """Gets the allocated of this HistoryFileStatistic.  # noqa: E501

        Nodes allocated for the sync action.  # noqa: E501

        :return: The allocated of this HistoryFileStatistic.  # noqa: E501
        :rtype: int
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this HistoryFileStatistic.

        Nodes allocated for the sync action.  # noqa: E501

        :param allocated: The allocated of this HistoryFileStatistic.  # noqa: E501
        :type: int
        """
        if allocated is None:
            raise ValueError("Invalid value for `allocated`, must not be `None`")  # noqa: E501
        if allocated is not None and allocated > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `allocated`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if allocated is not None and allocated < -1:  # noqa: E501
            raise ValueError("Invalid value for `allocated`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._allocated = allocated

    @property
    def id(self):
        """Gets the id of this HistoryFileStatistic.  # noqa: E501

        An ID for a single performance report.  # noqa: E501

        :return: The id of this HistoryFileStatistic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryFileStatistic.

        An ID for a single performance report.  # noqa: E501

        :param id: The id of this HistoryFileStatistic.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def limit(self):
        """Gets the limit of this HistoryFileStatistic.  # noqa: E501

        Sync action limit.  # noqa: E501

        :return: The limit of this HistoryFileStatistic.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this HistoryFileStatistic.

        Sync action limit.  # noqa: E501

        :param limit: The limit of this HistoryFileStatistic.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501
        if limit is not None and limit > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if limit is not None and limit < -1:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._limit = limit

    @property
    def name(self):
        """Gets the name of this HistoryFileStatistic.  # noqa: E501

        The name of the SyncIQ policy if specified.  # noqa: E501

        :return: The name of this HistoryFileStatistic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HistoryFileStatistic.

        The name of the SyncIQ policy if specified.  # noqa: E501

        :param name: The name of this HistoryFileStatistic.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def timestamp(self):
        """Gets the timestamp of this HistoryFileStatistic.  # noqa: E501

        Timestamp for the performance report.  # noqa: E501

        :return: The timestamp of this HistoryFileStatistic.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this HistoryFileStatistic.

        Timestamp for the performance report.  # noqa: E501

        :param timestamp: The timestamp of this HistoryFileStatistic.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501
        if timestamp is not None and timestamp > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if timestamp is not None and timestamp < 1000000000:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must be a value greater than or equal to `1000000000`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def total(self):
        """Gets the total of this HistoryFileStatistic.  # noqa: E501

        Total usage for the performance report.  # noqa: E501

        :return: The total of this HistoryFileStatistic.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this HistoryFileStatistic.

        Total usage for the performance report.  # noqa: E501

        :param total: The total of this HistoryFileStatistic.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501
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
        if not isinstance(other, HistoryFileStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other