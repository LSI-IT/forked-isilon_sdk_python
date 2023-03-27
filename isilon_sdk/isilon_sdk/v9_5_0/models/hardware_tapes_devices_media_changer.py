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

from isilon_sdk.v9_5_0.models.hardware_tapes_devices_media_changer_path import HardwareTapesDevicesMediaChangerPath  # noqa: F401,E501


class HardwareTapesDevicesMediaChanger(object):
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
        'id': 'str',
        'name': 'str',
        'opencount': 'int',
        'paths': 'list[HardwareTapesDevicesMediaChangerPath]',
        'product': 'str',
        'serial': 'str',
        'state': 'str',
        'wwnn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'opencount': 'opencount',
        'paths': 'paths',
        'product': 'product',
        'serial': 'serial',
        'state': 'state',
        'wwnn': 'wwnn'
    }

    def __init__(self, id=None, name=None, opencount=None, paths=None, product=None, serial=None, state=None, wwnn=None):  # noqa: E501
        """HardwareTapesDevicesMediaChanger - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._opencount = None
        self._paths = None
        self._product = None
        self._serial = None
        self._state = None
        self._wwnn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if opencount is not None:
            self.opencount = opencount
        if paths is not None:
            self.paths = paths
        if product is not None:
            self.product = product
        if serial is not None:
            self.serial = serial
        if state is not None:
            self.state = state
        if wwnn is not None:
            self.wwnn = wwnn

    @property
    def id(self):
        """Gets the id of this HardwareTapesDevicesMediaChanger.  # noqa: E501

        The unique display id.  # noqa: E501

        :return: The id of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HardwareTapesDevicesMediaChanger.

        The unique display id.  # noqa: E501

        :param id: The id of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this HardwareTapesDevicesMediaChanger.  # noqa: E501

        Name of the device  # noqa: E501

        :return: The name of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HardwareTapesDevicesMediaChanger.

        Name of the device  # noqa: E501

        :param name: The name of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def opencount(self):
        """Gets the opencount of this HardwareTapesDevicesMediaChanger.  # noqa: E501

        Number of open  # noqa: E501

        :return: The opencount of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :rtype: int
        """
        return self._opencount

    @opencount.setter
    def opencount(self, opencount):
        """Sets the opencount of this HardwareTapesDevicesMediaChanger.

        Number of open  # noqa: E501

        :param opencount: The opencount of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :type: int
        """

        self._opencount = opencount

    @property
    def paths(self):
        """Gets the paths of this HardwareTapesDevicesMediaChanger.  # noqa: E501

        Accessible paths of the device  # noqa: E501

        :return: The paths of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :rtype: list[HardwareTapesDevicesMediaChangerPath]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this HardwareTapesDevicesMediaChanger.

        Accessible paths of the device  # noqa: E501

        :param paths: The paths of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :type: list[HardwareTapesDevicesMediaChangerPath]
        """

        self._paths = paths

    @property
    def product(self):
        """Gets the product of this HardwareTapesDevicesMediaChanger.  # noqa: E501

        Product information string including vendor, model, and revision  # noqa: E501

        :return: The product of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this HardwareTapesDevicesMediaChanger.

        Product information string including vendor, model, and revision  # noqa: E501

        :param product: The product of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def serial(self):
        """Gets the serial of this HardwareTapesDevicesMediaChanger.  # noqa: E501

        Serial number of the device  # noqa: E501

        :return: The serial of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this HardwareTapesDevicesMediaChanger.

        Serial number of the device  # noqa: E501

        :param serial: The serial of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def state(self):
        """Gets the state of this HardwareTapesDevicesMediaChanger.  # noqa: E501

        Device state  # noqa: E501

        :return: The state of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this HardwareTapesDevicesMediaChanger.

        Device state  # noqa: E501

        :param state: The state of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :type: str
        """
        allowed_values = ["read/write", "write only", "read only", "raw", "closed"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def wwnn(self):
        """Gets the wwnn of this HardwareTapesDevicesMediaChanger.  # noqa: E501

        World wide node name of the port  # noqa: E501

        :return: The wwnn of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """Sets the wwnn of this HardwareTapesDevicesMediaChanger.

        World wide node name of the port  # noqa: E501

        :param wwnn: The wwnn of this HardwareTapesDevicesMediaChanger.  # noqa: E501
        :type: str
        """

        self._wwnn = wwnn

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
        if not isinstance(other, HardwareTapesDevicesMediaChanger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
