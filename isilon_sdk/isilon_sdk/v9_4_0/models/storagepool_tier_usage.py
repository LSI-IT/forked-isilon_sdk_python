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


class StoragepoolTierUsage(object):
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
        'avail_bytes': 'str',
        'avail_hdd_bytes': 'str',
        'avail_ssd_bytes': 'str',
        'balanced': 'bool',
        'free_bytes': 'str',
        'free_hdd_bytes': 'str',
        'free_ssd_bytes': 'str',
        'pct_used': 'str',
        'pct_used_hdd': 'str',
        'pct_used_ssd': 'str',
        'total_bytes': 'str',
        'total_hdd_bytes': 'str',
        'total_ssd_bytes': 'str',
        'usable_bytes': 'str',
        'usable_hdd_bytes': 'str',
        'usable_ssd_bytes': 'str',
        'used_bytes': 'str',
        'used_hdd_bytes': 'str',
        'used_ssd_bytes': 'str',
        'virtual_hot_spare_bytes': 'str'
    }

    attribute_map = {
        'avail_bytes': 'avail_bytes',
        'avail_hdd_bytes': 'avail_hdd_bytes',
        'avail_ssd_bytes': 'avail_ssd_bytes',
        'balanced': 'balanced',
        'free_bytes': 'free_bytes',
        'free_hdd_bytes': 'free_hdd_bytes',
        'free_ssd_bytes': 'free_ssd_bytes',
        'pct_used': 'pct_used',
        'pct_used_hdd': 'pct_used_hdd',
        'pct_used_ssd': 'pct_used_ssd',
        'total_bytes': 'total_bytes',
        'total_hdd_bytes': 'total_hdd_bytes',
        'total_ssd_bytes': 'total_ssd_bytes',
        'usable_bytes': 'usable_bytes',
        'usable_hdd_bytes': 'usable_hdd_bytes',
        'usable_ssd_bytes': 'usable_ssd_bytes',
        'used_bytes': 'used_bytes',
        'used_hdd_bytes': 'used_hdd_bytes',
        'used_ssd_bytes': 'used_ssd_bytes',
        'virtual_hot_spare_bytes': 'virtual_hot_spare_bytes'
    }

    def __init__(self, avail_bytes=None, avail_hdd_bytes=None, avail_ssd_bytes=None, balanced=None, free_bytes=None, free_hdd_bytes=None, free_ssd_bytes=None, pct_used=None, pct_used_hdd=None, pct_used_ssd=None, total_bytes=None, total_hdd_bytes=None, total_ssd_bytes=None, usable_bytes=None, usable_hdd_bytes=None, usable_ssd_bytes=None, used_bytes=None, used_hdd_bytes=None, used_ssd_bytes=None, virtual_hot_spare_bytes=None):  # noqa: E501
        """StoragepoolTierUsage - a model defined in Swagger"""  # noqa: E501

        self._avail_bytes = None
        self._avail_hdd_bytes = None
        self._avail_ssd_bytes = None
        self._balanced = None
        self._free_bytes = None
        self._free_hdd_bytes = None
        self._free_ssd_bytes = None
        self._pct_used = None
        self._pct_used_hdd = None
        self._pct_used_ssd = None
        self._total_bytes = None
        self._total_hdd_bytes = None
        self._total_ssd_bytes = None
        self._usable_bytes = None
        self._usable_hdd_bytes = None
        self._usable_ssd_bytes = None
        self._used_bytes = None
        self._used_hdd_bytes = None
        self._used_ssd_bytes = None
        self._virtual_hot_spare_bytes = None
        self.discriminator = None

        self.avail_bytes = avail_bytes
        self.avail_hdd_bytes = avail_hdd_bytes
        self.avail_ssd_bytes = avail_ssd_bytes
        self.balanced = balanced
        self.free_bytes = free_bytes
        self.free_hdd_bytes = free_hdd_bytes
        self.free_ssd_bytes = free_ssd_bytes
        self.pct_used = pct_used
        self.pct_used_hdd = pct_used_hdd
        self.pct_used_ssd = pct_used_ssd
        self.total_bytes = total_bytes
        self.total_hdd_bytes = total_hdd_bytes
        self.total_ssd_bytes = total_ssd_bytes
        self.usable_bytes = usable_bytes
        self.usable_hdd_bytes = usable_hdd_bytes
        self.usable_ssd_bytes = usable_ssd_bytes
        if used_bytes is not None:
            self.used_bytes = used_bytes
        self.used_hdd_bytes = used_hdd_bytes
        self.used_ssd_bytes = used_ssd_bytes
        if virtual_hot_spare_bytes is not None:
            self.virtual_hot_spare_bytes = virtual_hot_spare_bytes

    @property
    def avail_bytes(self):
        """Gets the avail_bytes of this StoragepoolTierUsage.  # noqa: E501

        Available free bytes remaining in the pool when virtual hot spare is taken into account.  # noqa: E501

        :return: The avail_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._avail_bytes

    @avail_bytes.setter
    def avail_bytes(self, avail_bytes):
        """Sets the avail_bytes of this StoragepoolTierUsage.

        Available free bytes remaining in the pool when virtual hot spare is taken into account.  # noqa: E501

        :param avail_bytes: The avail_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if avail_bytes is None:
            raise ValueError("Invalid value for `avail_bytes`, must not be `None`")  # noqa: E501
        if avail_bytes is not None and len(avail_bytes) > 255:
            raise ValueError("Invalid value for `avail_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if avail_bytes is not None and len(avail_bytes) < 1:
            raise ValueError("Invalid value for `avail_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._avail_bytes = avail_bytes

    @property
    def avail_hdd_bytes(self):
        """Gets the avail_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Available free bytes remaining in the pool on HDD drives when virtual hot spare is taken into account.  # noqa: E501

        :return: The avail_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._avail_hdd_bytes

    @avail_hdd_bytes.setter
    def avail_hdd_bytes(self, avail_hdd_bytes):
        """Sets the avail_hdd_bytes of this StoragepoolTierUsage.

        Available free bytes remaining in the pool on HDD drives when virtual hot spare is taken into account.  # noqa: E501

        :param avail_hdd_bytes: The avail_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if avail_hdd_bytes is None:
            raise ValueError("Invalid value for `avail_hdd_bytes`, must not be `None`")  # noqa: E501
        if avail_hdd_bytes is not None and len(avail_hdd_bytes) > 255:
            raise ValueError("Invalid value for `avail_hdd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if avail_hdd_bytes is not None and len(avail_hdd_bytes) < 1:
            raise ValueError("Invalid value for `avail_hdd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._avail_hdd_bytes = avail_hdd_bytes

    @property
    def avail_ssd_bytes(self):
        """Gets the avail_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Available free bytes remaining in the pool on SSD drives when virtual hot spare is taken into account.  # noqa: E501

        :return: The avail_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._avail_ssd_bytes

    @avail_ssd_bytes.setter
    def avail_ssd_bytes(self, avail_ssd_bytes):
        """Sets the avail_ssd_bytes of this StoragepoolTierUsage.

        Available free bytes remaining in the pool on SSD drives when virtual hot spare is taken into account.  # noqa: E501

        :param avail_ssd_bytes: The avail_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if avail_ssd_bytes is None:
            raise ValueError("Invalid value for `avail_ssd_bytes`, must not be `None`")  # noqa: E501
        if avail_ssd_bytes is not None and len(avail_ssd_bytes) > 255:
            raise ValueError("Invalid value for `avail_ssd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if avail_ssd_bytes is not None and len(avail_ssd_bytes) < 1:
            raise ValueError("Invalid value for `avail_ssd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._avail_ssd_bytes = avail_ssd_bytes

    @property
    def balanced(self):
        """Gets the balanced of this StoragepoolTierUsage.  # noqa: E501

        Whether or not the pool usage is currently balanced.  # noqa: E501

        :return: The balanced of this StoragepoolTierUsage.  # noqa: E501
        :rtype: bool
        """
        return self._balanced

    @balanced.setter
    def balanced(self, balanced):
        """Sets the balanced of this StoragepoolTierUsage.

        Whether or not the pool usage is currently balanced.  # noqa: E501

        :param balanced: The balanced of this StoragepoolTierUsage.  # noqa: E501
        :type: bool
        """
        if balanced is None:
            raise ValueError("Invalid value for `balanced`, must not be `None`")  # noqa: E501

        self._balanced = balanced

    @property
    def free_bytes(self):
        """Gets the free_bytes of this StoragepoolTierUsage.  # noqa: E501

        Free bytes remaining in the pool.  # noqa: E501

        :return: The free_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._free_bytes

    @free_bytes.setter
    def free_bytes(self, free_bytes):
        """Sets the free_bytes of this StoragepoolTierUsage.

        Free bytes remaining in the pool.  # noqa: E501

        :param free_bytes: The free_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if free_bytes is None:
            raise ValueError("Invalid value for `free_bytes`, must not be `None`")  # noqa: E501
        if free_bytes is not None and len(free_bytes) > 255:
            raise ValueError("Invalid value for `free_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if free_bytes is not None and len(free_bytes) < 1:
            raise ValueError("Invalid value for `free_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._free_bytes = free_bytes

    @property
    def free_hdd_bytes(self):
        """Gets the free_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Free bytes remaining in the pool on HDD drives.  # noqa: E501

        :return: The free_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._free_hdd_bytes

    @free_hdd_bytes.setter
    def free_hdd_bytes(self, free_hdd_bytes):
        """Sets the free_hdd_bytes of this StoragepoolTierUsage.

        Free bytes remaining in the pool on HDD drives.  # noqa: E501

        :param free_hdd_bytes: The free_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if free_hdd_bytes is None:
            raise ValueError("Invalid value for `free_hdd_bytes`, must not be `None`")  # noqa: E501
        if free_hdd_bytes is not None and len(free_hdd_bytes) > 255:
            raise ValueError("Invalid value for `free_hdd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if free_hdd_bytes is not None and len(free_hdd_bytes) < 1:
            raise ValueError("Invalid value for `free_hdd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._free_hdd_bytes = free_hdd_bytes

    @property
    def free_ssd_bytes(self):
        """Gets the free_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Free bytes remaining in the pool on SSD drives.  # noqa: E501

        :return: The free_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._free_ssd_bytes

    @free_ssd_bytes.setter
    def free_ssd_bytes(self, free_ssd_bytes):
        """Sets the free_ssd_bytes of this StoragepoolTierUsage.

        Free bytes remaining in the pool on SSD drives.  # noqa: E501

        :param free_ssd_bytes: The free_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if free_ssd_bytes is None:
            raise ValueError("Invalid value for `free_ssd_bytes`, must not be `None`")  # noqa: E501
        if free_ssd_bytes is not None and len(free_ssd_bytes) > 255:
            raise ValueError("Invalid value for `free_ssd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if free_ssd_bytes is not None and len(free_ssd_bytes) < 1:
            raise ValueError("Invalid value for `free_ssd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._free_ssd_bytes = free_ssd_bytes

    @property
    def pct_used(self):
        """Gets the pct_used of this StoragepoolTierUsage.  # noqa: E501

        Percentage of usable space in the pool which is used.  # noqa: E501

        :return: The pct_used of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._pct_used

    @pct_used.setter
    def pct_used(self, pct_used):
        """Sets the pct_used of this StoragepoolTierUsage.

        Percentage of usable space in the pool which is used.  # noqa: E501

        :param pct_used: The pct_used of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if pct_used is None:
            raise ValueError("Invalid value for `pct_used`, must not be `None`")  # noqa: E501
        if pct_used is not None and len(pct_used) > 255:
            raise ValueError("Invalid value for `pct_used`, length must be less than or equal to `255`")  # noqa: E501
        if pct_used is not None and len(pct_used) < 1:
            raise ValueError("Invalid value for `pct_used`, length must be greater than or equal to `1`")  # noqa: E501

        self._pct_used = pct_used

    @property
    def pct_used_hdd(self):
        """Gets the pct_used_hdd of this StoragepoolTierUsage.  # noqa: E501

        Percentage of usable space on HDD drives in the pool which is used.  # noqa: E501

        :return: The pct_used_hdd of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._pct_used_hdd

    @pct_used_hdd.setter
    def pct_used_hdd(self, pct_used_hdd):
        """Sets the pct_used_hdd of this StoragepoolTierUsage.

        Percentage of usable space on HDD drives in the pool which is used.  # noqa: E501

        :param pct_used_hdd: The pct_used_hdd of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if pct_used_hdd is None:
            raise ValueError("Invalid value for `pct_used_hdd`, must not be `None`")  # noqa: E501
        if pct_used_hdd is not None and len(pct_used_hdd) > 255:
            raise ValueError("Invalid value for `pct_used_hdd`, length must be less than or equal to `255`")  # noqa: E501
        if pct_used_hdd is not None and len(pct_used_hdd) < 1:
            raise ValueError("Invalid value for `pct_used_hdd`, length must be greater than or equal to `1`")  # noqa: E501

        self._pct_used_hdd = pct_used_hdd

    @property
    def pct_used_ssd(self):
        """Gets the pct_used_ssd of this StoragepoolTierUsage.  # noqa: E501

        Percentage of usable space on SSD drives in the pool which is used.  # noqa: E501

        :return: The pct_used_ssd of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._pct_used_ssd

    @pct_used_ssd.setter
    def pct_used_ssd(self, pct_used_ssd):
        """Sets the pct_used_ssd of this StoragepoolTierUsage.

        Percentage of usable space on SSD drives in the pool which is used.  # noqa: E501

        :param pct_used_ssd: The pct_used_ssd of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if pct_used_ssd is None:
            raise ValueError("Invalid value for `pct_used_ssd`, must not be `None`")  # noqa: E501
        if pct_used_ssd is not None and len(pct_used_ssd) > 255:
            raise ValueError("Invalid value for `pct_used_ssd`, length must be less than or equal to `255`")  # noqa: E501
        if pct_used_ssd is not None and len(pct_used_ssd) < 1:
            raise ValueError("Invalid value for `pct_used_ssd`, length must be greater than or equal to `1`")  # noqa: E501

        self._pct_used_ssd = pct_used_ssd

    @property
    def total_bytes(self):
        """Gets the total_bytes of this StoragepoolTierUsage.  # noqa: E501

        Total bytes in the pool.  # noqa: E501

        :return: The total_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        """Sets the total_bytes of this StoragepoolTierUsage.

        Total bytes in the pool.  # noqa: E501

        :param total_bytes: The total_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if total_bytes is None:
            raise ValueError("Invalid value for `total_bytes`, must not be `None`")  # noqa: E501
        if total_bytes is not None and len(total_bytes) > 255:
            raise ValueError("Invalid value for `total_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if total_bytes is not None and len(total_bytes) < 1:
            raise ValueError("Invalid value for `total_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._total_bytes = total_bytes

    @property
    def total_hdd_bytes(self):
        """Gets the total_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Total bytes in the pool on HDD drives.  # noqa: E501

        :return: The total_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._total_hdd_bytes

    @total_hdd_bytes.setter
    def total_hdd_bytes(self, total_hdd_bytes):
        """Sets the total_hdd_bytes of this StoragepoolTierUsage.

        Total bytes in the pool on HDD drives.  # noqa: E501

        :param total_hdd_bytes: The total_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if total_hdd_bytes is None:
            raise ValueError("Invalid value for `total_hdd_bytes`, must not be `None`")  # noqa: E501
        if total_hdd_bytes is not None and len(total_hdd_bytes) > 255:
            raise ValueError("Invalid value for `total_hdd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if total_hdd_bytes is not None and len(total_hdd_bytes) < 1:
            raise ValueError("Invalid value for `total_hdd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._total_hdd_bytes = total_hdd_bytes

    @property
    def total_ssd_bytes(self):
        """Gets the total_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Total bytes in the pool on SSD drives.  # noqa: E501

        :return: The total_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._total_ssd_bytes

    @total_ssd_bytes.setter
    def total_ssd_bytes(self, total_ssd_bytes):
        """Sets the total_ssd_bytes of this StoragepoolTierUsage.

        Total bytes in the pool on SSD drives.  # noqa: E501

        :param total_ssd_bytes: The total_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if total_ssd_bytes is None:
            raise ValueError("Invalid value for `total_ssd_bytes`, must not be `None`")  # noqa: E501
        if total_ssd_bytes is not None and len(total_ssd_bytes) > 255:
            raise ValueError("Invalid value for `total_ssd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if total_ssd_bytes is not None and len(total_ssd_bytes) < 1:
            raise ValueError("Invalid value for `total_ssd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._total_ssd_bytes = total_ssd_bytes

    @property
    def usable_bytes(self):
        """Gets the usable_bytes of this StoragepoolTierUsage.  # noqa: E501

        Total bytes in the pool drives when virtual hot spare is taken into account.  # noqa: E501

        :return: The usable_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._usable_bytes

    @usable_bytes.setter
    def usable_bytes(self, usable_bytes):
        """Sets the usable_bytes of this StoragepoolTierUsage.

        Total bytes in the pool drives when virtual hot spare is taken into account.  # noqa: E501

        :param usable_bytes: The usable_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if usable_bytes is None:
            raise ValueError("Invalid value for `usable_bytes`, must not be `None`")  # noqa: E501
        if usable_bytes is not None and len(usable_bytes) > 255:
            raise ValueError("Invalid value for `usable_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if usable_bytes is not None and len(usable_bytes) < 1:
            raise ValueError("Invalid value for `usable_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._usable_bytes = usable_bytes

    @property
    def usable_hdd_bytes(self):
        """Gets the usable_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Total bytes in the pool on HDD drives when virtual hot spare is taken into account.  # noqa: E501

        :return: The usable_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._usable_hdd_bytes

    @usable_hdd_bytes.setter
    def usable_hdd_bytes(self, usable_hdd_bytes):
        """Sets the usable_hdd_bytes of this StoragepoolTierUsage.

        Total bytes in the pool on HDD drives when virtual hot spare is taken into account.  # noqa: E501

        :param usable_hdd_bytes: The usable_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if usable_hdd_bytes is None:
            raise ValueError("Invalid value for `usable_hdd_bytes`, must not be `None`")  # noqa: E501
        if usable_hdd_bytes is not None and len(usable_hdd_bytes) > 255:
            raise ValueError("Invalid value for `usable_hdd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if usable_hdd_bytes is not None and len(usable_hdd_bytes) < 1:
            raise ValueError("Invalid value for `usable_hdd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._usable_hdd_bytes = usable_hdd_bytes

    @property
    def usable_ssd_bytes(self):
        """Gets the usable_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Total bytes in the pool on SSD drives when virtual hot spare is taken into account.  # noqa: E501

        :return: The usable_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._usable_ssd_bytes

    @usable_ssd_bytes.setter
    def usable_ssd_bytes(self, usable_ssd_bytes):
        """Sets the usable_ssd_bytes of this StoragepoolTierUsage.

        Total bytes in the pool on SSD drives when virtual hot spare is taken into account.  # noqa: E501

        :param usable_ssd_bytes: The usable_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if usable_ssd_bytes is None:
            raise ValueError("Invalid value for `usable_ssd_bytes`, must not be `None`")  # noqa: E501
        if usable_ssd_bytes is not None and len(usable_ssd_bytes) > 255:
            raise ValueError("Invalid value for `usable_ssd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if usable_ssd_bytes is not None and len(usable_ssd_bytes) < 1:
            raise ValueError("Invalid value for `usable_ssd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._usable_ssd_bytes = usable_ssd_bytes

    @property
    def used_bytes(self):
        """Gets the used_bytes of this StoragepoolTierUsage.  # noqa: E501

        Used bytes in the pool.  # noqa: E501

        :return: The used_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._used_bytes

    @used_bytes.setter
    def used_bytes(self, used_bytes):
        """Sets the used_bytes of this StoragepoolTierUsage.

        Used bytes in the pool.  # noqa: E501

        :param used_bytes: The used_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if used_bytes is not None and len(used_bytes) > 255:
            raise ValueError("Invalid value for `used_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if used_bytes is not None and len(used_bytes) < 1:
            raise ValueError("Invalid value for `used_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._used_bytes = used_bytes

    @property
    def used_hdd_bytes(self):
        """Gets the used_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Used bytes in the pool on HDD drives.  # noqa: E501

        :return: The used_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._used_hdd_bytes

    @used_hdd_bytes.setter
    def used_hdd_bytes(self, used_hdd_bytes):
        """Sets the used_hdd_bytes of this StoragepoolTierUsage.

        Used bytes in the pool on HDD drives.  # noqa: E501

        :param used_hdd_bytes: The used_hdd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if used_hdd_bytes is None:
            raise ValueError("Invalid value for `used_hdd_bytes`, must not be `None`")  # noqa: E501
        if used_hdd_bytes is not None and len(used_hdd_bytes) > 255:
            raise ValueError("Invalid value for `used_hdd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if used_hdd_bytes is not None and len(used_hdd_bytes) < 1:
            raise ValueError("Invalid value for `used_hdd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._used_hdd_bytes = used_hdd_bytes

    @property
    def used_ssd_bytes(self):
        """Gets the used_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501

        Used bytes in the pool on SSD drives.  # noqa: E501

        :return: The used_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._used_ssd_bytes

    @used_ssd_bytes.setter
    def used_ssd_bytes(self, used_ssd_bytes):
        """Sets the used_ssd_bytes of this StoragepoolTierUsage.

        Used bytes in the pool on SSD drives.  # noqa: E501

        :param used_ssd_bytes: The used_ssd_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if used_ssd_bytes is None:
            raise ValueError("Invalid value for `used_ssd_bytes`, must not be `None`")  # noqa: E501
        if used_ssd_bytes is not None and len(used_ssd_bytes) > 255:
            raise ValueError("Invalid value for `used_ssd_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if used_ssd_bytes is not None and len(used_ssd_bytes) < 1:
            raise ValueError("Invalid value for `used_ssd_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._used_ssd_bytes = used_ssd_bytes

    @property
    def virtual_hot_spare_bytes(self):
        """Gets the virtual_hot_spare_bytes of this StoragepoolTierUsage.  # noqa: E501

        Bytes reserved for virtual hot spare in the pool.  # noqa: E501

        :return: The virtual_hot_spare_bytes of this StoragepoolTierUsage.  # noqa: E501
        :rtype: str
        """
        return self._virtual_hot_spare_bytes

    @virtual_hot_spare_bytes.setter
    def virtual_hot_spare_bytes(self, virtual_hot_spare_bytes):
        """Sets the virtual_hot_spare_bytes of this StoragepoolTierUsage.

        Bytes reserved for virtual hot spare in the pool.  # noqa: E501

        :param virtual_hot_spare_bytes: The virtual_hot_spare_bytes of this StoragepoolTierUsage.  # noqa: E501
        :type: str
        """
        if virtual_hot_spare_bytes is not None and len(virtual_hot_spare_bytes) > 255:
            raise ValueError("Invalid value for `virtual_hot_spare_bytes`, length must be less than or equal to `255`")  # noqa: E501
        if virtual_hot_spare_bytes is not None and len(virtual_hot_spare_bytes) < 1:
            raise ValueError("Invalid value for `virtual_hot_spare_bytes`, length must be greater than or equal to `1`")  # noqa: E501

        self._virtual_hot_spare_bytes = virtual_hot_spare_bytes

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
        if not isinstance(other, StoragepoolTierUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
