# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_1_0.models.cluster_nodes_error import ClusterNodesError  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.cluster_nodes_onefs_version import ClusterNodesOnefsVersion  # noqa: F401,E501


class ClusterNodesExtended(object):
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
        'error': 'ClusterNodesError',
        'last_action': 'str',
        'last_action_result': 'str',
        'lnn': 'int',
        'node_state': 'str',
        'onefs_version': 'ClusterNodesOnefsVersion',
        'progress': 'int'
    }

    attribute_map = {
        'error': 'error',
        'last_action': 'last_action',
        'last_action_result': 'last_action_result',
        'lnn': 'lnn',
        'node_state': 'node_state',
        'onefs_version': 'onefs_version',
        'progress': 'progress'
    }

    def __init__(self, error=None, last_action=None, last_action_result=None, lnn=None, node_state=None, onefs_version=None, progress=None):  # noqa: E501
        """ClusterNodesExtended - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._last_action = None
        self._last_action_result = None
        self._lnn = None
        self._node_state = None
        self._onefs_version = None
        self._progress = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if last_action is not None:
            self.last_action = last_action
        if last_action_result is not None:
            self.last_action_result = last_action_result
        if lnn is not None:
            self.lnn = lnn
        if node_state is not None:
            self.node_state = node_state
        if onefs_version is not None:
            self.onefs_version = onefs_version
        if progress is not None:
            self.progress = progress

    @property
    def error(self):
        """Gets the error of this ClusterNodesExtended.  # noqa: E501

        The current OneFS version before upgrade.  # noqa: E501

        :return: The error of this ClusterNodesExtended.  # noqa: E501
        :rtype: ClusterNodesError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ClusterNodesExtended.

        The current OneFS version before upgrade.  # noqa: E501

        :param error: The error of this ClusterNodesExtended.  # noqa: E501
        :type: ClusterNodesError
        """

        self._error = error

    @property
    def last_action(self):
        """Gets the last_action of this ClusterNodesExtended.  # noqa: E501

        The last action performed to completion/failure on this node.  Null if the node_state is 'committed' or 'assessing.' One of the following values: 'upgrade', 'rollback'.  # noqa: E501

        :return: The last_action of this ClusterNodesExtended.  # noqa: E501
        :rtype: str
        """
        return self._last_action

    @last_action.setter
    def last_action(self, last_action):
        """Sets the last_action of this ClusterNodesExtended.

        The last action performed to completion/failure on this node.  Null if the node_state is 'committed' or 'assessing.' One of the following values: 'upgrade', 'rollback'.  # noqa: E501

        :param last_action: The last_action of this ClusterNodesExtended.  # noqa: E501
        :type: str
        """

        self._last_action = last_action

    @property
    def last_action_result(self):
        """Gets the last_action_result of this ClusterNodesExtended.  # noqa: E501

        Did the node pass upgrade or rollback without failing? Null if the node_state is 'committed.' One of the following values: 'pass', 'fail', null  # noqa: E501

        :return: The last_action_result of this ClusterNodesExtended.  # noqa: E501
        :rtype: str
        """
        return self._last_action_result

    @last_action_result.setter
    def last_action_result(self, last_action_result):
        """Sets the last_action_result of this ClusterNodesExtended.

        Did the node pass upgrade or rollback without failing? Null if the node_state is 'committed.' One of the following values: 'pass', 'fail', null  # noqa: E501

        :param last_action_result: The last_action_result of this ClusterNodesExtended.  # noqa: E501
        :type: str
        """

        self._last_action_result = last_action_result

    @property
    def lnn(self):
        """Gets the lnn of this ClusterNodesExtended.  # noqa: E501

        The lnn of the node.  # noqa: E501

        :return: The lnn of this ClusterNodesExtended.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this ClusterNodesExtended.

        The lnn of the node.  # noqa: E501

        :param lnn: The lnn of this ClusterNodesExtended.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 576:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `576`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def node_state(self):
        """Gets the node_state of this ClusterNodesExtended.  # noqa: E501

        \\e The state of the node during the upgrade, rollback, or assessment. One of the following values: 'committed', 'upgraded', 'upgrading', 'rolling back', 'assessing', 'error'  # noqa: E501

        :return: The node_state of this ClusterNodesExtended.  # noqa: E501
        :rtype: str
        """
        return self._node_state

    @node_state.setter
    def node_state(self, node_state):
        """Sets the node_state of this ClusterNodesExtended.

        \\e The state of the node during the upgrade, rollback, or assessment. One of the following values: 'committed', 'upgraded', 'upgrading', 'rolling back', 'assessing', 'error'  # noqa: E501

        :param node_state: The node_state of this ClusterNodesExtended.  # noqa: E501
        :type: str
        """

        self._node_state = node_state

    @property
    def onefs_version(self):
        """Gets the onefs_version of this ClusterNodesExtended.  # noqa: E501

        The current OneFS version before upgrade.  # noqa: E501

        :return: The onefs_version of this ClusterNodesExtended.  # noqa: E501
        :rtype: ClusterNodesOnefsVersion
        """
        return self._onefs_version

    @onefs_version.setter
    def onefs_version(self, onefs_version):
        """Sets the onefs_version of this ClusterNodesExtended.

        The current OneFS version before upgrade.  # noqa: E501

        :param onefs_version: The onefs_version of this ClusterNodesExtended.  # noqa: E501
        :type: ClusterNodesOnefsVersion
        """

        self._onefs_version = onefs_version

    @property
    def progress(self):
        """Gets the progress of this ClusterNodesExtended.  # noqa: E501

        What step is the upgrade, assessment, or rollback in? To show via progress indicator. NOTE: the value is an integer between 0 and 100 (percent)  # noqa: E501

        :return: The progress of this ClusterNodesExtended.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ClusterNodesExtended.

        What step is the upgrade, assessment, or rollback in? To show via progress indicator. NOTE: the value is an integer between 0 and 100 (percent)  # noqa: E501

        :param progress: The progress of this ClusterNodesExtended.  # noqa: E501
        :type: int
        """

        self._progress = progress

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
        if not isinstance(other, ClusterNodesExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
