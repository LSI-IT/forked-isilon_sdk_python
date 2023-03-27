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

from isilon_sdk.v9_1_0.models.empty import Empty  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.healthcheck_checklist_delivery_item import HealthcheckChecklistDeliveryItem  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.healthcheck_evaluation_detail import HealthcheckEvaluationDetail  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.healthcheck_evaluation_override import HealthcheckEvaluationOverride  # noqa: F401,E501


class HealthcheckEvaluationExtended(object):
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
        'checklist_id': 'str',
        'delivery': 'list[HealthcheckChecklistDeliveryItem]',
        'details': 'list[HealthcheckEvaluationDetail]',
        'id': 'str',
        'overrides': 'list[HealthcheckEvaluationOverride]',
        'parameters': 'Empty',
        'result': 'str',
        'run_status': 'str',
        'start_time': 'float'
    }

    attribute_map = {
        'checklist_id': 'checklist_id',
        'delivery': 'delivery',
        'details': 'details',
        'id': 'id',
        'overrides': 'overrides',
        'parameters': 'parameters',
        'result': 'result',
        'run_status': 'run_status',
        'start_time': 'start_time'
    }

    def __init__(self, checklist_id=None, delivery=None, details=None, id=None, overrides=None, parameters=None, result=None, run_status=None, start_time=None):  # noqa: E501
        """HealthcheckEvaluationExtended - a model defined in Swagger"""  # noqa: E501

        self._checklist_id = None
        self._delivery = None
        self._details = None
        self._id = None
        self._overrides = None
        self._parameters = None
        self._result = None
        self._run_status = None
        self._start_time = None
        self.discriminator = None

        if checklist_id is not None:
            self.checklist_id = checklist_id
        if delivery is not None:
            self.delivery = delivery
        if details is not None:
            self.details = details
        if id is not None:
            self.id = id
        if overrides is not None:
            self.overrides = overrides
        if parameters is not None:
            self.parameters = parameters
        if result is not None:
            self.result = result
        if run_status is not None:
            self.run_status = run_status
        if start_time is not None:
            self.start_time = start_time

    @property
    def checklist_id(self):
        """Gets the checklist_id of this HealthcheckEvaluationExtended.  # noqa: E501

        Checklist to be run  # noqa: E501

        :return: The checklist_id of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: str
        """
        return self._checklist_id

    @checklist_id.setter
    def checklist_id(self, checklist_id):
        """Sets the checklist_id of this HealthcheckEvaluationExtended.

        Checklist to be run  # noqa: E501

        :param checklist_id: The checklist_id of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: str
        """
        if checklist_id is not None and len(checklist_id) > 255:
            raise ValueError("Invalid value for `checklist_id`, length must be less than or equal to `255`")  # noqa: E501
        if checklist_id is not None and len(checklist_id) < 0:
            raise ValueError("Invalid value for `checklist_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._checklist_id = checklist_id

    @property
    def delivery(self):
        """Gets the delivery of this HealthcheckEvaluationExtended.  # noqa: E501

        List of delivery addresses/methods for results  # noqa: E501

        :return: The delivery of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: list[HealthcheckChecklistDeliveryItem]
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this HealthcheckEvaluationExtended.

        List of delivery addresses/methods for results  # noqa: E501

        :param delivery: The delivery of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: list[HealthcheckChecklistDeliveryItem]
        """

        self._delivery = delivery

    @property
    def details(self):
        """Gets the details of this HealthcheckEvaluationExtended.  # noqa: E501

        Evaluation results by item - only if COMPLETED  # noqa: E501

        :return: The details of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: list[HealthcheckEvaluationDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this HealthcheckEvaluationExtended.

        Evaluation results by item - only if COMPLETED  # noqa: E501

        :param details: The details of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: list[HealthcheckEvaluationDetail]
        """

        self._details = details

    @property
    def id(self):
        """Gets the id of this HealthcheckEvaluationExtended.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthcheckEvaluationExtended.

        Unique identifier  # noqa: E501

        :param id: The id of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def overrides(self):
        """Gets the overrides of this HealthcheckEvaluationExtended.  # noqa: E501

        Optional overrides for thresholds etc.  # noqa: E501

        :return: The overrides of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: list[HealthcheckEvaluationOverride]
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this HealthcheckEvaluationExtended.

        Optional overrides for thresholds etc.  # noqa: E501

        :param overrides: The overrides of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: list[HealthcheckEvaluationOverride]
        """

        self._overrides = overrides

    @property
    def parameters(self):
        """Gets the parameters of this HealthcheckEvaluationExtended.  # noqa: E501

        Parameters supplied for this evaluation  # noqa: E501

        :return: The parameters of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: Empty
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this HealthcheckEvaluationExtended.

        Parameters supplied for this evaluation  # noqa: E501

        :param parameters: The parameters of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: Empty
        """

        self._parameters = parameters

    @property
    def result(self):
        """Gets the result of this HealthcheckEvaluationExtended.  # noqa: E501

        Overall result of evaluation - only if COMPLETED  # noqa: E501

        :return: The result of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this HealthcheckEvaluationExtended.

        Overall result of evaluation - only if COMPLETED  # noqa: E501

        :param result: The result of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASS", "FAIL"]  # noqa: E501
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def run_status(self):
        """Gets the run_status of this HealthcheckEvaluationExtended.  # noqa: E501

        Execution status  # noqa: E501

        :return: The run_status of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this HealthcheckEvaluationExtended.

        Execution status  # noqa: E501

        :param run_status: The run_status of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["QUEUED", "RUNNING", "PAUSED", "FAILED", "COMPLETED"]  # noqa: E501
        if run_status not in allowed_values:
            raise ValueError(
                "Invalid value for `run_status` ({0}), must be one of {1}"  # noqa: E501
                .format(run_status, allowed_values)
            )

        self._run_status = run_status

    @property
    def start_time(self):
        """Gets the start_time of this HealthcheckEvaluationExtended.  # noqa: E501


        :return: The start_time of this HealthcheckEvaluationExtended.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this HealthcheckEvaluationExtended.


        :param start_time: The start_time of this HealthcheckEvaluationExtended.  # noqa: E501
        :type: float
        """
        if start_time is not None and start_time > 18446744073709551615:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must be a value less than or equal to `18446744073709551615`")  # noqa: E501
        if start_time is not None and start_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_time = start_time

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
        if not isinstance(other, HealthcheckEvaluationExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
