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


class NodeHardwareFastNode(object):
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
        'product': 'str',
        'serial_number': 'str',
        'storage_class': 'str'
    }

    attribute_map = {
        'id': 'id',
        'lnn': 'lnn',
        'product': 'product',
        'serial_number': 'serial_number',
        'storage_class': 'storage_class'
    }

    def __init__(self, id=None, lnn=None, product=None, serial_number=None, storage_class=None):  # noqa: E501
        """NodeHardwareFastNode - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._lnn = None
        self._product = None
        self._serial_number = None
        self._storage_class = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if product is not None:
            self.product = product
        if serial_number is not None:
            self.serial_number = serial_number
        if storage_class is not None:
            self.storage_class = storage_class

    @property
    def id(self):
        """Gets the id of this NodeHardwareFastNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeHardwareFastNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeHardwareFastNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeHardwareFastNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NodeHardwareFastNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeHardwareFastNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeHardwareFastNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeHardwareFastNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def product(self):
        """Gets the product of this NodeHardwareFastNode.  # noqa: E501

        PowerScale product name.  # noqa: E501

        :return: The product of this NodeHardwareFastNode.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this NodeHardwareFastNode.

        PowerScale product name.  # noqa: E501

        :param product: The product of this NodeHardwareFastNode.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def serial_number(self):
        """Gets the serial_number of this NodeHardwareFastNode.  # noqa: E501

        Serial number of this node.  # noqa: E501

        :return: The serial_number of this NodeHardwareFastNode.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this NodeHardwareFastNode.

        Serial number of this node.  # noqa: E501

        :param serial_number: The serial_number of this NodeHardwareFastNode.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def storage_class(self):
        """Gets the storage_class of this NodeHardwareFastNode.  # noqa: E501

        Storage class of this node (storage or diskless).  # noqa: E501

        :return: The storage_class of this NodeHardwareFastNode.  # noqa: E501
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this NodeHardwareFastNode.

        Storage class of this node (storage or diskless).  # noqa: E501

        :param storage_class: The storage_class of this NodeHardwareFastNode.  # noqa: E501
        :type: str
        """

        self._storage_class = storage_class

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
        if not isinstance(other, NodeHardwareFastNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
