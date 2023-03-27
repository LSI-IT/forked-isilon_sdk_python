# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_1_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501


class SummaryClientClientItem(object):
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
        '_class': 'str',
        '_in': 'float',
        'in_avg': 'float',
        'in_max': 'float',
        'in_min': 'float',
        'local_addr': 'str',
        'local_name': 'str',
        'node': 'int',
        'num_operations': 'int',
        'operation_rate': 'float',
        'out': 'float',
        'out_avg': 'float',
        'out_max': 'float',
        'out_min': 'float',
        'protocol': 'str',
        'remote_addr': 'str',
        'remote_name': 'str',
        'time': 'int',
        'time_avg': 'float',
        'time_max': 'float',
        'time_min': 'float',
        'user': 'AuthAccessAccessItemFileGroup'
    }

    attribute_map = {
        '_class': 'class',
        '_in': 'in',
        'in_avg': 'in_avg',
        'in_max': 'in_max',
        'in_min': 'in_min',
        'local_addr': 'local_addr',
        'local_name': 'local_name',
        'node': 'node',
        'num_operations': 'num_operations',
        'operation_rate': 'operation_rate',
        'out': 'out',
        'out_avg': 'out_avg',
        'out_max': 'out_max',
        'out_min': 'out_min',
        'protocol': 'protocol',
        'remote_addr': 'remote_addr',
        'remote_name': 'remote_name',
        'time': 'time',
        'time_avg': 'time_avg',
        'time_max': 'time_max',
        'time_min': 'time_min',
        'user': 'user'
    }

    def __init__(self, _class=None, _in=None, in_avg=None, in_max=None, in_min=None, local_addr=None, local_name=None, node=None, num_operations=None, operation_rate=None, out=None, out_avg=None, out_max=None, out_min=None, protocol=None, remote_addr=None, remote_name=None, time=None, time_avg=None, time_max=None, time_min=None, user=None):  # noqa: E501
        """SummaryClientClientItem - a model defined in Swagger"""  # noqa: E501

        self.__class = None
        self.__in = None
        self._in_avg = None
        self._in_max = None
        self._in_min = None
        self._local_addr = None
        self._local_name = None
        self._node = None
        self._num_operations = None
        self._operation_rate = None
        self._out = None
        self._out_avg = None
        self._out_max = None
        self._out_min = None
        self._protocol = None
        self._remote_addr = None
        self._remote_name = None
        self._time = None
        self._time_avg = None
        self._time_max = None
        self._time_min = None
        self._user = None
        self.discriminator = None

        self._class = _class
        self._in = _in
        self.in_avg = in_avg
        self.in_max = in_max
        self.in_min = in_min
        self.local_addr = local_addr
        self.local_name = local_name
        if node is not None:
            self.node = node
        self.num_operations = num_operations
        self.operation_rate = operation_rate
        self.out = out
        self.out_avg = out_avg
        self.out_max = out_max
        self.out_min = out_min
        self.protocol = protocol
        self.remote_addr = remote_addr
        self.remote_name = remote_name
        self.time = time
        self.time_avg = time_avg
        self.time_max = time_max
        self.time_min = time_min
        if user is not None:
            self.user = user

    @property
    def _class(self):
        """Gets the _class of this SummaryClientClientItem.  # noqa: E501

        The class of the operation.  # noqa: E501

        :return: The _class of this SummaryClientClientItem.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this SummaryClientClientItem.

        The class of the operation.  # noqa: E501

        :param _class: The _class of this SummaryClientClientItem.  # noqa: E501
        :type: str
        """
        if _class is None:
            raise ValueError("Invalid value for `_class`, must not be `None`")  # noqa: E501

        self.__class = _class

    @property
    def _in(self):
        """Gets the _in of this SummaryClientClientItem.  # noqa: E501

        Rate of input (in bytes/second) for an operation since the last time isi statistics collected the data.  # noqa: E501

        :return: The _in of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this SummaryClientClientItem.

        Rate of input (in bytes/second) for an operation since the last time isi statistics collected the data.  # noqa: E501

        :param _in: The _in of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if _in is None:
            raise ValueError("Invalid value for `_in`, must not be `None`")  # noqa: E501

        self.__in = _in

    @property
    def in_avg(self):
        """Gets the in_avg of this SummaryClientClientItem.  # noqa: E501

        Average input (received) bytes for an operation, in bytes.  # noqa: E501

        :return: The in_avg of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._in_avg

    @in_avg.setter
    def in_avg(self, in_avg):
        """Sets the in_avg of this SummaryClientClientItem.

        Average input (received) bytes for an operation, in bytes.  # noqa: E501

        :param in_avg: The in_avg of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if in_avg is None:
            raise ValueError("Invalid value for `in_avg`, must not be `None`")  # noqa: E501

        self._in_avg = in_avg

    @property
    def in_max(self):
        """Gets the in_max of this SummaryClientClientItem.  # noqa: E501

        Maximum input (received) bytes for an operation, in bytes.  # noqa: E501

        :return: The in_max of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._in_max

    @in_max.setter
    def in_max(self, in_max):
        """Sets the in_max of this SummaryClientClientItem.

        Maximum input (received) bytes for an operation, in bytes.  # noqa: E501

        :param in_max: The in_max of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if in_max is None:
            raise ValueError("Invalid value for `in_max`, must not be `None`")  # noqa: E501

        self._in_max = in_max

    @property
    def in_min(self):
        """Gets the in_min of this SummaryClientClientItem.  # noqa: E501

        Minimum input (received) bytes for an operation, in bytes.  # noqa: E501

        :return: The in_min of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._in_min

    @in_min.setter
    def in_min(self, in_min):
        """Sets the in_min of this SummaryClientClientItem.

        Minimum input (received) bytes for an operation, in bytes.  # noqa: E501

        :param in_min: The in_min of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if in_min is None:
            raise ValueError("Invalid value for `in_min`, must not be `None`")  # noqa: E501

        self._in_min = in_min

    @property
    def local_addr(self):
        """Gets the local_addr of this SummaryClientClientItem.  # noqa: E501

        The IP address (in dotted-quad form) of the host receiving the operation request.  # noqa: E501

        :return: The local_addr of this SummaryClientClientItem.  # noqa: E501
        :rtype: str
        """
        return self._local_addr

    @local_addr.setter
    def local_addr(self, local_addr):
        """Sets the local_addr of this SummaryClientClientItem.

        The IP address (in dotted-quad form) of the host receiving the operation request.  # noqa: E501

        :param local_addr: The local_addr of this SummaryClientClientItem.  # noqa: E501
        :type: str
        """
        if local_addr is None:
            raise ValueError("Invalid value for `local_addr`, must not be `None`")  # noqa: E501

        self._local_addr = local_addr

    @property
    def local_name(self):
        """Gets the local_name of this SummaryClientClientItem.  # noqa: E501

        The resolved text name of the LocalAddr, if resolution can be performed.  # noqa: E501

        :return: The local_name of this SummaryClientClientItem.  # noqa: E501
        :rtype: str
        """
        return self._local_name

    @local_name.setter
    def local_name(self, local_name):
        """Sets the local_name of this SummaryClientClientItem.

        The resolved text name of the LocalAddr, if resolution can be performed.  # noqa: E501

        :param local_name: The local_name of this SummaryClientClientItem.  # noqa: E501
        :type: str
        """
        if local_name is None:
            raise ValueError("Invalid value for `local_name`, must not be `None`")  # noqa: E501

        self._local_name = local_name

    @property
    def node(self):
        """Gets the node of this SummaryClientClientItem.  # noqa: E501

        The node on which the operation was performed.  # noqa: E501

        :return: The node of this SummaryClientClientItem.  # noqa: E501
        :rtype: int
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this SummaryClientClientItem.

        The node on which the operation was performed.  # noqa: E501

        :param node: The node of this SummaryClientClientItem.  # noqa: E501
        :type: int
        """

        self._node = node

    @property
    def num_operations(self):
        """Gets the num_operations of this SummaryClientClientItem.  # noqa: E501

        The number of times an operation has been performed.  # noqa: E501

        :return: The num_operations of this SummaryClientClientItem.  # noqa: E501
        :rtype: int
        """
        return self._num_operations

    @num_operations.setter
    def num_operations(self, num_operations):
        """Sets the num_operations of this SummaryClientClientItem.

        The number of times an operation has been performed.  # noqa: E501

        :param num_operations: The num_operations of this SummaryClientClientItem.  # noqa: E501
        :type: int
        """
        if num_operations is None:
            raise ValueError("Invalid value for `num_operations`, must not be `None`")  # noqa: E501

        self._num_operations = num_operations

    @property
    def operation_rate(self):
        """Gets the operation_rate of this SummaryClientClientItem.  # noqa: E501

        The rate (in ops/second) at which an operation has been performed.  # noqa: E501

        :return: The operation_rate of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._operation_rate

    @operation_rate.setter
    def operation_rate(self, operation_rate):
        """Sets the operation_rate of this SummaryClientClientItem.

        The rate (in ops/second) at which an operation has been performed.  # noqa: E501

        :param operation_rate: The operation_rate of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if operation_rate is None:
            raise ValueError("Invalid value for `operation_rate`, must not be `None`")  # noqa: E501

        self._operation_rate = operation_rate

    @property
    def out(self):
        """Gets the out of this SummaryClientClientItem.  # noqa: E501

        Rate of output (in bytes/second) for an operation since the last time isi statistics collected the data.  # noqa: E501

        :return: The out of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this SummaryClientClientItem.

        Rate of output (in bytes/second) for an operation since the last time isi statistics collected the data.  # noqa: E501

        :param out: The out of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if out is None:
            raise ValueError("Invalid value for `out`, must not be `None`")  # noqa: E501

        self._out = out

    @property
    def out_avg(self):
        """Gets the out_avg of this SummaryClientClientItem.  # noqa: E501

        Average output (sent) bytes for an operation, in bytes.  # noqa: E501

        :return: The out_avg of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._out_avg

    @out_avg.setter
    def out_avg(self, out_avg):
        """Sets the out_avg of this SummaryClientClientItem.

        Average output (sent) bytes for an operation, in bytes.  # noqa: E501

        :param out_avg: The out_avg of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if out_avg is None:
            raise ValueError("Invalid value for `out_avg`, must not be `None`")  # noqa: E501

        self._out_avg = out_avg

    @property
    def out_max(self):
        """Gets the out_max of this SummaryClientClientItem.  # noqa: E501

        Maximum output (sent) bytes for an operation, in bytes.  # noqa: E501

        :return: The out_max of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._out_max

    @out_max.setter
    def out_max(self, out_max):
        """Sets the out_max of this SummaryClientClientItem.

        Maximum output (sent) bytes for an operation, in bytes.  # noqa: E501

        :param out_max: The out_max of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if out_max is None:
            raise ValueError("Invalid value for `out_max`, must not be `None`")  # noqa: E501

        self._out_max = out_max

    @property
    def out_min(self):
        """Gets the out_min of this SummaryClientClientItem.  # noqa: E501

        Minimum output (sent) bytes for an operation, in bytes.  # noqa: E501

        :return: The out_min of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._out_min

    @out_min.setter
    def out_min(self, out_min):
        """Sets the out_min of this SummaryClientClientItem.

        Minimum output (sent) bytes for an operation, in bytes.  # noqa: E501

        :param out_min: The out_min of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if out_min is None:
            raise ValueError("Invalid value for `out_min`, must not be `None`")  # noqa: E501

        self._out_min = out_min

    @property
    def protocol(self):
        """Gets the protocol of this SummaryClientClientItem.  # noqa: E501

        The protocol of the operation.  # noqa: E501

        :return: The protocol of this SummaryClientClientItem.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SummaryClientClientItem.

        The protocol of the operation.  # noqa: E501

        :param protocol: The protocol of this SummaryClientClientItem.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def remote_addr(self):
        """Gets the remote_addr of this SummaryClientClientItem.  # noqa: E501

        The IP address (in dotted-quad form) of the host sending the operation request.  # noqa: E501

        :return: The remote_addr of this SummaryClientClientItem.  # noqa: E501
        :rtype: str
        """
        return self._remote_addr

    @remote_addr.setter
    def remote_addr(self, remote_addr):
        """Sets the remote_addr of this SummaryClientClientItem.

        The IP address (in dotted-quad form) of the host sending the operation request.  # noqa: E501

        :param remote_addr: The remote_addr of this SummaryClientClientItem.  # noqa: E501
        :type: str
        """
        if remote_addr is None:
            raise ValueError("Invalid value for `remote_addr`, must not be `None`")  # noqa: E501

        self._remote_addr = remote_addr

    @property
    def remote_name(self):
        """Gets the remote_name of this SummaryClientClientItem.  # noqa: E501

        The resolved text name of the RemoteAddr, if resolution can be performed.  # noqa: E501

        :return: The remote_name of this SummaryClientClientItem.  # noqa: E501
        :rtype: str
        """
        return self._remote_name

    @remote_name.setter
    def remote_name(self, remote_name):
        """Sets the remote_name of this SummaryClientClientItem.

        The resolved text name of the RemoteAddr, if resolution can be performed.  # noqa: E501

        :param remote_name: The remote_name of this SummaryClientClientItem.  # noqa: E501
        :type: str
        """
        if remote_name is None:
            raise ValueError("Invalid value for `remote_name`, must not be `None`")  # noqa: E501

        self._remote_name = remote_name

    @property
    def time(self):
        """Gets the time of this SummaryClientClientItem.  # noqa: E501

        Unix Epoch time in seconds of the request.  # noqa: E501

        :return: The time of this SummaryClientClientItem.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SummaryClientClientItem.

        Unix Epoch time in seconds of the request.  # noqa: E501

        :param time: The time of this SummaryClientClientItem.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def time_avg(self):
        """Gets the time_avg of this SummaryClientClientItem.  # noqa: E501

        The average elapsed time (in microseconds) taken to complete an operation.  # noqa: E501

        :return: The time_avg of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._time_avg

    @time_avg.setter
    def time_avg(self, time_avg):
        """Sets the time_avg of this SummaryClientClientItem.

        The average elapsed time (in microseconds) taken to complete an operation.  # noqa: E501

        :param time_avg: The time_avg of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if time_avg is None:
            raise ValueError("Invalid value for `time_avg`, must not be `None`")  # noqa: E501

        self._time_avg = time_avg

    @property
    def time_max(self):
        """Gets the time_max of this SummaryClientClientItem.  # noqa: E501

        The maximum elapsed time (in microseconds) taken to complete an operation.  # noqa: E501

        :return: The time_max of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._time_max

    @time_max.setter
    def time_max(self, time_max):
        """Sets the time_max of this SummaryClientClientItem.

        The maximum elapsed time (in microseconds) taken to complete an operation.  # noqa: E501

        :param time_max: The time_max of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if time_max is None:
            raise ValueError("Invalid value for `time_max`, must not be `None`")  # noqa: E501

        self._time_max = time_max

    @property
    def time_min(self):
        """Gets the time_min of this SummaryClientClientItem.  # noqa: E501

        The minimum elapsed time (in microseconds) taken to complete an operation.  # noqa: E501

        :return: The time_min of this SummaryClientClientItem.  # noqa: E501
        :rtype: float
        """
        return self._time_min

    @time_min.setter
    def time_min(self, time_min):
        """Sets the time_min of this SummaryClientClientItem.

        The minimum elapsed time (in microseconds) taken to complete an operation.  # noqa: E501

        :param time_min: The time_min of this SummaryClientClientItem.  # noqa: E501
        :type: float
        """
        if time_min is None:
            raise ValueError("Invalid value for `time_min`, must not be `None`")  # noqa: E501

        self._time_min = time_min

    @property
    def user(self):
        """Gets the user of this SummaryClientClientItem.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The user of this SummaryClientClientItem.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SummaryClientClientItem.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param user: The user of this SummaryClientClientItem.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._user = user

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
        if not isinstance(other, SummaryClientClientItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
