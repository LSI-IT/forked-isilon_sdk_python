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


class NdmpSession(object):
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
        'data_bytes_transferred': 'int',
        'data_state': 'str',
        'dest_path': 'str',
        'dma_ip_addr': 'str',
        'elapsed_time': 'int',
        'id': 'str',
        'lnn': 'str',
        'mover_bytes_transferred': 'int',
        'mover_state': 'str',
        'operation': 'str',
        'remote_ip_addr': 'str',
        'scsi_device': 'str',
        'session': 'str',
        'source_path': 'str',
        'start_time': 'int',
        'tape_device': 'str',
        'tape_open_mode': 'str',
        'throughput': 'int'
    }

    attribute_map = {
        'data_bytes_transferred': 'data_bytes_transferred',
        'data_state': 'data_state',
        'dest_path': 'dest_path',
        'dma_ip_addr': 'dma_ip_addr',
        'elapsed_time': 'elapsed_time',
        'id': 'id',
        'lnn': 'lnn',
        'mover_bytes_transferred': 'mover_bytes_transferred',
        'mover_state': 'mover_state',
        'operation': 'operation',
        'remote_ip_addr': 'remote_ip_addr',
        'scsi_device': 'scsi_device',
        'session': 'session',
        'source_path': 'source_path',
        'start_time': 'start_time',
        'tape_device': 'tape_device',
        'tape_open_mode': 'tape_open_mode',
        'throughput': 'throughput'
    }

    def __init__(self, data_bytes_transferred=None, data_state=None, dest_path=None, dma_ip_addr=None, elapsed_time=None, id=None, lnn=None, mover_bytes_transferred=None, mover_state=None, operation=None, remote_ip_addr=None, scsi_device=None, session=None, source_path=None, start_time=None, tape_device=None, tape_open_mode=None, throughput=None):  # noqa: E501
        """NdmpSession - a model defined in Swagger"""  # noqa: E501

        self._data_bytes_transferred = None
        self._data_state = None
        self._dest_path = None
        self._dma_ip_addr = None
        self._elapsed_time = None
        self._id = None
        self._lnn = None
        self._mover_bytes_transferred = None
        self._mover_state = None
        self._operation = None
        self._remote_ip_addr = None
        self._scsi_device = None
        self._session = None
        self._source_path = None
        self._start_time = None
        self._tape_device = None
        self._tape_open_mode = None
        self._throughput = None
        self.discriminator = None

        self.data_bytes_transferred = data_bytes_transferred
        self.data_state = data_state
        self.dest_path = dest_path
        self.dma_ip_addr = dma_ip_addr
        self.elapsed_time = elapsed_time
        self.id = id
        self.lnn = lnn
        self.mover_bytes_transferred = mover_bytes_transferred
        self.mover_state = mover_state
        self.operation = operation
        self.remote_ip_addr = remote_ip_addr
        self.scsi_device = scsi_device
        self.session = session
        self.source_path = source_path
        self.start_time = start_time
        self.tape_device = tape_device
        self.tape_open_mode = tape_open_mode
        self.throughput = throughput

    @property
    def data_bytes_transferred(self):
        """Gets the data_bytes_transferred of this NdmpSession.  # noqa: E501

        Bytes transferred to/from the filesystem  # noqa: E501

        :return: The data_bytes_transferred of this NdmpSession.  # noqa: E501
        :rtype: int
        """
        return self._data_bytes_transferred

    @data_bytes_transferred.setter
    def data_bytes_transferred(self, data_bytes_transferred):
        """Sets the data_bytes_transferred of this NdmpSession.

        Bytes transferred to/from the filesystem  # noqa: E501

        :param data_bytes_transferred: The data_bytes_transferred of this NdmpSession.  # noqa: E501
        :type: int
        """
        if data_bytes_transferred is None:
            raise ValueError("Invalid value for `data_bytes_transferred`, must not be `None`")  # noqa: E501

        self._data_bytes_transferred = data_bytes_transferred

    @property
    def data_state(self):
        """Gets the data_state of this NdmpSession.  # noqa: E501

        State of the NDMP Data Service  # noqa: E501

        :return: The data_state of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._data_state

    @data_state.setter
    def data_state(self, data_state):
        """Sets the data_state of this NdmpSession.

        State of the NDMP Data Service  # noqa: E501

        :param data_state: The data_state of this NdmpSession.  # noqa: E501
        :type: str
        """
        if data_state is None:
            raise ValueError("Invalid value for `data_state`, must not be `None`")  # noqa: E501
        allowed_values = ["IDLE", "LISTEN", "ACTIVE", "CONNECTED", "HALTED", "INVALID"]  # noqa: E501
        if data_state not in allowed_values:
            raise ValueError(
                "Invalid value for `data_state` ({0}), must be one of {1}"  # noqa: E501
                .format(data_state, allowed_values)
            )

        self._data_state = data_state

    @property
    def dest_path(self):
        """Gets the dest_path of this NdmpSession.  # noqa: E501

        The path being recovered to  # noqa: E501

        :return: The dest_path of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._dest_path

    @dest_path.setter
    def dest_path(self, dest_path):
        """Sets the dest_path of this NdmpSession.

        The path being recovered to  # noqa: E501

        :param dest_path: The dest_path of this NdmpSession.  # noqa: E501
        :type: str
        """
        if dest_path is None:
            raise ValueError("Invalid value for `dest_path`, must not be `None`")  # noqa: E501

        self._dest_path = dest_path

    @property
    def dma_ip_addr(self):
        """Gets the dma_ip_addr of this NdmpSession.  # noqa: E501

        IP address of the DMA  # noqa: E501

        :return: The dma_ip_addr of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._dma_ip_addr

    @dma_ip_addr.setter
    def dma_ip_addr(self, dma_ip_addr):
        """Sets the dma_ip_addr of this NdmpSession.

        IP address of the DMA  # noqa: E501

        :param dma_ip_addr: The dma_ip_addr of this NdmpSession.  # noqa: E501
        :type: str
        """
        if dma_ip_addr is None:
            raise ValueError("Invalid value for `dma_ip_addr`, must not be `None`")  # noqa: E501

        self._dma_ip_addr = dma_ip_addr

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this NdmpSession.  # noqa: E501

        Number of seconds elapsed since the backup was started  # noqa: E501

        :return: The elapsed_time of this NdmpSession.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this NdmpSession.

        Number of seconds elapsed since the backup was started  # noqa: E501

        :param elapsed_time: The elapsed_time of this NdmpSession.  # noqa: E501
        :type: int
        """
        if elapsed_time is None:
            raise ValueError("Invalid value for `elapsed_time`, must not be `None`")  # noqa: E501

        self._elapsed_time = elapsed_time

    @property
    def id(self):
        """Gets the id of this NdmpSession.  # noqa: E501

        Unique display ID.  # noqa: E501

        :return: The id of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NdmpSession.

        Unique display ID.  # noqa: E501

        :param id: The id of this NdmpSession.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NdmpSession.  # noqa: E501

        The lnn of the active session.  # noqa: E501

        :return: The lnn of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NdmpSession.

        The lnn of the active session.  # noqa: E501

        :param lnn: The lnn of this NdmpSession.  # noqa: E501
        :type: str
        """
        if lnn is None:
            raise ValueError("Invalid value for `lnn`, must not be `None`")  # noqa: E501

        self._lnn = lnn

    @property
    def mover_bytes_transferred(self):
        """Gets the mover_bytes_transferred of this NdmpSession.  # noqa: E501

        Bytes transferred to/from tape or remote writer  # noqa: E501

        :return: The mover_bytes_transferred of this NdmpSession.  # noqa: E501
        :rtype: int
        """
        return self._mover_bytes_transferred

    @mover_bytes_transferred.setter
    def mover_bytes_transferred(self, mover_bytes_transferred):
        """Sets the mover_bytes_transferred of this NdmpSession.

        Bytes transferred to/from tape or remote writer  # noqa: E501

        :param mover_bytes_transferred: The mover_bytes_transferred of this NdmpSession.  # noqa: E501
        :type: int
        """
        if mover_bytes_transferred is None:
            raise ValueError("Invalid value for `mover_bytes_transferred`, must not be `None`")  # noqa: E501

        self._mover_bytes_transferred = mover_bytes_transferred

    @property
    def mover_state(self):
        """Gets the mover_state of this NdmpSession.  # noqa: E501

        State of the NDMP Mover Service  # noqa: E501

        :return: The mover_state of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._mover_state

    @mover_state.setter
    def mover_state(self, mover_state):
        """Sets the mover_state of this NdmpSession.

        State of the NDMP Mover Service  # noqa: E501

        :param mover_state: The mover_state of this NdmpSession.  # noqa: E501
        :type: str
        """
        if mover_state is None:
            raise ValueError("Invalid value for `mover_state`, must not be `None`")  # noqa: E501
        allowed_values = ["IDLE", "LISTEN", "ACTIVE", "PAUSED", "HALTED", "INVALID"]  # noqa: E501
        if mover_state not in allowed_values:
            raise ValueError(
                "Invalid value for `mover_state` ({0}), must be one of {1}"  # noqa: E501
                .format(mover_state, allowed_values)
            )

        self._mover_state = mover_state

    @property
    def operation(self):
        """Gets the operation of this NdmpSession.  # noqa: E501

        The type of backup session  # noqa: E501

        :return: The operation of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this NdmpSession.

        The type of backup session  # noqa: E501

        :param operation: The operation of this NdmpSession.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Backup", "Recover", "Recover file history"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def remote_ip_addr(self):
        """Gets the remote_ip_addr of this NdmpSession.  # noqa: E501

        IP address of the remote NDMP participant  # noqa: E501

        :return: The remote_ip_addr of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._remote_ip_addr

    @remote_ip_addr.setter
    def remote_ip_addr(self, remote_ip_addr):
        """Sets the remote_ip_addr of this NdmpSession.

        IP address of the remote NDMP participant  # noqa: E501

        :param remote_ip_addr: The remote_ip_addr of this NdmpSession.  # noqa: E501
        :type: str
        """
        if remote_ip_addr is None:
            raise ValueError("Invalid value for `remote_ip_addr`, must not be `None`")  # noqa: E501

        self._remote_ip_addr = remote_ip_addr

    @property
    def scsi_device(self):
        """Gets the scsi_device of this NdmpSession.  # noqa: E501

        Name of the media changer device used if any  # noqa: E501

        :return: The scsi_device of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._scsi_device

    @scsi_device.setter
    def scsi_device(self, scsi_device):
        """Sets the scsi_device of this NdmpSession.

        Name of the media changer device used if any  # noqa: E501

        :param scsi_device: The scsi_device of this NdmpSession.  # noqa: E501
        :type: str
        """
        if scsi_device is None:
            raise ValueError("Invalid value for `scsi_device`, must not be `None`")  # noqa: E501

        self._scsi_device = scsi_device

    @property
    def session(self):
        """Gets the session of this NdmpSession.  # noqa: E501

        Session ID in form <lnn>.<pid>.  # noqa: E501

        :return: The session of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this NdmpSession.

        Session ID in form <lnn>.<pid>.  # noqa: E501

        :param session: The session of this NdmpSession.  # noqa: E501
        :type: str
        """
        if session is None:
            raise ValueError("Invalid value for `session`, must not be `None`")  # noqa: E501

        self._session = session

    @property
    def source_path(self):
        """Gets the source_path of this NdmpSession.  # noqa: E501

        The path being backed up  # noqa: E501

        :return: The source_path of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._source_path

    @source_path.setter
    def source_path(self, source_path):
        """Sets the source_path of this NdmpSession.

        The path being backed up  # noqa: E501

        :param source_path: The source_path of this NdmpSession.  # noqa: E501
        :type: str
        """
        if source_path is None:
            raise ValueError("Invalid value for `source_path`, must not be `None`")  # noqa: E501

        self._source_path = source_path

    @property
    def start_time(self):
        """Gets the start_time of this NdmpSession.  # noqa: E501

        Time backup was started in seconds since epoch  # noqa: E501

        :return: The start_time of this NdmpSession.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this NdmpSession.

        Time backup was started in seconds since epoch  # noqa: E501

        :param start_time: The start_time of this NdmpSession.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def tape_device(self):
        """Gets the tape_device of this NdmpSession.  # noqa: E501

        Name of the tape device used if any  # noqa: E501

        :return: The tape_device of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._tape_device

    @tape_device.setter
    def tape_device(self, tape_device):
        """Sets the tape_device of this NdmpSession.

        Name of the tape device used if any  # noqa: E501

        :param tape_device: The tape_device of this NdmpSession.  # noqa: E501
        :type: str
        """
        if tape_device is None:
            raise ValueError("Invalid value for `tape_device`, must not be `None`")  # noqa: E501

        self._tape_device = tape_device

    @property
    def tape_open_mode(self):
        """Gets the tape_open_mode of this NdmpSession.  # noqa: E501

        Describes the mode in which the tape is opened  # noqa: E501

        :return: The tape_open_mode of this NdmpSession.  # noqa: E501
        :rtype: str
        """
        return self._tape_open_mode

    @tape_open_mode.setter
    def tape_open_mode(self, tape_open_mode):
        """Sets the tape_open_mode of this NdmpSession.

        Describes the mode in which the tape is opened  # noqa: E501

        :param tape_open_mode: The tape_open_mode of this NdmpSession.  # noqa: E501
        :type: str
        """
        if tape_open_mode is None:
            raise ValueError("Invalid value for `tape_open_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["Read", "Read/Write", "Raw", "Invalid"]  # noqa: E501
        if tape_open_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `tape_open_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(tape_open_mode, allowed_values)
            )

        self._tape_open_mode = tape_open_mode

    @property
    def throughput(self):
        """Gets the throughput of this NdmpSession.  # noqa: E501

        The throughput in MB/s  # noqa: E501

        :return: The throughput of this NdmpSession.  # noqa: E501
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this NdmpSession.

        The throughput in MB/s  # noqa: E501

        :param throughput: The throughput of this NdmpSession.  # noqa: E501
        :type: int
        """
        if throughput is None:
            raise ValueError("Invalid value for `throughput`, must not be `None`")  # noqa: E501

        self._throughput = throughput

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
        if not isinstance(other, NdmpSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
