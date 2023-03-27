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

from isilon_sdk.v9_5_0.models.supportassist_license_task_audit import SupportassistLicenseTaskAudit  # noqa: F401,E501


class SupportassistLicenseTask(object):
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
        'audit': 'SupportassistLicenseTaskAudit',
        'data': 'str',
        'description': 'str',
        'display_state': 'str',
        'display_state_history': 'list[str]',
        'error_msg': 'str',
        'source': 'str',
        'state': 'str',
        'sub_state': 'str',
        'success': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'audit': 'audit',
        'data': 'data',
        'description': 'description',
        'display_state': 'display_state',
        'display_state_history': 'display_state_history',
        'error_msg': 'error_msg',
        'source': 'source',
        'state': 'state',
        'sub_state': 'sub_state',
        'success': 'success',
        'task_id': 'task_id'
    }

    def __init__(self, audit=None, data=None, description='null', display_state=None, display_state_history=None, error_msg='null', source=None, state=None, sub_state=None, success=None, task_id=None):  # noqa: E501
        """SupportassistLicenseTask - a model defined in Swagger"""  # noqa: E501

        self._audit = None
        self._data = None
        self._description = None
        self._display_state = None
        self._display_state_history = None
        self._error_msg = None
        self._source = None
        self._state = None
        self._sub_state = None
        self._success = None
        self._task_id = None
        self.discriminator = None

        if audit is not None:
            self.audit = audit
        if data is not None:
            self.data = data
        self.description = description
        self.display_state = display_state
        self.display_state_history = display_state_history
        self.error_msg = error_msg
        if source is not None:
            self.source = source
        if state is not None:
            self.state = state
        if sub_state is not None:
            self.sub_state = sub_state
        if success is not None:
            self.success = success
        if task_id is not None:
            self.task_id = task_id

    @property
    def audit(self):
        """Gets the audit of this SupportassistLicenseTask.  # noqa: E501

        The audit trail of the task  # noqa: E501

        :return: The audit of this SupportassistLicenseTask.  # noqa: E501
        :rtype: SupportassistLicenseTaskAudit
        """
        return self._audit

    @audit.setter
    def audit(self, audit):
        """Sets the audit of this SupportassistLicenseTask.

        The audit trail of the task  # noqa: E501

        :param audit: The audit of this SupportassistLicenseTask.  # noqa: E501
        :type: SupportassistLicenseTaskAudit
        """

        self._audit = audit

    @property
    def data(self):
        """Gets the data of this SupportassistLicenseTask.  # noqa: E501

        The data related to the task  # noqa: E501

        :return: The data of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SupportassistLicenseTask.

        The data related to the task  # noqa: E501

        :param data: The data of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        if data is not None and len(data) > 8192:
            raise ValueError("Invalid value for `data`, length must be less than or equal to `8192`")  # noqa: E501
        if data is not None and len(data) < 0:
            raise ValueError("Invalid value for `data`, length must be greater than or equal to `0`")  # noqa: E501

        self._data = data

    @property
    def description(self):
        """Gets the description of this SupportassistLicenseTask.  # noqa: E501

        Describe current state detail  # noqa: E501

        :return: The description of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupportassistLicenseTask.

        Describe current state detail  # noqa: E501

        :param description: The description of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def display_state(self):
        """Gets the display_state of this SupportassistLicenseTask.  # noqa: E501

        The state of the task should be displayed  # noqa: E501

        :return: The display_state of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._display_state

    @display_state.setter
    def display_state(self, display_state):
        """Sets the display_state of this SupportassistLicenseTask.

        The state of the task should be displayed  # noqa: E501

        :param display_state: The display_state of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        if display_state is None:
            raise ValueError("Invalid value for `display_state`, must not be `None`")  # noqa: E501
        if display_state is not None and len(display_state) > 255:
            raise ValueError("Invalid value for `display_state`, length must be less than or equal to `255`")  # noqa: E501
        if display_state is not None and len(display_state) < 1:
            raise ValueError("Invalid value for `display_state`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_state = display_state

    @property
    def display_state_history(self):
        """Gets the display_state_history of this SupportassistLicenseTask.  # noqa: E501

        Array showing the history of display_state for this task  # noqa: E501

        :return: The display_state_history of this SupportassistLicenseTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._display_state_history

    @display_state_history.setter
    def display_state_history(self, display_state_history):
        """Sets the display_state_history of this SupportassistLicenseTask.

        Array showing the history of display_state for this task  # noqa: E501

        :param display_state_history: The display_state_history of this SupportassistLicenseTask.  # noqa: E501
        :type: list[str]
        """
        if display_state_history is None:
            raise ValueError("Invalid value for `display_state_history`, must not be `None`")  # noqa: E501
        allowed_values = ["waiting", "pre_check", "verify", "post_check", "success", "failure"]  # noqa: E501
        if not set(display_state_history).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `display_state_history` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(display_state_history) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._display_state_history = display_state_history

    @property
    def error_msg(self):
        """Gets the error_msg of this SupportassistLicenseTask.  # noqa: E501

        The error of the task should be displayed  # noqa: E501

        :return: The error_msg of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this SupportassistLicenseTask.

        The error of the task should be displayed  # noqa: E501

        :param error_msg: The error_msg of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        if error_msg is None:
            raise ValueError("Invalid value for `error_msg`, must not be `None`")  # noqa: E501
        if error_msg is not None and len(error_msg) > 255:
            raise ValueError("Invalid value for `error_msg`, length must be less than or equal to `255`")  # noqa: E501
        if error_msg is not None and len(error_msg) < 0:
            raise ValueError("Invalid value for `error_msg`, length must be greater than or equal to `0`")  # noqa: E501

        self._error_msg = error_msg

    @property
    def source(self):
        """Gets the source of this SupportassistLicenseTask.  # noqa: E501

        The source of the task  # noqa: E501

        :return: The source of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SupportassistLicenseTask.

        The source of the task  # noqa: E501

        :param source: The source of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONFIG", "EVENT", "TELEMETRY", "LICENSE", "LOG", "DOWNLOAD"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def state(self):
        """Gets the state of this SupportassistLicenseTask.  # noqa: E501

        The state of the task  # noqa: E501

        :return: The state of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SupportassistLicenseTask.

        The state of the task  # noqa: E501

        :param state: The state of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "COMPLETED", "INCOMING", "WAITING"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def sub_state(self):
        """Gets the sub_state of this SupportassistLicenseTask.  # noqa: E501

        The sub-state of the task  # noqa: E501

        :return: The sub_state of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._sub_state

    @sub_state.setter
    def sub_state(self, sub_state):
        """Sets the sub_state of this SupportassistLicenseTask.

        The sub-state of the task  # noqa: E501

        :param sub_state: The sub_state of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        if sub_state is not None and len(sub_state) > 255:
            raise ValueError("Invalid value for `sub_state`, length must be less than or equal to `255`")  # noqa: E501
        if sub_state is not None and len(sub_state) < 0:
            raise ValueError("Invalid value for `sub_state`, length must be greater than or equal to `0`")  # noqa: E501

        self._sub_state = sub_state

    @property
    def success(self):
        """Gets the success of this SupportassistLicenseTask.  # noqa: E501

        The success state of the task, if finished  # noqa: E501

        :return: The success of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this SupportassistLicenseTask.

        The success state of the task, if finished  # noqa: E501

        :param success: The success of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        if success is not None and len(success) > 255:
            raise ValueError("Invalid value for `success`, length must be less than or equal to `255`")  # noqa: E501
        if success is not None and len(success) < 0:
            raise ValueError("Invalid value for `success`, length must be greater than or equal to `0`")  # noqa: E501

        self._success = success

    @property
    def task_id(self):
        """Gets the task_id of this SupportassistLicenseTask.  # noqa: E501

        Task ID  # noqa: E501

        :return: The task_id of this SupportassistLicenseTask.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this SupportassistLicenseTask.

        Task ID  # noqa: E501

        :param task_id: The task_id of this SupportassistLicenseTask.  # noqa: E501
        :type: str
        """
        if task_id is not None and len(task_id) > 255:
            raise ValueError("Invalid value for `task_id`, length must be less than or equal to `255`")  # noqa: E501
        if task_id is not None and len(task_id) < 1:
            raise ValueError("Invalid value for `task_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._task_id = task_id

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
        if not isinstance(other, SupportassistLicenseTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other