# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_3_0.models.antivirus_policy import AntivirusPolicy  # noqa: F401,E501


class AntivirusPolicyCreateParams(object):
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
        'force_run': 'bool',
        'impact': 'str',
        'name': 'str',
        'paths': 'list[str]',
        'recursion_depth': 'int',
        'schedule': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'force_run': 'force_run',
        'impact': 'impact',
        'name': 'name',
        'paths': 'paths',
        'recursion_depth': 'recursion_depth',
        'schedule': 'schedule'
    }

    def __init__(self, description=None, enabled=None, force_run=None, impact=None, name=None, paths=None, recursion_depth=None, schedule=None):  # noqa: E501
        """AntivirusPolicyCreateParams - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._enabled = None
        self._force_run = None
        self._impact = None
        self._name = None
        self._paths = None
        self._recursion_depth = None
        self._schedule = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if force_run is not None:
            self.force_run = force_run
        if impact is not None:
            self.impact = impact
        self.name = name
        if paths is not None:
            self.paths = paths
        if recursion_depth is not None:
            self.recursion_depth = recursion_depth
        if schedule is not None:
            self.schedule = schedule

    @property
    def description(self):
        """Gets the description of this AntivirusPolicyCreateParams.  # noqa: E501

        A description for the policy.  # noqa: E501

        :return: The description of this AntivirusPolicyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AntivirusPolicyCreateParams.

        A description for the policy.  # noqa: E501

        :param description: The description of this AntivirusPolicyCreateParams.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this AntivirusPolicyCreateParams.  # noqa: E501

        Whether the policy is enabled.  # noqa: E501

        :return: The enabled of this AntivirusPolicyCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AntivirusPolicyCreateParams.

        Whether the policy is enabled.  # noqa: E501

        :param enabled: The enabled of this AntivirusPolicyCreateParams.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def force_run(self):
        """Gets the force_run of this AntivirusPolicyCreateParams.  # noqa: E501

        Forces the scan to run regardless of whether the files were recently scanned.  # noqa: E501

        :return: The force_run of this AntivirusPolicyCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._force_run

    @force_run.setter
    def force_run(self, force_run):
        """Sets the force_run of this AntivirusPolicyCreateParams.

        Forces the scan to run regardless of whether the files were recently scanned.  # noqa: E501

        :param force_run: The force_run of this AntivirusPolicyCreateParams.  # noqa: E501
        :type: bool
        """

        self._force_run = force_run

    @property
    def impact(self):
        """Gets the impact of this AntivirusPolicyCreateParams.  # noqa: E501


        :return: The impact of this AntivirusPolicyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this AntivirusPolicyCreateParams.


        :param impact: The impact of this AntivirusPolicyCreateParams.  # noqa: E501
        :type: str
        """
        if impact is not None and len(impact) > 255:
            raise ValueError("Invalid value for `impact`, length must be less than or equal to `255`")  # noqa: E501
        if impact is not None and len(impact) < 0:
            raise ValueError("Invalid value for `impact`, length must be greater than or equal to `0`")  # noqa: E501

        self._impact = impact

    @property
    def name(self):
        """Gets the name of this AntivirusPolicyCreateParams.  # noqa: E501

        The name of the policy.  # noqa: E501

        :return: The name of this AntivirusPolicyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AntivirusPolicyCreateParams.

        The name of the policy.  # noqa: E501

        :param name: The name of this AntivirusPolicyCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def paths(self):
        """Gets the paths of this AntivirusPolicyCreateParams.  # noqa: E501

        Paths to include in the scan.  # noqa: E501

        :return: The paths of this AntivirusPolicyCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this AntivirusPolicyCreateParams.

        Paths to include in the scan.  # noqa: E501

        :param paths: The paths of this AntivirusPolicyCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._paths = paths

    @property
    def recursion_depth(self):
        """Gets the recursion_depth of this AntivirusPolicyCreateParams.  # noqa: E501

        The depth to recurse in directories.  The default of -1 gives unlimited recursion.  # noqa: E501

        :return: The recursion_depth of this AntivirusPolicyCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._recursion_depth

    @recursion_depth.setter
    def recursion_depth(self, recursion_depth):
        """Sets the recursion_depth of this AntivirusPolicyCreateParams.

        The depth to recurse in directories.  The default of -1 gives unlimited recursion.  # noqa: E501

        :param recursion_depth: The recursion_depth of this AntivirusPolicyCreateParams.  # noqa: E501
        :type: int
        """
        if recursion_depth is not None and recursion_depth > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `recursion_depth`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if recursion_depth is not None and recursion_depth < -1:  # noqa: E501
            raise ValueError("Invalid value for `recursion_depth`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._recursion_depth = recursion_depth

    @property
    def schedule(self):
        """Gets the schedule of this AntivirusPolicyCreateParams.  # noqa: E501


        :return: The schedule of this AntivirusPolicyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AntivirusPolicyCreateParams.


        :param schedule: The schedule of this AntivirusPolicyCreateParams.  # noqa: E501
        :type: str
        """
        if schedule is not None and len(schedule) > 255:
            raise ValueError("Invalid value for `schedule`, length must be less than or equal to `255`")  # noqa: E501
        if schedule is not None and len(schedule) < 0:
            raise ValueError("Invalid value for `schedule`, length must be greater than or equal to `0`")  # noqa: E501

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
        if not isinstance(other, AntivirusPolicyCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
