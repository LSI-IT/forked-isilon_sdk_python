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


class AvscanServer(object):
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
        'id': 'str',
        'new_name': 'str',
        'server_uri': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'id': 'id',
        'new_name': 'new_name',
        'server_uri': 'server_uri'
    }

    def __init__(self, enabled=None, id=None, new_name=None, server_uri=None):  # noqa: E501
        """AvscanServer - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._id = None
        self._new_name = None
        self._server_uri = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if new_name is not None:
            self.new_name = new_name
        if server_uri is not None:
            self.server_uri = server_uri

    @property
    def enabled(self):
        """Gets the enabled of this AvscanServer.  # noqa: E501

        Whether the server is enabled.  # noqa: E501

        :return: The enabled of this AvscanServer.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AvscanServer.

        Whether the server is enabled.  # noqa: E501

        :param enabled: The enabled of this AvscanServer.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this AvscanServer.  # noqa: E501

        A unique identifier for the server.  # noqa: E501

        :return: The id of this AvscanServer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvscanServer.

        A unique identifier for the server.  # noqa: E501

        :param id: The id of this AvscanServer.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 128:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `128`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def new_name(self):
        """Gets the new_name of this AvscanServer.  # noqa: E501

        New unique short name for the server.  # noqa: E501

        :return: The new_name of this AvscanServer.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this AvscanServer.

        New unique short name for the server.  # noqa: E501

        :param new_name: The new_name of this AvscanServer.  # noqa: E501
        :type: str
        """
        if new_name is not None and len(new_name) > 128:
            raise ValueError("Invalid value for `new_name`, length must be less than or equal to `128`")  # noqa: E501
        if new_name is not None and len(new_name) < 1:
            raise ValueError("Invalid value for `new_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._new_name = new_name

    @property
    def server_uri(self):
        """Gets the server_uri of this AvscanServer.  # noqa: E501

        URI of the server. Typical format is: domain:port/path  # noqa: E501

        :return: The server_uri of this AvscanServer.  # noqa: E501
        :rtype: str
        """
        return self._server_uri

    @server_uri.setter
    def server_uri(self, server_uri):
        """Sets the server_uri of this AvscanServer.

        URI of the server. Typical format is: domain:port/path  # noqa: E501

        :param server_uri: The server_uri of this AvscanServer.  # noqa: E501
        :type: str
        """
        if server_uri is not None and len(server_uri) > 256:
            raise ValueError("Invalid value for `server_uri`, length must be less than or equal to `256`")  # noqa: E501
        if server_uri is not None and len(server_uri) < 1:
            raise ValueError("Invalid value for `server_uri`, length must be greater than or equal to `1`")  # noqa: E501

        self._server_uri = server_uri

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
        if not isinstance(other, AvscanServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
