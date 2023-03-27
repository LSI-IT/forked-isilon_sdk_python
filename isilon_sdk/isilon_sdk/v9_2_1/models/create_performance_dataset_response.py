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


class CreatePerformanceDatasetResponse(object):
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
        'id': 'int',
        'name': 'str',
        'note': 'str',
        'statkey': 'str',
        'stats_summary_uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'note': 'note',
        'statkey': 'statkey',
        'stats_summary_uri': 'stats_summary_uri'
    }

    def __init__(self, id=None, name=None, note=None, statkey=None, stats_summary_uri=None):  # noqa: E501
        """CreatePerformanceDatasetResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._note = None
        self._statkey = None
        self._stats_summary_uri = None
        self.discriminator = None

        self.id = id
        self.name = name
        if note is not None:
            self.note = note
        self.statkey = statkey
        self.stats_summary_uri = stats_summary_uri

    @property
    def id(self):
        """Gets the id of this CreatePerformanceDatasetResponse.  # noqa: E501

        Unique identifier for the configured dataset.  # noqa: E501

        :return: The id of this CreatePerformanceDatasetResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePerformanceDatasetResponse.

        Unique identifier for the configured dataset.  # noqa: E501

        :param id: The id of this CreatePerformanceDatasetResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this CreatePerformanceDatasetResponse.  # noqa: E501

        The name of the performance dataset. If a name is not specified then a default name is assigned. The default name will be an underscore separated list of the performance metrics and filters used to configure the dataset.  # noqa: E501

        :return: The name of this CreatePerformanceDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePerformanceDatasetResponse.

        The name of the performance dataset. If a name is not specified then a default name is assigned. The default name will be an underscore separated list of the performance metrics and filters used to configure the dataset.  # noqa: E501

        :param name: The name of this CreatePerformanceDatasetResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def note(self):
        """Gets the note of this CreatePerformanceDatasetResponse.  # noqa: E501

        Additional information about this dataset  # noqa: E501

        :return: The note of this CreatePerformanceDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this CreatePerformanceDatasetResponse.

        Additional information about this dataset  # noqa: E501

        :param note: The note of this CreatePerformanceDatasetResponse.  # noqa: E501
        :type: str
        """
        if note is not None and len(note) > 255:
            raise ValueError("Invalid value for `note`, length must be less than or equal to `255`")  # noqa: E501
        if note is not None and len(note) < 1:
            raise ValueError("Invalid value for `note`, length must be greater than or equal to `1`")  # noqa: E501

        self._note = note

    @property
    def statkey(self):
        """Gets the statkey of this CreatePerformanceDatasetResponse.  # noqa: E501

        Key for use in viewing associated raw statistics under the endpoints /statistics/history and /statistics/current.  # noqa: E501

        :return: The statkey of this CreatePerformanceDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._statkey

    @statkey.setter
    def statkey(self, statkey):
        """Sets the statkey of this CreatePerformanceDatasetResponse.

        Key for use in viewing associated raw statistics under the endpoints /statistics/history and /statistics/current.  # noqa: E501

        :param statkey: The statkey of this CreatePerformanceDatasetResponse.  # noqa: E501
        :type: str
        """
        if statkey is None:
            raise ValueError("Invalid value for `statkey`, must not be `None`")  # noqa: E501
        if statkey is not None and len(statkey) > 29:
            raise ValueError("Invalid value for `statkey`, length must be less than or equal to `29`")  # noqa: E501
        if statkey is not None and len(statkey) < 29:
            raise ValueError("Invalid value for `statkey`, length must be greater than or equal to `29`")  # noqa: E501

        self._statkey = statkey

    @property
    def stats_summary_uri(self):
        """Gets the stats_summary_uri of this CreatePerformanceDatasetResponse.  # noqa: E501

        URI used to view associated summary statistics.  # noqa: E501

        :return: The stats_summary_uri of this CreatePerformanceDatasetResponse.  # noqa: E501
        :rtype: str
        """
        return self._stats_summary_uri

    @stats_summary_uri.setter
    def stats_summary_uri(self, stats_summary_uri):
        """Sets the stats_summary_uri of this CreatePerformanceDatasetResponse.

        URI used to view associated summary statistics.  # noqa: E501

        :param stats_summary_uri: The stats_summary_uri of this CreatePerformanceDatasetResponse.  # noqa: E501
        :type: str
        """
        if stats_summary_uri is None:
            raise ValueError("Invalid value for `stats_summary_uri`, must not be `None`")  # noqa: E501
        if stats_summary_uri is not None and len(stats_summary_uri) > 255:
            raise ValueError("Invalid value for `stats_summary_uri`, length must be less than or equal to `255`")  # noqa: E501
        if stats_summary_uri is not None and len(stats_summary_uri) < 1:
            raise ValueError("Invalid value for `stats_summary_uri`, length must be greater than or equal to `1`")  # noqa: E501

        self._stats_summary_uri = stats_summary_uri

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
        if not isinstance(other, CreatePerformanceDatasetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
