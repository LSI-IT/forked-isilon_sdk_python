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

from isilon_sdk.v9_4_0.models.datamover_base_policy_src_dataset_retention import DatamoverBasePolicySrcDatasetRetention  # noqa: F401,E501


class DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob(object):
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
        'create_dataset_on_target': 'bool',
        'dataset_id': 'int',
        'new_tasks_account': 'str',
        'retention': 'DatamoverBasePolicySrcDatasetRetention',
        'source_account_id': 'str',
        'source_base_path': 'str',
        'source_subpaths': 'list[str]',
        'target_account_id': 'str',
        'target_base_path': 'str',
        'target_dataset_type': 'str'
    }

    attribute_map = {
        'create_dataset_on_target': 'create_dataset_on_target',
        'dataset_id': 'dataset_id',
        'new_tasks_account': 'new_tasks_account',
        'retention': 'retention',
        'source_account_id': 'source_account_id',
        'source_base_path': 'source_base_path',
        'source_subpaths': 'source_subpaths',
        'target_account_id': 'target_account_id',
        'target_base_path': 'target_base_path',
        'target_dataset_type': 'target_dataset_type'
    }

    def __init__(self, create_dataset_on_target=None, dataset_id=None, new_tasks_account=None, retention=None, source_account_id=None, source_base_path=None, source_subpaths=None, target_account_id=None, target_base_path=None, target_dataset_type=None):  # noqa: E501
        """DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob - a model defined in Swagger"""  # noqa: E501

        self._create_dataset_on_target = None
        self._dataset_id = None
        self._new_tasks_account = None
        self._retention = None
        self._source_account_id = None
        self._source_base_path = None
        self._source_subpaths = None
        self._target_account_id = None
        self._target_base_path = None
        self._target_dataset_type = None
        self.discriminator = None

        if create_dataset_on_target is not None:
            self.create_dataset_on_target = create_dataset_on_target
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if new_tasks_account is not None:
            self.new_tasks_account = new_tasks_account
        if retention is not None:
            self.retention = retention
        if source_account_id is not None:
            self.source_account_id = source_account_id
        if source_base_path is not None:
            self.source_base_path = source_base_path
        if source_subpaths is not None:
            self.source_subpaths = source_subpaths
        if target_account_id is not None:
            self.target_account_id = target_account_id
        if target_base_path is not None:
            self.target_base_path = target_base_path
        if target_dataset_type is not None:
            self.target_dataset_type = target_dataset_type

    @property
    def create_dataset_on_target(self):
        """Gets the create_dataset_on_target of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        Target dataset creation flag. True if dataset should be created on target, false otherwise.  # noqa: E501

        :return: The create_dataset_on_target of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: bool
        """
        return self._create_dataset_on_target

    @create_dataset_on_target.setter
    def create_dataset_on_target(self, create_dataset_on_target):
        """Sets the create_dataset_on_target of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        Target dataset creation flag. True if dataset should be created on target, false otherwise.  # noqa: E501

        :param create_dataset_on_target: The create_dataset_on_target of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: bool
        """

        self._create_dataset_on_target = create_dataset_on_target

    @property
    def dataset_id(self):
        """Gets the dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        The unique dataset identifier.  # noqa: E501

        :return: The dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: int
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        The unique dataset identifier.  # noqa: E501

        :param dataset_id: The dataset_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: int
        """
        if dataset_id is not None and dataset_id > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `dataset_id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if dataset_id is not None and dataset_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `dataset_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def new_tasks_account(self):
        """Gets the new_tasks_account of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        Account where to create task.  # noqa: E501

        :return: The new_tasks_account of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: str
        """
        return self._new_tasks_account

    @new_tasks_account.setter
    def new_tasks_account(self, new_tasks_account):
        """Sets the new_tasks_account of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        Account where to create task.  # noqa: E501

        :param new_tasks_account: The new_tasks_account of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: str
        """
        if new_tasks_account is not None and len(new_tasks_account) > 48:
            raise ValueError("Invalid value for `new_tasks_account`, length must be less than or equal to `48`")  # noqa: E501
        if new_tasks_account is not None and len(new_tasks_account) < 2:
            raise ValueError("Invalid value for `new_tasks_account`, length must be greater than or equal to `2`")  # noqa: E501

        self._new_tasks_account = new_tasks_account

    @property
    def retention(self):
        """Gets the retention of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

          # noqa: E501

        :return: The retention of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: DatamoverBasePolicySrcDatasetRetention
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

          # noqa: E501

        :param retention: The retention of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: DatamoverBasePolicySrcDatasetRetention
        """

        self._retention = retention

    @property
    def source_account_id(self):
        """Gets the source_account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        Account ID of the source storage system.  # noqa: E501

        :return: The source_account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: str
        """
        return self._source_account_id

    @source_account_id.setter
    def source_account_id(self, source_account_id):
        """Sets the source_account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        Account ID of the source storage system.  # noqa: E501

        :param source_account_id: The source_account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: str
        """
        if source_account_id is not None and len(source_account_id) > 48:
            raise ValueError("Invalid value for `source_account_id`, length must be less than or equal to `48`")  # noqa: E501
        if source_account_id is not None and len(source_account_id) < 2:
            raise ValueError("Invalid value for `source_account_id`, length must be greater than or equal to `2`")  # noqa: E501

        self._source_account_id = source_account_id

    @property
    def source_base_path(self):
        """Gets the source_base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        Filesystem source base path.  # noqa: E501

        :return: The source_base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: str
        """
        return self._source_base_path

    @source_base_path.setter
    def source_base_path(self, source_base_path):
        """Sets the source_base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        Filesystem source base path.  # noqa: E501

        :param source_base_path: The source_base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: str
        """
        if source_base_path is not None and len(source_base_path) > 4096:
            raise ValueError("Invalid value for `source_base_path`, length must be less than or equal to `4096`")  # noqa: E501
        if source_base_path is not None and len(source_base_path) < 1:
            raise ValueError("Invalid value for `source_base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._source_base_path = source_base_path

    @property
    def source_subpaths(self):
        """Gets the source_subpaths of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        Set of filesystem paths relative to base path.  # noqa: E501

        :return: The source_subpaths of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_subpaths

    @source_subpaths.setter
    def source_subpaths(self, source_subpaths):
        """Sets the source_subpaths of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        Set of filesystem paths relative to base path.  # noqa: E501

        :param source_subpaths: The source_subpaths of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: list[str]
        """

        self._source_subpaths = source_subpaths

    @property
    def target_account_id(self):
        """Gets the target_account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        Account ID of the target storage system.  # noqa: E501

        :return: The target_account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: str
        """
        return self._target_account_id

    @target_account_id.setter
    def target_account_id(self, target_account_id):
        """Sets the target_account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        Account ID of the target storage system.  # noqa: E501

        :param target_account_id: The target_account_id of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: str
        """
        if target_account_id is not None and len(target_account_id) > 48:
            raise ValueError("Invalid value for `target_account_id`, length must be less than or equal to `48`")  # noqa: E501
        if target_account_id is not None and len(target_account_id) < 2:
            raise ValueError("Invalid value for `target_account_id`, length must be greater than or equal to `2`")  # noqa: E501

        self._target_account_id = target_account_id

    @property
    def target_base_path(self):
        """Gets the target_base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        Target base path.  # noqa: E501

        :return: The target_base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: str
        """
        return self._target_base_path

    @target_base_path.setter
    def target_base_path(self, target_base_path):
        """Sets the target_base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        Target base path.  # noqa: E501

        :param target_base_path: The target_base_path of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: str
        """
        if target_base_path is not None and len(target_base_path) > 4096:
            raise ValueError("Invalid value for `target_base_path`, length must be less than or equal to `4096`")  # noqa: E501
        if target_base_path is not None and len(target_base_path) < 1:
            raise ValueError("Invalid value for `target_base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._target_base_path = target_base_path

    @property
    def target_dataset_type(self):
        """Gets the target_dataset_type of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501

        Dataset type on target.  # noqa: E501

        :return: The target_dataset_type of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :rtype: str
        """
        return self._target_dataset_type

    @target_dataset_type.setter
    def target_dataset_type(self, target_dataset_type):
        """Sets the target_dataset_type of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.

        Dataset type on target.  # noqa: E501

        :param target_dataset_type: The target_dataset_type of this DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["FILE_ON_OBJECT_COPY", "FILE_ON_OBJECT_BACKUP", "FILE"]  # noqa: E501
        if target_dataset_type not in allowed_values:
            raise ValueError(
                "Invalid value for `target_dataset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(target_dataset_type, allowed_values)
            )

        self._target_dataset_type = target_dataset_type

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
        if not isinstance(other, DatamoverHistoricalJobsJobJobTypeSpecificAttrsDatasetBaselineCopyJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
