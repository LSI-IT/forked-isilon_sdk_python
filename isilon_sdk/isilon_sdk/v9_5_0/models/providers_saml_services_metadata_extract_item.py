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


class ProvidersSamlServicesMetadataExtractItem(object):
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
        'entity_id': 'str',
        'metadata': 'str',
        'metadata_location': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'metadata': 'metadata',
        'metadata_location': 'metadata_location'
    }

    def __init__(self, entity_id=None, metadata=None, metadata_location=None):  # noqa: E501
        """ProvidersSamlServicesMetadataExtractItem - a model defined in Swagger"""  # noqa: E501

        self._entity_id = None
        self._metadata = None
        self._metadata_location = None
        self.discriminator = None

        if entity_id is not None:
            self.entity_id = entity_id
        if metadata is not None:
            self.metadata = metadata
        if metadata_location is not None:
            self.metadata_location = metadata_location

    @property
    def entity_id(self):
        """Gets the entity_id of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501

        When provided the SAML entity ID matching this string will be the IDP data returned. When not provided the SAML metadata must contain a single entity descriptor with a IDP descriptor.  # noqa: E501

        :return: The entity_id of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ProvidersSamlServicesMetadataExtractItem.

        When provided the SAML entity ID matching this string will be the IDP data returned. When not provided the SAML metadata must contain a single entity descriptor with a IDP descriptor.  # noqa: E501

        :param entity_id: The entity_id of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501
        :type: str
        """
        if entity_id is not None and len(entity_id) > 1024:
            raise ValueError("Invalid value for `entity_id`, length must be less than or equal to `1024`")  # noqa: E501
        if entity_id is not None and len(entity_id) < 1:
            raise ValueError("Invalid value for `entity_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def metadata(self):
        """Gets the metadata of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501

        Metadata XML data of the SAML IDP.  # noqa: E501

        :return: The metadata of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ProvidersSamlServicesMetadataExtractItem.

        Metadata XML data of the SAML IDP.  # noqa: E501

        :param metadata: The metadata of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501
        :type: str
        """
        if metadata is not None and len(metadata) > 8000000:
            raise ValueError("Invalid value for `metadata`, length must be less than or equal to `8000000`")  # noqa: E501
        if metadata is not None and len(metadata) < 0:
            raise ValueError("Invalid value for `metadata`, length must be greater than or equal to `0`")  # noqa: E501

        self._metadata = metadata

    @property
    def metadata_location(self):
        """Gets the metadata_location of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501

        Path to the SAML IDP metadata.  # noqa: E501

        :return: The metadata_location of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501
        :rtype: str
        """
        return self._metadata_location

    @metadata_location.setter
    def metadata_location(self, metadata_location):
        """Sets the metadata_location of this ProvidersSamlServicesMetadataExtractItem.

        Path to the SAML IDP metadata.  # noqa: E501

        :param metadata_location: The metadata_location of this ProvidersSamlServicesMetadataExtractItem.  # noqa: E501
        :type: str
        """
        if metadata_location is not None and len(metadata_location) > 4096:
            raise ValueError("Invalid value for `metadata_location`, length must be less than or equal to `4096`")  # noqa: E501
        if metadata_location is not None and len(metadata_location) < 2:
            raise ValueError("Invalid value for `metadata_location`, length must be greater than or equal to `2`")  # noqa: E501

        self._metadata_location = metadata_location

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
        if not isinstance(other, ProvidersSamlServicesMetadataExtractItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other