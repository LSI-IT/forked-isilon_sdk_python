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

from isilon_sdk.v9_0_0.models.diagnostics_gather_status_gather_status import DiagnosticsGatherStatusGatherStatus  # noqa: F401,E501


class DiagnosticsGatherStatusGather(object):
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
        'path': 'str',
        'status': 'DiagnosticsGatherStatusGatherStatus'
    }

    attribute_map = {
        'path': 'path',
        'status': 'status'
    }

    def __init__(self, path=None, status=None):  # noqa: E501
        """DiagnosticsGatherStatusGather - a model defined in Swagger"""  # noqa: E501

        self._path = None
        self._status = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if status is not None:
            self.status = status

    @property
    def path(self):
        """Gets the path of this DiagnosticsGatherStatusGather.  # noqa: E501


        :return: The path of this DiagnosticsGatherStatusGather.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DiagnosticsGatherStatusGather.


        :param path: The path of this DiagnosticsGatherStatusGather.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def status(self):
        """Gets the status of this DiagnosticsGatherStatusGather.  # noqa: E501

          # noqa: E501

        :return: The status of this DiagnosticsGatherStatusGather.  # noqa: E501
        :rtype: DiagnosticsGatherStatusGatherStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DiagnosticsGatherStatusGather.

          # noqa: E501

        :param status: The status of this DiagnosticsGatherStatusGather.  # noqa: E501
        :type: DiagnosticsGatherStatusGatherStatus
        """

        self._status = status

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
        if not isinstance(other, DiagnosticsGatherStatusGather):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
