# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_0_0.models.node_driveconfig_node_alert import NodeDriveconfigNodeAlert  # noqa: F401,E501
from isilon_sdk.v9_0_0.models.node_driveconfig_node_allow import NodeDriveconfigNodeAllow  # noqa: F401,E501
from isilon_sdk.v9_0_0.models.node_driveconfig_node_automatic_replacement_recognition import NodeDriveconfigNodeAutomaticReplacementRecognition  # noqa: F401,E501
from isilon_sdk.v9_0_0.models.node_driveconfig_node_instant_secure_erase import NodeDriveconfigNodeInstantSecureErase  # noqa: F401,E501
from isilon_sdk.v9_0_0.models.node_driveconfig_node_log import NodeDriveconfigNodeLog  # noqa: F401,E501
from isilon_sdk.v9_0_0.models.node_driveconfig_node_reboot import NodeDriveconfigNodeReboot  # noqa: F401,E501
from isilon_sdk.v9_0_0.models.node_driveconfig_node_spin_wait import NodeDriveconfigNodeSpinWait  # noqa: F401,E501
from isilon_sdk.v9_0_0.models.node_driveconfig_node_stall import NodeDriveconfigNodeStall  # noqa: F401,E501


class NodeDriveconfigNode(object):
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
        'alert': 'NodeDriveconfigNodeAlert',
        'allow': 'NodeDriveconfigNodeAllow',
        'automatic_replacement_recognition': 'NodeDriveconfigNodeAutomaticReplacementRecognition',
        'id': 'int',
        'instant_secure_erase': 'NodeDriveconfigNodeInstantSecureErase',
        'lnn': 'int',
        'log': 'NodeDriveconfigNodeLog',
        'reboot': 'NodeDriveconfigNodeReboot',
        'spin_wait': 'NodeDriveconfigNodeSpinWait',
        'stall': 'NodeDriveconfigNodeStall'
    }

    attribute_map = {
        'alert': 'alert',
        'allow': 'allow',
        'automatic_replacement_recognition': 'automatic_replacement_recognition',
        'id': 'id',
        'instant_secure_erase': 'instant_secure_erase',
        'lnn': 'lnn',
        'log': 'log',
        'reboot': 'reboot',
        'spin_wait': 'spin_wait',
        'stall': 'stall'
    }

    def __init__(self, alert=None, allow=None, automatic_replacement_recognition=None, id=None, instant_secure_erase=None, lnn=None, log=None, reboot=None, spin_wait=None, stall=None):  # noqa: E501
        """NodeDriveconfigNode - a model defined in Swagger"""  # noqa: E501

        self._alert = None
        self._allow = None
        self._automatic_replacement_recognition = None
        self._id = None
        self._instant_secure_erase = None
        self._lnn = None
        self._log = None
        self._reboot = None
        self._spin_wait = None
        self._stall = None
        self.discriminator = None

        if alert is not None:
            self.alert = alert
        if allow is not None:
            self.allow = allow
        if automatic_replacement_recognition is not None:
            self.automatic_replacement_recognition = automatic_replacement_recognition
        if id is not None:
            self.id = id
        if instant_secure_erase is not None:
            self.instant_secure_erase = instant_secure_erase
        if lnn is not None:
            self.lnn = lnn
        if log is not None:
            self.log = log
        if reboot is not None:
            self.reboot = reboot
        if spin_wait is not None:
            self.spin_wait = spin_wait
        if stall is not None:
            self.stall = stall

    @property
    def alert(self):
        """Gets the alert of this NodeDriveconfigNode.  # noqa: E501

        Configuration setting for drive alerts.  # noqa: E501

        :return: The alert of this NodeDriveconfigNode.  # noqa: E501
        :rtype: NodeDriveconfigNodeAlert
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this NodeDriveconfigNode.

        Configuration setting for drive alerts.  # noqa: E501

        :param alert: The alert of this NodeDriveconfigNode.  # noqa: E501
        :type: NodeDriveconfigNodeAlert
        """

        self._alert = alert

    @property
    def allow(self):
        """Gets the allow of this NodeDriveconfigNode.  # noqa: E501

        Configuration settings for drive formatting.  # noqa: E501

        :return: The allow of this NodeDriveconfigNode.  # noqa: E501
        :rtype: NodeDriveconfigNodeAllow
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """Sets the allow of this NodeDriveconfigNode.

        Configuration settings for drive formatting.  # noqa: E501

        :param allow: The allow of this NodeDriveconfigNode.  # noqa: E501
        :type: NodeDriveconfigNodeAllow
        """

        self._allow = allow

    @property
    def automatic_replacement_recognition(self):
        """Gets the automatic_replacement_recognition of this NodeDriveconfigNode.  # noqa: E501

        Configuration settings for Automatic Replacement Recognition (ARR).  # noqa: E501

        :return: The automatic_replacement_recognition of this NodeDriveconfigNode.  # noqa: E501
        :rtype: NodeDriveconfigNodeAutomaticReplacementRecognition
        """
        return self._automatic_replacement_recognition

    @automatic_replacement_recognition.setter
    def automatic_replacement_recognition(self, automatic_replacement_recognition):
        """Sets the automatic_replacement_recognition of this NodeDriveconfigNode.

        Configuration settings for Automatic Replacement Recognition (ARR).  # noqa: E501

        :param automatic_replacement_recognition: The automatic_replacement_recognition of this NodeDriveconfigNode.  # noqa: E501
        :type: NodeDriveconfigNodeAutomaticReplacementRecognition
        """

        self._automatic_replacement_recognition = automatic_replacement_recognition

    @property
    def id(self):
        """Gets the id of this NodeDriveconfigNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeDriveconfigNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeDriveconfigNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeDriveconfigNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def instant_secure_erase(self):
        """Gets the instant_secure_erase of this NodeDriveconfigNode.  # noqa: E501

        Configuration settings for instant secure erase (ISE).  # noqa: E501

        :return: The instant_secure_erase of this NodeDriveconfigNode.  # noqa: E501
        :rtype: NodeDriveconfigNodeInstantSecureErase
        """
        return self._instant_secure_erase

    @instant_secure_erase.setter
    def instant_secure_erase(self, instant_secure_erase):
        """Sets the instant_secure_erase of this NodeDriveconfigNode.

        Configuration settings for instant secure erase (ISE).  # noqa: E501

        :param instant_secure_erase: The instant_secure_erase of this NodeDriveconfigNode.  # noqa: E501
        :type: NodeDriveconfigNodeInstantSecureErase
        """

        self._instant_secure_erase = instant_secure_erase

    @property
    def lnn(self):
        """Gets the lnn of this NodeDriveconfigNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeDriveconfigNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeDriveconfigNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeDriveconfigNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def log(self):
        """Gets the log of this NodeDriveconfigNode.  # noqa: E501

        Configuration settings for drive statistics logs.  # noqa: E501

        :return: The log of this NodeDriveconfigNode.  # noqa: E501
        :rtype: NodeDriveconfigNodeLog
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this NodeDriveconfigNode.

        Configuration settings for drive statistics logs.  # noqa: E501

        :param log: The log of this NodeDriveconfigNode.  # noqa: E501
        :type: NodeDriveconfigNodeLog
        """

        self._log = log

    @property
    def reboot(self):
        """Gets the reboot of this NodeDriveconfigNode.  # noqa: E501

        Configuration settings for a node reboot due to a drive error.  # noqa: E501

        :return: The reboot of this NodeDriveconfigNode.  # noqa: E501
        :rtype: NodeDriveconfigNodeReboot
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        """Sets the reboot of this NodeDriveconfigNode.

        Configuration settings for a node reboot due to a drive error.  # noqa: E501

        :param reboot: The reboot of this NodeDriveconfigNode.  # noqa: E501
        :type: NodeDriveconfigNodeReboot
        """

        self._reboot = reboot

    @property
    def spin_wait(self):
        """Gets the spin_wait of this NodeDriveconfigNode.  # noqa: E501

        Configuration settings for sleeping the drive daemon before node is rescanned.  # noqa: E501

        :return: The spin_wait of this NodeDriveconfigNode.  # noqa: E501
        :rtype: NodeDriveconfigNodeSpinWait
        """
        return self._spin_wait

    @spin_wait.setter
    def spin_wait(self, spin_wait):
        """Sets the spin_wait of this NodeDriveconfigNode.

        Configuration settings for sleeping the drive daemon before node is rescanned.  # noqa: E501

        :param spin_wait: The spin_wait of this NodeDriveconfigNode.  # noqa: E501
        :type: NodeDriveconfigNodeSpinWait
        """

        self._spin_wait = spin_wait

    @property
    def stall(self):
        """Gets the stall of this NodeDriveconfigNode.  # noqa: E501

        Configuration settings to evaluate a drive stall.  # noqa: E501

        :return: The stall of this NodeDriveconfigNode.  # noqa: E501
        :rtype: NodeDriveconfigNodeStall
        """
        return self._stall

    @stall.setter
    def stall(self, stall):
        """Sets the stall of this NodeDriveconfigNode.

        Configuration settings to evaluate a drive stall.  # noqa: E501

        :param stall: The stall of this NodeDriveconfigNode.  # noqa: E501
        :type: NodeDriveconfigNodeStall
        """

        self._stall = stall

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
        if not isinstance(other, NodeDriveconfigNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
