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

from isilon_sdk.v9_1_0.models.job_statistics_job_node_cpu import JobStatisticsJobNodeCpu  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.job_statistics_job_node_io import JobStatisticsJobNodeIo  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.job_statistics_job_node_memory import JobStatisticsJobNodeMemory  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.job_statistics_job_node_worker import JobStatisticsJobNodeWorker  # noqa: F401,E501


class JobStatisticsJobNode(object):
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
        'cpu': 'JobStatisticsJobNodeCpu',
        'io': 'JobStatisticsJobNodeIo',
        'memory': 'JobStatisticsJobNodeMemory',
        'node': 'int',
        'pid': 'int',
        'total_workers': 'int',
        'workers': 'list[JobStatisticsJobNodeWorker]'
    }

    attribute_map = {
        'cpu': 'cpu',
        'io': 'io',
        'memory': 'memory',
        'node': 'node',
        'pid': 'pid',
        'total_workers': 'total_workers',
        'workers': 'workers'
    }

    def __init__(self, cpu=None, io=None, memory=None, node=None, pid=None, total_workers=None, workers=None):  # noqa: E501
        """JobStatisticsJobNode - a model defined in Swagger"""  # noqa: E501

        self._cpu = None
        self._io = None
        self._memory = None
        self._node = None
        self._pid = None
        self._total_workers = None
        self._workers = None
        self.discriminator = None

        self.cpu = cpu
        self.io = io
        self.memory = memory
        self.node = node
        self.pid = pid
        self.total_workers = total_workers
        self.workers = workers

    @property
    def cpu(self):
        """Gets the cpu of this JobStatisticsJobNode.  # noqa: E501

          # noqa: E501

        :return: The cpu of this JobStatisticsJobNode.  # noqa: E501
        :rtype: JobStatisticsJobNodeCpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this JobStatisticsJobNode.

          # noqa: E501

        :param cpu: The cpu of this JobStatisticsJobNode.  # noqa: E501
        :type: JobStatisticsJobNodeCpu
        """
        if cpu is None:
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def io(self):
        """Gets the io of this JobStatisticsJobNode.  # noqa: E501

          # noqa: E501

        :return: The io of this JobStatisticsJobNode.  # noqa: E501
        :rtype: JobStatisticsJobNodeIo
        """
        return self._io

    @io.setter
    def io(self, io):
        """Sets the io of this JobStatisticsJobNode.

          # noqa: E501

        :param io: The io of this JobStatisticsJobNode.  # noqa: E501
        :type: JobStatisticsJobNodeIo
        """
        if io is None:
            raise ValueError("Invalid value for `io`, must not be `None`")  # noqa: E501

        self._io = io

    @property
    def memory(self):
        """Gets the memory of this JobStatisticsJobNode.  # noqa: E501

          # noqa: E501

        :return: The memory of this JobStatisticsJobNode.  # noqa: E501
        :rtype: JobStatisticsJobNodeMemory
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this JobStatisticsJobNode.

          # noqa: E501

        :param memory: The memory of this JobStatisticsJobNode.  # noqa: E501
        :type: JobStatisticsJobNodeMemory
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def node(self):
        """Gets the node of this JobStatisticsJobNode.  # noqa: E501

        The devid of the node.  # noqa: E501

        :return: The node of this JobStatisticsJobNode.  # noqa: E501
        :rtype: int
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this JobStatisticsJobNode.

        The devid of the node.  # noqa: E501

        :param node: The node of this JobStatisticsJobNode.  # noqa: E501
        :type: int
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def pid(self):
        """Gets the pid of this JobStatisticsJobNode.  # noqa: E501

        The process ID of the job on this node.  # noqa: E501

        :return: The pid of this JobStatisticsJobNode.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this JobStatisticsJobNode.

        The process ID of the job on this node.  # noqa: E501

        :param pid: The pid of this JobStatisticsJobNode.  # noqa: E501
        :type: int
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")  # noqa: E501

        self._pid = pid

    @property
    def total_workers(self):
        """Gets the total_workers of this JobStatisticsJobNode.  # noqa: E501

        The number of workers for this job on this node.  # noqa: E501

        :return: The total_workers of this JobStatisticsJobNode.  # noqa: E501
        :rtype: int
        """
        return self._total_workers

    @total_workers.setter
    def total_workers(self, total_workers):
        """Sets the total_workers of this JobStatisticsJobNode.

        The number of workers for this job on this node.  # noqa: E501

        :param total_workers: The total_workers of this JobStatisticsJobNode.  # noqa: E501
        :type: int
        """
        if total_workers is None:
            raise ValueError("Invalid value for `total_workers`, must not be `None`")  # noqa: E501

        self._total_workers = total_workers

    @property
    def workers(self):
        """Gets the workers of this JobStatisticsJobNode.  # noqa: E501


        :return: The workers of this JobStatisticsJobNode.  # noqa: E501
        :rtype: list[JobStatisticsJobNodeWorker]
        """
        return self._workers

    @workers.setter
    def workers(self, workers):
        """Sets the workers of this JobStatisticsJobNode.


        :param workers: The workers of this JobStatisticsJobNode.  # noqa: E501
        :type: list[JobStatisticsJobNodeWorker]
        """
        if workers is None:
            raise ValueError("Invalid value for `workers`, must not be `None`")  # noqa: E501

        self._workers = workers

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
        if not isinstance(other, JobStatisticsJobNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
