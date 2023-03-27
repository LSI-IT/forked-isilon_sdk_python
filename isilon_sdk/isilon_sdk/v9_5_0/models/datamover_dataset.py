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

from isilon_sdk.v9_5_0.models.datamover_dataset_dataset_global_id import DatamoverDatasetDatasetGlobalId  # noqa: F401,E501


class DatamoverDataset(object):
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
        'dataset_base_path': 'str',
        'dataset_creation_time': 'int',
        'dataset_expiry_action': 'str',
        'dataset_global_id': 'DatamoverDatasetDatasetGlobalId',
        'dataset_retention_period': 'int',
        'dataset_state': 'str',
        'dataset_subpaths': 'list[str]',
        'dataset_type': 'str',
        'id': 'int',
        'snapshot_path': 'str'
    }

    attribute_map = {
        'dataset_base_path': 'dataset_base_path',
        'dataset_creation_time': 'dataset_creation_time',
        'dataset_expiry_action': 'dataset_expiry_action',
        'dataset_global_id': 'dataset_global_id',
        'dataset_retention_period': 'dataset_retention_period',
        'dataset_state': 'dataset_state',
        'dataset_subpaths': 'dataset_subpaths',
        'dataset_type': 'dataset_type',
        'id': 'id',
        'snapshot_path': 'snapshot_path'
    }

    def __init__(self, dataset_base_path=None, dataset_creation_time=None, dataset_expiry_action=None, dataset_global_id=None, dataset_retention_period=None, dataset_state=None, dataset_subpaths=None, dataset_type=None, id=None, snapshot_path=None):  # noqa: E501
        """DatamoverDataset - a model defined in Swagger"""  # noqa: E501

        self._dataset_base_path = None
        self._dataset_creation_time = None
        self._dataset_expiry_action = None
        self._dataset_global_id = None
        self._dataset_retention_period = None
        self._dataset_state = None
        self._dataset_subpaths = None
        self._dataset_type = None
        self._id = None
        self._snapshot_path = None
        self.discriminator = None

        if dataset_base_path is not None:
            self.dataset_base_path = dataset_base_path
        if dataset_creation_time is not None:
            self.dataset_creation_time = dataset_creation_time
        if dataset_expiry_action is not None:
            self.dataset_expiry_action = dataset_expiry_action
        if dataset_global_id is not None:
            self.dataset_global_id = dataset_global_id
        if dataset_retention_period is not None:
            self.dataset_retention_period = dataset_retention_period
        if dataset_state is not None:
            self.dataset_state = dataset_state
        if dataset_subpaths is not None:
            self.dataset_subpaths = dataset_subpaths
        if dataset_type is not None:
            self.dataset_type = dataset_type
        if id is not None:
            self.id = id
        if snapshot_path is not None:
            self.snapshot_path = snapshot_path

    @property
    def dataset_base_path(self):
        """Gets the dataset_base_path of this DatamoverDataset.  # noqa: E501


        :return: The dataset_base_path of this DatamoverDataset.  # noqa: E501
        :rtype: str
        """
        return self._dataset_base_path

    @dataset_base_path.setter
    def dataset_base_path(self, dataset_base_path):
        """Sets the dataset_base_path of this DatamoverDataset.


        :param dataset_base_path: The dataset_base_path of this DatamoverDataset.  # noqa: E501
        :type: str
        """
        if dataset_base_path is not None and len(dataset_base_path) > 4096:
            raise ValueError("Invalid value for `dataset_base_path`, length must be less than or equal to `4096`")  # noqa: E501
        if dataset_base_path is not None and len(dataset_base_path) < 1:
            raise ValueError("Invalid value for `dataset_base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._dataset_base_path = dataset_base_path

    @property
    def dataset_creation_time(self):
        """Gets the dataset_creation_time of this DatamoverDataset.  # noqa: E501

        The time when the dataset is created. The time in seconds past the epoch  # noqa: E501

        :return: The dataset_creation_time of this DatamoverDataset.  # noqa: E501
        :rtype: int
        """
        return self._dataset_creation_time

    @dataset_creation_time.setter
    def dataset_creation_time(self, dataset_creation_time):
        """Sets the dataset_creation_time of this DatamoverDataset.

        The time when the dataset is created. The time in seconds past the epoch  # noqa: E501

        :param dataset_creation_time: The dataset_creation_time of this DatamoverDataset.  # noqa: E501
        :type: int
        """
        if dataset_creation_time is not None and dataset_creation_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `dataset_creation_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if dataset_creation_time is not None and dataset_creation_time < 1:  # noqa: E501
            raise ValueError("Invalid value for `dataset_creation_time`, must be a value greater than or equal to `1`")  # noqa: E501

        self._dataset_creation_time = dataset_creation_time

    @property
    def dataset_expiry_action(self):
        """Gets the dataset_expiry_action of this DatamoverDataset.  # noqa: E501

        The action to be taken after dataset expiry.  # noqa: E501

        :return: The dataset_expiry_action of this DatamoverDataset.  # noqa: E501
        :rtype: str
        """
        return self._dataset_expiry_action

    @dataset_expiry_action.setter
    def dataset_expiry_action(self, dataset_expiry_action):
        """Sets the dataset_expiry_action of this DatamoverDataset.

        The action to be taken after dataset expiry.  # noqa: E501

        :param dataset_expiry_action: The dataset_expiry_action of this DatamoverDataset.  # noqa: E501
        :type: str
        """
        allowed_values = ["DELETE"]  # noqa: E501
        if dataset_expiry_action not in allowed_values:
            raise ValueError(
                "Invalid value for `dataset_expiry_action` ({0}), must be one of {1}"  # noqa: E501
                .format(dataset_expiry_action, allowed_values)
            )

        self._dataset_expiry_action = dataset_expiry_action

    @property
    def dataset_global_id(self):
        """Gets the dataset_global_id of this DatamoverDataset.  # noqa: E501

        The globally unique identifier of dataset.  # noqa: E501

        :return: The dataset_global_id of this DatamoverDataset.  # noqa: E501
        :rtype: DatamoverDatasetDatasetGlobalId
        """
        return self._dataset_global_id

    @dataset_global_id.setter
    def dataset_global_id(self, dataset_global_id):
        """Sets the dataset_global_id of this DatamoverDataset.

        The globally unique identifier of dataset.  # noqa: E501

        :param dataset_global_id: The dataset_global_id of this DatamoverDataset.  # noqa: E501
        :type: DatamoverDatasetDatasetGlobalId
        """

        self._dataset_global_id = dataset_global_id

    @property
    def dataset_retention_period(self):
        """Gets the dataset_retention_period of this DatamoverDataset.  # noqa: E501

        The time when dataset will expire which is calculated based upon dataset creation time plus dataset retention period specified for the dataset. It is the time in seconds past the epoch  # noqa: E501

        :return: The dataset_retention_period of this DatamoverDataset.  # noqa: E501
        :rtype: int
        """
        return self._dataset_retention_period

    @dataset_retention_period.setter
    def dataset_retention_period(self, dataset_retention_period):
        """Sets the dataset_retention_period of this DatamoverDataset.

        The time when dataset will expire which is calculated based upon dataset creation time plus dataset retention period specified for the dataset. It is the time in seconds past the epoch  # noqa: E501

        :param dataset_retention_period: The dataset_retention_period of this DatamoverDataset.  # noqa: E501
        :type: int
        """
        if dataset_retention_period is not None and dataset_retention_period > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `dataset_retention_period`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if dataset_retention_period is not None and dataset_retention_period < 1:  # noqa: E501
            raise ValueError("Invalid value for `dataset_retention_period`, must be a value greater than or equal to `1`")  # noqa: E501

        self._dataset_retention_period = dataset_retention_period

    @property
    def dataset_state(self):
        """Gets the dataset_state of this DatamoverDataset.  # noqa: E501

        The state of dataset.  # noqa: E501

        :return: The dataset_state of this DatamoverDataset.  # noqa: E501
        :rtype: str
        """
        return self._dataset_state

    @dataset_state.setter
    def dataset_state(self, dataset_state):
        """Sets the dataset_state of this DatamoverDataset.

        The state of dataset.  # noqa: E501

        :param dataset_state: The dataset_state of this DatamoverDataset.  # noqa: E501
        :type: str
        """
        allowed_values = ["INVALID", "INPROGRESS", "COMPLETE", "COMPLETE_PARTIAL", "ERROR"]  # noqa: E501
        if dataset_state not in allowed_values:
            raise ValueError(
                "Invalid value for `dataset_state` ({0}), must be one of {1}"  # noqa: E501
                .format(dataset_state, allowed_values)
            )

        self._dataset_state = dataset_state

    @property
    def dataset_subpaths(self):
        """Gets the dataset_subpaths of this DatamoverDataset.  # noqa: E501

        Set of filesystem paths relative to base path.  # noqa: E501

        :return: The dataset_subpaths of this DatamoverDataset.  # noqa: E501
        :rtype: list[str]
        """
        return self._dataset_subpaths

    @dataset_subpaths.setter
    def dataset_subpaths(self, dataset_subpaths):
        """Sets the dataset_subpaths of this DatamoverDataset.

        Set of filesystem paths relative to base path.  # noqa: E501

        :param dataset_subpaths: The dataset_subpaths of this DatamoverDataset.  # noqa: E501
        :type: list[str]
        """

        self._dataset_subpaths = dataset_subpaths

    @property
    def dataset_type(self):
        """Gets the dataset_type of this DatamoverDataset.  # noqa: E501

        Dataset type from one of these: A file system on object store in a copy format, a file system on object store in a backup format or file on file dataset.  # noqa: E501

        :return: The dataset_type of this DatamoverDataset.  # noqa: E501
        :rtype: str
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        """Sets the dataset_type of this DatamoverDataset.

        Dataset type from one of these: A file system on object store in a copy format, a file system on object store in a backup format or file on file dataset.  # noqa: E501

        :param dataset_type: The dataset_type of this DatamoverDataset.  # noqa: E501
        :type: str
        """
        allowed_values = ["FILE_ON_OBJECT_COPY", "FILE_ON_OBJECT_BACKUP", "FILE"]  # noqa: E501
        if dataset_type not in allowed_values:
            raise ValueError(
                "Invalid value for `dataset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(dataset_type, allowed_values)
            )

        self._dataset_type = dataset_type

    @property
    def id(self):
        """Gets the id of this DatamoverDataset.  # noqa: E501

        The locally unique dataset identifier.  # noqa: E501

        :return: The id of this DatamoverDataset.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatamoverDataset.

        The locally unique dataset identifier.  # noqa: E501

        :param id: The id of this DatamoverDataset.  # noqa: E501
        :type: int
        """
        if id is not None and id > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def snapshot_path(self):
        """Gets the snapshot_path of this DatamoverDataset.  # noqa: E501


        :return: The snapshot_path of this DatamoverDataset.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_path

    @snapshot_path.setter
    def snapshot_path(self, snapshot_path):
        """Sets the snapshot_path of this DatamoverDataset.


        :param snapshot_path: The snapshot_path of this DatamoverDataset.  # noqa: E501
        :type: str
        """
        if snapshot_path is not None and len(snapshot_path) > 4096:
            raise ValueError("Invalid value for `snapshot_path`, length must be less than or equal to `4096`")  # noqa: E501
        if snapshot_path is not None and len(snapshot_path) < 0:
            raise ValueError("Invalid value for `snapshot_path`, length must be greater than or equal to `0`")  # noqa: E501

        self._snapshot_path = snapshot_path

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
        if not isinstance(other, DatamoverDataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
