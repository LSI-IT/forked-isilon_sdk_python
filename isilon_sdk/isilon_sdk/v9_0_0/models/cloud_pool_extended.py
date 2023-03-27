# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_0_0.models.cloud_pool import CloudPool  # noqa: F401,E501


class CloudPoolExtended(object):
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
        'accounts': 'list[str]',
        'birth_cluster_id': 'str',
        'description': 'str',
        'name': 'str',
        'vendor': 'str',
        'id': 'str',
        'state': 'str',
        'state_details': 'str',
        'type': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'birth_cluster_id': 'birth_cluster_id',
        'description': 'description',
        'name': 'name',
        'vendor': 'vendor',
        'id': 'id',
        'state': 'state',
        'state_details': 'state_details',
        'type': 'type'
    }

    def __init__(self, accounts=None, birth_cluster_id=None, description=None, name=None, vendor=None, id=None, state=None, state_details=None, type=None):  # noqa: E501
        """CloudPoolExtended - a model defined in Swagger"""  # noqa: E501

        self._accounts = None
        self._birth_cluster_id = None
        self._description = None
        self._name = None
        self._vendor = None
        self._id = None
        self._state = None
        self._state_details = None
        self._type = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if birth_cluster_id is not None:
            self.birth_cluster_id = birth_cluster_id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if vendor is not None:
            self.vendor = vendor
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if state_details is not None:
            self.state_details = state_details
        if type is not None:
            self.type = type

    @property
    def accounts(self):
        """Gets the accounts of this CloudPoolExtended.  # noqa: E501

        A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool.  # noqa: E501

        :return: The accounts of this CloudPoolExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this CloudPoolExtended.

        A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool.  # noqa: E501

        :param accounts: The accounts of this CloudPoolExtended.  # noqa: E501
        :type: list[str]
        """

        self._accounts = accounts

    @property
    def birth_cluster_id(self):
        """Gets the birth_cluster_id of this CloudPoolExtended.  # noqa: E501

        The guid of the cluster where this pool was created  # noqa: E501

        :return: The birth_cluster_id of this CloudPoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """Sets the birth_cluster_id of this CloudPoolExtended.

        The guid of the cluster where this pool was created  # noqa: E501

        :param birth_cluster_id: The birth_cluster_id of this CloudPoolExtended.  # noqa: E501
        :type: str
        """
        if birth_cluster_id is not None and len(birth_cluster_id) > 255:
            raise ValueError("Invalid value for `birth_cluster_id`, length must be less than or equal to `255`")  # noqa: E501
        if birth_cluster_id is not None and len(birth_cluster_id) < 0:
            raise ValueError("Invalid value for `birth_cluster_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._birth_cluster_id = birth_cluster_id

    @property
    def description(self):
        """Gets the description of this CloudPoolExtended.  # noqa: E501

        A brief description of this pool  # noqa: E501

        :return: The description of this CloudPoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudPoolExtended.

        A brief description of this pool  # noqa: E501

        :param description: The description of this CloudPoolExtended.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 4096:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `4096`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this CloudPoolExtended.  # noqa: E501

        A unique name for this pool  # noqa: E501

        :return: The name of this CloudPoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudPoolExtended.

        A unique name for this pool  # noqa: E501

        :param name: The name of this CloudPoolExtended.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 768:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `768`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def vendor(self):
        """Gets the vendor of this CloudPoolExtended.  # noqa: E501

        A string identifier of the cloud services vendor  # noqa: E501

        :return: The vendor of this CloudPoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this CloudPoolExtended.

        A string identifier of the cloud services vendor  # noqa: E501

        :param vendor: The vendor of this CloudPoolExtended.  # noqa: E501
        :type: str
        """
        if vendor is not None and len(vendor) > 2048:
            raise ValueError("Invalid value for `vendor`, length must be less than or equal to `2048`")  # noqa: E501
        if vendor is not None and len(vendor) < 0:
            raise ValueError("Invalid value for `vendor`, length must be greater than or equal to `0`")  # noqa: E501

        self._vendor = vendor

    @property
    def id(self):
        """Gets the id of this CloudPoolExtended.  # noqa: E501

        A unique name for this pool  # noqa: E501

        :return: The id of this CloudPoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudPoolExtended.

        A unique name for this pool  # noqa: E501

        :param id: The id of this CloudPoolExtended.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 768:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `768`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def state(self):
        """Gets the state of this CloudPoolExtended.  # noqa: E501

        Indicates whether this pool is in a good state (\"OK\") or disabled (\"disabled\")  # noqa: E501

        :return: The state of this CloudPoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CloudPoolExtended.

        Indicates whether this pool is in a good state (\"OK\") or disabled (\"disabled\")  # noqa: E501

        :param state: The state of this CloudPoolExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "disabled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_details(self):
        """Gets the state_details of this CloudPoolExtended.  # noqa: E501

        Gives further information to describe the state of this pool  # noqa: E501

        :return: The state_details of this CloudPoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._state_details

    @state_details.setter
    def state_details(self, state_details):
        """Sets the state_details of this CloudPoolExtended.

        Gives further information to describe the state of this pool  # noqa: E501

        :param state_details: The state_details of this CloudPoolExtended.  # noqa: E501
        :type: str
        """
        if state_details is not None and len(state_details) > 4096:
            raise ValueError("Invalid value for `state_details`, length must be less than or equal to `4096`")  # noqa: E501
        if state_details is not None and len(state_details) < 0:
            raise ValueError("Invalid value for `state_details`, length must be greater than or equal to `0`")  # noqa: E501

        self._state_details = state_details

    @property
    def type(self):
        """Gets the type of this CloudPoolExtended.  # noqa: E501

        The type of cloud protocol required.  E.g., \"isilon\" for Dell EMC PowerScale, \"ecs\" for Dell EMC ECS Appliance, \"virtustream\" for Virtustream Storage Cloud, \"azure\" for Microsoft Azure, \"s3\" for Amazon S3, \"c2s-s3\" for Amazon Commercial Cloud Services S3 and \"google\" for Google Cloud Platform and \"alibaba-cloud\" for Alibaba Cloud  # noqa: E501

        :return: The type of this CloudPoolExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudPoolExtended.

        The type of cloud protocol required.  E.g., \"isilon\" for Dell EMC PowerScale, \"ecs\" for Dell EMC ECS Appliance, \"virtustream\" for Virtustream Storage Cloud, \"azure\" for Microsoft Azure, \"s3\" for Amazon S3, \"c2s-s3\" for Amazon Commercial Cloud Services S3 and \"google\" for Google Cloud Platform and \"alibaba-cloud\" for Alibaba Cloud  # noqa: E501

        :param type: The type of this CloudPoolExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["isilon", "ecs", "virtustream", "azure", "s3", "c2s-s3", "google", "alibaba-cloud"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, CloudPoolExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
