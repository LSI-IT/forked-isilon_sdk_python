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

from isilon_sdk.v9_5_0.models.fsa_result import FsaResult  # noqa: F401,E501


class FsaResultExtended(object):
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
        'pinned': 'bool',
        'begin_time': 'int',
        'content_path': 'str',
        'delete_link': 'str',
        'end_time': 'int',
        'fsa_state': 'str',
        'id': 'int',
        'job_state': 'list[str]',
        'properties_link': 'str',
        'size': 'int',
        'version': 'int'
    }

    attribute_map = {
        'pinned': 'pinned',
        'begin_time': 'begin_time',
        'content_path': 'content_path',
        'delete_link': 'delete_link',
        'end_time': 'end_time',
        'fsa_state': 'fsa_state',
        'id': 'id',
        'job_state': 'job_state',
        'properties_link': 'properties_link',
        'size': 'size',
        'version': 'version'
    }

    def __init__(self, pinned=None, begin_time=None, content_path=None, delete_link=None, end_time=None, fsa_state=None, id=None, job_state=None, properties_link=None, size=None, version=None):  # noqa: E501
        """FsaResultExtended - a model defined in Swagger"""  # noqa: E501

        self._pinned = None
        self._begin_time = None
        self._content_path = None
        self._delete_link = None
        self._end_time = None
        self._fsa_state = None
        self._id = None
        self._job_state = None
        self._properties_link = None
        self._size = None
        self._version = None
        self.discriminator = None

        self.pinned = pinned
        self.begin_time = begin_time
        if content_path is not None:
            self.content_path = content_path
        if delete_link is not None:
            self.delete_link = delete_link
        self.end_time = end_time
        self.fsa_state = fsa_state
        self.id = id
        self.job_state = job_state
        self.properties_link = properties_link
        self.size = size
        self.version = version

    @property
    def pinned(self):
        """Gets the pinned of this FsaResultExtended.  # noqa: E501

        True if the result is pinned to prevent automatic removal.  # noqa: E501

        :return: The pinned of this FsaResultExtended.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this FsaResultExtended.

        True if the result is pinned to prevent automatic removal.  # noqa: E501

        :param pinned: The pinned of this FsaResultExtended.  # noqa: E501
        :type: bool
        """
        if pinned is None:
            raise ValueError("Invalid value for `pinned`, must not be `None`")  # noqa: E501

        self._pinned = pinned

    @property
    def begin_time(self):
        """Gets the begin_time of this FsaResultExtended.  # noqa: E501

        Unix Epoch time of start of results collection job.  # noqa: E501

        :return: The begin_time of this FsaResultExtended.  # noqa: E501
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this FsaResultExtended.

        Unix Epoch time of start of results collection job.  # noqa: E501

        :param begin_time: The begin_time of this FsaResultExtended.  # noqa: E501
        :type: int
        """
        if begin_time is None:
            raise ValueError("Invalid value for `begin_time`, must not be `None`")  # noqa: E501

        self._begin_time = begin_time

    @property
    def content_path(self):
        """Gets the content_path of this FsaResultExtended.  # noqa: E501

        Path to results database.  # noqa: E501

        :return: The content_path of this FsaResultExtended.  # noqa: E501
        :rtype: str
        """
        return self._content_path

    @content_path.setter
    def content_path(self, content_path):
        """Sets the content_path of this FsaResultExtended.

        Path to results database.  # noqa: E501

        :param content_path: The content_path of this FsaResultExtended.  # noqa: E501
        :type: str
        """

        self._content_path = content_path

    @property
    def delete_link(self):
        """Gets the delete_link of this FsaResultExtended.  # noqa: E501

        Resource to call with DELETE to remove results..  # noqa: E501

        :return: The delete_link of this FsaResultExtended.  # noqa: E501
        :rtype: str
        """
        return self._delete_link

    @delete_link.setter
    def delete_link(self, delete_link):
        """Sets the delete_link of this FsaResultExtended.

        Resource to call with DELETE to remove results..  # noqa: E501

        :param delete_link: The delete_link of this FsaResultExtended.  # noqa: E501
        :type: str
        """

        self._delete_link = delete_link

    @property
    def end_time(self):
        """Gets the end_time of this FsaResultExtended.  # noqa: E501

        Unix Epoch time of end of results collection job.  # noqa: E501

        :return: The end_time of this FsaResultExtended.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this FsaResultExtended.

        Unix Epoch time of end of results collection job.  # noqa: E501

        :param end_time: The end_time of this FsaResultExtended.  # noqa: E501
        :type: int
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def fsa_state(self):
        """Gets the fsa_state of this FsaResultExtended.  # noqa: E501

        State of the result set.  # noqa: E501

        :return: The fsa_state of this FsaResultExtended.  # noqa: E501
        :rtype: str
        """
        return self._fsa_state

    @fsa_state.setter
    def fsa_state(self, fsa_state):
        """Sets the fsa_state of this FsaResultExtended.

        State of the result set.  # noqa: E501

        :param fsa_state: The fsa_state of this FsaResultExtended.  # noqa: E501
        :type: str
        """
        if fsa_state is None:
            raise ValueError("Invalid value for `fsa_state`, must not be `None`")  # noqa: E501
        allowed_values = ["unknown", "work", "reduce", "publish"]  # noqa: E501
        if fsa_state not in allowed_values:
            raise ValueError(
                "Invalid value for `fsa_state` ({0}), must be one of {1}"  # noqa: E501
                .format(fsa_state, allowed_values)
            )

        self._fsa_state = fsa_state

    @property
    def id(self):
        """Gets the id of this FsaResultExtended.  # noqa: E501

        The system generated result set ID.  # noqa: E501

        :return: The id of this FsaResultExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FsaResultExtended.

        The system generated result set ID.  # noqa: E501

        :param id: The id of this FsaResultExtended.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def job_state(self):
        """Gets the job_state of this FsaResultExtended.  # noqa: E501

        State information about the FSA Job.  # noqa: E501

        :return: The job_state of this FsaResultExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this FsaResultExtended.

        State information about the FSA Job.  # noqa: E501

        :param job_state: The job_state of this FsaResultExtended.  # noqa: E501
        :type: list[str]
        """
        if job_state is None:
            raise ValueError("Invalid value for `job_state`, must not be `None`")  # noqa: E501

        self._job_state = job_state

    @property
    def properties_link(self):
        """Gets the properties_link of this FsaResultExtended.  # noqa: E501

        Resource to call to get result properties.  # noqa: E501

        :return: The properties_link of this FsaResultExtended.  # noqa: E501
        :rtype: str
        """
        return self._properties_link

    @properties_link.setter
    def properties_link(self, properties_link):
        """Sets the properties_link of this FsaResultExtended.

        Resource to call to get result properties.  # noqa: E501

        :param properties_link: The properties_link of this FsaResultExtended.  # noqa: E501
        :type: str
        """
        if properties_link is None:
            raise ValueError("Invalid value for `properties_link`, must not be `None`")  # noqa: E501

        self._properties_link = properties_link

    @property
    def size(self):
        """Gets the size of this FsaResultExtended.  # noqa: E501

        Size of the result set database in bytes.  # noqa: E501

        :return: The size of this FsaResultExtended.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FsaResultExtended.

        Size of the result set database in bytes.  # noqa: E501

        :param size: The size of this FsaResultExtended.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def version(self):
        """Gets the version of this FsaResultExtended.  # noqa: E501

        FSA version used to create result set.  # noqa: E501

        :return: The version of this FsaResultExtended.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FsaResultExtended.

        FSA version used to create result set.  # noqa: E501

        :param version: The version of this FsaResultExtended.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, FsaResultExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
