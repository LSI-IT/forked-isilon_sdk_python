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

from isilon_sdk.v9_5_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.quota_quota_thresholds import QuotaQuotaThresholds  # noqa: F401,E501


class QuotaQuotaCreateParams(object):
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
        'container': 'bool',
        'description': 'str',
        'enforced': 'bool',
        'force': 'bool',
        'ignore_limit_checks': 'bool',
        'include_snapshots': 'bool',
        'labels': 'str',
        'path': 'str',
        'persona': 'AuthAccessAccessItemFileGroup',
        'thresholds': 'QuotaQuotaThresholds',
        'thresholds_include_overhead': 'bool',
        'thresholds_on': 'str',
        'type': 'str'
    }

    attribute_map = {
        'container': 'container',
        'description': 'description',
        'enforced': 'enforced',
        'force': 'force',
        'ignore_limit_checks': 'ignore_limit_checks',
        'include_snapshots': 'include_snapshots',
        'labels': 'labels',
        'path': 'path',
        'persona': 'persona',
        'thresholds': 'thresholds',
        'thresholds_include_overhead': 'thresholds_include_overhead',
        'thresholds_on': 'thresholds_on',
        'type': 'type'
    }

    def __init__(self, container=None, description=None, enforced=None, force=None, ignore_limit_checks=None, include_snapshots=None, labels=None, path=None, persona=None, thresholds=None, thresholds_include_overhead=None, thresholds_on='fslogicalsize', type=None):  # noqa: E501
        """QuotaQuotaCreateParams - a model defined in Swagger"""  # noqa: E501

        self._container = None
        self._description = None
        self._enforced = None
        self._force = None
        self._ignore_limit_checks = None
        self._include_snapshots = None
        self._labels = None
        self._path = None
        self._persona = None
        self._thresholds = None
        self._thresholds_include_overhead = None
        self._thresholds_on = None
        self._type = None
        self.discriminator = None

        if container is not None:
            self.container = container
        if description is not None:
            self.description = description
        if enforced is not None:
            self.enforced = enforced
        if force is not None:
            self.force = force
        if ignore_limit_checks is not None:
            self.ignore_limit_checks = ignore_limit_checks
        self.include_snapshots = include_snapshots
        if labels is not None:
            self.labels = labels
        self.path = path
        if persona is not None:
            self.persona = persona
        if thresholds is not None:
            self.thresholds = thresholds
        if thresholds_include_overhead is not None:
            self.thresholds_include_overhead = thresholds_include_overhead
        if thresholds_on is not None:
            self.thresholds_on = thresholds_on
        self.type = type

    @property
    def container(self):
        """Gets the container of this QuotaQuotaCreateParams.  # noqa: E501

        If true, SMB shares using the quota directory see the quota thresholds as share size.  # noqa: E501

        :return: The container of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this QuotaQuotaCreateParams.

        If true, SMB shares using the quota directory see the quota thresholds as share size.  # noqa: E501

        :param container: The container of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """

        self._container = container

    @property
    def description(self):
        """Gets the description of this QuotaQuotaCreateParams.  # noqa: E501

        Free form text description of the quota.  # noqa: E501

        :return: The description of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QuotaQuotaCreateParams.

        Free form text description of the quota.  # noqa: E501

        :param description: The description of this QuotaQuotaCreateParams.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def enforced(self):
        """Gets the enforced of this QuotaQuotaCreateParams.  # noqa: E501

        True if the quota provides enforcement, otherwise an accounting quota.  # noqa: E501

        :return: The enforced of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._enforced

    @enforced.setter
    def enforced(self, enforced):
        """Sets the enforced of this QuotaQuotaCreateParams.

        True if the quota provides enforcement, otherwise an accounting quota.  # noqa: E501

        :param enforced: The enforced of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """

        self._enforced = enforced

    @property
    def force(self):
        """Gets the force of this QuotaQuotaCreateParams.  # noqa: E501

        Force creation of quotas on the root of /ifs or percent based quotas.  # noqa: E501

        :return: The force of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this QuotaQuotaCreateParams.

        Force creation of quotas on the root of /ifs or percent based quotas.  # noqa: E501

        :param force: The force of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def ignore_limit_checks(self):
        """Gets the ignore_limit_checks of this QuotaQuotaCreateParams.  # noqa: E501

        If true, skip child quota's threshold comparison with parent quota path.  # noqa: E501

        :return: The ignore_limit_checks of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_limit_checks

    @ignore_limit_checks.setter
    def ignore_limit_checks(self, ignore_limit_checks):
        """Sets the ignore_limit_checks of this QuotaQuotaCreateParams.

        If true, skip child quota's threshold comparison with parent quota path.  # noqa: E501

        :param ignore_limit_checks: The ignore_limit_checks of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """

        self._ignore_limit_checks = ignore_limit_checks

    @property
    def include_snapshots(self):
        """Gets the include_snapshots of this QuotaQuotaCreateParams.  # noqa: E501

        If true, quota governs snapshot data as well as head data.  # noqa: E501

        :return: The include_snapshots of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._include_snapshots

    @include_snapshots.setter
    def include_snapshots(self, include_snapshots):
        """Sets the include_snapshots of this QuotaQuotaCreateParams.

        If true, quota governs snapshot data as well as head data.  # noqa: E501

        :param include_snapshots: The include_snapshots of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """
        if include_snapshots is None:
            raise ValueError("Invalid value for `include_snapshots`, must not be `None`")  # noqa: E501

        self._include_snapshots = include_snapshots

    @property
    def labels(self):
        """Gets the labels of this QuotaQuotaCreateParams.  # noqa: E501

        Tags to identify a quota domain.  # noqa: E501

        :return: The labels of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this QuotaQuotaCreateParams.

        Tags to identify a quota domain.  # noqa: E501

        :param labels: The labels of this QuotaQuotaCreateParams.  # noqa: E501
        :type: str
        """
        if labels is not None and len(labels) > 1024:
            raise ValueError("Invalid value for `labels`, length must be less than or equal to `1024`")  # noqa: E501
        if labels is not None and len(labels) < 0:
            raise ValueError("Invalid value for `labels`, length must be greater than or equal to `0`")  # noqa: E501

        self._labels = labels

    @property
    def path(self):
        """Gets the path of this QuotaQuotaCreateParams.  # noqa: E501


        :return: The path of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this QuotaQuotaCreateParams.


        :param path: The path of this QuotaQuotaCreateParams.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if path is not None and len(path) > 4096:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `4096`")  # noqa: E501
        if path is not None and len(path) < 4:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `4`")  # noqa: E501
        if path is not None and not re.search('^\/ifs$|^\/ifs\/', path):  # noqa: E501
            raise ValueError("Invalid value for `path`, must be a follow pattern or equal to `/^\/ifs$|^\/ifs\//`")  # noqa: E501

        self._path = path

    @property
    def persona(self):
        """Gets the persona of this QuotaQuotaCreateParams.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The persona of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._persona

    @persona.setter
    def persona(self, persona):
        """Sets the persona of this QuotaQuotaCreateParams.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param persona: The persona of this QuotaQuotaCreateParams.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._persona = persona

    @property
    def thresholds(self):
        """Gets the thresholds of this QuotaQuotaCreateParams.  # noqa: E501

          # noqa: E501

        :return: The thresholds of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: QuotaQuotaThresholds
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this QuotaQuotaCreateParams.

          # noqa: E501

        :param thresholds: The thresholds of this QuotaQuotaCreateParams.  # noqa: E501
        :type: QuotaQuotaThresholds
        """

        self._thresholds = thresholds

    @property
    def thresholds_include_overhead(self):
        """Gets the thresholds_include_overhead of this QuotaQuotaCreateParams.  # noqa: E501

        This option is deprecated. Use the option 'thresholds_on' to select the usage on which thresholds to apply.  # noqa: E501

        :return: The thresholds_include_overhead of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._thresholds_include_overhead

    @thresholds_include_overhead.setter
    def thresholds_include_overhead(self, thresholds_include_overhead):
        """Sets the thresholds_include_overhead of this QuotaQuotaCreateParams.

        This option is deprecated. Use the option 'thresholds_on' to select the usage on which thresholds to apply.  # noqa: E501

        :param thresholds_include_overhead: The thresholds_include_overhead of this QuotaQuotaCreateParams.  # noqa: E501
        :type: bool
        """

        self._thresholds_include_overhead = thresholds_include_overhead

    @property
    def thresholds_on(self):
        """Gets the thresholds_on of this QuotaQuotaCreateParams.  # noqa: E501

        Thresholds apply on quota accounting metric.  # noqa: E501

        :return: The thresholds_on of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._thresholds_on

    @thresholds_on.setter
    def thresholds_on(self, thresholds_on):
        """Sets the thresholds_on of this QuotaQuotaCreateParams.

        Thresholds apply on quota accounting metric.  # noqa: E501

        :param thresholds_on: The thresholds_on of this QuotaQuotaCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["applogicalsize", "fslogicalsize", "physicalsize"]  # noqa: E501
        if thresholds_on not in allowed_values:
            raise ValueError(
                "Invalid value for `thresholds_on` ({0}), must be one of {1}"  # noqa: E501
                .format(thresholds_on, allowed_values)
            )

        self._thresholds_on = thresholds_on

    @property
    def type(self):
        """Gets the type of this QuotaQuotaCreateParams.  # noqa: E501

        The type of quota.  # noqa: E501

        :return: The type of this QuotaQuotaCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaQuotaCreateParams.

        The type of quota.  # noqa: E501

        :param type: The type of this QuotaQuotaCreateParams.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["directory", "user", "group", "default-directory", "default-user", "default-group"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, QuotaQuotaCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
