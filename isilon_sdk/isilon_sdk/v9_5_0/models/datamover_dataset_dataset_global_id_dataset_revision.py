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


class DatamoverDatasetDatasetGlobalIdDatasetRevision(object):
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
        'local_unid': 'int',
        'system_guid': 'str'
    }

    attribute_map = {
        'local_unid': 'local_unid',
        'system_guid': 'system_guid'
    }

    def __init__(self, local_unid=None, system_guid=None):  # noqa: E501
        """DatamoverDatasetDatasetGlobalIdDatasetRevision - a model defined in Swagger"""  # noqa: E501

        self._local_unid = None
        self._system_guid = None
        self.discriminator = None

        if local_unid is not None:
            self.local_unid = local_unid
        if system_guid is not None:
            self.system_guid = system_guid

    @property
    def local_unid(self):
        """Gets the local_unid of this DatamoverDatasetDatasetGlobalIdDatasetRevision.  # noqa: E501

        The locally unique Data Mover identifier.  # noqa: E501

        :return: The local_unid of this DatamoverDatasetDatasetGlobalIdDatasetRevision.  # noqa: E501
        :rtype: int
        """
        return self._local_unid

    @local_unid.setter
    def local_unid(self, local_unid):
        """Sets the local_unid of this DatamoverDatasetDatasetGlobalIdDatasetRevision.

        The locally unique Data Mover identifier.  # noqa: E501

        :param local_unid: The local_unid of this DatamoverDatasetDatasetGlobalIdDatasetRevision.  # noqa: E501
        :type: int
        """
        if local_unid is not None and local_unid > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `local_unid`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if local_unid is not None and local_unid < 0:  # noqa: E501
            raise ValueError("Invalid value for `local_unid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._local_unid = local_unid

    @property
    def system_guid(self):
        """Gets the system_guid of this DatamoverDatasetDatasetGlobalIdDatasetRevision.  # noqa: E501

        The globally unique Data Mover identifier.  # noqa: E501

        :return: The system_guid of this DatamoverDatasetDatasetGlobalIdDatasetRevision.  # noqa: E501
        :rtype: str
        """
        return self._system_guid

    @system_guid.setter
    def system_guid(self, system_guid):
        """Sets the system_guid of this DatamoverDatasetDatasetGlobalIdDatasetRevision.

        The globally unique Data Mover identifier.  # noqa: E501

        :param system_guid: The system_guid of this DatamoverDatasetDatasetGlobalIdDatasetRevision.  # noqa: E501
        :type: str
        """
        if system_guid is not None and len(system_guid) > 36:
            raise ValueError("Invalid value for `system_guid`, length must be less than or equal to `36`")  # noqa: E501
        if system_guid is not None and len(system_guid) < 2:
            raise ValueError("Invalid value for `system_guid`, length must be greater than or equal to `2`")  # noqa: E501

        self._system_guid = system_guid

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
        if not isinstance(other, DatamoverDatasetDatasetGlobalIdDatasetRevision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other