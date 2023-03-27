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

from isilon_sdk.v9_5_0.models.datamover_base_policy_src_dataset_retention import DatamoverBasePolicySrcDatasetRetention  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.datamover_historical_jobs_job_job_type_specific_attrs_dataset_creation_job_statistics import DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJobStatistics  # noqa: F401,E501


class DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob(object):
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
        'account_id': 'str',
        'base_path': 'str',
        'retention': 'DatamoverBasePolicySrcDatasetRetention',
        'statistics': 'DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJobStatistics',
        'subpaths': 'list[str]'
    }

    attribute_map = {
        'account_id': 'account_id',
        'base_path': 'base_path',
        'retention': 'retention',
        'statistics': 'statistics',
        'subpaths': 'subpaths'
    }

    def __init__(self, account_id=None, base_path=None, retention=None, statistics=None, subpaths=None):  # noqa: E501
        """DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._base_path = None
        self._retention = None
        self._statistics = None
        self._subpaths = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if base_path is not None:
            self.base_path = base_path
        if retention is not None:
            self.retention = retention
        if statistics is not None:
            self.statistics = statistics
        if subpaths is not None:
            self.subpaths = subpaths

    @property
    def account_id(self):
        """Gets the account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501

        Account ID of the source storage system, where the dataset is to be created.  # noqa: E501

        :return: The account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.

        Account ID of the source storage system, where the dataset is to be created.  # noqa: E501

        :param account_id: The account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :type: str
        """
        if account_id is not None and len(account_id) > 48:
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `48`")  # noqa: E501
        if account_id is not None and len(account_id) < 2:
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `2`")  # noqa: E501

        self._account_id = account_id

    @property
    def base_path(self):
        """Gets the base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501

        Filesystem path for dataset creation. The subpath is relative to this path.  # noqa: E501

        :return: The base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.

        Filesystem path for dataset creation. The subpath is relative to this path.  # noqa: E501

        :param base_path: The base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :type: str
        """
        if base_path is not None and len(base_path) > 4096:
            raise ValueError("Invalid value for `base_path`, length must be less than or equal to `4096`")  # noqa: E501
        if base_path is not None and len(base_path) < 1:
            raise ValueError("Invalid value for `base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._base_path = base_path

    @property
    def retention(self):
        """Gets the retention of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501

          # noqa: E501

        :return: The retention of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :rtype: DatamoverBasePolicySrcDatasetRetention
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.

          # noqa: E501

        :param retention: The retention of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :type: DatamoverBasePolicySrcDatasetRetention
        """

        self._retention = retention

    @property
    def statistics(self):
        """Gets the statistics of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501

        Statistics for this job  # noqa: E501

        :return: The statistics of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :rtype: DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJobStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.

        Statistics for this job  # noqa: E501

        :param statistics: The statistics of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :type: DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJobStatistics
        """

        self._statistics = statistics

    @property
    def subpaths(self):
        """Gets the subpaths of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501

        Set of filesystem paths relative to base path.  # noqa: E501

        :return: The subpaths of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._subpaths

    @subpaths.setter
    def subpaths(self, subpaths):
        """Sets the subpaths of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.

        Set of filesystem paths relative to base path.  # noqa: E501

        :param subpaths: The subpaths of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob.  # noqa: E501
        :type: list[str]
        """

        self._subpaths = subpaths

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
        if not isinstance(other, DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
