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


class CreateAntivirusScanItemResponse(object):
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
        'report_id': 'str',
        'result': 'str'
    }

    attribute_map = {
        'report_id': 'report_id',
        'result': 'result'
    }

    def __init__(self, report_id=None, result=None):  # noqa: E501
        """CreateAntivirusScanItemResponse - a model defined in Swagger"""  # noqa: E501

        self._report_id = None
        self._result = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if result is not None:
            self.result = result

    @property
    def report_id(self):
        """Gets the report_id of this CreateAntivirusScanItemResponse.  # noqa: E501

        The ID for the report for this scan. A report ID will be generated if one is not provided.   # noqa: E501

        :return: The report_id of this CreateAntivirusScanItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this CreateAntivirusScanItemResponse.

        The ID for the report for this scan. A report ID will be generated if one is not provided.   # noqa: E501

        :param report_id: The report_id of this CreateAntivirusScanItemResponse.  # noqa: E501
        :type: str
        """
        if report_id is not None and len(report_id) > 255:
            raise ValueError("Invalid value for `report_id`, length must be less than or equal to `255`")  # noqa: E501
        if report_id is not None and len(report_id) < 0:
            raise ValueError("Invalid value for `report_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._report_id = report_id

    @property
    def result(self):
        """Gets the result of this CreateAntivirusScanItemResponse.  # noqa: E501

        The result of the scan.  # noqa: E501

        :return: The result of this CreateAntivirusScanItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CreateAntivirusScanItemResponse.

        The result of the scan.  # noqa: E501

        :param result: The result of this CreateAntivirusScanItemResponse.  # noqa: E501
        :type: str
        """
        if result is not None and len(result) > 255:
            raise ValueError("Invalid value for `result`, length must be less than or equal to `255`")  # noqa: E501
        if result is not None and len(result) < 0:
            raise ValueError("Invalid value for `result`, length must be greater than or equal to `0`")  # noqa: E501

        self._result = result

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
        if not isinstance(other, CreateAntivirusScanItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
