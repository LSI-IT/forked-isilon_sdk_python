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


class DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy(object):
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
        'dataset_copy_policy_base': 'DatamoverPolicyPolicySpecificAttrCopyPolicyDatasetCopyPolicyBase',
        'reconnect': 'bool',
        'source_base_path': 'str'
    }

    attribute_map = {
        'dataset_copy_policy_base': 'dataset_copy_policy_base',
        'reconnect': 'reconnect',
        'source_base_path': 'source_base_path'
    }

    def __init__(self, dataset_copy_policy_base=None, reconnect=None, source_base_path=None):  # noqa: E501
        """DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy - a model defined in Swagger"""  # noqa: E501

        self._dataset_copy_policy_base = None
        self._reconnect = None
        self._source_base_path = None
        self.discriminator = None

        if dataset_copy_policy_base is not None:
            self.dataset_copy_policy_base = dataset_copy_policy_base
        if reconnect is not None:
            self.reconnect = reconnect
        if source_base_path is not None:
            self.source_base_path = source_base_path

    @property
    def dataset_copy_policy_base(self):
        """Gets the dataset_copy_policy_base of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501

          # noqa: E501

        :return: The dataset_copy_policy_base of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501
        :rtype: DatamoverPolicyPolicySpecificAttrCopyPolicyDatasetCopyPolicyBase
        """
        return self._dataset_copy_policy_base

    @dataset_copy_policy_base.setter
    def dataset_copy_policy_base(self, dataset_copy_policy_base):
        """Sets the dataset_copy_policy_base of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.

          # noqa: E501

        :param dataset_copy_policy_base: The dataset_copy_policy_base of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501
        :type: DatamoverPolicyPolicySpecificAttrCopyPolicyDatasetCopyPolicyBase
        """

        self._dataset_copy_policy_base = dataset_copy_policy_base

    @property
    def reconnect(self):
        """Gets the reconnect of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501

        This boolean allows starting with incremental syncs and skipping the initial baseline sync if the target base path contains a leaf dataset which is an ancestor of a source base path dataset.  # noqa: E501

        :return: The reconnect of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._reconnect

    @reconnect.setter
    def reconnect(self, reconnect):
        """Sets the reconnect of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.

        This boolean allows starting with incremental syncs and skipping the initial baseline sync if the target base path contains a leaf dataset which is an ancestor of a source base path dataset.  # noqa: E501

        :param reconnect: The reconnect of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501
        :type: bool
        """

        self._reconnect = reconnect

    @property
    def source_base_path(self):
        """Gets the source_base_path of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501


        :return: The source_base_path of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501
        :rtype: str
        """
        return self._source_base_path

    @source_base_path.setter
    def source_base_path(self, source_base_path):
        """Sets the source_base_path of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.


        :param source_base_path: The source_base_path of this DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy.  # noqa: E501
        :type: str
        """
        if source_base_path is not None and len(source_base_path) > 4096:
            raise ValueError("Invalid value for `source_base_path`, length must be less than or equal to `4096`")  # noqa: E501
        if source_base_path is not None and len(source_base_path) < 1:
            raise ValueError("Invalid value for `source_base_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._source_base_path = source_base_path

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
        if not isinstance(other, DatamoverPolicyPolicySpecificAttrRepeatCopyPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
