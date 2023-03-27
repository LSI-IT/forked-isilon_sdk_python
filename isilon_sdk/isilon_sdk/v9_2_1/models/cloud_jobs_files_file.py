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


class CloudJobsFilesFile(object):
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
        'name': 'str',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state'
    }

    def __init__(self, id=None, name=None, state=None):  # noqa: E501
        """CloudJobsFilesFile - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this CloudJobsFilesFile.  # noqa: E501

        ID number of the file within the job  # noqa: E501

        :return: The id of this CloudJobsFilesFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudJobsFilesFile.

        ID number of the file within the job  # noqa: E501

        :param id: The id of this CloudJobsFilesFile.  # noqa: E501
        :type: int
        """
        if id is not None and id < 1:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this CloudJobsFilesFile.  # noqa: E501

        File path  # noqa: E501

        :return: The name of this CloudJobsFilesFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudJobsFilesFile.

        File path  # noqa: E501

        :param name: The name of this CloudJobsFilesFile.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 4096:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `4096`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this CloudJobsFilesFile.  # noqa: E501

        State of file.  # noqa: E501

        :return: The state of this CloudJobsFilesFile.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CloudJobsFilesFile.

        State of file.  # noqa: E501

        :param state: The state of this CloudJobsFilesFile.  # noqa: E501
        :type: str
        """
        allowed_values = ["waiting", "running", "paused", "canceled", "completed", "error", "none", "pending"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, CloudJobsFilesFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
