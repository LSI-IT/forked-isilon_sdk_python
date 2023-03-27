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


class SnapshotAliasExtended(object):
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
        'created': 'int',
        'id': 'int',
        'name': 'str',
        'target_id': 'int',
        'target_name': 'str'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'name': 'name',
        'target_id': 'target_id',
        'target_name': 'target_name'
    }

    def __init__(self, created=None, id=None, name=None, target_id=None, target_name=None):  # noqa: E501
        """SnapshotAliasExtended - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._id = None
        self._name = None
        self._target_id = None
        self._target_name = None
        self.discriminator = None

        self.created = created
        self.id = id
        self.name = name
        self.target_id = target_id
        self.target_name = target_name

    @property
    def created(self):
        """Gets the created of this SnapshotAliasExtended.  # noqa: E501

        The Unix Epoch time the snapshot alias was created.  # noqa: E501

        :return: The created of this SnapshotAliasExtended.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SnapshotAliasExtended.

        The Unix Epoch time the snapshot alias was created.  # noqa: E501

        :param created: The created of this SnapshotAliasExtended.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def id(self):
        """Gets the id of this SnapshotAliasExtended.  # noqa: E501

        The system ID given to the snapshot alias.  # noqa: E501

        :return: The id of this SnapshotAliasExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotAliasExtended.

        The system ID given to the snapshot alias.  # noqa: E501

        :param id: The id of this SnapshotAliasExtended.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SnapshotAliasExtended.  # noqa: E501

        The user or system supplied snapshot alias name.  # noqa: E501

        :return: The name of this SnapshotAliasExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotAliasExtended.

        The user or system supplied snapshot alias name.  # noqa: E501

        :param name: The name of this SnapshotAliasExtended.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def target_id(self):
        """Gets the target_id of this SnapshotAliasExtended.  # noqa: E501

        The ID of the snapshot pointed to.  # noqa: E501

        :return: The target_id of this SnapshotAliasExtended.  # noqa: E501
        :rtype: int
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this SnapshotAliasExtended.

        The ID of the snapshot pointed to.  # noqa: E501

        :param target_id: The target_id of this SnapshotAliasExtended.  # noqa: E501
        :type: int
        """
        if target_id is None:
            raise ValueError("Invalid value for `target_id`, must not be `None`")  # noqa: E501

        self._target_id = target_id

    @property
    def target_name(self):
        """Gets the target_name of this SnapshotAliasExtended.  # noqa: E501

        The name of the snapshot pointed to.  # noqa: E501

        :return: The target_name of this SnapshotAliasExtended.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this SnapshotAliasExtended.

        The name of the snapshot pointed to.  # noqa: E501

        :param target_name: The target_name of this SnapshotAliasExtended.  # noqa: E501
        :type: str
        """
        if target_name is None:
            raise ValueError("Invalid value for `target_name`, must not be `None`")  # noqa: E501

        self._target_name = target_name

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
        if not isinstance(other, SnapshotAliasExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
