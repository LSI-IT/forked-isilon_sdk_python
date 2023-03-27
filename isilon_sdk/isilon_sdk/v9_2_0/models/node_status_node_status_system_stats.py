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


class NodeStatusNodeStatusSystemStats(object):
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
        'all_scan_requests': 'int',
        'avg_scan_block_time': 'int',
        'avg_scan_duration': 'int',
        'batch_file_queue_max_size': 'int',
        'batch_file_queue_size': 'int',
        'cee_failure_count': 'int',
        'cee_infected_count': 'int',
        'cee_success_count': 'int',
        'fast_file_queue_max_size': 'int',
        'fast_file_queue_size': 'int',
        'files_processed': 'int',
        'files_skipped_per_filter': 'int',
        'files_skipped_per_size': 'int',
        'job_scan_requests': 'int',
        'manual_scan_requests': 'int',
        'on_demand_scan_requests': 'int',
        'scan_fails': 'int',
        'scan_timeouts': 'int',
        'slow_file_queue_max_size': 'int',
        'slow_file_queue_size': 'int'
    }

    attribute_map = {
        'all_scan_requests': 'all_scan_requests',
        'avg_scan_block_time': 'avg_scan_block_time',
        'avg_scan_duration': 'avg_scan_duration',
        'batch_file_queue_max_size': 'batch_file_queue_max_size',
        'batch_file_queue_size': 'batch_file_queue_size',
        'cee_failure_count': 'cee_failure_count',
        'cee_infected_count': 'cee_infected_count',
        'cee_success_count': 'cee_success_count',
        'fast_file_queue_max_size': 'fast_file_queue_max_size',
        'fast_file_queue_size': 'fast_file_queue_size',
        'files_processed': 'files_processed',
        'files_skipped_per_filter': 'files_skipped_per_filter',
        'files_skipped_per_size': 'files_skipped_per_size',
        'job_scan_requests': 'job_scan_requests',
        'manual_scan_requests': 'manual_scan_requests',
        'on_demand_scan_requests': 'on_demand_scan_requests',
        'scan_fails': 'scan_fails',
        'scan_timeouts': 'scan_timeouts',
        'slow_file_queue_max_size': 'slow_file_queue_max_size',
        'slow_file_queue_size': 'slow_file_queue_size'
    }

    def __init__(self, all_scan_requests=None, avg_scan_block_time=None, avg_scan_duration=None, batch_file_queue_max_size=None, batch_file_queue_size=None, cee_failure_count=None, cee_infected_count=None, cee_success_count=None, fast_file_queue_max_size=None, fast_file_queue_size=None, files_processed=None, files_skipped_per_filter=None, files_skipped_per_size=None, job_scan_requests=None, manual_scan_requests=None, on_demand_scan_requests=None, scan_fails=None, scan_timeouts=None, slow_file_queue_max_size=None, slow_file_queue_size=None):  # noqa: E501
        """NodeStatusNodeStatusSystemStats - a model defined in Swagger"""  # noqa: E501

        self._all_scan_requests = None
        self._avg_scan_block_time = None
        self._avg_scan_duration = None
        self._batch_file_queue_max_size = None
        self._batch_file_queue_size = None
        self._cee_failure_count = None
        self._cee_infected_count = None
        self._cee_success_count = None
        self._fast_file_queue_max_size = None
        self._fast_file_queue_size = None
        self._files_processed = None
        self._files_skipped_per_filter = None
        self._files_skipped_per_size = None
        self._job_scan_requests = None
        self._manual_scan_requests = None
        self._on_demand_scan_requests = None
        self._scan_fails = None
        self._scan_timeouts = None
        self._slow_file_queue_max_size = None
        self._slow_file_queue_size = None
        self.discriminator = None

        if all_scan_requests is not None:
            self.all_scan_requests = all_scan_requests
        if avg_scan_block_time is not None:
            self.avg_scan_block_time = avg_scan_block_time
        if avg_scan_duration is not None:
            self.avg_scan_duration = avg_scan_duration
        if batch_file_queue_max_size is not None:
            self.batch_file_queue_max_size = batch_file_queue_max_size
        if batch_file_queue_size is not None:
            self.batch_file_queue_size = batch_file_queue_size
        if cee_failure_count is not None:
            self.cee_failure_count = cee_failure_count
        if cee_infected_count is not None:
            self.cee_infected_count = cee_infected_count
        if cee_success_count is not None:
            self.cee_success_count = cee_success_count
        if fast_file_queue_max_size is not None:
            self.fast_file_queue_max_size = fast_file_queue_max_size
        if fast_file_queue_size is not None:
            self.fast_file_queue_size = fast_file_queue_size
        if files_processed is not None:
            self.files_processed = files_processed
        if files_skipped_per_filter is not None:
            self.files_skipped_per_filter = files_skipped_per_filter
        if files_skipped_per_size is not None:
            self.files_skipped_per_size = files_skipped_per_size
        if job_scan_requests is not None:
            self.job_scan_requests = job_scan_requests
        if manual_scan_requests is not None:
            self.manual_scan_requests = manual_scan_requests
        if on_demand_scan_requests is not None:
            self.on_demand_scan_requests = on_demand_scan_requests
        if scan_fails is not None:
            self.scan_fails = scan_fails
        if scan_timeouts is not None:
            self.scan_timeouts = scan_timeouts
        if slow_file_queue_max_size is not None:
            self.slow_file_queue_max_size = slow_file_queue_max_size
        if slow_file_queue_size is not None:
            self.slow_file_queue_size = slow_file_queue_size

    @property
    def all_scan_requests(self):
        """Gets the all_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Total number of scan requests received by the CAVA antivirus system.  # noqa: E501

        :return: The all_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._all_scan_requests

    @all_scan_requests.setter
    def all_scan_requests(self, all_scan_requests):
        """Sets the all_scan_requests of this NodeStatusNodeStatusSystemStats.

        Total number of scan requests received by the CAVA antivirus system.  # noqa: E501

        :param all_scan_requests: The all_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if all_scan_requests is not None and all_scan_requests > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `all_scan_requests`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if all_scan_requests is not None and all_scan_requests < 0:  # noqa: E501
            raise ValueError("Invalid value for `all_scan_requests`, must be a value greater than or equal to `0`")  # noqa: E501

        self._all_scan_requests = all_scan_requests

    @property
    def avg_scan_block_time(self):
        """Gets the avg_scan_block_time of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Average time spent during which the scan requests are blocked.  # noqa: E501

        :return: The avg_scan_block_time of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._avg_scan_block_time

    @avg_scan_block_time.setter
    def avg_scan_block_time(self, avg_scan_block_time):
        """Sets the avg_scan_block_time of this NodeStatusNodeStatusSystemStats.

        Average time spent during which the scan requests are blocked.  # noqa: E501

        :param avg_scan_block_time: The avg_scan_block_time of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if avg_scan_block_time is not None and avg_scan_block_time > 3600000:  # noqa: E501
            raise ValueError("Invalid value for `avg_scan_block_time`, must be a value less than or equal to `3600000`")  # noqa: E501
        if avg_scan_block_time is not None and avg_scan_block_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `avg_scan_block_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._avg_scan_block_time = avg_scan_block_time

    @property
    def avg_scan_duration(self):
        """Gets the avg_scan_duration of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Average time to scan a file (in milliseconds).  # noqa: E501

        :return: The avg_scan_duration of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._avg_scan_duration

    @avg_scan_duration.setter
    def avg_scan_duration(self, avg_scan_duration):
        """Sets the avg_scan_duration of this NodeStatusNodeStatusSystemStats.

        Average time to scan a file (in milliseconds).  # noqa: E501

        :param avg_scan_duration: The avg_scan_duration of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if avg_scan_duration is not None and avg_scan_duration > 3600000:  # noqa: E501
            raise ValueError("Invalid value for `avg_scan_duration`, must be a value less than or equal to `3600000`")  # noqa: E501
        if avg_scan_duration is not None and avg_scan_duration < 0:  # noqa: E501
            raise ValueError("Invalid value for `avg_scan_duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._avg_scan_duration = avg_scan_duration

    @property
    def batch_file_queue_max_size(self):
        """Gets the batch_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Maximum number of files that can be queued in the batch file queue.  # noqa: E501

        :return: The batch_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._batch_file_queue_max_size

    @batch_file_queue_max_size.setter
    def batch_file_queue_max_size(self, batch_file_queue_max_size):
        """Sets the batch_file_queue_max_size of this NodeStatusNodeStatusSystemStats.

        Maximum number of files that can be queued in the batch file queue.  # noqa: E501

        :param batch_file_queue_max_size: The batch_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if batch_file_queue_max_size is not None and batch_file_queue_max_size > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `batch_file_queue_max_size`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if batch_file_queue_max_size is not None and batch_file_queue_max_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `batch_file_queue_max_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._batch_file_queue_max_size = batch_file_queue_max_size

    @property
    def batch_file_queue_size(self):
        """Gets the batch_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Number of scan requests queued for scanning in the batch file queue.  # noqa: E501

        :return: The batch_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._batch_file_queue_size

    @batch_file_queue_size.setter
    def batch_file_queue_size(self, batch_file_queue_size):
        """Sets the batch_file_queue_size of this NodeStatusNodeStatusSystemStats.

        Number of scan requests queued for scanning in the batch file queue.  # noqa: E501

        :param batch_file_queue_size: The batch_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if batch_file_queue_size is not None and batch_file_queue_size > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `batch_file_queue_size`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if batch_file_queue_size is not None and batch_file_queue_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `batch_file_queue_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._batch_file_queue_size = batch_file_queue_size

    @property
    def cee_failure_count(self):
        """Gets the cee_failure_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Number of scan failure responses received from CEE server.  # noqa: E501

        :return: The cee_failure_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._cee_failure_count

    @cee_failure_count.setter
    def cee_failure_count(self, cee_failure_count):
        """Sets the cee_failure_count of this NodeStatusNodeStatusSystemStats.

        Number of scan failure responses received from CEE server.  # noqa: E501

        :param cee_failure_count: The cee_failure_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if cee_failure_count is not None and cee_failure_count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `cee_failure_count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if cee_failure_count is not None and cee_failure_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `cee_failure_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cee_failure_count = cee_failure_count

    @property
    def cee_infected_count(self):
        """Gets the cee_infected_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Number of scan infected responses received from CEE server.  # noqa: E501

        :return: The cee_infected_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._cee_infected_count

    @cee_infected_count.setter
    def cee_infected_count(self, cee_infected_count):
        """Sets the cee_infected_count of this NodeStatusNodeStatusSystemStats.

        Number of scan infected responses received from CEE server.  # noqa: E501

        :param cee_infected_count: The cee_infected_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if cee_infected_count is not None and cee_infected_count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `cee_infected_count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if cee_infected_count is not None and cee_infected_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `cee_infected_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cee_infected_count = cee_infected_count

    @property
    def cee_success_count(self):
        """Gets the cee_success_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Number of scan success responses received from CEE server.  # noqa: E501

        :return: The cee_success_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._cee_success_count

    @cee_success_count.setter
    def cee_success_count(self, cee_success_count):
        """Sets the cee_success_count of this NodeStatusNodeStatusSystemStats.

        Number of scan success responses received from CEE server.  # noqa: E501

        :param cee_success_count: The cee_success_count of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if cee_success_count is not None and cee_success_count > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `cee_success_count`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if cee_success_count is not None and cee_success_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `cee_success_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cee_success_count = cee_success_count

    @property
    def fast_file_queue_max_size(self):
        """Gets the fast_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Maximum number of files that can be queued in the fast file queue.  # noqa: E501

        :return: The fast_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._fast_file_queue_max_size

    @fast_file_queue_max_size.setter
    def fast_file_queue_max_size(self, fast_file_queue_max_size):
        """Sets the fast_file_queue_max_size of this NodeStatusNodeStatusSystemStats.

        Maximum number of files that can be queued in the fast file queue.  # noqa: E501

        :param fast_file_queue_max_size: The fast_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if fast_file_queue_max_size is not None and fast_file_queue_max_size > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `fast_file_queue_max_size`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if fast_file_queue_max_size is not None and fast_file_queue_max_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `fast_file_queue_max_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fast_file_queue_max_size = fast_file_queue_max_size

    @property
    def fast_file_queue_size(self):
        """Gets the fast_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Number of scan requests queued for scanning in the fast file queue.  # noqa: E501

        :return: The fast_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._fast_file_queue_size

    @fast_file_queue_size.setter
    def fast_file_queue_size(self, fast_file_queue_size):
        """Sets the fast_file_queue_size of this NodeStatusNodeStatusSystemStats.

        Number of scan requests queued for scanning in the fast file queue.  # noqa: E501

        :param fast_file_queue_size: The fast_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if fast_file_queue_size is not None and fast_file_queue_size > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `fast_file_queue_size`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if fast_file_queue_size is not None and fast_file_queue_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `fast_file_queue_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fast_file_queue_size = fast_file_queue_size

    @property
    def files_processed(self):
        """Gets the files_processed of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Total number of files processed by the CAVA antivirus system.  # noqa: E501

        :return: The files_processed of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._files_processed

    @files_processed.setter
    def files_processed(self, files_processed):
        """Sets the files_processed of this NodeStatusNodeStatusSystemStats.

        Total number of files processed by the CAVA antivirus system.  # noqa: E501

        :param files_processed: The files_processed of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if files_processed is not None and files_processed > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `files_processed`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if files_processed is not None and files_processed < 0:  # noqa: E501
            raise ValueError("Invalid value for `files_processed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._files_processed = files_processed

    @property
    def files_skipped_per_filter(self):
        """Gets the files_skipped_per_filter of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Total number of files skipped per filter settings.  # noqa: E501

        :return: The files_skipped_per_filter of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._files_skipped_per_filter

    @files_skipped_per_filter.setter
    def files_skipped_per_filter(self, files_skipped_per_filter):
        """Sets the files_skipped_per_filter of this NodeStatusNodeStatusSystemStats.

        Total number of files skipped per filter settings.  # noqa: E501

        :param files_skipped_per_filter: The files_skipped_per_filter of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if files_skipped_per_filter is not None and files_skipped_per_filter > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `files_skipped_per_filter`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if files_skipped_per_filter is not None and files_skipped_per_filter < 0:  # noqa: E501
            raise ValueError("Invalid value for `files_skipped_per_filter`, must be a value greater than or equal to `0`")  # noqa: E501

        self._files_skipped_per_filter = files_skipped_per_filter

    @property
    def files_skipped_per_size(self):
        """Gets the files_skipped_per_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Total number of files skipped per maximum size setting.  # noqa: E501

        :return: The files_skipped_per_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._files_skipped_per_size

    @files_skipped_per_size.setter
    def files_skipped_per_size(self, files_skipped_per_size):
        """Sets the files_skipped_per_size of this NodeStatusNodeStatusSystemStats.

        Total number of files skipped per maximum size setting.  # noqa: E501

        :param files_skipped_per_size: The files_skipped_per_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if files_skipped_per_size is not None and files_skipped_per_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `files_skipped_per_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if files_skipped_per_size is not None and files_skipped_per_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `files_skipped_per_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._files_skipped_per_size = files_skipped_per_size

    @property
    def job_scan_requests(self):
        """Gets the job_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Total number of scan requests received from the job engine.  # noqa: E501

        :return: The job_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._job_scan_requests

    @job_scan_requests.setter
    def job_scan_requests(self, job_scan_requests):
        """Sets the job_scan_requests of this NodeStatusNodeStatusSystemStats.

        Total number of scan requests received from the job engine.  # noqa: E501

        :param job_scan_requests: The job_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if job_scan_requests is not None and job_scan_requests > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `job_scan_requests`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if job_scan_requests is not None and job_scan_requests < 0:  # noqa: E501
            raise ValueError("Invalid value for `job_scan_requests`, must be a value greater than or equal to `0`")  # noqa: E501

        self._job_scan_requests = job_scan_requests

    @property
    def manual_scan_requests(self):
        """Gets the manual_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Total number of scan requests initiated through PAPI.  # noqa: E501

        :return: The manual_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._manual_scan_requests

    @manual_scan_requests.setter
    def manual_scan_requests(self, manual_scan_requests):
        """Sets the manual_scan_requests of this NodeStatusNodeStatusSystemStats.

        Total number of scan requests initiated through PAPI.  # noqa: E501

        :param manual_scan_requests: The manual_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if manual_scan_requests is not None and manual_scan_requests > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `manual_scan_requests`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if manual_scan_requests is not None and manual_scan_requests < 0:  # noqa: E501
            raise ValueError("Invalid value for `manual_scan_requests`, must be a value greater than or equal to `0`")  # noqa: E501

        self._manual_scan_requests = manual_scan_requests

    @property
    def on_demand_scan_requests(self):
        """Gets the on_demand_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Total number of on-demand (protocol) scan requests received.  # noqa: E501

        :return: The on_demand_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._on_demand_scan_requests

    @on_demand_scan_requests.setter
    def on_demand_scan_requests(self, on_demand_scan_requests):
        """Sets the on_demand_scan_requests of this NodeStatusNodeStatusSystemStats.

        Total number of on-demand (protocol) scan requests received.  # noqa: E501

        :param on_demand_scan_requests: The on_demand_scan_requests of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if on_demand_scan_requests is not None and on_demand_scan_requests > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `on_demand_scan_requests`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if on_demand_scan_requests is not None and on_demand_scan_requests < 0:  # noqa: E501
            raise ValueError("Invalid value for `on_demand_scan_requests`, must be a value greater than or equal to `0`")  # noqa: E501

        self._on_demand_scan_requests = on_demand_scan_requests

    @property
    def scan_fails(self):
        """Gets the scan_fails of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Number of scan failures occurred while scanning.  # noqa: E501

        :return: The scan_fails of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._scan_fails

    @scan_fails.setter
    def scan_fails(self, scan_fails):
        """Sets the scan_fails of this NodeStatusNodeStatusSystemStats.

        Number of scan failures occurred while scanning.  # noqa: E501

        :param scan_fails: The scan_fails of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if scan_fails is not None and scan_fails > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `scan_fails`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if scan_fails is not None and scan_fails < 0:  # noqa: E501
            raise ValueError("Invalid value for `scan_fails`, must be a value greater than or equal to `0`")  # noqa: E501

        self._scan_fails = scan_fails

    @property
    def scan_timeouts(self):
        """Gets the scan_timeouts of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Number of scan timeouts occurred while scanning.  # noqa: E501

        :return: The scan_timeouts of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._scan_timeouts

    @scan_timeouts.setter
    def scan_timeouts(self, scan_timeouts):
        """Sets the scan_timeouts of this NodeStatusNodeStatusSystemStats.

        Number of scan timeouts occurred while scanning.  # noqa: E501

        :param scan_timeouts: The scan_timeouts of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if scan_timeouts is not None and scan_timeouts > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `scan_timeouts`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if scan_timeouts is not None and scan_timeouts < 0:  # noqa: E501
            raise ValueError("Invalid value for `scan_timeouts`, must be a value greater than or equal to `0`")  # noqa: E501

        self._scan_timeouts = scan_timeouts

    @property
    def slow_file_queue_max_size(self):
        """Gets the slow_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Maximum number of files that can be queued in the slow (large/cloudpool) file queue.  # noqa: E501

        :return: The slow_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._slow_file_queue_max_size

    @slow_file_queue_max_size.setter
    def slow_file_queue_max_size(self, slow_file_queue_max_size):
        """Sets the slow_file_queue_max_size of this NodeStatusNodeStatusSystemStats.

        Maximum number of files that can be queued in the slow (large/cloudpool) file queue.  # noqa: E501

        :param slow_file_queue_max_size: The slow_file_queue_max_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if slow_file_queue_max_size is not None and slow_file_queue_max_size > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `slow_file_queue_max_size`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if slow_file_queue_max_size is not None and slow_file_queue_max_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `slow_file_queue_max_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._slow_file_queue_max_size = slow_file_queue_max_size

    @property
    def slow_file_queue_size(self):
        """Gets the slow_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501

        Number of scan requests queued for scanning in the slow (large/cloudpool) file queue.  # noqa: E501

        :return: The slow_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :rtype: int
        """
        return self._slow_file_queue_size

    @slow_file_queue_size.setter
    def slow_file_queue_size(self, slow_file_queue_size):
        """Sets the slow_file_queue_size of this NodeStatusNodeStatusSystemStats.

        Number of scan requests queued for scanning in the slow (large/cloudpool) file queue.  # noqa: E501

        :param slow_file_queue_size: The slow_file_queue_size of this NodeStatusNodeStatusSystemStats.  # noqa: E501
        :type: int
        """
        if slow_file_queue_size is not None and slow_file_queue_size > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `slow_file_queue_size`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if slow_file_queue_size is not None and slow_file_queue_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `slow_file_queue_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._slow_file_queue_size = slow_file_queue_size

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
        if not isinstance(other, NodeStatusNodeStatusSystemStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
