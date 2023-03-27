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


class NodeStatusCpuError(object):
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
        'code': 'str',
        'field': 'str',
        'id': 'int',
        'lnn': 'int',
        'message': 'str',
        'status': 'int'
    }

    attribute_map = {
        'code': 'code',
        'field': 'field',
        'id': 'id',
        'lnn': 'lnn',
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, code=None, field=None, id=None, lnn=None, message=None, status=None):  # noqa: E501
        """NodeStatusCpuError - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._field = None
        self._id = None
        self._lnn = None
        self._message = None
        self._status = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if field is not None:
            self.field = field
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def code(self):
        """Gets the code of this NodeStatusCpuError.  # noqa: E501

        The error code.  # noqa: E501

        :return: The code of this NodeStatusCpuError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this NodeStatusCpuError.

        The error code.  # noqa: E501

        :param code: The code of this NodeStatusCpuError.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 8192:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `8192`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def field(self):
        """Gets the field of this NodeStatusCpuError.  # noqa: E501

        The field with the error if applicable.  # noqa: E501

        :return: The field of this NodeStatusCpuError.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this NodeStatusCpuError.

        The field with the error if applicable.  # noqa: E501

        :param field: The field of this NodeStatusCpuError.  # noqa: E501
        :type: str
        """
        if field is not None and len(field) > 8192:
            raise ValueError("Invalid value for `field`, length must be less than or equal to `8192`")  # noqa: E501
        if field is not None and len(field) < 1:
            raise ValueError("Invalid value for `field`, length must be greater than or equal to `1`")  # noqa: E501

        self._field = field

    @property
    def id(self):
        """Gets the id of this NodeStatusCpuError.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeStatusCpuError.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeStatusCpuError.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeStatusCpuError.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NodeStatusCpuError.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeStatusCpuError.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeStatusCpuError.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeStatusCpuError.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def message(self):
        """Gets the message of this NodeStatusCpuError.  # noqa: E501

        The error message.  # noqa: E501

        :return: The message of this NodeStatusCpuError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NodeStatusCpuError.

        The error message.  # noqa: E501

        :param message: The message of this NodeStatusCpuError.  # noqa: E501
        :type: str
        """
        if message is not None and len(message) > 8192:
            raise ValueError("Invalid value for `message`, length must be less than or equal to `8192`")  # noqa: E501
        if message is not None and len(message) < 1:
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501

        self._message = message

    @property
    def status(self):
        """Gets the status of this NodeStatusCpuError.  # noqa: E501

        HTTP Status code returned by this node.  # noqa: E501

        :return: The status of this NodeStatusCpuError.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeStatusCpuError.

        HTTP Status code returned by this node.  # noqa: E501

        :param status: The status of this NodeStatusCpuError.  # noqa: E501
        :type: int
        """
        if status is not None and status > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if status is not None and status < 0:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0`")  # noqa: E501

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
        if not isinstance(other, NodeStatusCpuError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
