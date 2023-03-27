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

from isilon_sdk.v9_5_0.models.sync_policy_source_network import SyncPolicySourceNetwork  # noqa: F401,E501


class SyncSettingsSettings(object):
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
        'bandwidth_reservation_reserve_absolute': 'int',
        'bandwidth_reservation_reserve_percentage': 'int',
        'cluster_certificate_id': 'str',
        'encryption_cipher_list': 'str',
        'encryption_required': 'bool',
        'force_interface': 'bool',
        'max_concurrent_jobs': 'int',
        'ocsp_address': 'str',
        'ocsp_issuer_certificate_id': 'str',
        'password_set': 'bool',
        'preferred_rpo_alert': 'int',
        'renegotiation_period': 'int',
        'report_email': 'list[str]',
        'report_max_age': 'int',
        'report_max_count': 'int',
        'restrict_target_network': 'bool',
        'rpo_alerts': 'bool',
        'service': 'str',
        'service_history_max_age': 'int',
        'service_history_max_count': 'int',
        'source_network': 'SyncPolicySourceNetwork',
        'tw_chkpt_interval': 'int',
        'use_workers_per_node': 'bool'
    }

    attribute_map = {
        'bandwidth_reservation_reserve_absolute': 'bandwidth_reservation_reserve_absolute',
        'bandwidth_reservation_reserve_percentage': 'bandwidth_reservation_reserve_percentage',
        'cluster_certificate_id': 'cluster_certificate_id',
        'encryption_cipher_list': 'encryption_cipher_list',
        'encryption_required': 'encryption_required',
        'force_interface': 'force_interface',
        'max_concurrent_jobs': 'max_concurrent_jobs',
        'ocsp_address': 'ocsp_address',
        'ocsp_issuer_certificate_id': 'ocsp_issuer_certificate_id',
        'password_set': 'password_set',
        'preferred_rpo_alert': 'preferred_rpo_alert',
        'renegotiation_period': 'renegotiation_period',
        'report_email': 'report_email',
        'report_max_age': 'report_max_age',
        'report_max_count': 'report_max_count',
        'restrict_target_network': 'restrict_target_network',
        'rpo_alerts': 'rpo_alerts',
        'service': 'service',
        'service_history_max_age': 'service_history_max_age',
        'service_history_max_count': 'service_history_max_count',
        'source_network': 'source_network',
        'tw_chkpt_interval': 'tw_chkpt_interval',
        'use_workers_per_node': 'use_workers_per_node'
    }

    def __init__(self, bandwidth_reservation_reserve_absolute=None, bandwidth_reservation_reserve_percentage=None, cluster_certificate_id=None, encryption_cipher_list=None, encryption_required=None, force_interface=None, max_concurrent_jobs=None, ocsp_address=None, ocsp_issuer_certificate_id=None, password_set=None, preferred_rpo_alert=None, renegotiation_period=None, report_email=None, report_max_age=None, report_max_count=None, restrict_target_network=None, rpo_alerts=None, service=None, service_history_max_age=None, service_history_max_count=None, source_network=None, tw_chkpt_interval=None, use_workers_per_node=None):  # noqa: E501
        """SyncSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._bandwidth_reservation_reserve_absolute = None
        self._bandwidth_reservation_reserve_percentage = None
        self._cluster_certificate_id = None
        self._encryption_cipher_list = None
        self._encryption_required = None
        self._force_interface = None
        self._max_concurrent_jobs = None
        self._ocsp_address = None
        self._ocsp_issuer_certificate_id = None
        self._password_set = None
        self._preferred_rpo_alert = None
        self._renegotiation_period = None
        self._report_email = None
        self._report_max_age = None
        self._report_max_count = None
        self._restrict_target_network = None
        self._rpo_alerts = None
        self._service = None
        self._service_history_max_age = None
        self._service_history_max_count = None
        self._source_network = None
        self._tw_chkpt_interval = None
        self._use_workers_per_node = None
        self.discriminator = None

        if bandwidth_reservation_reserve_absolute is not None:
            self.bandwidth_reservation_reserve_absolute = bandwidth_reservation_reserve_absolute
        if bandwidth_reservation_reserve_percentage is not None:
            self.bandwidth_reservation_reserve_percentage = bandwidth_reservation_reserve_percentage
        if cluster_certificate_id is not None:
            self.cluster_certificate_id = cluster_certificate_id
        if encryption_cipher_list is not None:
            self.encryption_cipher_list = encryption_cipher_list
        if encryption_required is not None:
            self.encryption_required = encryption_required
        if force_interface is not None:
            self.force_interface = force_interface
        if max_concurrent_jobs is not None:
            self.max_concurrent_jobs = max_concurrent_jobs
        if ocsp_address is not None:
            self.ocsp_address = ocsp_address
        if ocsp_issuer_certificate_id is not None:
            self.ocsp_issuer_certificate_id = ocsp_issuer_certificate_id
        if password_set is not None:
            self.password_set = password_set
        if preferred_rpo_alert is not None:
            self.preferred_rpo_alert = preferred_rpo_alert
        if renegotiation_period is not None:
            self.renegotiation_period = renegotiation_period
        if report_email is not None:
            self.report_email = report_email
        if report_max_age is not None:
            self.report_max_age = report_max_age
        if report_max_count is not None:
            self.report_max_count = report_max_count
        if restrict_target_network is not None:
            self.restrict_target_network = restrict_target_network
        if rpo_alerts is not None:
            self.rpo_alerts = rpo_alerts
        if service is not None:
            self.service = service
        if service_history_max_age is not None:
            self.service_history_max_age = service_history_max_age
        if service_history_max_count is not None:
            self.service_history_max_count = service_history_max_count
        if source_network is not None:
            self.source_network = source_network
        if tw_chkpt_interval is not None:
            self.tw_chkpt_interval = tw_chkpt_interval
        if use_workers_per_node is not None:
            self.use_workers_per_node = use_workers_per_node

    @property
    def bandwidth_reservation_reserve_absolute(self):
        """Gets the bandwidth_reservation_reserve_absolute of this SyncSettingsSettings.  # noqa: E501

        The amount of SyncIQ bandwidth to reserve in kb/s for policies that did not specify a bandwidth reservation. This field takes precedence over bandwidth_reservation_reserve_percentage.  # noqa: E501

        :return: The bandwidth_reservation_reserve_absolute of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_reservation_reserve_absolute

    @bandwidth_reservation_reserve_absolute.setter
    def bandwidth_reservation_reserve_absolute(self, bandwidth_reservation_reserve_absolute):
        """Sets the bandwidth_reservation_reserve_absolute of this SyncSettingsSettings.

        The amount of SyncIQ bandwidth to reserve in kb/s for policies that did not specify a bandwidth reservation. This field takes precedence over bandwidth_reservation_reserve_percentage.  # noqa: E501

        :param bandwidth_reservation_reserve_absolute: The bandwidth_reservation_reserve_absolute of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if bandwidth_reservation_reserve_absolute is not None and bandwidth_reservation_reserve_absolute > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `bandwidth_reservation_reserve_absolute`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if bandwidth_reservation_reserve_absolute is not None and bandwidth_reservation_reserve_absolute < 0:  # noqa: E501
            raise ValueError("Invalid value for `bandwidth_reservation_reserve_absolute`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bandwidth_reservation_reserve_absolute = bandwidth_reservation_reserve_absolute

    @property
    def bandwidth_reservation_reserve_percentage(self):
        """Gets the bandwidth_reservation_reserve_percentage of this SyncSettingsSettings.  # noqa: E501

        The percentage of SyncIQ bandwidth to reserve for policies that did not specify a bandwidth reservation.  # noqa: E501

        :return: The bandwidth_reservation_reserve_percentage of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_reservation_reserve_percentage

    @bandwidth_reservation_reserve_percentage.setter
    def bandwidth_reservation_reserve_percentage(self, bandwidth_reservation_reserve_percentage):
        """Sets the bandwidth_reservation_reserve_percentage of this SyncSettingsSettings.

        The percentage of SyncIQ bandwidth to reserve for policies that did not specify a bandwidth reservation.  # noqa: E501

        :param bandwidth_reservation_reserve_percentage: The bandwidth_reservation_reserve_percentage of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if bandwidth_reservation_reserve_percentage is not None and bandwidth_reservation_reserve_percentage > 99:  # noqa: E501
            raise ValueError("Invalid value for `bandwidth_reservation_reserve_percentage`, must be a value less than or equal to `99`")  # noqa: E501
        if bandwidth_reservation_reserve_percentage is not None and bandwidth_reservation_reserve_percentage < 1:  # noqa: E501
            raise ValueError("Invalid value for `bandwidth_reservation_reserve_percentage`, must be a value greater than or equal to `1`")  # noqa: E501

        self._bandwidth_reservation_reserve_percentage = bandwidth_reservation_reserve_percentage

    @property
    def cluster_certificate_id(self):
        """Gets the cluster_certificate_id of this SyncSettingsSettings.  # noqa: E501

        The ID of this cluster's certificate being used for encryption.  # noqa: E501

        :return: The cluster_certificate_id of this SyncSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._cluster_certificate_id

    @cluster_certificate_id.setter
    def cluster_certificate_id(self, cluster_certificate_id):
        """Sets the cluster_certificate_id of this SyncSettingsSettings.

        The ID of this cluster's certificate being used for encryption.  # noqa: E501

        :param cluster_certificate_id: The cluster_certificate_id of this SyncSettingsSettings.  # noqa: E501
        :type: str
        """
        if cluster_certificate_id is not None and len(cluster_certificate_id) > 255:
            raise ValueError("Invalid value for `cluster_certificate_id`, length must be less than or equal to `255`")  # noqa: E501
        if cluster_certificate_id is not None and len(cluster_certificate_id) < 0:
            raise ValueError("Invalid value for `cluster_certificate_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._cluster_certificate_id = cluster_certificate_id

    @property
    def encryption_cipher_list(self):
        """Gets the encryption_cipher_list of this SyncSettingsSettings.  # noqa: E501

        The cipher list being used with encryption. For SyncIQ targets, this list serves as a list of supported ciphers. For SyncIQ sources, the list of ciphers will be attempted to be used in order.  # noqa: E501

        :return: The encryption_cipher_list of this SyncSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._encryption_cipher_list

    @encryption_cipher_list.setter
    def encryption_cipher_list(self, encryption_cipher_list):
        """Sets the encryption_cipher_list of this SyncSettingsSettings.

        The cipher list being used with encryption. For SyncIQ targets, this list serves as a list of supported ciphers. For SyncIQ sources, the list of ciphers will be attempted to be used in order.  # noqa: E501

        :param encryption_cipher_list: The encryption_cipher_list of this SyncSettingsSettings.  # noqa: E501
        :type: str
        """
        if encryption_cipher_list is not None and len(encryption_cipher_list) > 255:
            raise ValueError("Invalid value for `encryption_cipher_list`, length must be less than or equal to `255`")  # noqa: E501
        if encryption_cipher_list is not None and len(encryption_cipher_list) < 0:
            raise ValueError("Invalid value for `encryption_cipher_list`, length must be greater than or equal to `0`")  # noqa: E501

        self._encryption_cipher_list = encryption_cipher_list

    @property
    def encryption_required(self):
        """Gets the encryption_required of this SyncSettingsSettings.  # noqa: E501

        If true, requires all SyncIQ policies to utilize encrypted communications.  # noqa: E501

        :return: The encryption_required of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._encryption_required

    @encryption_required.setter
    def encryption_required(self, encryption_required):
        """Sets the encryption_required of this SyncSettingsSettings.

        If true, requires all SyncIQ policies to utilize encrypted communications.  # noqa: E501

        :param encryption_required: The encryption_required of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._encryption_required = encryption_required

    @property
    def force_interface(self):
        """Gets the force_interface of this SyncSettingsSettings.  # noqa: E501

        NOTE: This field should not be changed without the help of PowerScale support.  Default for the \"force_interface\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \"source_network\" field. This option can be useful if there are multiple interfaces for the given source subnet.  # noqa: E501

        :return: The force_interface of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_interface

    @force_interface.setter
    def force_interface(self, force_interface):
        """Sets the force_interface of this SyncSettingsSettings.

        NOTE: This field should not be changed without the help of PowerScale support.  Default for the \"force_interface\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \"source_network\" field. This option can be useful if there are multiple interfaces for the given source subnet.  # noqa: E501

        :param force_interface: The force_interface of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._force_interface = force_interface

    @property
    def max_concurrent_jobs(self):
        """Gets the max_concurrent_jobs of this SyncSettingsSettings.  # noqa: E501

        The max concurrent jobs that SyncIQ can support. This number is based on the size of the current cluster and the current SyncIQ worker throttle rule.  # noqa: E501

        :return: The max_concurrent_jobs of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_concurrent_jobs

    @max_concurrent_jobs.setter
    def max_concurrent_jobs(self, max_concurrent_jobs):
        """Sets the max_concurrent_jobs of this SyncSettingsSettings.

        The max concurrent jobs that SyncIQ can support. This number is based on the size of the current cluster and the current SyncIQ worker throttle rule.  # noqa: E501

        :param max_concurrent_jobs: The max_concurrent_jobs of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if max_concurrent_jobs is not None and max_concurrent_jobs > 1000:  # noqa: E501
            raise ValueError("Invalid value for `max_concurrent_jobs`, must be a value less than or equal to `1000`")  # noqa: E501
        if max_concurrent_jobs is not None and max_concurrent_jobs < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_concurrent_jobs`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_concurrent_jobs = max_concurrent_jobs

    @property
    def ocsp_address(self):
        """Gets the ocsp_address of this SyncSettingsSettings.  # noqa: E501

        The address of the OCSP responder to which to connect.  # noqa: E501

        :return: The ocsp_address of this SyncSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ocsp_address

    @ocsp_address.setter
    def ocsp_address(self, ocsp_address):
        """Sets the ocsp_address of this SyncSettingsSettings.

        The address of the OCSP responder to which to connect.  # noqa: E501

        :param ocsp_address: The ocsp_address of this SyncSettingsSettings.  # noqa: E501
        :type: str
        """
        if ocsp_address is not None and len(ocsp_address) > 255:
            raise ValueError("Invalid value for `ocsp_address`, length must be less than or equal to `255`")  # noqa: E501
        if ocsp_address is not None and len(ocsp_address) < 0:
            raise ValueError("Invalid value for `ocsp_address`, length must be greater than or equal to `0`")  # noqa: E501

        self._ocsp_address = ocsp_address

    @property
    def ocsp_issuer_certificate_id(self):
        """Gets the ocsp_issuer_certificate_id of this SyncSettingsSettings.  # noqa: E501

        The ID of the certificate authority that issued the certificate whose revocation status is being checked.  # noqa: E501

        :return: The ocsp_issuer_certificate_id of this SyncSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ocsp_issuer_certificate_id

    @ocsp_issuer_certificate_id.setter
    def ocsp_issuer_certificate_id(self, ocsp_issuer_certificate_id):
        """Sets the ocsp_issuer_certificate_id of this SyncSettingsSettings.

        The ID of the certificate authority that issued the certificate whose revocation status is being checked.  # noqa: E501

        :param ocsp_issuer_certificate_id: The ocsp_issuer_certificate_id of this SyncSettingsSettings.  # noqa: E501
        :type: str
        """
        if ocsp_issuer_certificate_id is not None and len(ocsp_issuer_certificate_id) > 255:
            raise ValueError("Invalid value for `ocsp_issuer_certificate_id`, length must be less than or equal to `255`")  # noqa: E501
        if ocsp_issuer_certificate_id is not None and len(ocsp_issuer_certificate_id) < 0:
            raise ValueError("Invalid value for `ocsp_issuer_certificate_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._ocsp_issuer_certificate_id = ocsp_issuer_certificate_id

    @property
    def password_set(self):
        """Gets the password_set of this SyncSettingsSettings.  # noqa: E501

        Indicates if a password is set for authentication. Password value is not shown with GET.  # noqa: E501

        :return: The password_set of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._password_set

    @password_set.setter
    def password_set(self, password_set):
        """Sets the password_set of this SyncSettingsSettings.

        Indicates if a password is set for authentication. Password value is not shown with GET.  # noqa: E501

        :param password_set: The password_set of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._password_set = password_set

    @property
    def preferred_rpo_alert(self):
        """Gets the preferred_rpo_alert of this SyncSettingsSettings.  # noqa: E501

        If specified, display as default RPO Alert value for new policy creation via WebUI  # noqa: E501

        :return: The preferred_rpo_alert of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._preferred_rpo_alert

    @preferred_rpo_alert.setter
    def preferred_rpo_alert(self, preferred_rpo_alert):
        """Sets the preferred_rpo_alert of this SyncSettingsSettings.

        If specified, display as default RPO Alert value for new policy creation via WebUI  # noqa: E501

        :param preferred_rpo_alert: The preferred_rpo_alert of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if preferred_rpo_alert is not None and preferred_rpo_alert > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `preferred_rpo_alert`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if preferred_rpo_alert is not None and preferred_rpo_alert < 0:  # noqa: E501
            raise ValueError("Invalid value for `preferred_rpo_alert`, must be a value greater than or equal to `0`")  # noqa: E501

        self._preferred_rpo_alert = preferred_rpo_alert

    @property
    def renegotiation_period(self):
        """Gets the renegotiation_period of this SyncSettingsSettings.  # noqa: E501

        If specified, the duration to persist encrypted connection before forcing a renegotiation.  # noqa: E501

        :return: The renegotiation_period of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._renegotiation_period

    @renegotiation_period.setter
    def renegotiation_period(self, renegotiation_period):
        """Sets the renegotiation_period of this SyncSettingsSettings.

        If specified, the duration to persist encrypted connection before forcing a renegotiation.  # noqa: E501

        :param renegotiation_period: The renegotiation_period of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if renegotiation_period is not None and renegotiation_period > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `renegotiation_period`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if renegotiation_period is not None and renegotiation_period < 60:  # noqa: E501
            raise ValueError("Invalid value for `renegotiation_period`, must be a value greater than or equal to `60`")  # noqa: E501

        self._renegotiation_period = renegotiation_period

    @property
    def report_email(self):
        """Gets the report_email of this SyncSettingsSettings.  # noqa: E501

        Email sync reports to these addresses.  # noqa: E501

        :return: The report_email of this SyncSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._report_email

    @report_email.setter
    def report_email(self, report_email):
        """Sets the report_email of this SyncSettingsSettings.

        Email sync reports to these addresses.  # noqa: E501

        :param report_email: The report_email of this SyncSettingsSettings.  # noqa: E501
        :type: list[str]
        """

        self._report_email = report_email

    @property
    def report_max_age(self):
        """Gets the report_max_age of this SyncSettingsSettings.  # noqa: E501

        The default length of time (in seconds) a policy report will be stored.  # noqa: E501

        :return: The report_max_age of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._report_max_age

    @report_max_age.setter
    def report_max_age(self, report_max_age):
        """Sets the report_max_age of this SyncSettingsSettings.

        The default length of time (in seconds) a policy report will be stored.  # noqa: E501

        :param report_max_age: The report_max_age of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if report_max_age is not None and report_max_age > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `report_max_age`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if report_max_age is not None and report_max_age < 0:  # noqa: E501
            raise ValueError("Invalid value for `report_max_age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._report_max_age = report_max_age

    @property
    def report_max_count(self):
        """Gets the report_max_count of this SyncSettingsSettings.  # noqa: E501

        The default maximum number of reports to retain for a policy.  # noqa: E501

        :return: The report_max_count of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._report_max_count

    @report_max_count.setter
    def report_max_count(self, report_max_count):
        """Sets the report_max_count of this SyncSettingsSettings.

        The default maximum number of reports to retain for a policy.  # noqa: E501

        :param report_max_count: The report_max_count of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if report_max_count is not None and report_max_count > 2000:  # noqa: E501
            raise ValueError("Invalid value for `report_max_count`, must be a value less than or equal to `2000`")  # noqa: E501
        if report_max_count is not None and report_max_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `report_max_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._report_max_count = report_max_count

    @property
    def restrict_target_network(self):
        """Gets the restrict_target_network of this SyncSettingsSettings.  # noqa: E501

        Default for the \"restrict_target_network\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \"target_host\" field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster.  # noqa: E501

        :return: The restrict_target_network of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_target_network

    @restrict_target_network.setter
    def restrict_target_network(self, restrict_target_network):
        """Sets the restrict_target_network of this SyncSettingsSettings.

        Default for the \"restrict_target_network\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \"target_host\" field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster.  # noqa: E501

        :param restrict_target_network: The restrict_target_network of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._restrict_target_network = restrict_target_network

    @property
    def rpo_alerts(self):
        """Gets the rpo_alerts of this SyncSettingsSettings.  # noqa: E501

        If disabled, no RPO alerts will be generated.  # noqa: E501

        :return: The rpo_alerts of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._rpo_alerts

    @rpo_alerts.setter
    def rpo_alerts(self, rpo_alerts):
        """Sets the rpo_alerts of this SyncSettingsSettings.

        If disabled, no RPO alerts will be generated.  # noqa: E501

        :param rpo_alerts: The rpo_alerts of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._rpo_alerts = rpo_alerts

    @property
    def service(self):
        """Gets the service of this SyncSettingsSettings.  # noqa: E501

        Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled.  # noqa: E501

        :return: The service of this SyncSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this SyncSettingsSettings.

        Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled.  # noqa: E501

        :param service: The service of this SyncSettingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["on", "off", "paused"]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def service_history_max_age(self):
        """Gets the service_history_max_age of this SyncSettingsSettings.  # noqa: E501

        Maximum age of service information to maintain, in seconds.  # noqa: E501

        :return: The service_history_max_age of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._service_history_max_age

    @service_history_max_age.setter
    def service_history_max_age(self, service_history_max_age):
        """Sets the service_history_max_age of this SyncSettingsSettings.

        Maximum age of service information to maintain, in seconds.  # noqa: E501

        :param service_history_max_age: The service_history_max_age of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if service_history_max_age is not None and service_history_max_age > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `service_history_max_age`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if service_history_max_age is not None and service_history_max_age < 0:  # noqa: E501
            raise ValueError("Invalid value for `service_history_max_age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._service_history_max_age = service_history_max_age

    @property
    def service_history_max_count(self):
        """Gets the service_history_max_count of this SyncSettingsSettings.  # noqa: E501

        Maximum number of historical service information records to maintain.  # noqa: E501

        :return: The service_history_max_count of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._service_history_max_count

    @service_history_max_count.setter
    def service_history_max_count(self, service_history_max_count):
        """Sets the service_history_max_count of this SyncSettingsSettings.

        Maximum number of historical service information records to maintain.  # noqa: E501

        :param service_history_max_count: The service_history_max_count of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if service_history_max_count is not None and service_history_max_count > 2000:  # noqa: E501
            raise ValueError("Invalid value for `service_history_max_count`, must be a value less than or equal to `2000`")  # noqa: E501
        if service_history_max_count is not None and service_history_max_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `service_history_max_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._service_history_max_count = service_history_max_count

    @property
    def source_network(self):
        """Gets the source_network of this SyncSettingsSettings.  # noqa: E501

        Restricts replication policies on the local cluster to running on the specified subnet and pool.  # noqa: E501

        :return: The source_network of this SyncSettingsSettings.  # noqa: E501
        :rtype: SyncPolicySourceNetwork
        """
        return self._source_network

    @source_network.setter
    def source_network(self, source_network):
        """Sets the source_network of this SyncSettingsSettings.

        Restricts replication policies on the local cluster to running on the specified subnet and pool.  # noqa: E501

        :param source_network: The source_network of this SyncSettingsSettings.  # noqa: E501
        :type: SyncPolicySourceNetwork
        """

        self._source_network = source_network

    @property
    def tw_chkpt_interval(self):
        """Gets the tw_chkpt_interval of this SyncSettingsSettings.  # noqa: E501

        The interval (in seconds) in which treewalk syncs are forced to checkpoint.  # noqa: E501

        :return: The tw_chkpt_interval of this SyncSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._tw_chkpt_interval

    @tw_chkpt_interval.setter
    def tw_chkpt_interval(self, tw_chkpt_interval):
        """Sets the tw_chkpt_interval of this SyncSettingsSettings.

        The interval (in seconds) in which treewalk syncs are forced to checkpoint.  # noqa: E501

        :param tw_chkpt_interval: The tw_chkpt_interval of this SyncSettingsSettings.  # noqa: E501
        :type: int
        """
        if tw_chkpt_interval is not None and tw_chkpt_interval > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `tw_chkpt_interval`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if tw_chkpt_interval is not None and tw_chkpt_interval < 0:  # noqa: E501
            raise ValueError("Invalid value for `tw_chkpt_interval`, must be a value greater than or equal to `0`")  # noqa: E501

        self._tw_chkpt_interval = tw_chkpt_interval

    @property
    def use_workers_per_node(self):
        """Gets the use_workers_per_node of this SyncSettingsSettings.  # noqa: E501

        If enabled, SyncIQ will use the deprecated workers_per_node field with worker pools functionality and limit workers accordingly.  # noqa: E501

        :return: The use_workers_per_node of this SyncSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_workers_per_node

    @use_workers_per_node.setter
    def use_workers_per_node(self, use_workers_per_node):
        """Sets the use_workers_per_node of this SyncSettingsSettings.

        If enabled, SyncIQ will use the deprecated workers_per_node field with worker pools functionality and limit workers accordingly.  # noqa: E501

        :param use_workers_per_node: The use_workers_per_node of this SyncSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._use_workers_per_node = use_workers_per_node

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
        if not isinstance(other, SyncSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
