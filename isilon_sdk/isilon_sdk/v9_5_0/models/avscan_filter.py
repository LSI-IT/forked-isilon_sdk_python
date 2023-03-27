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


class AvscanFilter(object):
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
        'file_extension_action': 'str',
        'file_extensions': 'list[str]',
        'filter_enabled': 'bool',
        'id': 'str',
        'open_on_fail': 'bool',
        'paths_to_exclude': 'list[str]',
        'scan_cloudpool_files': 'bool',
        'scan_if_no_extension': 'bool',
        'scan_on_close': 'bool',
        'scan_on_read': 'bool',
        'scan_on_rename': 'bool',
        'scan_profile': 'str',
        'zone_name': 'str'
    }

    attribute_map = {
        'file_extension_action': 'file_extension_action',
        'file_extensions': 'file_extensions',
        'filter_enabled': 'filter_enabled',
        'id': 'id',
        'open_on_fail': 'open_on_fail',
        'paths_to_exclude': 'paths_to_exclude',
        'scan_cloudpool_files': 'scan_cloudpool_files',
        'scan_if_no_extension': 'scan_if_no_extension',
        'scan_on_close': 'scan_on_close',
        'scan_on_read': 'scan_on_read',
        'scan_on_rename': 'scan_on_rename',
        'scan_profile': 'scan_profile',
        'zone_name': 'zone_name'
    }

    def __init__(self, file_extension_action=None, file_extensions=None, filter_enabled=None, id=None, open_on_fail=None, paths_to_exclude=None, scan_cloudpool_files=None, scan_if_no_extension=None, scan_on_close=None, scan_on_read=None, scan_on_rename=None, scan_profile=None, zone_name=None):  # noqa: E501
        """AvscanFilter - a model defined in Swagger"""  # noqa: E501

        self._file_extension_action = None
        self._file_extensions = None
        self._filter_enabled = None
        self._id = None
        self._open_on_fail = None
        self._paths_to_exclude = None
        self._scan_cloudpool_files = None
        self._scan_if_no_extension = None
        self._scan_on_close = None
        self._scan_on_read = None
        self._scan_on_rename = None
        self._scan_profile = None
        self._zone_name = None
        self.discriminator = None

        if file_extension_action is not None:
            self.file_extension_action = file_extension_action
        if file_extensions is not None:
            self.file_extensions = file_extensions
        if filter_enabled is not None:
            self.filter_enabled = filter_enabled
        if id is not None:
            self.id = id
        if open_on_fail is not None:
            self.open_on_fail = open_on_fail
        if paths_to_exclude is not None:
            self.paths_to_exclude = paths_to_exclude
        if scan_cloudpool_files is not None:
            self.scan_cloudpool_files = scan_cloudpool_files
        if scan_if_no_extension is not None:
            self.scan_if_no_extension = scan_if_no_extension
        if scan_on_close is not None:
            self.scan_on_close = scan_on_close
        if scan_on_read is not None:
            self.scan_on_read = scan_on_read
        if scan_on_rename is not None:
            self.scan_on_rename = scan_on_rename
        if scan_profile is not None:
            self.scan_profile = scan_profile
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def file_extension_action(self):
        """Gets the file_extension_action of this AvscanFilter.  # noqa: E501

        When a file matches an entry in the list of file extensions, do we include or exclude it?.  # noqa: E501

        :return: The file_extension_action of this AvscanFilter.  # noqa: E501
        :rtype: str
        """
        return self._file_extension_action

    @file_extension_action.setter
    def file_extension_action(self, file_extension_action):
        """Sets the file_extension_action of this AvscanFilter.

        When a file matches an entry in the list of file extensions, do we include or exclude it?.  # noqa: E501

        :param file_extension_action: The file_extension_action of this AvscanFilter.  # noqa: E501
        :type: str
        """

        self._file_extension_action = file_extension_action

    @property
    def file_extensions(self):
        """Gets the file_extensions of this AvscanFilter.  # noqa: E501

        Array of file extensions to use in scanning decision.  # noqa: E501

        :return: The file_extensions of this AvscanFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_extensions

    @file_extensions.setter
    def file_extensions(self, file_extensions):
        """Sets the file_extensions of this AvscanFilter.

        Array of file extensions to use in scanning decision.  # noqa: E501

        :param file_extensions: The file_extensions of this AvscanFilter.  # noqa: E501
        :type: list[str]
        """

        self._file_extensions = file_extensions

    @property
    def filter_enabled(self):
        """Gets the filter_enabled of this AvscanFilter.  # noqa: E501

        Access zone enabled for AV scanning.  # noqa: E501

        :return: The filter_enabled of this AvscanFilter.  # noqa: E501
        :rtype: bool
        """
        return self._filter_enabled

    @filter_enabled.setter
    def filter_enabled(self, filter_enabled):
        """Sets the filter_enabled of this AvscanFilter.

        Access zone enabled for AV scanning.  # noqa: E501

        :param filter_enabled: The filter_enabled of this AvscanFilter.  # noqa: E501
        :type: bool
        """

        self._filter_enabled = filter_enabled

    @property
    def id(self):
        """Gets the id of this AvscanFilter.  # noqa: E501

        A unique identifier for the zone.  # noqa: E501

        :return: The id of this AvscanFilter.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvscanFilter.

        A unique identifier for the zone.  # noqa: E501

        :param id: The id of this AvscanFilter.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 128:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `128`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def open_on_fail(self):
        """Gets the open_on_fail of this AvscanFilter.  # noqa: E501

        Allow access to files when scanning fails.  # noqa: E501

        :return: The open_on_fail of this AvscanFilter.  # noqa: E501
        :rtype: bool
        """
        return self._open_on_fail

    @open_on_fail.setter
    def open_on_fail(self, open_on_fail):
        """Sets the open_on_fail of this AvscanFilter.

        Allow access to files when scanning fails.  # noqa: E501

        :param open_on_fail: The open_on_fail of this AvscanFilter.  # noqa: E501
        :type: bool
        """

        self._open_on_fail = open_on_fail

    @property
    def paths_to_exclude(self):
        """Gets the paths_to_exclude of this AvscanFilter.  # noqa: E501

        Array of relative paths under zone root not to scan.  # noqa: E501

        :return: The paths_to_exclude of this AvscanFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths_to_exclude

    @paths_to_exclude.setter
    def paths_to_exclude(self, paths_to_exclude):
        """Sets the paths_to_exclude of this AvscanFilter.

        Array of relative paths under zone root not to scan.  # noqa: E501

        :param paths_to_exclude: The paths_to_exclude of this AvscanFilter.  # noqa: E501
        :type: list[str]
        """

        self._paths_to_exclude = paths_to_exclude

    @property
    def scan_cloudpool_files(self):
        """Gets the scan_cloudpool_files of this AvscanFilter.  # noqa: E501

        Perform real-time scans of cloudpool files?  # noqa: E501

        :return: The scan_cloudpool_files of this AvscanFilter.  # noqa: E501
        :rtype: bool
        """
        return self._scan_cloudpool_files

    @scan_cloudpool_files.setter
    def scan_cloudpool_files(self, scan_cloudpool_files):
        """Sets the scan_cloudpool_files of this AvscanFilter.

        Perform real-time scans of cloudpool files?  # noqa: E501

        :param scan_cloudpool_files: The scan_cloudpool_files of this AvscanFilter.  # noqa: E501
        :type: bool
        """

        self._scan_cloudpool_files = scan_cloudpool_files

    @property
    def scan_if_no_extension(self):
        """Gets the scan_if_no_extension of this AvscanFilter.  # noqa: E501

        Scan files without extensions?  # noqa: E501

        :return: The scan_if_no_extension of this AvscanFilter.  # noqa: E501
        :rtype: bool
        """
        return self._scan_if_no_extension

    @scan_if_no_extension.setter
    def scan_if_no_extension(self, scan_if_no_extension):
        """Sets the scan_if_no_extension of this AvscanFilter.

        Scan files without extensions?  # noqa: E501

        :param scan_if_no_extension: The scan_if_no_extension of this AvscanFilter.  # noqa: E501
        :type: bool
        """

        self._scan_if_no_extension = scan_if_no_extension

    @property
    def scan_on_close(self):
        """Gets the scan_on_close of this AvscanFilter.  # noqa: E501

        Perform real-time scans of files when the file handle is closed.  # noqa: E501

        :return: The scan_on_close of this AvscanFilter.  # noqa: E501
        :rtype: bool
        """
        return self._scan_on_close

    @scan_on_close.setter
    def scan_on_close(self, scan_on_close):
        """Sets the scan_on_close of this AvscanFilter.

        Perform real-time scans of files when the file handle is closed.  # noqa: E501

        :param scan_on_close: The scan_on_close of this AvscanFilter.  # noqa: E501
        :type: bool
        """

        self._scan_on_close = scan_on_close

    @property
    def scan_on_read(self):
        """Gets the scan_on_read of this AvscanFilter.  # noqa: E501

        Perform real-time scans of files on first file read.  # noqa: E501

        :return: The scan_on_read of this AvscanFilter.  # noqa: E501
        :rtype: bool
        """
        return self._scan_on_read

    @scan_on_read.setter
    def scan_on_read(self, scan_on_read):
        """Sets the scan_on_read of this AvscanFilter.

        Perform real-time scans of files on first file read.  # noqa: E501

        :param scan_on_read: The scan_on_read of this AvscanFilter.  # noqa: E501
        :type: bool
        """

        self._scan_on_read = scan_on_read

    @property
    def scan_on_rename(self):
        """Gets the scan_on_rename of this AvscanFilter.  # noqa: E501

        Perform real-time scan of file when the file is renamed.  # noqa: E501

        :return: The scan_on_rename of this AvscanFilter.  # noqa: E501
        :rtype: bool
        """
        return self._scan_on_rename

    @scan_on_rename.setter
    def scan_on_rename(self, scan_on_rename):
        """Sets the scan_on_rename of this AvscanFilter.

        Perform real-time scan of file when the file is renamed.  # noqa: E501

        :param scan_on_rename: The scan_on_rename of this AvscanFilter.  # noqa: E501
        :type: bool
        """

        self._scan_on_rename = scan_on_rename

    @property
    def scan_profile(self):
        """Gets the scan_profile of this AvscanFilter.  # noqa: E501

        Type of scan profile applicable to the zone.  # noqa: E501

        :return: The scan_profile of this AvscanFilter.  # noqa: E501
        :rtype: str
        """
        return self._scan_profile

    @scan_profile.setter
    def scan_profile(self, scan_profile):
        """Sets the scan_profile of this AvscanFilter.

        Type of scan profile applicable to the zone.  # noqa: E501

        :param scan_profile: The scan_profile of this AvscanFilter.  # noqa: E501
        :type: str
        """

        self._scan_profile = scan_profile

    @property
    def zone_name(self):
        """Gets the zone_name of this AvscanFilter.  # noqa: E501

        Access zone name containing filter settings.  # noqa: E501

        :return: The zone_name of this AvscanFilter.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this AvscanFilter.

        Access zone name containing filter settings.  # noqa: E501

        :param zone_name: The zone_name of this AvscanFilter.  # noqa: E501
        :type: str
        """
        if zone_name is not None and len(zone_name) > 255:
            raise ValueError("Invalid value for `zone_name`, length must be less than or equal to `255`")  # noqa: E501
        if zone_name is not None and len(zone_name) < 1:
            raise ValueError("Invalid value for `zone_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._zone_name = zone_name

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
        if not isinstance(other, AvscanFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
