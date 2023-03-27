# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class QuotaQuotaUsage(object):
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
        'applogical': 'int',
        'applogical_ready': 'bool',
        'fslogical': 'int',
        'fslogical_ready': 'bool',
        'fsphysical': 'int',
        'fsphysical_ready': 'bool',
        'inodes': 'int',
        'inodes_ready': 'bool',
        'physical': 'int',
        'physical_data': 'int',
        'physical_data_ready': 'bool',
        'physical_protection': 'int',
        'physical_protection_ready': 'bool',
        'physical_ready': 'bool',
        'shadow_refs': 'int',
        'shadow_refs_ready': 'bool'
    }

    attribute_map = {
        'applogical': 'applogical',
        'applogical_ready': 'applogical_ready',
        'fslogical': 'fslogical',
        'fslogical_ready': 'fslogical_ready',
        'fsphysical': 'fsphysical',
        'fsphysical_ready': 'fsphysical_ready',
        'inodes': 'inodes',
        'inodes_ready': 'inodes_ready',
        'physical': 'physical',
        'physical_data': 'physical_data',
        'physical_data_ready': 'physical_data_ready',
        'physical_protection': 'physical_protection',
        'physical_protection_ready': 'physical_protection_ready',
        'physical_ready': 'physical_ready',
        'shadow_refs': 'shadow_refs',
        'shadow_refs_ready': 'shadow_refs_ready'
    }

    def __init__(self, applogical=None, applogical_ready=None, fslogical=None, fslogical_ready=None, fsphysical=None, fsphysical_ready=None, inodes=None, inodes_ready=None, physical=None, physical_data=None, physical_data_ready=None, physical_protection=None, physical_protection_ready=None, physical_ready=None, shadow_refs=None, shadow_refs_ready=None):  # noqa: E501
        """QuotaQuotaUsage - a model defined in Swagger"""  # noqa: E501

        self._applogical = None
        self._applogical_ready = None
        self._fslogical = None
        self._fslogical_ready = None
        self._fsphysical = None
        self._fsphysical_ready = None
        self._inodes = None
        self._inodes_ready = None
        self._physical = None
        self._physical_data = None
        self._physical_data_ready = None
        self._physical_protection = None
        self._physical_protection_ready = None
        self._physical_ready = None
        self._shadow_refs = None
        self._shadow_refs_ready = None
        self.discriminator = None

        self.applogical = applogical
        self.applogical_ready = applogical_ready
        self.fslogical = fslogical
        self.fslogical_ready = fslogical_ready
        if fsphysical is not None:
            self.fsphysical = fsphysical
        self.fsphysical_ready = fsphysical_ready
        self.inodes = inodes
        self.inodes_ready = inodes_ready
        self.physical = physical
        self.physical_data = physical_data
        self.physical_data_ready = physical_data_ready
        self.physical_protection = physical_protection
        self.physical_protection_ready = physical_protection_ready
        self.physical_ready = physical_ready
        self.shadow_refs = shadow_refs
        self.shadow_refs_ready = shadow_refs_ready

    @property
    def applogical(self):
        """Gets the applogical of this QuotaQuotaUsage.  # noqa: E501

        Bytes used by governed data apparent to application.  # noqa: E501

        :return: The applogical of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._applogical

    @applogical.setter
    def applogical(self, applogical):
        """Sets the applogical of this QuotaQuotaUsage.

        Bytes used by governed data apparent to application.  # noqa: E501

        :param applogical: The applogical of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if applogical is None:
            raise ValueError("Invalid value for `applogical`, must not be `None`")  # noqa: E501
        if applogical is not None and applogical > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `applogical`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if applogical is not None and applogical < 0:  # noqa: E501
            raise ValueError("Invalid value for `applogical`, must be a value greater than or equal to `0`")  # noqa: E501

        self._applogical = applogical

    @property
    def applogical_ready(self):
        """Gets the applogical_ready of this QuotaQuotaUsage.  # noqa: E501

        True if applogical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :return: The applogical_ready of this QuotaQuotaUsage.  # noqa: E501
        :rtype: bool
        """
        return self._applogical_ready

    @applogical_ready.setter
    def applogical_ready(self, applogical_ready):
        """Sets the applogical_ready of this QuotaQuotaUsage.

        True if applogical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :param applogical_ready: The applogical_ready of this QuotaQuotaUsage.  # noqa: E501
        :type: bool
        """
        if applogical_ready is None:
            raise ValueError("Invalid value for `applogical_ready`, must not be `None`")  # noqa: E501

        self._applogical_ready = applogical_ready

    @property
    def fslogical(self):
        """Gets the fslogical of this QuotaQuotaUsage.  # noqa: E501

        Bytes used by governed data apparent to filesystem.  # noqa: E501

        :return: The fslogical of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._fslogical

    @fslogical.setter
    def fslogical(self, fslogical):
        """Sets the fslogical of this QuotaQuotaUsage.

        Bytes used by governed data apparent to filesystem.  # noqa: E501

        :param fslogical: The fslogical of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if fslogical is None:
            raise ValueError("Invalid value for `fslogical`, must not be `None`")  # noqa: E501
        if fslogical is not None and fslogical > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `fslogical`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if fslogical is not None and fslogical < 0:  # noqa: E501
            raise ValueError("Invalid value for `fslogical`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fslogical = fslogical

    @property
    def fslogical_ready(self):
        """Gets the fslogical_ready of this QuotaQuotaUsage.  # noqa: E501

        True if fslogical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :return: The fslogical_ready of this QuotaQuotaUsage.  # noqa: E501
        :rtype: bool
        """
        return self._fslogical_ready

    @fslogical_ready.setter
    def fslogical_ready(self, fslogical_ready):
        """Sets the fslogical_ready of this QuotaQuotaUsage.

        True if fslogical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :param fslogical_ready: The fslogical_ready of this QuotaQuotaUsage.  # noqa: E501
        :type: bool
        """
        if fslogical_ready is None:
            raise ValueError("Invalid value for `fslogical_ready`, must not be `None`")  # noqa: E501

        self._fslogical_ready = fslogical_ready

    @property
    def fsphysical(self):
        """Gets the fsphysical of this QuotaQuotaUsage.  # noqa: E501

        Physical data usage adjusted to account for shadow store efficiency  # noqa: E501

        :return: The fsphysical of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._fsphysical

    @fsphysical.setter
    def fsphysical(self, fsphysical):
        """Sets the fsphysical of this QuotaQuotaUsage.

        Physical data usage adjusted to account for shadow store efficiency  # noqa: E501

        :param fsphysical: The fsphysical of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if fsphysical is not None and fsphysical > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `fsphysical`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if fsphysical is not None and fsphysical < 0:  # noqa: E501
            raise ValueError("Invalid value for `fsphysical`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fsphysical = fsphysical

    @property
    def fsphysical_ready(self):
        """Gets the fsphysical_ready of this QuotaQuotaUsage.  # noqa: E501

        True if fsphysical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :return: The fsphysical_ready of this QuotaQuotaUsage.  # noqa: E501
        :rtype: bool
        """
        return self._fsphysical_ready

    @fsphysical_ready.setter
    def fsphysical_ready(self, fsphysical_ready):
        """Sets the fsphysical_ready of this QuotaQuotaUsage.

        True if fsphysical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :param fsphysical_ready: The fsphysical_ready of this QuotaQuotaUsage.  # noqa: E501
        :type: bool
        """
        if fsphysical_ready is None:
            raise ValueError("Invalid value for `fsphysical_ready`, must not be `None`")  # noqa: E501

        self._fsphysical_ready = fsphysical_ready

    @property
    def inodes(self):
        """Gets the inodes of this QuotaQuotaUsage.  # noqa: E501

        Number of inodes (filesystem entities) used by governed data.  # noqa: E501

        :return: The inodes of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._inodes

    @inodes.setter
    def inodes(self, inodes):
        """Sets the inodes of this QuotaQuotaUsage.

        Number of inodes (filesystem entities) used by governed data.  # noqa: E501

        :param inodes: The inodes of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if inodes is None:
            raise ValueError("Invalid value for `inodes`, must not be `None`")  # noqa: E501
        if inodes is not None and inodes > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `inodes`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if inodes is not None and inodes < 0:  # noqa: E501
            raise ValueError("Invalid value for `inodes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._inodes = inodes

    @property
    def inodes_ready(self):
        """Gets the inodes_ready of this QuotaQuotaUsage.  # noqa: E501

        True if inodes resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :return: The inodes_ready of this QuotaQuotaUsage.  # noqa: E501
        :rtype: bool
        """
        return self._inodes_ready

    @inodes_ready.setter
    def inodes_ready(self, inodes_ready):
        """Sets the inodes_ready of this QuotaQuotaUsage.

        True if inodes resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :param inodes_ready: The inodes_ready of this QuotaQuotaUsage.  # noqa: E501
        :type: bool
        """
        if inodes_ready is None:
            raise ValueError("Invalid value for `inodes_ready`, must not be `None`")  # noqa: E501

        self._inodes_ready = inodes_ready

    @property
    def physical(self):
        """Gets the physical of this QuotaQuotaUsage.  # noqa: E501

        Bytes used for governed data and filesystem overhead.  # noqa: E501

        :return: The physical of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._physical

    @physical.setter
    def physical(self, physical):
        """Sets the physical of this QuotaQuotaUsage.

        Bytes used for governed data and filesystem overhead.  # noqa: E501

        :param physical: The physical of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if physical is None:
            raise ValueError("Invalid value for `physical`, must not be `None`")  # noqa: E501
        if physical is not None and physical > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `physical`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if physical is not None and physical < 0:  # noqa: E501
            raise ValueError("Invalid value for `physical`, must be a value greater than or equal to `0`")  # noqa: E501

        self._physical = physical

    @property
    def physical_data(self):
        """Gets the physical_data of this QuotaQuotaUsage.  # noqa: E501

        Number of physical blocks for file data  # noqa: E501

        :return: The physical_data of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._physical_data

    @physical_data.setter
    def physical_data(self, physical_data):
        """Sets the physical_data of this QuotaQuotaUsage.

        Number of physical blocks for file data  # noqa: E501

        :param physical_data: The physical_data of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if physical_data is None:
            raise ValueError("Invalid value for `physical_data`, must not be `None`")  # noqa: E501
        if physical_data is not None and physical_data > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `physical_data`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if physical_data is not None and physical_data < 0:  # noqa: E501
            raise ValueError("Invalid value for `physical_data`, must be a value greater than or equal to `0`")  # noqa: E501

        self._physical_data = physical_data

    @property
    def physical_data_ready(self):
        """Gets the physical_data_ready of this QuotaQuotaUsage.  # noqa: E501

        True if physical_data resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :return: The physical_data_ready of this QuotaQuotaUsage.  # noqa: E501
        :rtype: bool
        """
        return self._physical_data_ready

    @physical_data_ready.setter
    def physical_data_ready(self, physical_data_ready):
        """Sets the physical_data_ready of this QuotaQuotaUsage.

        True if physical_data resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :param physical_data_ready: The physical_data_ready of this QuotaQuotaUsage.  # noqa: E501
        :type: bool
        """
        if physical_data_ready is None:
            raise ValueError("Invalid value for `physical_data_ready`, must not be `None`")  # noqa: E501

        self._physical_data_ready = physical_data_ready

    @property
    def physical_protection(self):
        """Gets the physical_protection of this QuotaQuotaUsage.  # noqa: E501

        Number of physical blocks for file protection  # noqa: E501

        :return: The physical_protection of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._physical_protection

    @physical_protection.setter
    def physical_protection(self, physical_protection):
        """Sets the physical_protection of this QuotaQuotaUsage.

        Number of physical blocks for file protection  # noqa: E501

        :param physical_protection: The physical_protection of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if physical_protection is None:
            raise ValueError("Invalid value for `physical_protection`, must not be `None`")  # noqa: E501
        if physical_protection is not None and physical_protection > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `physical_protection`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if physical_protection is not None and physical_protection < 0:  # noqa: E501
            raise ValueError("Invalid value for `physical_protection`, must be a value greater than or equal to `0`")  # noqa: E501

        self._physical_protection = physical_protection

    @property
    def physical_protection_ready(self):
        """Gets the physical_protection_ready of this QuotaQuotaUsage.  # noqa: E501

        True if physical_protection resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :return: The physical_protection_ready of this QuotaQuotaUsage.  # noqa: E501
        :rtype: bool
        """
        return self._physical_protection_ready

    @physical_protection_ready.setter
    def physical_protection_ready(self, physical_protection_ready):
        """Sets the physical_protection_ready of this QuotaQuotaUsage.

        True if physical_protection resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :param physical_protection_ready: The physical_protection_ready of this QuotaQuotaUsage.  # noqa: E501
        :type: bool
        """
        if physical_protection_ready is None:
            raise ValueError("Invalid value for `physical_protection_ready`, must not be `None`")  # noqa: E501

        self._physical_protection_ready = physical_protection_ready

    @property
    def physical_ready(self):
        """Gets the physical_ready of this QuotaQuotaUsage.  # noqa: E501

        True if physical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :return: The physical_ready of this QuotaQuotaUsage.  # noqa: E501
        :rtype: bool
        """
        return self._physical_ready

    @physical_ready.setter
    def physical_ready(self, physical_ready):
        """Sets the physical_ready of this QuotaQuotaUsage.

        True if physical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :param physical_ready: The physical_ready of this QuotaQuotaUsage.  # noqa: E501
        :type: bool
        """
        if physical_ready is None:
            raise ValueError("Invalid value for `physical_ready`, must not be `None`")  # noqa: E501

        self._physical_ready = physical_ready

    @property
    def shadow_refs(self):
        """Gets the shadow_refs of this QuotaQuotaUsage.  # noqa: E501

        Number of shadow references (cloned, deduplicated or packed filesystem blocks) used by governed data.  # noqa: E501

        :return: The shadow_refs of this QuotaQuotaUsage.  # noqa: E501
        :rtype: int
        """
        return self._shadow_refs

    @shadow_refs.setter
    def shadow_refs(self, shadow_refs):
        """Sets the shadow_refs of this QuotaQuotaUsage.

        Number of shadow references (cloned, deduplicated or packed filesystem blocks) used by governed data.  # noqa: E501

        :param shadow_refs: The shadow_refs of this QuotaQuotaUsage.  # noqa: E501
        :type: int
        """
        if shadow_refs is None:
            raise ValueError("Invalid value for `shadow_refs`, must not be `None`")  # noqa: E501
        if shadow_refs is not None and shadow_refs > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `shadow_refs`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if shadow_refs is not None and shadow_refs < 0:  # noqa: E501
            raise ValueError("Invalid value for `shadow_refs`, must be a value greater than or equal to `0`")  # noqa: E501

        self._shadow_refs = shadow_refs

    @property
    def shadow_refs_ready(self):
        """Gets the shadow_refs_ready of this QuotaQuotaUsage.  # noqa: E501

        True if shadow_refs resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :return: The shadow_refs_ready of this QuotaQuotaUsage.  # noqa: E501
        :rtype: bool
        """
        return self._shadow_refs_ready

    @shadow_refs_ready.setter
    def shadow_refs_ready(self, shadow_refs_ready):
        """Sets the shadow_refs_ready of this QuotaQuotaUsage.

        True if shadow_refs resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job.  # noqa: E501

        :param shadow_refs_ready: The shadow_refs_ready of this QuotaQuotaUsage.  # noqa: E501
        :type: bool
        """
        if shadow_refs_ready is None:
            raise ValueError("Invalid value for `shadow_refs_ready`, must not be `None`")  # noqa: E501

        self._shadow_refs_ready = shadow_refs_ready

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
        if not isinstance(other, QuotaQuotaUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
