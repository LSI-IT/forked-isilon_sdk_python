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

from isilon_sdk.v9_2_0.models.license_activation_elms_error import LicenseActivationElmsError  # noqa: F401,E501


class LicenseActivation(object):
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
        'elms_errors': 'list[LicenseActivationElmsError]',
        'last_action_time': 'int',
        'status': 'str',
        'transaction_id': 'str'
    }

    attribute_map = {
        'elms_errors': 'elms_errors',
        'last_action_time': 'last_action_time',
        'status': 'status',
        'transaction_id': 'transaction_id'
    }

    def __init__(self, elms_errors=None, last_action_time=None, status=None, transaction_id=None):  # noqa: E501
        """LicenseActivation - a model defined in Swagger"""  # noqa: E501

        self._elms_errors = None
        self._last_action_time = None
        self._status = None
        self._transaction_id = None
        self.discriminator = None

        if elms_errors is not None:
            self.elms_errors = elms_errors
        if last_action_time is not None:
            self.last_action_time = last_action_time
        self.status = status
        if transaction_id is not None:
            self.transaction_id = transaction_id

    @property
    def elms_errors(self):
        """Gets the elms_errors of this LicenseActivation.  # noqa: E501

        An array of licenses not included in activation file.  # noqa: E501

        :return: The elms_errors of this LicenseActivation.  # noqa: E501
        :rtype: list[LicenseActivationElmsError]
        """
        return self._elms_errors

    @elms_errors.setter
    def elms_errors(self, elms_errors):
        """Sets the elms_errors of this LicenseActivation.

        An array of licenses not included in activation file.  # noqa: E501

        :param elms_errors: The elms_errors of this LicenseActivation.  # noqa: E501
        :type: list[LicenseActivationElmsError]
        """

        self._elms_errors = elms_errors

    @property
    def last_action_time(self):
        """Gets the last_action_time of this LicenseActivation.  # noqa: E501

        Number of days before a license expires.  # noqa: E501

        :return: The last_action_time of this LicenseActivation.  # noqa: E501
        :rtype: int
        """
        return self._last_action_time

    @last_action_time.setter
    def last_action_time(self, last_action_time):
        """Sets the last_action_time of this LicenseActivation.

        Number of days before a license expires.  # noqa: E501

        :param last_action_time: The last_action_time of this LicenseActivation.  # noqa: E501
        :type: int
        """
        if last_action_time is not None and last_action_time > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `last_action_time`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if last_action_time is not None and last_action_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `last_action_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._last_action_time = last_action_time

    @property
    def status(self):
        """Gets the status of this LicenseActivation.  # noqa: E501

        The state of activation. File creating, created, submitted, awaiting license, error, or approved.  # noqa: E501

        :return: The status of this LicenseActivation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LicenseActivation.

        The state of activation. File creating, created, submitted, awaiting license, error, or approved.  # noqa: E501

        :param status: The status of this LicenseActivation.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if status is not None and len(status) > 50:
            raise ValueError("Invalid value for `status`, length must be less than or equal to `50`")  # noqa: E501
        if status is not None and len(status) < 1:
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def transaction_id(self):
        """Gets the transaction_id of this LicenseActivation.  # noqa: E501

        The license activation transaction ID  # noqa: E501

        :return: The transaction_id of this LicenseActivation.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this LicenseActivation.

        The license activation transaction ID  # noqa: E501

        :param transaction_id: The transaction_id of this LicenseActivation.  # noqa: E501
        :type: str
        """
        if transaction_id is not None and len(transaction_id) > 64:
            raise ValueError("Invalid value for `transaction_id`, length must be less than or equal to `64`")  # noqa: E501
        if transaction_id is not None and len(transaction_id) < 0:
            raise ValueError("Invalid value for `transaction_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._transaction_id = transaction_id

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
        if not isinstance(other, LicenseActivation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
