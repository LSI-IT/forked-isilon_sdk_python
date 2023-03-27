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

from isilon_sdk.v9_4_0.models.datamover_historical_jobs_job_job_type_specific_attrs_dataset_creation_job import DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob  # noqa: F401,E501
from isilon_sdk.v9_4_0.models.datamover_historical_jobs_job_job_type_specific_attrs_dataset_expiration_job import DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetExpirationJob  # noqa: F401,E501
from isilon_sdk.v9_4_0.models.datamover_job_job_type_specific_attrs_dataset_baseline_copy_job import DatamoverJobJobTypeSpecificAttrsDatasetBaselineCopyJob  # noqa: F401,E501
from isilon_sdk.v9_4_0.models.datamover_job_job_type_specific_attrs_dataset_incremental_copy_job import DatamoverJobJobTypeSpecificAttrsDatasetIncrementalCopyJob  # noqa: F401,E501


class DatamoverJobJobTypeSpecificAttrs(object):
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
        'dataset_baseline_copy_job': 'DatamoverJobJobTypeSpecificAttrsDatasetBaselineCopyJob',
        'dataset_creation_job': 'DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob',
        'dataset_expiration_job': 'DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetExpirationJob',
        'dataset_incremental_copy_job': 'DatamoverJobJobTypeSpecificAttrsDatasetIncrementalCopyJob',
        'job_type': 'str'
    }

    attribute_map = {
        'dataset_baseline_copy_job': 'dataset_baseline_copy_job',
        'dataset_creation_job': 'dataset_creation_job',
        'dataset_expiration_job': 'dataset_expiration_job',
        'dataset_incremental_copy_job': 'dataset_incremental_copy_job',
        'job_type': 'job_type'
    }

    def __init__(self, dataset_baseline_copy_job=None, dataset_creation_job=None, dataset_expiration_job=None, dataset_incremental_copy_job=None, job_type=None):  # noqa: E501
        """DatamoverJobJobTypeSpecificAttrs - a model defined in Swagger"""  # noqa: E501

        self._dataset_baseline_copy_job = None
        self._dataset_creation_job = None
        self._dataset_expiration_job = None
        self._dataset_incremental_copy_job = None
        self._job_type = None
        self.discriminator = None

        if dataset_baseline_copy_job is not None:
            self.dataset_baseline_copy_job = dataset_baseline_copy_job
        if dataset_creation_job is not None:
            self.dataset_creation_job = dataset_creation_job
        if dataset_expiration_job is not None:
            self.dataset_expiration_job = dataset_expiration_job
        if dataset_incremental_copy_job is not None:
            self.dataset_incremental_copy_job = dataset_incremental_copy_job
        if job_type is not None:
            self.job_type = job_type

    @property
    def dataset_baseline_copy_job(self):
        """Gets the dataset_baseline_copy_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501

        Fields specific to dataset baseline copy job.  # noqa: E501

        :return: The dataset_baseline_copy_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :rtype: DatamoverJobJobTypeSpecificAttrsDatasetBaselineCopyJob
        """
        return self._dataset_baseline_copy_job

    @dataset_baseline_copy_job.setter
    def dataset_baseline_copy_job(self, dataset_baseline_copy_job):
        """Sets the dataset_baseline_copy_job of this DatamoverJobJobTypeSpecificAttrs.

        Fields specific to dataset baseline copy job.  # noqa: E501

        :param dataset_baseline_copy_job: The dataset_baseline_copy_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :type: DatamoverJobJobTypeSpecificAttrsDatasetBaselineCopyJob
        """

        self._dataset_baseline_copy_job = dataset_baseline_copy_job

    @property
    def dataset_creation_job(self):
        """Gets the dataset_creation_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501

        Fields specific to dataset creation job.  # noqa: E501

        :return: The dataset_creation_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :rtype: DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob
        """
        return self._dataset_creation_job

    @dataset_creation_job.setter
    def dataset_creation_job(self, dataset_creation_job):
        """Sets the dataset_creation_job of this DatamoverJobJobTypeSpecificAttrs.

        Fields specific to dataset creation job.  # noqa: E501

        :param dataset_creation_job: The dataset_creation_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :type: DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetCreationJob
        """

        self._dataset_creation_job = dataset_creation_job

    @property
    def dataset_expiration_job(self):
        """Gets the dataset_expiration_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501

        Fields specific to dataset retention job.  # noqa: E501

        :return: The dataset_expiration_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :rtype: DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetExpirationJob
        """
        return self._dataset_expiration_job

    @dataset_expiration_job.setter
    def dataset_expiration_job(self, dataset_expiration_job):
        """Sets the dataset_expiration_job of this DatamoverJobJobTypeSpecificAttrs.

        Fields specific to dataset retention job.  # noqa: E501

        :param dataset_expiration_job: The dataset_expiration_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :type: DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetExpirationJob
        """

        self._dataset_expiration_job = dataset_expiration_job

    @property
    def dataset_incremental_copy_job(self):
        """Gets the dataset_incremental_copy_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501

        Fields specific to dataset incremental copy job.  # noqa: E501

        :return: The dataset_incremental_copy_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :rtype: DatamoverJobJobTypeSpecificAttrsDatasetIncrementalCopyJob
        """
        return self._dataset_incremental_copy_job

    @dataset_incremental_copy_job.setter
    def dataset_incremental_copy_job(self, dataset_incremental_copy_job):
        """Sets the dataset_incremental_copy_job of this DatamoverJobJobTypeSpecificAttrs.

        Fields specific to dataset incremental copy job.  # noqa: E501

        :param dataset_incremental_copy_job: The dataset_incremental_copy_job of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :type: DatamoverJobJobTypeSpecificAttrsDatasetIncrementalCopyJob
        """

        self._dataset_incremental_copy_job = dataset_incremental_copy_job

    @property
    def job_type(self):
        """Gets the job_type of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501

        Type of the Data Mover job.  # noqa: E501

        :return: The job_type of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this DatamoverJobJobTypeSpecificAttrs.

        Type of the Data Mover job.  # noqa: E501

        :param job_type: The job_type of this DatamoverJobJobTypeSpecificAttrs.  # noqa: E501
        :type: str
        """
        allowed_values = ["DATASET_CREATION_JOB", "DATASET_EXPIRATION_JOB", "DATASET_INCREMENTAL_COPY_JOB", "DATASET_BASELINE_COPY_JOB"]  # noqa: E501
        if job_type not in allowed_values:
            raise ValueError(
                "Invalid value for `job_type` ({0}), must be one of {1}"  # noqa: E501
                .format(job_type, allowed_values)
            )

        self._job_type = job_type

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
        if not isinstance(other, DatamoverJobJobTypeSpecificAttrs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
