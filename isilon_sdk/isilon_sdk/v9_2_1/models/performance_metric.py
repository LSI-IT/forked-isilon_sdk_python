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


class PerformanceMetric(object):
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
        'datatype': 'str',
        'description': 'str',
        'id': 'str',
        'system_only': 'bool',
        'value_set': 'str'
    }

    attribute_map = {
        'datatype': 'datatype',
        'description': 'description',
        'id': 'id',
        'system_only': 'system_only',
        'value_set': 'value_set'
    }

    def __init__(self, datatype=None, description=None, id=None, system_only=None, value_set=None):  # noqa: E501
        """PerformanceMetric - a model defined in Swagger"""  # noqa: E501

        self._datatype = None
        self._description = None
        self._id = None
        self._system_only = None
        self._value_set = None
        self.discriminator = None

        if datatype is not None:
            self.datatype = datatype
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if system_only is not None:
            self.system_only = system_only
        if value_set is not None:
            self.value_set = value_set

    @property
    def datatype(self):
        """Gets the datatype of this PerformanceMetric.  # noqa: E501

        The data type of the performance metric.  # noqa: E501

        :return: The datatype of this PerformanceMetric.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this PerformanceMetric.

        The data type of the performance metric.  # noqa: E501

        :param datatype: The datatype of this PerformanceMetric.  # noqa: E501
        :type: str
        """
        allowed_values = ["integer", "string"]  # noqa: E501
        if datatype not in allowed_values:
            raise ValueError(
                "Invalid value for `datatype` ({0}), must be one of {1}"  # noqa: E501
                .format(datatype, allowed_values)
            )

        self._datatype = datatype

    @property
    def description(self):
        """Gets the description of this PerformanceMetric.  # noqa: E501

        Text description of the performance metric.  # noqa: E501

        :return: The description of this PerformanceMetric.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PerformanceMetric.

        Text description of the performance metric.  # noqa: E501

        :param description: The description of this PerformanceMetric.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this PerformanceMetric.  # noqa: E501

        Performance metrics that can be used to configure a performance dataset, and performance metrics used by the default system performance dataset.  # noqa: E501

        :return: The id of this PerformanceMetric.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PerformanceMetric.

        Performance metrics that can be used to configure a performance dataset, and performance metrics used by the default system performance dataset.  # noqa: E501

        :param id: The id of this PerformanceMetric.  # noqa: E501
        :type: str
        """
        allowed_values = ["groupname", "local_address", "path", "protocol", "remote_address", "share_name", "username", "zone_name", "job_type", "system_name", "export_id"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"  # noqa: E501
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def system_only(self):
        """Gets the system_only of this PerformanceMetric.  # noqa: E501

        A 'system_only' metric is reserved for use by the system. This metric cannot be used to configure a new dataset.  # noqa: E501

        :return: The system_only of this PerformanceMetric.  # noqa: E501
        :rtype: bool
        """
        return self._system_only

    @system_only.setter
    def system_only(self, system_only):
        """Sets the system_only of this PerformanceMetric.

        A 'system_only' metric is reserved for use by the system. This metric cannot be used to configure a new dataset.  # noqa: E501

        :param system_only: The system_only of this PerformanceMetric.  # noqa: E501
        :type: bool
        """

        self._system_only = system_only

    @property
    def value_set(self):
        """Gets the value_set of this PerformanceMetric.  # noqa: E501

        The set of applicable values for the metric.  # noqa: E501

        :return: The value_set of this PerformanceMetric.  # noqa: E501
        :rtype: str
        """
        return self._value_set

    @value_set.setter
    def value_set(self, value_set):
        """Sets the value_set of this PerformanceMetric.

        The set of applicable values for the metric.  # noqa: E501

        :param value_set: The value_set of this PerformanceMetric.  # noqa: E501
        :type: str
        """

        self._value_set = value_set

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
        if not isinstance(other, PerformanceMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
