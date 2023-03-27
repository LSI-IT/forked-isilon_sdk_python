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

from isilon_sdk.v9_5_0.models.supportassist_settings_connection import SupportassistSettingsConnection  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.supportassist_settings_contact import SupportassistSettingsContact  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.supportassist_settings_telemetry import SupportassistSettingsTelemetry  # noqa: F401,E501


class SupportassistSettings(object):
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
        'automatic_case_creation': 'bool',
        'connection': 'SupportassistSettingsConnection',
        'connection_state': 'str',
        'contact': 'SupportassistSettingsContact',
        'enable_download': 'bool',
        'enable_remote_support': 'bool',
        'onefs_software_id': 'str',
        'supportassist_enabled': 'bool',
        'telemetry': 'SupportassistSettingsTelemetry'
    }

    attribute_map = {
        'automatic_case_creation': 'automatic_case_creation',
        'connection': 'connection',
        'connection_state': 'connection_state',
        'contact': 'contact',
        'enable_download': 'enable_download',
        'enable_remote_support': 'enable_remote_support',
        'onefs_software_id': 'onefs_software_id',
        'supportassist_enabled': 'supportassist_enabled',
        'telemetry': 'telemetry'
    }

    def __init__(self, automatic_case_creation=True, connection=None, connection_state=None, contact=None, enable_download=True, enable_remote_support=False, onefs_software_id=None, supportassist_enabled=None, telemetry=None):  # noqa: E501
        """SupportassistSettings - a model defined in Swagger"""  # noqa: E501

        self._automatic_case_creation = None
        self._connection = None
        self._connection_state = None
        self._contact = None
        self._enable_download = None
        self._enable_remote_support = None
        self._onefs_software_id = None
        self._supportassist_enabled = None
        self._telemetry = None
        self.discriminator = None

        if automatic_case_creation is not None:
            self.automatic_case_creation = automatic_case_creation
        if connection is not None:
            self.connection = connection
        if connection_state is not None:
            self.connection_state = connection_state
        if contact is not None:
            self.contact = contact
        if enable_download is not None:
            self.enable_download = enable_download
        if enable_remote_support is not None:
            self.enable_remote_support = enable_remote_support
        if onefs_software_id is not None:
            self.onefs_software_id = onefs_software_id
        self.supportassist_enabled = supportassist_enabled
        if telemetry is not None:
            self.telemetry = telemetry

    @property
    def automatic_case_creation(self):
        """Gets the automatic_case_creation of this SupportassistSettings.  # noqa: E501

        True indicates automatic case creation is enabled  # noqa: E501

        :return: The automatic_case_creation of this SupportassistSettings.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_case_creation

    @automatic_case_creation.setter
    def automatic_case_creation(self, automatic_case_creation):
        """Sets the automatic_case_creation of this SupportassistSettings.

        True indicates automatic case creation is enabled  # noqa: E501

        :param automatic_case_creation: The automatic_case_creation of this SupportassistSettings.  # noqa: E501
        :type: bool
        """

        self._automatic_case_creation = automatic_case_creation

    @property
    def connection(self):
        """Gets the connection of this SupportassistSettings.  # noqa: E501

          # noqa: E501

        :return: The connection of this SupportassistSettings.  # noqa: E501
        :rtype: SupportassistSettingsConnection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this SupportassistSettings.

          # noqa: E501

        :param connection: The connection of this SupportassistSettings.  # noqa: E501
        :type: SupportassistSettingsConnection
        """

        self._connection = connection

    @property
    def connection_state(self):
        """Gets the connection_state of this SupportassistSettings.  # noqa: E501

        connection state.  # noqa: E501

        :return: The connection_state of this SupportassistSettings.  # noqa: E501
        :rtype: str
        """
        return self._connection_state

    @connection_state.setter
    def connection_state(self, connection_state):
        """Sets the connection_state of this SupportassistSettings.

        connection state.  # noqa: E501

        :param connection_state: The connection_state of this SupportassistSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled", "enabledinprogress", "disabledinprogress"]  # noqa: E501
        if connection_state not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_state` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_state, allowed_values)
            )

        self._connection_state = connection_state

    @property
    def contact(self):
        """Gets the contact of this SupportassistSettings.  # noqa: E501

          # noqa: E501

        :return: The contact of this SupportassistSettings.  # noqa: E501
        :rtype: SupportassistSettingsContact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this SupportassistSettings.

          # noqa: E501

        :param contact: The contact of this SupportassistSettings.  # noqa: E501
        :type: SupportassistSettingsContact
        """

        self._contact = contact

    @property
    def enable_download(self):
        """Gets the enable_download of this SupportassistSettings.  # noqa: E501

        True indicates downloads are enabled  # noqa: E501

        :return: The enable_download of this SupportassistSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_download

    @enable_download.setter
    def enable_download(self, enable_download):
        """Sets the enable_download of this SupportassistSettings.

        True indicates downloads are enabled  # noqa: E501

        :param enable_download: The enable_download of this SupportassistSettings.  # noqa: E501
        :type: bool
        """

        self._enable_download = enable_download

    @property
    def enable_remote_support(self):
        """Gets the enable_remote_support of this SupportassistSettings.  # noqa: E501

        Whether remoteAccessEnabled is enabled  # noqa: E501

        :return: The enable_remote_support of this SupportassistSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_remote_support

    @enable_remote_support.setter
    def enable_remote_support(self, enable_remote_support):
        """Sets the enable_remote_support of this SupportassistSettings.

        Whether remoteAccessEnabled is enabled  # noqa: E501

        :param enable_remote_support: The enable_remote_support of this SupportassistSettings.  # noqa: E501
        :type: bool
        """

        self._enable_remote_support = enable_remote_support

    @property
    def onefs_software_id(self):
        """Gets the onefs_software_id of this SupportassistSettings.  # noqa: E501

        The software ID used by SupportAssist  # noqa: E501

        :return: The onefs_software_id of this SupportassistSettings.  # noqa: E501
        :rtype: str
        """
        return self._onefs_software_id

    @onefs_software_id.setter
    def onefs_software_id(self, onefs_software_id):
        """Sets the onefs_software_id of this SupportassistSettings.

        The software ID used by SupportAssist  # noqa: E501

        :param onefs_software_id: The onefs_software_id of this SupportassistSettings.  # noqa: E501
        :type: str
        """
        if onefs_software_id is not None and len(onefs_software_id) > 2048:
            raise ValueError("Invalid value for `onefs_software_id`, length must be less than or equal to `2048`")  # noqa: E501
        if onefs_software_id is not None and len(onefs_software_id) < 0:
            raise ValueError("Invalid value for `onefs_software_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._onefs_software_id = onefs_software_id

    @property
    def supportassist_enabled(self):
        """Gets the supportassist_enabled of this SupportassistSettings.  # noqa: E501

        Whether SupportAssist is enabled  # noqa: E501

        :return: The supportassist_enabled of this SupportassistSettings.  # noqa: E501
        :rtype: bool
        """
        return self._supportassist_enabled

    @supportassist_enabled.setter
    def supportassist_enabled(self, supportassist_enabled):
        """Sets the supportassist_enabled of this SupportassistSettings.

        Whether SupportAssist is enabled  # noqa: E501

        :param supportassist_enabled: The supportassist_enabled of this SupportassistSettings.  # noqa: E501
        :type: bool
        """
        if supportassist_enabled is None:
            raise ValueError("Invalid value for `supportassist_enabled`, must not be `None`")  # noqa: E501

        self._supportassist_enabled = supportassist_enabled

    @property
    def telemetry(self):
        """Gets the telemetry of this SupportassistSettings.  # noqa: E501

          # noqa: E501

        :return: The telemetry of this SupportassistSettings.  # noqa: E501
        :rtype: SupportassistSettingsTelemetry
        """
        return self._telemetry

    @telemetry.setter
    def telemetry(self, telemetry):
        """Sets the telemetry of this SupportassistSettings.

          # noqa: E501

        :param telemetry: The telemetry of this SupportassistSettings.  # noqa: E501
        :type: SupportassistSettingsTelemetry
        """

        self._telemetry = telemetry

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
        if not isinstance(other, SupportassistSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
