# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_1_0.models.license_license import LicenseLicense  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.license_licenses import LicenseLicenses  # noqa: F401,E501


class LicenseLicensesExtended(object):
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
        'licenses': 'list[LicenseLicense]',
        'activation_incomplete_alert': 'bool',
        'base_only_licenses': 'list[str]',
        'evaluatable': 'list[str]',
        'resume': 'str',
        'swid': 'str',
        'total': 'int',
        'valid_signature': 'bool'
    }

    attribute_map = {
        'licenses': 'licenses',
        'activation_incomplete_alert': 'activation_incomplete_alert',
        'base_only_licenses': 'base_only_licenses',
        'evaluatable': 'evaluatable',
        'resume': 'resume',
        'swid': 'swid',
        'total': 'total',
        'valid_signature': 'valid_signature'
    }

    def __init__(self, licenses=None, activation_incomplete_alert=None, base_only_licenses=None, evaluatable=None, resume=None, swid=None, total=None, valid_signature=None):  # noqa: E501
        """LicenseLicensesExtended - a model defined in Swagger"""  # noqa: E501

        self._licenses = None
        self._activation_incomplete_alert = None
        self._base_only_licenses = None
        self._evaluatable = None
        self._resume = None
        self._swid = None
        self._total = None
        self._valid_signature = None
        self.discriminator = None

        if licenses is not None:
            self.licenses = licenses
        self.activation_incomplete_alert = activation_incomplete_alert
        self.base_only_licenses = base_only_licenses
        self.evaluatable = evaluatable
        if resume is not None:
            self.resume = resume
        if swid is not None:
            self.swid = swid
        if total is not None:
            self.total = total
        self.valid_signature = valid_signature

    @property
    def licenses(self):
        """Gets the licenses of this LicenseLicensesExtended.  # noqa: E501


        :return: The licenses of this LicenseLicensesExtended.  # noqa: E501
        :rtype: list[LicenseLicense]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """Sets the licenses of this LicenseLicensesExtended.


        :param licenses: The licenses of this LicenseLicensesExtended.  # noqa: E501
        :type: list[LicenseLicense]
        """

        self._licenses = licenses

    @property
    def activation_incomplete_alert(self):
        """Gets the activation_incomplete_alert of this LicenseLicensesExtended.  # noqa: E501

        True when we are generating an activation incomplete alert. An activation incomplete alert is generated if we do not have a signed license file 90 days after OneFS is upgraded.  # noqa: E501

        :return: The activation_incomplete_alert of this LicenseLicensesExtended.  # noqa: E501
        :rtype: bool
        """
        return self._activation_incomplete_alert

    @activation_incomplete_alert.setter
    def activation_incomplete_alert(self, activation_incomplete_alert):
        """Sets the activation_incomplete_alert of this LicenseLicensesExtended.

        True when we are generating an activation incomplete alert. An activation incomplete alert is generated if we do not have a signed license file 90 days after OneFS is upgraded.  # noqa: E501

        :param activation_incomplete_alert: The activation_incomplete_alert of this LicenseLicensesExtended.  # noqa: E501
        :type: bool
        """
        if activation_incomplete_alert is None:
            raise ValueError("Invalid value for `activation_incomplete_alert`, must not be `None`")  # noqa: E501

        self._activation_incomplete_alert = activation_incomplete_alert

    @property
    def base_only_licenses(self):
        """Gets the base_only_licenses of this LicenseLicensesExtended.  # noqa: E501


        :return: The base_only_licenses of this LicenseLicensesExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._base_only_licenses

    @base_only_licenses.setter
    def base_only_licenses(self, base_only_licenses):
        """Sets the base_only_licenses of this LicenseLicensesExtended.


        :param base_only_licenses: The base_only_licenses of this LicenseLicensesExtended.  # noqa: E501
        :type: list[str]
        """
        if base_only_licenses is None:
            raise ValueError("Invalid value for `base_only_licenses`, must not be `None`")  # noqa: E501

        self._base_only_licenses = base_only_licenses

    @property
    def evaluatable(self):
        """Gets the evaluatable of this LicenseLicensesExtended.  # noqa: E501


        :return: The evaluatable of this LicenseLicensesExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._evaluatable

    @evaluatable.setter
    def evaluatable(self, evaluatable):
        """Sets the evaluatable of this LicenseLicensesExtended.


        :param evaluatable: The evaluatable of this LicenseLicensesExtended.  # noqa: E501
        :type: list[str]
        """
        if evaluatable is None:
            raise ValueError("Invalid value for `evaluatable`, must not be `None`")  # noqa: E501

        self._evaluatable = evaluatable

    @property
    def resume(self):
        """Gets the resume of this LicenseLicensesExtended.  # noqa: E501

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :return: The resume of this LicenseLicensesExtended.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this LicenseLicensesExtended.

        Provide this token as the 'resume' query argument to continue listing results.  # noqa: E501

        :param resume: The resume of this LicenseLicensesExtended.  # noqa: E501
        :type: str
        """
        if resume is not None and len(resume) > 8192:
            raise ValueError("Invalid value for `resume`, length must be less than or equal to `8192`")  # noqa: E501
        if resume is not None and len(resume) < 0:
            raise ValueError("Invalid value for `resume`, length must be greater than or equal to `0`")  # noqa: E501

        self._resume = resume

    @property
    def swid(self):
        """Gets the swid of this LicenseLicensesExtended.  # noqa: E501

        Software license identifier. SWID will be absent if not yet obtained from a license file.  # noqa: E501

        :return: The swid of this LicenseLicensesExtended.  # noqa: E501
        :rtype: str
        """
        return self._swid

    @swid.setter
    def swid(self, swid):
        """Sets the swid of this LicenseLicensesExtended.

        Software license identifier. SWID will be absent if not yet obtained from a license file.  # noqa: E501

        :param swid: The swid of this LicenseLicensesExtended.  # noqa: E501
        :type: str
        """
        if swid is not None and len(swid) > 50:
            raise ValueError("Invalid value for `swid`, length must be less than or equal to `50`")  # noqa: E501
        if swid is not None and len(swid) < 1:
            raise ValueError("Invalid value for `swid`, length must be greater than or equal to `1`")  # noqa: E501
        if swid is not None and not re.search('.+', swid):  # noqa: E501
            raise ValueError("Invalid value for `swid`, must be a follow pattern or equal to `/.+/`")  # noqa: E501

        self._swid = swid

    @property
    def total(self):
        """Gets the total of this LicenseLicensesExtended.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The total of this LicenseLicensesExtended.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this LicenseLicensesExtended.

        Total number of items available.  # noqa: E501

        :param total: The total of this LicenseLicensesExtended.  # noqa: E501
        :type: int
        """
        if total is not None and total > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if total is not None and total < 0:  # noqa: E501
            raise ValueError("Invalid value for `total`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total = total

    @property
    def valid_signature(self):
        """Gets the valid_signature of this LicenseLicensesExtended.  # noqa: E501

        True if license file contains a valid signature.  # noqa: E501

        :return: The valid_signature of this LicenseLicensesExtended.  # noqa: E501
        :rtype: bool
        """
        return self._valid_signature

    @valid_signature.setter
    def valid_signature(self, valid_signature):
        """Sets the valid_signature of this LicenseLicensesExtended.

        True if license file contains a valid signature.  # noqa: E501

        :param valid_signature: The valid_signature of this LicenseLicensesExtended.  # noqa: E501
        :type: bool
        """
        if valid_signature is None:
            raise ValueError("Invalid value for `valid_signature`, must not be `None`")  # noqa: E501

        self._valid_signature = valid_signature

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
        if not isinstance(other, LicenseLicensesExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
