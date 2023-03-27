# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 12
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NodeDriveconfigNodeStall(object):
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
        'clear_time': 'int',
        'diskscrub_stripes': 'int',
        'max_error_frequency': 'int',
        'max_slow_access': 'int',
        'max_slow_frequency': 'int',
        'max_total_stall_time': 'int',
        'scan_max_ecc_delay': 'int',
        'scan_size': 'int',
        'sleep': 'int'
    }

    attribute_map = {
        'clear_time': 'clear_time',
        'diskscrub_stripes': 'diskscrub_stripes',
        'max_error_frequency': 'max_error_frequency',
        'max_slow_access': 'max_slow_access',
        'max_slow_frequency': 'max_slow_frequency',
        'max_total_stall_time': 'max_total_stall_time',
        'scan_max_ecc_delay': 'scan_max_ecc_delay',
        'scan_size': 'scan_size',
        'sleep': 'sleep'
    }

    def __init__(self, clear_time=None, diskscrub_stripes=None, max_error_frequency=None, max_slow_access=None, max_slow_frequency=None, max_total_stall_time=None, scan_max_ecc_delay=None, scan_size=None, sleep=None):  # noqa: E501
        """NodeDriveconfigNodeStall - a model defined in Swagger"""  # noqa: E501

        self._clear_time = None
        self._diskscrub_stripes = None
        self._max_error_frequency = None
        self._max_slow_access = None
        self._max_slow_frequency = None
        self._max_total_stall_time = None
        self._scan_max_ecc_delay = None
        self._scan_size = None
        self._sleep = None
        self.discriminator = None

        if clear_time is not None:
            self.clear_time = clear_time
        if diskscrub_stripes is not None:
            self.diskscrub_stripes = diskscrub_stripes
        if max_error_frequency is not None:
            self.max_error_frequency = max_error_frequency
        if max_slow_access is not None:
            self.max_slow_access = max_slow_access
        if max_slow_frequency is not None:
            self.max_slow_frequency = max_slow_frequency
        if max_total_stall_time is not None:
            self.max_total_stall_time = max_total_stall_time
        if scan_max_ecc_delay is not None:
            self.scan_max_ecc_delay = scan_max_ecc_delay
        if scan_size is not None:
            self.scan_size = scan_size
        if sleep is not None:
            self.sleep = sleep

    @property
    def clear_time(self):
        """Gets the clear_time of this NodeDriveconfigNodeStall.  # noqa: E501

        The amount of time in seconds with no stalls before ignoring previous stalls.  # noqa: E501

        :return: The clear_time of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._clear_time

    @clear_time.setter
    def clear_time(self, clear_time):
        """Sets the clear_time of this NodeDriveconfigNodeStall.

        The amount of time in seconds with no stalls before ignoring previous stalls.  # noqa: E501

        :param clear_time: The clear_time of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if clear_time is not None and clear_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `clear_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if clear_time is not None and clear_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `clear_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._clear_time = clear_time

    @property
    def diskscrub_stripes(self):
        """Gets the diskscrub_stripes of this NodeDriveconfigNodeStall.  # noqa: E501

        Number of stripes to read during a diskscrub.  # noqa: E501

        :return: The diskscrub_stripes of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._diskscrub_stripes

    @diskscrub_stripes.setter
    def diskscrub_stripes(self, diskscrub_stripes):
        """Sets the diskscrub_stripes of this NodeDriveconfigNodeStall.

        Number of stripes to read during a diskscrub.  # noqa: E501

        :param diskscrub_stripes: The diskscrub_stripes of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if diskscrub_stripes is not None and diskscrub_stripes > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `diskscrub_stripes`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if diskscrub_stripes is not None and diskscrub_stripes < 0:  # noqa: E501
            raise ValueError("Invalid value for `diskscrub_stripes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._diskscrub_stripes = diskscrub_stripes

    @property
    def max_error_frequency(self):
        """Gets the max_error_frequency of this NodeDriveconfigNodeStall.  # noqa: E501

        The number of errors during stalled drive disk exercises to cause the drive to be softfailed.  # noqa: E501

        :return: The max_error_frequency of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._max_error_frequency

    @max_error_frequency.setter
    def max_error_frequency(self, max_error_frequency):
        """Sets the max_error_frequency of this NodeDriveconfigNodeStall.

        The number of errors during stalled drive disk exercises to cause the drive to be softfailed.  # noqa: E501

        :param max_error_frequency: The max_error_frequency of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if max_error_frequency is not None and max_error_frequency > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `max_error_frequency`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if max_error_frequency is not None and max_error_frequency < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_error_frequency`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_error_frequency = max_error_frequency

    @property
    def max_slow_access(self):
        """Gets the max_slow_access of this NodeDriveconfigNodeStall.  # noqa: E501

        The number of slow accesses during stalled drive disk exercises to cause the drive to be softfailed.  # noqa: E501

        :return: The max_slow_access of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._max_slow_access

    @max_slow_access.setter
    def max_slow_access(self, max_slow_access):
        """Sets the max_slow_access of this NodeDriveconfigNodeStall.

        The number of slow accesses during stalled drive disk exercises to cause the drive to be softfailed.  # noqa: E501

        :param max_slow_access: The max_slow_access of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if max_slow_access is not None and max_slow_access > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `max_slow_access`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if max_slow_access is not None and max_slow_access < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_slow_access`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_slow_access = max_slow_access

    @property
    def max_slow_frequency(self):
        """Gets the max_slow_frequency of this NodeDriveconfigNodeStall.  # noqa: E501

        The number of slow frequency triggers during stalled drive disk exercises to cause the drive to be softfailed.  # noqa: E501

        :return: The max_slow_frequency of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._max_slow_frequency

    @max_slow_frequency.setter
    def max_slow_frequency(self, max_slow_frequency):
        """Sets the max_slow_frequency of this NodeDriveconfigNodeStall.

        The number of slow frequency triggers during stalled drive disk exercises to cause the drive to be softfailed.  # noqa: E501

        :param max_slow_frequency: The max_slow_frequency of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if max_slow_frequency is not None and max_slow_frequency > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `max_slow_frequency`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if max_slow_frequency is not None and max_slow_frequency < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_slow_frequency`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_slow_frequency = max_slow_frequency

    @property
    def max_total_stall_time(self):
        """Gets the max_total_stall_time of this NodeDriveconfigNodeStall.  # noqa: E501

        The maximum amount of time, in seconds, to remain stalled before softfailing the drive.  # noqa: E501

        :return: The max_total_stall_time of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._max_total_stall_time

    @max_total_stall_time.setter
    def max_total_stall_time(self, max_total_stall_time):
        """Sets the max_total_stall_time of this NodeDriveconfigNodeStall.

        The maximum amount of time, in seconds, to remain stalled before softfailing the drive.  # noqa: E501

        :param max_total_stall_time: The max_total_stall_time of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if max_total_stall_time is not None and max_total_stall_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `max_total_stall_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if max_total_stall_time is not None and max_total_stall_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_total_stall_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_total_stall_time = max_total_stall_time

    @property
    def scan_max_ecc_delay(self):
        """Gets the scan_max_ecc_delay of this NodeDriveconfigNodeStall.  # noqa: E501

        Maximum delay in seconds after an ECC correction during a scan.  # noqa: E501

        :return: The scan_max_ecc_delay of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._scan_max_ecc_delay

    @scan_max_ecc_delay.setter
    def scan_max_ecc_delay(self, scan_max_ecc_delay):
        """Sets the scan_max_ecc_delay of this NodeDriveconfigNodeStall.

        Maximum delay in seconds after an ECC correction during a scan.  # noqa: E501

        :param scan_max_ecc_delay: The scan_max_ecc_delay of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if scan_max_ecc_delay is not None and scan_max_ecc_delay > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `scan_max_ecc_delay`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if scan_max_ecc_delay is not None and scan_max_ecc_delay < 0:  # noqa: E501
            raise ValueError("Invalid value for `scan_max_ecc_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._scan_max_ecc_delay = scan_max_ecc_delay

    @property
    def scan_size(self):
        """Gets the scan_size of this NodeDriveconfigNodeStall.  # noqa: E501

        Total bytes of error-free reads to complete a scan.  # noqa: E501

        :return: The scan_size of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._scan_size

    @scan_size.setter
    def scan_size(self, scan_size):
        """Sets the scan_size of this NodeDriveconfigNodeStall.

        Total bytes of error-free reads to complete a scan.  # noqa: E501

        :param scan_size: The scan_size of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if scan_size is not None and scan_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `scan_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if scan_size is not None and scan_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `scan_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._scan_size = scan_size

    @property
    def sleep(self):
        """Gets the sleep of this NodeDriveconfigNodeStall.  # noqa: E501

        Delay in seconds between evaluations.  # noqa: E501

        :return: The sleep of this NodeDriveconfigNodeStall.  # noqa: E501
        :rtype: int
        """
        return self._sleep

    @sleep.setter
    def sleep(self, sleep):
        """Sets the sleep of this NodeDriveconfigNodeStall.

        Delay in seconds between evaluations.  # noqa: E501

        :param sleep: The sleep of this NodeDriveconfigNodeStall.  # noqa: E501
        :type: int
        """
        if sleep is not None and sleep > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `sleep`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if sleep is not None and sleep < 0:  # noqa: E501
            raise ValueError("Invalid value for `sleep`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sleep = sleep

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
        if not isinstance(other, NodeDriveconfigNodeStall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
