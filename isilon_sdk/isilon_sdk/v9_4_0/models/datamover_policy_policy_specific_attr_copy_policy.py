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

from isilon_sdk.v9_4_0.models.datamover_policy_policy_specific_attr_copy_policy_dataset_copy_policy_base import DatamoverPolicyPolicySpecificAttrCopyPolicyDatasetCopyPolicyBase  # noqa: F401,E501


class DatamoverPolicyPolicySpecificAttrCopyPolicy(object):
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
        'dataset_copy_policy_base': 'DatamoverPolicyPolicySpecificAttrCopyPolicyDatasetCopyPolicyBase',
        'dataset_id': 'int',
        'source_base_path': 'str',
        'source_subpaths': 'list[str]'
    }

    attribute_map = {
        'create_dataset_on_target': 'create_dataset_on_target',
        'dataset_copy_policy_base': 'dataset_copy_policy_base',
        'dataset_id': 'dataset_id',
        'source_base_path': 'source_base_path',
        'source_subpaths': 'source_subpaths'
    }

    def __init__(self, create_dataset_on_target=None, dataset_copy_policy_base=None, dataset_id=None, source_base_path=None, source_subpaths=None):  # noqa: E501
        """DatamoverPolicyPolicySpecificAttrCopyPolicy - a model defined in Swagger"""  # noqa: E501

        self._create_dataset_on_target = None
        self._dataset_copy_policy_base = None
        self._dataset_id = None
        self._source_base_path = None
        self._source_subpaths = None
        self.discriminator = None

        if create_dataset_on_target is not None:
            self.create_dataset_on_target = create_dataset_on_target
        if dataset_copy_policy_base is not None:
            self.dataset_copy_policy_base = dataset_copy_policy_base
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if source_base_path is not None:
            self.source_base_path = source_base_path
        if source_subpaths is not None:
            self.source_subpaths = source_subpaths

    @property
    def create_dataset_on_target(self):
        """Gets the create_dataset_on_target of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501

        Whether or not to create dataset on the target storage system.  # noqa: E501

        :return: The create_dataset_on_target of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._create_dataset_on_target

    @create_dataset_on_target.setter
    def create_dataset_on_target(self, create_dataset_on_target):
        """Sets the create_dataset_on_target of this DatamoverPolicyPolicySpecificAttrCopyPolicy.

        Whether or not to create dataset on the target storage system.  # noqa: E501

        :param create_dataset_on_target: The create_dataset_on_target of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :type: bool
        """

        self._create_dataset_on_target = create_dataset_on_target

    @property
    def dataset_copy_policy_base(self):
        """Gets the dataset_copy_policy_base of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501

          # noqa: E501

        :return: The dataset_copy_policy_base of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :rtype: DatamoverPolicyPolicySpecificAttrCopyPolicyDatasetCopyPolicyBase
        """
        return self._dataset_copy_policy_base

    @dataset_copy_policy_base.setter
    def dataset_copy_policy_base(self, dataset_copy_policy_base):
        """Sets the dataset_copy_policy_base of this DatamoverPolicyPolicySpecificAttrCopyPolicy.

          # noqa: E501

        :param dataset_copy_policy_base: The dataset_copy_policy_base of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :type: DatamoverPolicyPolicySpecificAttrCopyPolicyDatasetCopyPolicyBase
        """

        self._dataset_copy_policy_base = dataset_copy_policy_base

    @property
    def dataset_id(self):
        """Gets the dataset_id of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501

        The unique dataset identifier.  # noqa: E501

        :return: The dataset_id of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :rtype: int
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this DatamoverPolicyPolicySpecificAttrCopyPolicy.

        The unique dataset identifier.  # noqa: E501

        :param dataset_id: The dataset_id of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :type: int
        """
        if dataset_id is not None and dataset_id > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `dataset_id`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if dataset_id is not None and dataset_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `dataset_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def source_base_path(self):
        """Gets the source_base_path of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501

        Base path of the dataset on the source storage system.  # noqa: E501

        :return: The source_base_path of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :rtype: str
        """
        return self._source_base_path

    @source_base_path.setter
    def source_base_path(self, source_base_path):
        """Sets the source_base_path of this DatamoverPolicyPolicySpecificAttrCopyPolicy.

        Base path of the dataset on the source storage system.  # noqa: E501

        :param source_base_path: The source_base_path of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :type: str
        """
        if source_base_path is not None and len(source_base_path) > 4096:
            raise ValueError("Invalid value for `source_base_path`, length must be less than or equal to `4096`")  # noqa: E501
        if source_base_path is not None and len(source_base_path) < 1:
            raise ValueError("Invalid value for `source_base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._source_base_path = source_base_path

    @property
    def source_subpaths(self):
        """Gets the source_subpaths of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501

        Set of filesystem paths relative to base path.  # noqa: E501

        :return: The source_subpaths of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_subpaths

    @source_subpaths.setter
    def source_subpaths(self, source_subpaths):
        """Sets the source_subpaths of this DatamoverPolicyPolicySpecificAttrCopyPolicy.

        Set of filesystem paths relative to base path.  # noqa: E501

        :param source_subpaths: The source_subpaths of this DatamoverPolicyPolicySpecificAttrCopyPolicy.  # noqa: E501
        :type: list[str]
        """

        self._source_subpaths = source_subpaths

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
        if not isinstance(other, DatamoverPolicyPolicySpecificAttrCopyPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other