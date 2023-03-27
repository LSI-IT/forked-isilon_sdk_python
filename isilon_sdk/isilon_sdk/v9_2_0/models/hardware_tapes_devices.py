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

from isilon_sdk.v9_2_0.models.hardware_tapes_devices_media_changer import HardwareTapesDevicesMediaChanger  # noqa: F401,E501


class HardwareTapesDevices(object):
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
        'media_changers': 'list[HardwareTapesDevicesMediaChanger]',
        'tapes': 'list[HardwareTapesDevicesMediaChanger]'
    }

    attribute_map = {
        'media_changers': 'media_changers',
        'tapes': 'tapes'
    }

    def __init__(self, media_changers=None, tapes=None):  # noqa: E501
        """HardwareTapesDevices - a model defined in Swagger"""  # noqa: E501

        self._media_changers = None
        self._tapes = None
        self.discriminator = None

        if media_changers is not None:
            self.media_changers = media_changers
        if tapes is not None:
            self.tapes = tapes

    @property
    def media_changers(self):
        """Gets the media_changers of this HardwareTapesDevices.  # noqa: E501

        Information of media-changer devices  # noqa: E501

        :return: The media_changers of this HardwareTapesDevices.  # noqa: E501
        :rtype: list[HardwareTapesDevicesMediaChanger]
        """
        return self._media_changers

    @media_changers.setter
    def media_changers(self, media_changers):
        """Sets the media_changers of this HardwareTapesDevices.

        Information of media-changer devices  # noqa: E501

        :param media_changers: The media_changers of this HardwareTapesDevices.  # noqa: E501
        :type: list[HardwareTapesDevicesMediaChanger]
        """

        self._media_changers = media_changers

    @property
    def tapes(self):
        """Gets the tapes of this HardwareTapesDevices.  # noqa: E501

        Information of tape devices  # noqa: E501

        :return: The tapes of this HardwareTapesDevices.  # noqa: E501
        :rtype: list[HardwareTapesDevicesMediaChanger]
        """
        return self._tapes

    @tapes.setter
    def tapes(self, tapes):
        """Sets the tapes of this HardwareTapesDevices.

        Information of tape devices  # noqa: E501

        :param tapes: The tapes of this HardwareTapesDevices.  # noqa: E501
        :type: list[HardwareTapesDevicesMediaChanger]
        """

        self._tapes = tapes

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
        if not isinstance(other, HardwareTapesDevices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other