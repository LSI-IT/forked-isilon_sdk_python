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


class AvscanJobCreateParams(object):
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
        'description': 'str',
        'enabled': 'bool',
        'file_extension_action': 'str',
        'file_extensions': 'list[str]',
        'id': 'str',
        'ignore_previous_scan_status': 'bool',
        'impact': 'str',
        'job_name': 'str',
        'paths_to_exclude': 'list[str]',
        'paths_to_include': 'list[str]',
        'scan_cloudpool_files': 'bool',
        'scan_if_no_extension': 'bool',
        'schedule': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'file_extension_action': 'file_extension_action',
        'file_extensions': 'file_extensions',
        'id': 'id',
        'ignore_previous_scan_status': 'ignore_previous_scan_status',
        'impact': 'impact',
        'job_name': 'job_name',
        'paths_to_exclude': 'paths_to_exclude',
        'paths_to_include': 'paths_to_include',
        'scan_cloudpool_files': 'scan_cloudpool_files',
        'scan_if_no_extension': 'scan_if_no_extension',
        'schedule': 'schedule'
    }

    def __init__(self, description=None, enabled=None, file_extension_action=None, file_extensions=None, id=None, ignore_previous_scan_status=None, impact=None, job_name=None, paths_to_exclude=None, paths_to_include=None, scan_cloudpool_files=None, scan_if_no_extension=None, schedule=None):  # noqa: E501
        """AvscanJobCreateParams - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._enabled = None
        self._file_extension_action = None
        self._file_extensions = None
        self._id = None
        self._ignore_previous_scan_status = None
        self._impact = None
        self._job_name = None
        self._paths_to_exclude = None
        self._paths_to_include = None
        self._scan_cloudpool_files = None
        self._scan_if_no_extension = None
        self._schedule = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if file_extension_action is not None:
            self.file_extension_action = file_extension_action
        if file_extensions is not None:
            self.file_extensions = file_extensions
        if id is not None:
            self.id = id
        if ignore_previous_scan_status is not None:
            self.ignore_previous_scan_status = ignore_previous_scan_status
        if impact is not None:
            self.impact = impact
        self.job_name = job_name
        if paths_to_exclude is not None:
            self.paths_to_exclude = paths_to_exclude
        if paths_to_include is not None:
            self.paths_to_include = paths_to_include
        if scan_cloudpool_files is not None:
            self.scan_cloudpool_files = scan_cloudpool_files
        if scan_if_no_extension is not None:
            self.scan_if_no_extension = scan_if_no_extension
        if schedule is not None:
            self.schedule = schedule

    @property
    def description(self):
        """Gets the description of this AvscanJobCreateParams.  # noqa: E501

        Free-form customer description of job.  # noqa: E501

        :return: The description of this AvscanJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AvscanJobCreateParams.

        Free-form customer description of job.  # noqa: E501

        :param description: The description of this AvscanJobCreateParams.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this AvscanJobCreateParams.  # noqa: E501

        Whether the job is enabled.  # noqa: E501

        :return: The enabled of this AvscanJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AvscanJobCreateParams.

        Whether the job is enabled.  # noqa: E501

        :param enabled: The enabled of this AvscanJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def file_extension_action(self):
        """Gets the file_extension_action of this AvscanJobCreateParams.  # noqa: E501

        When a file matches an entry in the list of file extensions, do we include or exclude it?.  # noqa: E501

        :return: The file_extension_action of this AvscanJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._file_extension_action

    @file_extension_action.setter
    def file_extension_action(self, file_extension_action):
        """Sets the file_extension_action of this AvscanJobCreateParams.

        When a file matches an entry in the list of file extensions, do we include or exclude it?.  # noqa: E501

        :param file_extension_action: The file_extension_action of this AvscanJobCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["include", "exclude"]  # noqa: E501
        if file_extension_action not in allowed_values:
            raise ValueError(
                "Invalid value for `file_extension_action` ({0}), must be one of {1}"  # noqa: E501
                .format(file_extension_action, allowed_values)
            )

        self._file_extension_action = file_extension_action

    @property
    def file_extensions(self):
        """Gets the file_extensions of this AvscanJobCreateParams.  # noqa: E501

        Array of file extensions to use in scanning decision.  # noqa: E501

        :return: The file_extensions of this AvscanJobCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_extensions

    @file_extensions.setter
    def file_extensions(self, file_extensions):
        """Sets the file_extensions of this AvscanJobCreateParams.

        Array of file extensions to use in scanning decision.  # noqa: E501

        :param file_extensions: The file_extensions of this AvscanJobCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._file_extensions = file_extensions

    @property
    def id(self):
        """Gets the id of this AvscanJobCreateParams.  # noqa: E501

        A unique identifier for the job.  # noqa: E501

        :return: The id of this AvscanJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvscanJobCreateParams.

        A unique identifier for the job.  # noqa: E501

        :param id: The id of this AvscanJobCreateParams.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 128:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `128`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def ignore_previous_scan_status(self):
        """Gets the ignore_previous_scan_status of this AvscanJobCreateParams.  # noqa: E501

        If True, force a scan of a previously scanned file.  # noqa: E501

        :return: The ignore_previous_scan_status of this AvscanJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_previous_scan_status

    @ignore_previous_scan_status.setter
    def ignore_previous_scan_status(self, ignore_previous_scan_status):
        """Sets the ignore_previous_scan_status of this AvscanJobCreateParams.

        If True, force a scan of a previously scanned file.  # noqa: E501

        :param ignore_previous_scan_status: The ignore_previous_scan_status of this AvscanJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._ignore_previous_scan_status = ignore_previous_scan_status

    @property
    def impact(self):
        """Gets the impact of this AvscanJobCreateParams.  # noqa: E501

        Specifies an impact policy for the antivirus scan jobs.  # noqa: E501

        :return: The impact of this AvscanJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this AvscanJobCreateParams.

        Specifies an impact policy for the antivirus scan jobs.  # noqa: E501

        :param impact: The impact of this AvscanJobCreateParams.  # noqa: E501
        :type: str
        """
        if impact is not None and len(impact) > 255:
            raise ValueError("Invalid value for `impact`, length must be less than or equal to `255`")  # noqa: E501
        if impact is not None and len(impact) < 1:
            raise ValueError("Invalid value for `impact`, length must be greater than or equal to `1`")  # noqa: E501

        self._impact = impact

    @property
    def job_name(self):
        """Gets the job_name of this AvscanJobCreateParams.  # noqa: E501

        Unique short name for job.  # noqa: E501

        :return: The job_name of this AvscanJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this AvscanJobCreateParams.

        Unique short name for job.  # noqa: E501

        :param job_name: The job_name of this AvscanJobCreateParams.  # noqa: E501
        :type: str
        """
        if job_name is None:
            raise ValueError("Invalid value for `job_name`, must not be `None`")  # noqa: E501
        if job_name is not None and len(job_name) > 128:
            raise ValueError("Invalid value for `job_name`, length must be less than or equal to `128`")  # noqa: E501
        if job_name is not None and len(job_name) < 1:
            raise ValueError("Invalid value for `job_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._job_name = job_name

    @property
    def paths_to_exclude(self):
        """Gets the paths_to_exclude of this AvscanJobCreateParams.  # noqa: E501

        Array of relative paths under paths_to_include not to scan.  # noqa: E501

        :return: The paths_to_exclude of this AvscanJobCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths_to_exclude

    @paths_to_exclude.setter
    def paths_to_exclude(self, paths_to_exclude):
        """Sets the paths_to_exclude of this AvscanJobCreateParams.

        Array of relative paths under paths_to_include not to scan.  # noqa: E501

        :param paths_to_exclude: The paths_to_exclude of this AvscanJobCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._paths_to_exclude = paths_to_exclude

    @property
    def paths_to_include(self):
        """Gets the paths_to_include of this AvscanJobCreateParams.  # noqa: E501

        Array of absolute paths under /ifs to scan.  # noqa: E501

        :return: The paths_to_include of this AvscanJobCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths_to_include

    @paths_to_include.setter
    def paths_to_include(self, paths_to_include):
        """Sets the paths_to_include of this AvscanJobCreateParams.

        Array of absolute paths under /ifs to scan.  # noqa: E501

        :param paths_to_include: The paths_to_include of this AvscanJobCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._paths_to_include = paths_to_include

    @property
    def scan_cloudpool_files(self):
        """Gets the scan_cloudpool_files of this AvscanJobCreateParams.  # noqa: E501

        Perform real-time scans of cloudpool files?  # noqa: E501

        :return: The scan_cloudpool_files of this AvscanJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._scan_cloudpool_files

    @scan_cloudpool_files.setter
    def scan_cloudpool_files(self, scan_cloudpool_files):
        """Sets the scan_cloudpool_files of this AvscanJobCreateParams.

        Perform real-time scans of cloudpool files?  # noqa: E501

        :param scan_cloudpool_files: The scan_cloudpool_files of this AvscanJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._scan_cloudpool_files = scan_cloudpool_files

    @property
    def scan_if_no_extension(self):
        """Gets the scan_if_no_extension of this AvscanJobCreateParams.  # noqa: E501

        Scan files without extensions?  # noqa: E501

        :return: The scan_if_no_extension of this AvscanJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._scan_if_no_extension

    @scan_if_no_extension.setter
    def scan_if_no_extension(self, scan_if_no_extension):
        """Sets the scan_if_no_extension of this AvscanJobCreateParams.

        Scan files without extensions?  # noqa: E501

        :param scan_if_no_extension: The scan_if_no_extension of this AvscanJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._scan_if_no_extension = scan_if_no_extension

    @property
    def schedule(self):
        """Gets the schedule of this AvscanJobCreateParams.  # noqa: E501

        The ever-unfortunate 'schedule' string type, e.g. 'every Thursday at 01:00'.  # noqa: E501

        :return: The schedule of this AvscanJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AvscanJobCreateParams.

        The ever-unfortunate 'schedule' string type, e.g. 'every Thursday at 01:00'.  # noqa: E501

        :param schedule: The schedule of this AvscanJobCreateParams.  # noqa: E501
        :type: str
        """
        if schedule is not None and len(schedule) > 255:
            raise ValueError("Invalid value for `schedule`, length must be less than or equal to `255`")  # noqa: E501
        if schedule is not None and len(schedule) < 1:
            raise ValueError("Invalid value for `schedule`, length must be greater than or equal to `1`")  # noqa: E501

        self._schedule = schedule

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
        if not isinstance(other, AvscanJobCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other