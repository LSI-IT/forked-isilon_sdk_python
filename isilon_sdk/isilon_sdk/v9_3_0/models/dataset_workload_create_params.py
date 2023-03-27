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

from isilon_sdk.v9_3_0.models.dataset_filter_metric_values_create_params import DatasetFilterMetricValuesCreateParams  # noqa: F401,E501
from isilon_sdk.v9_3_0.models.dataset_workload import DatasetWorkload  # noqa: F401,E501


class DatasetWorkloadCreateParams(object):
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
        'name': 'str',
        'metric_values': 'DatasetFilterMetricValuesCreateParams'
    }

    attribute_map = {
        'name': 'name',
        'metric_values': 'metric_values'
    }

    def __init__(self, name=None, metric_values=None):  # noqa: E501
        """DatasetWorkloadCreateParams - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._metric_values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.metric_values = metric_values

    @property
    def name(self):
        """Gets the name of this DatasetWorkloadCreateParams.  # noqa: E501

        The name of the workload. User specified.  # noqa: E501

        :return: The name of this DatasetWorkloadCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetWorkloadCreateParams.

        The name of the workload. User specified.  # noqa: E501

        :param name: The name of this DatasetWorkloadCreateParams.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 80:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `80`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def metric_values(self):
        """Gets the metric_values of this DatasetWorkloadCreateParams.  # noqa: E501

        Configurable metrics.  # noqa: E501

        :return: The metric_values of this DatasetWorkloadCreateParams.  # noqa: E501
        :rtype: DatasetFilterMetricValuesCreateParams
        """
        return self._metric_values

    @metric_values.setter
    def metric_values(self, metric_values):
        """Sets the metric_values of this DatasetWorkloadCreateParams.

        Configurable metrics.  # noqa: E501

        :param metric_values: The metric_values of this DatasetWorkloadCreateParams.  # noqa: E501
        :type: DatasetFilterMetricValuesCreateParams
        """
        if metric_values is None:
            raise ValueError("Invalid value for `metric_values`, must not be `None`")  # noqa: E501

        self._metric_values = metric_values

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
        if not isinstance(other, DatasetWorkloadCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
