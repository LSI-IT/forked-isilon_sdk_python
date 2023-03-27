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

from isilon_sdk.v9_5_0.models.healthcheck_checklist_delivery_item import HealthcheckChecklistDeliveryItem  # noqa: F401,E501


class HealthcheckChecklist(object):
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
        'delivery': 'list[HealthcheckChecklistDeliveryItem]',
        'history': 'int'
    }

    attribute_map = {
        'delivery': 'delivery',
        'history': 'history'
    }

    def __init__(self, delivery=None, history=None):  # noqa: E501
        """HealthcheckChecklist - a model defined in Swagger"""  # noqa: E501

        self._delivery = None
        self._history = None
        self.discriminator = None

        if delivery is not None:
            self.delivery = delivery
        if history is not None:
            self.history = history

    @property
    def delivery(self):
        """Gets the delivery of this HealthcheckChecklist.  # noqa: E501

        List of delivery addresses/methods for results  # noqa: E501

        :return: The delivery of this HealthcheckChecklist.  # noqa: E501
        :rtype: list[HealthcheckChecklistDeliveryItem]
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this HealthcheckChecklist.

        List of delivery addresses/methods for results  # noqa: E501

        :param delivery: The delivery of this HealthcheckChecklist.  # noqa: E501
        :type: list[HealthcheckChecklistDeliveryItem]
        """

        self._delivery = delivery

    @property
    def history(self):
        """Gets the history of this HealthcheckChecklist.  # noqa: E501

        Number of evaluation results to keep  # noqa: E501

        :return: The history of this HealthcheckChecklist.  # noqa: E501
        :rtype: int
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this HealthcheckChecklist.

        Number of evaluation results to keep  # noqa: E501

        :param history: The history of this HealthcheckChecklist.  # noqa: E501
        :type: int
        """
        if history is not None and history > 1000:  # noqa: E501
            raise ValueError("Invalid value for `history`, must be a value less than or equal to `1000`")  # noqa: E501
        if history is not None and history < 1:  # noqa: E501
            raise ValueError("Invalid value for `history`, must be a value greater than or equal to `1`")  # noqa: E501

        self._history = history

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
        if not isinstance(other, HealthcheckChecklist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
