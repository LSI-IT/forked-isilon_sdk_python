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


class LicenseLicenseCreateParams(object):
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
        'evaluation': 'list[str]',
        'license_file_content': 'str',
        'license_file_path': 'str'
    }

    attribute_map = {
        'evaluation': 'evaluation',
        'license_file_content': 'license_file_content',
        'license_file_path': 'license_file_path'
    }

    def __init__(self, evaluation=None, license_file_content=None, license_file_path=None):  # noqa: E501
        """LicenseLicenseCreateParams - a model defined in Swagger"""  # noqa: E501

        self._evaluation = None
        self._license_file_content = None
        self._license_file_path = None
        self.discriminator = None

        if evaluation is not None:
            self.evaluation = evaluation
        if license_file_content is not None:
            self.license_file_content = license_file_content
        if license_file_path is not None:
            self.license_file_path = license_file_path

    @property
    def evaluation(self):
        """Gets the evaluation of this LicenseLicenseCreateParams.  # noqa: E501

        A list of evaluation licenses to enable on the cluster.  # noqa: E501

        :return: The evaluation of this LicenseLicenseCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        """Sets the evaluation of this LicenseLicenseCreateParams.

        A list of evaluation licenses to enable on the cluster.  # noqa: E501

        :param evaluation: The evaluation of this LicenseLicenseCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._evaluation = evaluation

    @property
    def license_file_content(self):
        """Gets the license_file_content of this LicenseLicenseCreateParams.  # noqa: E501

        License file string content. The license file is obtained from Dell EMC's SLC web portal. Do not use with the license_file_path option.  # noqa: E501

        :return: The license_file_content of this LicenseLicenseCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._license_file_content

    @license_file_content.setter
    def license_file_content(self, license_file_content):
        """Sets the license_file_content of this LicenseLicenseCreateParams.

        License file string content. The license file is obtained from Dell EMC's SLC web portal. Do not use with the license_file_path option.  # noqa: E501

        :param license_file_content: The license_file_content of this LicenseLicenseCreateParams.  # noqa: E501
        :type: str
        """
        if license_file_content is not None and len(license_file_content) > 2147483647:
            raise ValueError("Invalid value for `license_file_content`, length must be less than or equal to `2147483647`")  # noqa: E501
        if license_file_content is not None and len(license_file_content) < 1:
            raise ValueError("Invalid value for `license_file_content`, length must be greater than or equal to `1`")  # noqa: E501
        if license_file_content is not None and not re.search('.+', license_file_content):  # noqa: E501
            raise ValueError("Invalid value for `license_file_content`, must be a follow pattern or equal to `/.+/`")  # noqa: E501

        self._license_file_content = license_file_content

    @property
    def license_file_path(self):
        """Gets the license_file_path of this LicenseLicenseCreateParams.  # noqa: E501

        Path to new license file, must be under /ifs. The license file is obtained from Dell EMC's SLC web portal. Do not include the path when only enabling evaluation licenses. Do not use with the license_file_content option.  # noqa: E501

        :return: The license_file_path of this LicenseLicenseCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._license_file_path

    @license_file_path.setter
    def license_file_path(self, license_file_path):
        """Sets the license_file_path of this LicenseLicenseCreateParams.

        Path to new license file, must be under /ifs. The license file is obtained from Dell EMC's SLC web portal. Do not include the path when only enabling evaluation licenses. Do not use with the license_file_content option.  # noqa: E501

        :param license_file_path: The license_file_path of this LicenseLicenseCreateParams.  # noqa: E501
        :type: str
        """
        if license_file_path is not None and len(license_file_path) > 4096:
            raise ValueError("Invalid value for `license_file_path`, length must be less than or equal to `4096`")  # noqa: E501
        if license_file_path is not None and len(license_file_path) < 4:
            raise ValueError("Invalid value for `license_file_path`, length must be greater than or equal to `4`")  # noqa: E501
        if license_file_path is not None and not re.search('^\/ifs$|^\/ifs\/', license_file_path):  # noqa: E501
            raise ValueError("Invalid value for `license_file_path`, must be a follow pattern or equal to `/^\/ifs$|^\/ifs\//`")  # noqa: E501

        self._license_file_path = license_file_path

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
        if not isinstance(other, LicenseLicenseCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other