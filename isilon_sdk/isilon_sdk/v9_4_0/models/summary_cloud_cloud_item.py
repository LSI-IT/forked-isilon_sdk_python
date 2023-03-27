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


class SummaryCloudCloudItem(object):
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
        'account': 'str',
        'account_key': 'str',
        'cloud': 'str',
        'deletes': 'int',
        'guid': 'str',
        '_in': 'int',
        'node': 'int',
        'out': 'int',
        'policy': 'str',
        'policy_id': 'int',
        'reads': 'int',
        'time': 'int',
        'writes': 'int'
    }

    attribute_map = {
        'account': 'account',
        'account_key': 'account_key',
        'cloud': 'cloud',
        'deletes': 'deletes',
        'guid': 'guid',
        '_in': 'in',
        'node': 'node',
        'out': 'out',
        'policy': 'policy',
        'policy_id': 'policy_id',
        'reads': 'reads',
        'time': 'time',
        'writes': 'writes'
    }

    def __init__(self, account=None, account_key=None, cloud=None, deletes=None, guid=None, _in=None, node=None, out=None, policy=None, policy_id=None, reads=None, time=None, writes=None):  # noqa: E501
        """SummaryCloudCloudItem - a model defined in Swagger"""  # noqa: E501

        self._account = None
        self._account_key = None
        self._cloud = None
        self._deletes = None
        self._guid = None
        self.__in = None
        self._node = None
        self._out = None
        self._policy = None
        self._policy_id = None
        self._reads = None
        self._time = None
        self._writes = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if account_key is not None:
            self.account_key = account_key
        if cloud is not None:
            self.cloud = cloud
        if deletes is not None:
            self.deletes = deletes
        if guid is not None:
            self.guid = guid
        if _in is not None:
            self._in = _in
        if node is not None:
            self.node = node
        if out is not None:
            self.out = out
        if policy is not None:
            self.policy = policy
        if policy_id is not None:
            self.policy_id = policy_id
        if reads is not None:
            self.reads = reads
        if time is not None:
            self.time = time
        if writes is not None:
            self.writes = writes

    @property
    def account(self):
        """Gets the account of this SummaryCloudCloudItem.  # noqa: E501

        Account name  # noqa: E501

        :return: The account of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this SummaryCloudCloudItem.

        Account name  # noqa: E501

        :param account: The account of this SummaryCloudCloudItem.  # noqa: E501
        :type: str
        """
        if account is not None and len(account) > 768:
            raise ValueError("Invalid value for `account`, length must be less than or equal to `768`")  # noqa: E501
        if account is not None and len(account) < 1:
            raise ValueError("Invalid value for `account`, length must be greater than or equal to `1`")  # noqa: E501

        self._account = account

    @property
    def account_key(self):
        """Gets the account_key of this SummaryCloudCloudItem.  # noqa: E501

        Key for account  # noqa: E501

        :return: The account_key of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: str
        """
        return self._account_key

    @account_key.setter
    def account_key(self, account_key):
        """Sets the account_key of this SummaryCloudCloudItem.

        Key for account  # noqa: E501

        :param account_key: The account_key of this SummaryCloudCloudItem.  # noqa: E501
        :type: str
        """
        if account_key is not None and len(account_key) > 256:
            raise ValueError("Invalid value for `account_key`, length must be less than or equal to `256`")  # noqa: E501
        if account_key is not None and len(account_key) < 1:
            raise ValueError("Invalid value for `account_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_key = account_key

    @property
    def cloud(self):
        """Gets the cloud of this SummaryCloudCloudItem.  # noqa: E501

        Name of cloud provider  # noqa: E501

        :return: The cloud of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this SummaryCloudCloudItem.

        Name of cloud provider  # noqa: E501

        :param cloud: The cloud of this SummaryCloudCloudItem.  # noqa: E501
        :type: str
        """
        if cloud is not None and len(cloud) > 255:
            raise ValueError("Invalid value for `cloud`, length must be less than or equal to `255`")  # noqa: E501
        if cloud is not None and len(cloud) < 1:
            raise ValueError("Invalid value for `cloud`, length must be greater than or equal to `1`")  # noqa: E501

        self._cloud = cloud

    @property
    def deletes(self):
        """Gets the deletes of this SummaryCloudCloudItem.  # noqa: E501

        Number of delete operations  # noqa: E501

        :return: The deletes of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: int
        """
        return self._deletes

    @deletes.setter
    def deletes(self, deletes):
        """Sets the deletes of this SummaryCloudCloudItem.

        Number of delete operations  # noqa: E501

        :param deletes: The deletes of this SummaryCloudCloudItem.  # noqa: E501
        :type: int
        """
        if deletes is not None and deletes > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `deletes`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if deletes is not None and deletes < 0:  # noqa: E501
            raise ValueError("Invalid value for `deletes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._deletes = deletes

    @property
    def guid(self):
        """Gets the guid of this SummaryCloudCloudItem.  # noqa: E501

        Cluster GUID  # noqa: E501

        :return: The guid of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this SummaryCloudCloudItem.

        Cluster GUID  # noqa: E501

        :param guid: The guid of this SummaryCloudCloudItem.  # noqa: E501
        :type: str
        """
        if guid is not None and len(guid) > 255:
            raise ValueError("Invalid value for `guid`, length must be less than or equal to `255`")  # noqa: E501
        if guid is not None and len(guid) < 1:
            raise ValueError("Invalid value for `guid`, length must be greater than or equal to `1`")  # noqa: E501

        self._guid = guid

    @property
    def _in(self):
        """Gets the _in of this SummaryCloudCloudItem.  # noqa: E501

        Number of bytes in  # noqa: E501

        :return: The _in of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: int
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this SummaryCloudCloudItem.

        Number of bytes in  # noqa: E501

        :param _in: The _in of this SummaryCloudCloudItem.  # noqa: E501
        :type: int
        """
        if _in is not None and _in > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `_in`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if _in is not None and _in < 0:  # noqa: E501
            raise ValueError("Invalid value for `_in`, must be a value greater than or equal to `0`")  # noqa: E501

        self.__in = _in

    @property
    def node(self):
        """Gets the node of this SummaryCloudCloudItem.  # noqa: E501

        The node this data came from  # noqa: E501

        :return: The node of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: int
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this SummaryCloudCloudItem.

        The node this data came from  # noqa: E501

        :param node: The node of this SummaryCloudCloudItem.  # noqa: E501
        :type: int
        """
        if node is not None and node > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `node`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if node is not None and node < 0:  # noqa: E501
            raise ValueError("Invalid value for `node`, must be a value greater than or equal to `0`")  # noqa: E501

        self._node = node

    @property
    def out(self):
        """Gets the out of this SummaryCloudCloudItem.  # noqa: E501

        Number of bytes out  # noqa: E501

        :return: The out of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: int
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this SummaryCloudCloudItem.

        Number of bytes out  # noqa: E501

        :param out: The out of this SummaryCloudCloudItem.  # noqa: E501
        :type: int
        """
        if out is not None and out > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `out`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if out is not None and out < 0:  # noqa: E501
            raise ValueError("Invalid value for `out`, must be a value greater than or equal to `0`")  # noqa: E501

        self._out = out

    @property
    def policy(self):
        """Gets the policy of this SummaryCloudCloudItem.  # noqa: E501

        Policy name  # noqa: E501

        :return: The policy of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this SummaryCloudCloudItem.

        Policy name  # noqa: E501

        :param policy: The policy of this SummaryCloudCloudItem.  # noqa: E501
        :type: str
        """
        if policy is not None and len(policy) > 255:
            raise ValueError("Invalid value for `policy`, length must be less than or equal to `255`")  # noqa: E501
        if policy is not None and len(policy) < 1:
            raise ValueError("Invalid value for `policy`, length must be greater than or equal to `1`")  # noqa: E501

        self._policy = policy

    @property
    def policy_id(self):
        """Gets the policy_id of this SummaryCloudCloudItem.  # noqa: E501

        Id of the policy  # noqa: E501

        :return: The policy_id of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this SummaryCloudCloudItem.

        Id of the policy  # noqa: E501

        :param policy_id: The policy_id of this SummaryCloudCloudItem.  # noqa: E501
        :type: int
        """
        if policy_id is not None and policy_id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `policy_id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if policy_id is not None and policy_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `policy_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._policy_id = policy_id

    @property
    def reads(self):
        """Gets the reads of this SummaryCloudCloudItem.  # noqa: E501

        Number of read operations  # noqa: E501

        :return: The reads of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: int
        """
        return self._reads

    @reads.setter
    def reads(self, reads):
        """Sets the reads of this SummaryCloudCloudItem.

        Number of read operations  # noqa: E501

        :param reads: The reads of this SummaryCloudCloudItem.  # noqa: E501
        :type: int
        """
        if reads is not None and reads > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `reads`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if reads is not None and reads < 0:  # noqa: E501
            raise ValueError("Invalid value for `reads`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reads = reads

    @property
    def time(self):
        """Gets the time of this SummaryCloudCloudItem.  # noqa: E501

        Timestamp  # noqa: E501

        :return: The time of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SummaryCloudCloudItem.

        Timestamp  # noqa: E501

        :param time: The time of this SummaryCloudCloudItem.  # noqa: E501
        :type: int
        """
        if time is not None and time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if time is not None and time < 0:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._time = time

    @property
    def writes(self):
        """Gets the writes of this SummaryCloudCloudItem.  # noqa: E501

        Number of write operations  # noqa: E501

        :return: The writes of this SummaryCloudCloudItem.  # noqa: E501
        :rtype: int
        """
        return self._writes

    @writes.setter
    def writes(self, writes):
        """Sets the writes of this SummaryCloudCloudItem.

        Number of write operations  # noqa: E501

        :param writes: The writes of this SummaryCloudCloudItem.  # noqa: E501
        :type: int
        """
        if writes is not None and writes > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `writes`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if writes is not None and writes < 0:  # noqa: E501
            raise ValueError("Invalid value for `writes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._writes = writes

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
        if not isinstance(other, SummaryCloudCloudItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
