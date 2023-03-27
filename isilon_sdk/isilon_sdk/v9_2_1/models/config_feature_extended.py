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

from isilon_sdk.v9_2_1.models.config_feature import ConfigFeature  # noqa: F401,E501


class ConfigFeatureExtended(object):
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
        'enabled': 'bool',
        'feature_description': 'str',
        'id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'feature_description': 'feature_description',
        'id': 'id'
    }

    def __init__(self, enabled=None, feature_description=None, id=None):  # noqa: E501
        """ConfigFeatureExtended - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._feature_description = None
        self._id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if feature_description is not None:
            self.feature_description = feature_description
        if id is not None:
            self.id = id

    @property
    def enabled(self):
        """Gets the enabled of this ConfigFeatureExtended.  # noqa: E501

        A True value indicates the BMC LAN feature is currently enabled on the cluster.  # noqa: E501

        :return: The enabled of this ConfigFeatureExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConfigFeatureExtended.

        A True value indicates the BMC LAN feature is currently enabled on the cluster.  # noqa: E501

        :param enabled: The enabled of this ConfigFeatureExtended.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def feature_description(self):
        """Gets the feature_description of this ConfigFeatureExtended.  # noqa: E501

        A longer more formal description of the feature.  # noqa: E501

        :return: The feature_description of this ConfigFeatureExtended.  # noqa: E501
        :rtype: str
        """
        return self._feature_description

    @feature_description.setter
    def feature_description(self, feature_description):
        """Sets the feature_description of this ConfigFeatureExtended.

        A longer more formal description of the feature.  # noqa: E501

        :param feature_description: The feature_description of this ConfigFeatureExtended.  # noqa: E501
        :type: str
        """
        if feature_description is not None and len(feature_description) > 32:
            raise ValueError("Invalid value for `feature_description`, length must be less than or equal to `32`")  # noqa: E501
        if feature_description is not None and len(feature_description) < 0:
            raise ValueError("Invalid value for `feature_description`, length must be greater than or equal to `0`")  # noqa: E501

        self._feature_description = feature_description

    @property
    def id(self):
        """Gets the id of this ConfigFeatureExtended.  # noqa: E501

        A string used to identify the feature, such as sol for Serial-Over-LAN or power-control for Power Control.  # noqa: E501

        :return: The id of this ConfigFeatureExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigFeatureExtended.

        A string used to identify the feature, such as sol for Serial-Over-LAN or power-control for Power Control.  # noqa: E501

        :param id: The id of this ConfigFeatureExtended.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 16:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `16`")  # noqa: E501
        if id is not None and len(id) < 3:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `3`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, ConfigFeatureExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
