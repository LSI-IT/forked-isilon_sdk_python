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


class LicenseActivationItem(object):
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
        'lacs': 'list[str]',
        'licenses_to_exclude': 'str',
        'licenses_to_include': 'str',
        'only_these_licenses': 'str'
    }

    attribute_map = {
        'lacs': 'lacs',
        'licenses_to_exclude': 'licenses_to_exclude',
        'licenses_to_include': 'licenses_to_include',
        'only_these_licenses': 'only_these_licenses'
    }

    def __init__(self, lacs=None, licenses_to_exclude=None, licenses_to_include=None, only_these_licenses=None):  # noqa: E501
        """LicenseActivationItem - a model defined in Swagger"""  # noqa: E501

        self._lacs = None
        self._licenses_to_exclude = None
        self._licenses_to_include = None
        self._only_these_licenses = None
        self.discriminator = None

        if lacs is not None:
            self.lacs = lacs
        if licenses_to_exclude is not None:
            self.licenses_to_exclude = licenses_to_exclude
        if licenses_to_include is not None:
            self.licenses_to_include = licenses_to_include
        if only_these_licenses is not None:
            self.only_these_licenses = only_these_licenses

    @property
    def lacs(self):
        """Gets the lacs of this LicenseActivationItem.  # noqa: E501

        An array of licenses not included in activation file.  # noqa: E501

        :return: The lacs of this LicenseActivationItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._lacs

    @lacs.setter
    def lacs(self, lacs):
        """Sets the lacs of this LicenseActivationItem.

        An array of licenses not included in activation file.  # noqa: E501

        :param lacs: The lacs of this LicenseActivationItem.  # noqa: E501
        :type: list[str]
        """

        self._lacs = lacs

    @property
    def licenses_to_exclude(self):
        """Gets the licenses_to_exclude of this LicenseActivationItem.  # noqa: E501

        Licenses to omit from activation file.  # noqa: E501

        :return: The licenses_to_exclude of this LicenseActivationItem.  # noqa: E501
        :rtype: str
        """
        return self._licenses_to_exclude

    @licenses_to_exclude.setter
    def licenses_to_exclude(self, licenses_to_exclude):
        """Sets the licenses_to_exclude of this LicenseActivationItem.

        Licenses to omit from activation file.  # noqa: E501

        :param licenses_to_exclude: The licenses_to_exclude of this LicenseActivationItem.  # noqa: E501
        :type: str
        """
        if licenses_to_exclude is not None and len(licenses_to_exclude) > 2500:
            raise ValueError("Invalid value for `licenses_to_exclude`, length must be less than or equal to `2500`")  # noqa: E501
        if licenses_to_exclude is not None and len(licenses_to_exclude) < 1:
            raise ValueError("Invalid value for `licenses_to_exclude`, length must be greater than or equal to `1`")  # noqa: E501
        if licenses_to_exclude is not None and not re.search('.*', licenses_to_exclude):  # noqa: E501
            raise ValueError("Invalid value for `licenses_to_exclude`, must be a follow pattern or equal to `/.*/`")  # noqa: E501

        self._licenses_to_exclude = licenses_to_exclude

    @property
    def licenses_to_include(self):
        """Gets the licenses_to_include of this LicenseActivationItem.  # noqa: E501

        Licenses to include in activation file.  # noqa: E501

        :return: The licenses_to_include of this LicenseActivationItem.  # noqa: E501
        :rtype: str
        """
        return self._licenses_to_include

    @licenses_to_include.setter
    def licenses_to_include(self, licenses_to_include):
        """Sets the licenses_to_include of this LicenseActivationItem.

        Licenses to include in activation file.  # noqa: E501

        :param licenses_to_include: The licenses_to_include of this LicenseActivationItem.  # noqa: E501
        :type: str
        """
        if licenses_to_include is not None and len(licenses_to_include) > 2500:
            raise ValueError("Invalid value for `licenses_to_include`, length must be less than or equal to `2500`")  # noqa: E501
        if licenses_to_include is not None and len(licenses_to_include) < 1:
            raise ValueError("Invalid value for `licenses_to_include`, length must be greater than or equal to `1`")  # noqa: E501
        if licenses_to_include is not None and not re.search('.*', licenses_to_include):  # noqa: E501
            raise ValueError("Invalid value for `licenses_to_include`, must be a follow pattern or equal to `/.*/`")  # noqa: E501

        self._licenses_to_include = licenses_to_include

    @property
    def only_these_licenses(self):
        """Gets the only_these_licenses of this LicenseActivationItem.  # noqa: E501

        Activate only the defined licenses. This setting overrides all other license activation settings.  # noqa: E501

        :return: The only_these_licenses of this LicenseActivationItem.  # noqa: E501
        :rtype: str
        """
        return self._only_these_licenses

    @only_these_licenses.setter
    def only_these_licenses(self, only_these_licenses):
        """Sets the only_these_licenses of this LicenseActivationItem.

        Activate only the defined licenses. This setting overrides all other license activation settings.  # noqa: E501

        :param only_these_licenses: The only_these_licenses of this LicenseActivationItem.  # noqa: E501
        :type: str
        """
        if only_these_licenses is not None and len(only_these_licenses) > 2500:
            raise ValueError("Invalid value for `only_these_licenses`, length must be less than or equal to `2500`")  # noqa: E501
        if only_these_licenses is not None and len(only_these_licenses) < 1:
            raise ValueError("Invalid value for `only_these_licenses`, length must be greater than or equal to `1`")  # noqa: E501
        if only_these_licenses is not None and not re.search('.*', only_these_licenses):  # noqa: E501
            raise ValueError("Invalid value for `only_these_licenses`, must be a follow pattern or equal to `/.*/`")  # noqa: E501

        self._only_these_licenses = only_these_licenses

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
        if not isinstance(other, LicenseActivationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
