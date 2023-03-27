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


class CreateKmipServerVerifyItemResponseNode(object):
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
        'id': 'int',
        'lnn': 'int',
        'message': 'str',
        'status': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'lnn': 'lnn',
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, id=None, lnn=None, message=None, status=None):  # noqa: E501
        """CreateKmipServerVerifyItemResponseNode - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._lnn = None
        self._message = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.lnn = lnn
        self.message = message
        self.status = status

    @property
    def id(self):
        """Gets the id of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateKmipServerVerifyItemResponseNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this CreateKmipServerVerifyItemResponseNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501
        :type: int
        """
        if lnn is None:
            raise ValueError("Invalid value for `lnn`, must not be `None`")  # noqa: E501
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def message(self):
        """Gets the message of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501

        Response message.  # noqa: E501

        :return: The message of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateKmipServerVerifyItemResponseNode.

        Response message.  # noqa: E501

        :param message: The message of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        if message is not None and len(message) > 8192:
            raise ValueError("Invalid value for `message`, length must be less than or equal to `8192`")  # noqa: E501
        if message is not None and len(message) < 0:
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `0`")  # noqa: E501

        self._message = message

    @property
    def status(self):
        """Gets the status of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501

        True if the KMIP configuration was verified, otherwise false.  # noqa: E501

        :return: The status of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateKmipServerVerifyItemResponseNode.

        True if the KMIP configuration was verified, otherwise false.  # noqa: E501

        :param status: The status of this CreateKmipServerVerifyItemResponseNode.  # noqa: E501
        :type: bool
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, CreateKmipServerVerifyItemResponseNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other