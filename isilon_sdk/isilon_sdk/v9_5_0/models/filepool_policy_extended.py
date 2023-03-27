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

from isilon_sdk.v9_5_0.models.filepool_policy_action_extended import FilepoolPolicyActionExtended  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.filepool_policy_file_matching_pattern import FilepoolPolicyFileMatchingPattern  # noqa: F401,E501


class FilepoolPolicyExtended(object):
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
        'actions': 'list[FilepoolPolicyActionExtended]',
        'apply_order': 'int',
        'birth_cluster_id': 'str',
        'description': 'str',
        'file_matching_pattern': 'FilepoolPolicyFileMatchingPattern',
        'id': 'str',
        'name': 'str',
        'state': 'str',
        'state_details': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'apply_order': 'apply_order',
        'birth_cluster_id': 'birth_cluster_id',
        'description': 'description',
        'file_matching_pattern': 'file_matching_pattern',
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'state_details': 'state_details'
    }

    def __init__(self, actions=None, apply_order=None, birth_cluster_id=None, description=None, file_matching_pattern=None, id=None, name=None, state=None, state_details=None):  # noqa: E501
        """FilepoolPolicyExtended - a model defined in Swagger"""  # noqa: E501

        self._actions = None
        self._apply_order = None
        self._birth_cluster_id = None
        self._description = None
        self._file_matching_pattern = None
        self._id = None
        self._name = None
        self._state = None
        self._state_details = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if apply_order is not None:
            self.apply_order = apply_order
        if birth_cluster_id is not None:
            self.birth_cluster_id = birth_cluster_id
        if description is not None:
            self.description = description
        if file_matching_pattern is not None:
            self.file_matching_pattern = file_matching_pattern
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if state_details is not None:
            self.state_details = state_details

    @property
    def actions(self):
        """Gets the actions of this FilepoolPolicyExtended.  # noqa: E501

        A list of actions to be taken for matching files  # noqa: E501

        :return: The actions of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: list[FilepoolPolicyActionExtended]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this FilepoolPolicyExtended.

        A list of actions to be taken for matching files  # noqa: E501

        :param actions: The actions of this FilepoolPolicyExtended.  # noqa: E501
        :type: list[FilepoolPolicyActionExtended]
        """

        self._actions = actions

    @property
    def apply_order(self):
        """Gets the apply_order of this FilepoolPolicyExtended.  # noqa: E501

        The order in which this policy should be applied (relative to other policies)  # noqa: E501

        :return: The apply_order of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: int
        """
        return self._apply_order

    @apply_order.setter
    def apply_order(self, apply_order):
        """Sets the apply_order of this FilepoolPolicyExtended.

        The order in which this policy should be applied (relative to other policies)  # noqa: E501

        :param apply_order: The apply_order of this FilepoolPolicyExtended.  # noqa: E501
        :type: int
        """
        if apply_order is not None and apply_order > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `apply_order`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if apply_order is not None and apply_order < 1:  # noqa: E501
            raise ValueError("Invalid value for `apply_order`, must be a value greater than or equal to `1`")  # noqa: E501

        self._apply_order = apply_order

    @property
    def birth_cluster_id(self):
        """Gets the birth_cluster_id of this FilepoolPolicyExtended.  # noqa: E501

        The guid assigned to the cluster on which the policy was created  # noqa: E501

        :return: The birth_cluster_id of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """Sets the birth_cluster_id of this FilepoolPolicyExtended.

        The guid assigned to the cluster on which the policy was created  # noqa: E501

        :param birth_cluster_id: The birth_cluster_id of this FilepoolPolicyExtended.  # noqa: E501
        :type: str
        """
        if birth_cluster_id is not None and len(birth_cluster_id) > 255:
            raise ValueError("Invalid value for `birth_cluster_id`, length must be less than or equal to `255`")  # noqa: E501
        if birth_cluster_id is not None and len(birth_cluster_id) < 1:
            raise ValueError("Invalid value for `birth_cluster_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._birth_cluster_id = birth_cluster_id

    @property
    def description(self):
        """Gets the description of this FilepoolPolicyExtended.  # noqa: E501

        A description for this policy  # noqa: E501

        :return: The description of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FilepoolPolicyExtended.

        A description for this policy  # noqa: E501

        :param description: The description of this FilepoolPolicyExtended.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def file_matching_pattern(self):
        """Gets the file_matching_pattern of this FilepoolPolicyExtended.  # noqa: E501

        The file matching rules for this policy  # noqa: E501

        :return: The file_matching_pattern of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: FilepoolPolicyFileMatchingPattern
        """
        return self._file_matching_pattern

    @file_matching_pattern.setter
    def file_matching_pattern(self, file_matching_pattern):
        """Sets the file_matching_pattern of this FilepoolPolicyExtended.

        The file matching rules for this policy  # noqa: E501

        :param file_matching_pattern: The file_matching_pattern of this FilepoolPolicyExtended.  # noqa: E501
        :type: FilepoolPolicyFileMatchingPattern
        """

        self._file_matching_pattern = file_matching_pattern

    @property
    def id(self):
        """Gets the id of this FilepoolPolicyExtended.  # noqa: E501

        A unique name for this policy  # noqa: E501

        :return: The id of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FilepoolPolicyExtended.

        A unique name for this policy  # noqa: E501

        :param id: The id of this FilepoolPolicyExtended.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 768:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `768`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this FilepoolPolicyExtended.  # noqa: E501

        A unique name for this policy  # noqa: E501

        :return: The name of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilepoolPolicyExtended.

        A unique name for this policy  # noqa: E501

        :param name: The name of this FilepoolPolicyExtended.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 768:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `768`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this FilepoolPolicyExtended.  # noqa: E501

        Indicates whether this policy is in a good state (\"OK\") or disabled (\"disabled\")  # noqa: E501

        :return: The state of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FilepoolPolicyExtended.

        Indicates whether this policy is in a good state (\"OK\") or disabled (\"disabled\")  # noqa: E501

        :param state: The state of this FilepoolPolicyExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "disabled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_details(self):
        """Gets the state_details of this FilepoolPolicyExtended.  # noqa: E501

        Gives further information to describe the state of this policy  # noqa: E501

        :return: The state_details of this FilepoolPolicyExtended.  # noqa: E501
        :rtype: str
        """
        return self._state_details

    @state_details.setter
    def state_details(self, state_details):
        """Sets the state_details of this FilepoolPolicyExtended.

        Gives further information to describe the state of this policy  # noqa: E501

        :param state_details: The state_details of this FilepoolPolicyExtended.  # noqa: E501
        :type: str
        """
        if state_details is not None and len(state_details) > 255:
            raise ValueError("Invalid value for `state_details`, length must be less than or equal to `255`")  # noqa: E501
        if state_details is not None and len(state_details) < 0:
            raise ValueError("Invalid value for `state_details`, length must be greater than or equal to `0`")  # noqa: E501

        self._state_details = state_details

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
        if not isinstance(other, FilepoolPolicyExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
