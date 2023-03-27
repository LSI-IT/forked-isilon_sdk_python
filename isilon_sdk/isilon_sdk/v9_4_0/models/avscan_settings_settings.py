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


class AvscanSettingsSettings(object):
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
        'ip_pool': 'str',
        'report_expiry': 'int',
        'scan_cloudpool_timeout': 'int',
        'scan_size_maximum': 'int',
        'scan_timeout': 'int',
        'scan_zones': 'list[str]',
        'service_enabled': 'bool'
    }

    attribute_map = {
        'ip_pool': 'ip_pool',
        'report_expiry': 'report_expiry',
        'scan_cloudpool_timeout': 'scan_cloudpool_timeout',
        'scan_size_maximum': 'scan_size_maximum',
        'scan_timeout': 'scan_timeout',
        'scan_zones': 'scan_zones',
        'service_enabled': 'service_enabled'
    }

    def __init__(self, ip_pool=None, report_expiry=None, scan_cloudpool_timeout=None, scan_size_maximum=None, scan_timeout=None, scan_zones=None, service_enabled=None):  # noqa: E501
        """AvscanSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._ip_pool = None
        self._report_expiry = None
        self._scan_cloudpool_timeout = None
        self._scan_size_maximum = None
        self._scan_timeout = None
        self._scan_zones = None
        self._service_enabled = None
        self.discriminator = None

        if ip_pool is not None:
            self.ip_pool = ip_pool
        if report_expiry is not None:
            self.report_expiry = report_expiry
        if scan_cloudpool_timeout is not None:
            self.scan_cloudpool_timeout = scan_cloudpool_timeout
        if scan_size_maximum is not None:
            self.scan_size_maximum = scan_size_maximum
        if scan_timeout is not None:
            self.scan_timeout = scan_timeout
        if scan_zones is not None:
            self.scan_zones = scan_zones
        if service_enabled is not None:
            self.service_enabled = service_enabled

    @property
    def ip_pool(self):
        """Gets the ip_pool of this AvscanSettingsSettings.  # noqa: E501

        The IP Pool to be used by the CAVA server.  # noqa: E501

        :return: The ip_pool of this AvscanSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ip_pool

    @ip_pool.setter
    def ip_pool(self, ip_pool):
        """Sets the ip_pool of this AvscanSettingsSettings.

        The IP Pool to be used by the CAVA server.  # noqa: E501

        :param ip_pool: The ip_pool of this AvscanSettingsSettings.  # noqa: E501
        :type: str
        """
        if ip_pool is not None and len(ip_pool) > 255:
            raise ValueError("Invalid value for `ip_pool`, length must be less than or equal to `255`")  # noqa: E501
        if ip_pool is not None and len(ip_pool) < 1:
            raise ValueError("Invalid value for `ip_pool`, length must be greater than or equal to `1`")  # noqa: E501

        self._ip_pool = ip_pool

    @property
    def report_expiry(self):
        """Gets the report_expiry of this AvscanSettingsSettings.  # noqa: E501

        How many seconds a scan report will be kept.  # noqa: E501

        :return: The report_expiry of this AvscanSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._report_expiry

    @report_expiry.setter
    def report_expiry(self, report_expiry):
        """Sets the report_expiry of this AvscanSettingsSettings.

        How many seconds a scan report will be kept.  # noqa: E501

        :param report_expiry: The report_expiry of this AvscanSettingsSettings.  # noqa: E501
        :type: int
        """
        if report_expiry is not None and report_expiry > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `report_expiry`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if report_expiry is not None and report_expiry < 1:  # noqa: E501
            raise ValueError("Invalid value for `report_expiry`, must be a value greater than or equal to `1`")  # noqa: E501

        self._report_expiry = report_expiry

    @property
    def scan_cloudpool_timeout(self):
        """Gets the scan_cloudpool_timeout of this AvscanSettingsSettings.  # noqa: E501

        How many seconds SMB will wait for an AV scan of a cloudpool to complete.  # noqa: E501

        :return: The scan_cloudpool_timeout of this AvscanSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._scan_cloudpool_timeout

    @scan_cloudpool_timeout.setter
    def scan_cloudpool_timeout(self, scan_cloudpool_timeout):
        """Sets the scan_cloudpool_timeout of this AvscanSettingsSettings.

        How many seconds SMB will wait for an AV scan of a cloudpool to complete.  # noqa: E501

        :param scan_cloudpool_timeout: The scan_cloudpool_timeout of this AvscanSettingsSettings.  # noqa: E501
        :type: int
        """
        if scan_cloudpool_timeout is not None and scan_cloudpool_timeout > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `scan_cloudpool_timeout`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if scan_cloudpool_timeout is not None and scan_cloudpool_timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `scan_cloudpool_timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._scan_cloudpool_timeout = scan_cloudpool_timeout

    @property
    def scan_size_maximum(self):
        """Gets the scan_size_maximum of this AvscanSettingsSettings.  # noqa: E501

        Maximum size file that will be scanned (in kBs). 0 means no limit.  # noqa: E501

        :return: The scan_size_maximum of this AvscanSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._scan_size_maximum

    @scan_size_maximum.setter
    def scan_size_maximum(self, scan_size_maximum):
        """Sets the scan_size_maximum of this AvscanSettingsSettings.

        Maximum size file that will be scanned (in kBs). 0 means no limit.  # noqa: E501

        :param scan_size_maximum: The scan_size_maximum of this AvscanSettingsSettings.  # noqa: E501
        :type: int
        """
        if scan_size_maximum is not None and scan_size_maximum > 17179869184:  # noqa: E501
            raise ValueError("Invalid value for `scan_size_maximum`, must be a value less than or equal to `17179869184`")  # noqa: E501
        if scan_size_maximum is not None and scan_size_maximum < 0:  # noqa: E501
            raise ValueError("Invalid value for `scan_size_maximum`, must be a value greater than or equal to `0`")  # noqa: E501

        self._scan_size_maximum = scan_size_maximum

    @property
    def scan_timeout(self):
        """Gets the scan_timeout of this AvscanSettingsSettings.  # noqa: E501

        How many seconds SMB will wait for an AV scan to complete.  # noqa: E501

        :return: The scan_timeout of this AvscanSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._scan_timeout

    @scan_timeout.setter
    def scan_timeout(self, scan_timeout):
        """Sets the scan_timeout of this AvscanSettingsSettings.

        How many seconds SMB will wait for an AV scan to complete.  # noqa: E501

        :param scan_timeout: The scan_timeout of this AvscanSettingsSettings.  # noqa: E501
        :type: int
        """
        if scan_timeout is not None and scan_timeout > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `scan_timeout`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if scan_timeout is not None and scan_timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `scan_timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._scan_timeout = scan_timeout

    @property
    def scan_zones(self):
        """Gets the scan_zones of this AvscanSettingsSettings.  # noqa: E501

        Array of access zones that are enabled for antivirus scanning.  # noqa: E501

        :return: The scan_zones of this AvscanSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._scan_zones

    @scan_zones.setter
    def scan_zones(self, scan_zones):
        """Sets the scan_zones of this AvscanSettingsSettings.

        Array of access zones that are enabled for antivirus scanning.  # noqa: E501

        :param scan_zones: The scan_zones of this AvscanSettingsSettings.  # noqa: E501
        :type: list[str]
        """

        self._scan_zones = scan_zones

    @property
    def service_enabled(self):
        """Gets the service_enabled of this AvscanSettingsSettings.  # noqa: E501

        CAVA antivirus service is on/off.  # noqa: E501

        :return: The service_enabled of this AvscanSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._service_enabled

    @service_enabled.setter
    def service_enabled(self, service_enabled):
        """Sets the service_enabled of this AvscanSettingsSettings.

        CAVA antivirus service is on/off.  # noqa: E501

        :param service_enabled: The service_enabled of this AvscanSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._service_enabled = service_enabled

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
        if not isinstance(other, AvscanSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
