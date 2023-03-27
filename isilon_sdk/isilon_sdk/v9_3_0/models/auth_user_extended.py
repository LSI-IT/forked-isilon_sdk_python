# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_3_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isilon_sdk.v9_3_0.models.auth_group_object_history_item import AuthGroupObjectHistoryItem  # noqa: F401,E501


class AuthUserExtended(object):
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
        'dn': 'str',
        'dns_domain': 'str',
        'domain': 'str',
        'email': 'str',
        'enabled': 'bool',
        'expired': 'bool',
        'expiry': 'int',
        'gecos': 'str',
        'generated_gid': 'bool',
        'generated_uid': 'bool',
        'generated_upn': 'bool',
        'gid': 'AuthAccessAccessItemFileGroup',
        'home_directory': 'str',
        'id': 'str',
        'locked': 'bool',
        'max_password_age': 'int',
        'member_of': 'list[AuthAccessAccessItemFileGroup]',
        'name': 'str',
        'object_history': 'list[AuthGroupObjectHistoryItem]',
        'on_disk_group_identity': 'AuthAccessAccessItemFileGroup',
        'on_disk_user_identity': 'AuthAccessAccessItemFileGroup',
        'password_expired': 'bool',
        'password_expires': 'bool',
        'password_expiry': 'int',
        'password_last_set': 'int',
        'primary_group_sid': 'AuthAccessAccessItemFileGroup',
        'prompt_password_change': 'bool',
        'provider': 'str',
        'sam_account_name': 'str',
        'shell': 'str',
        'sid': 'AuthAccessAccessItemFileGroup',
        'ssh_public_keys': 'list[str]',
        'type': 'str',
        'uid': 'AuthAccessAccessItemFileGroup',
        'upn': 'str',
        'user_can_change_password': 'bool'
    }

    attribute_map = {
        'dn': 'dn',
        'dns_domain': 'dns_domain',
        'domain': 'domain',
        'email': 'email',
        'enabled': 'enabled',
        'expired': 'expired',
        'expiry': 'expiry',
        'gecos': 'gecos',
        'generated_gid': 'generated_gid',
        'generated_uid': 'generated_uid',
        'generated_upn': 'generated_upn',
        'gid': 'gid',
        'home_directory': 'home_directory',
        'id': 'id',
        'locked': 'locked',
        'max_password_age': 'max_password_age',
        'member_of': 'member_of',
        'name': 'name',
        'object_history': 'object_history',
        'on_disk_group_identity': 'on_disk_group_identity',
        'on_disk_user_identity': 'on_disk_user_identity',
        'password_expired': 'password_expired',
        'password_expires': 'password_expires',
        'password_expiry': 'password_expiry',
        'password_last_set': 'password_last_set',
        'primary_group_sid': 'primary_group_sid',
        'prompt_password_change': 'prompt_password_change',
        'provider': 'provider',
        'sam_account_name': 'sam_account_name',
        'shell': 'shell',
        'sid': 'sid',
        'ssh_public_keys': 'ssh_public_keys',
        'type': 'type',
        'uid': 'uid',
        'upn': 'upn',
        'user_can_change_password': 'user_can_change_password'
    }

    def __init__(self, dn=None, dns_domain=None, domain=None, email=None, enabled=None, expired=None, expiry=None, gecos=None, generated_gid=None, generated_uid=None, generated_upn=None, gid=None, home_directory=None, id=None, locked=None, max_password_age=None, member_of=None, name=None, object_history=None, on_disk_group_identity=None, on_disk_user_identity=None, password_expired=None, password_expires=None, password_expiry=None, password_last_set=None, primary_group_sid=None, prompt_password_change=None, provider=None, sam_account_name=None, shell=None, sid=None, ssh_public_keys=None, type=None, uid=None, upn=None, user_can_change_password=None):  # noqa: E501
        """AuthUserExtended - a model defined in Swagger"""  # noqa: E501

        self._dn = None
        self._dns_domain = None
        self._domain = None
        self._email = None
        self._enabled = None
        self._expired = None
        self._expiry = None
        self._gecos = None
        self._generated_gid = None
        self._generated_uid = None
        self._generated_upn = None
        self._gid = None
        self._home_directory = None
        self._id = None
        self._locked = None
        self._max_password_age = None
        self._member_of = None
        self._name = None
        self._object_history = None
        self._on_disk_group_identity = None
        self._on_disk_user_identity = None
        self._password_expired = None
        self._password_expires = None
        self._password_expiry = None
        self._password_last_set = None
        self._primary_group_sid = None
        self._prompt_password_change = None
        self._provider = None
        self._sam_account_name = None
        self._shell = None
        self._sid = None
        self._ssh_public_keys = None
        self._type = None
        self._uid = None
        self._upn = None
        self._user_can_change_password = None
        self.discriminator = None

        if dn is not None:
            self.dn = dn
        if dns_domain is not None:
            self.dns_domain = dns_domain
        if domain is not None:
            self.domain = domain
        if email is not None:
            self.email = email
        self.enabled = enabled
        self.expired = expired
        if expiry is not None:
            self.expiry = expiry
        if gecos is not None:
            self.gecos = gecos
        if generated_gid is not None:
            self.generated_gid = generated_gid
        if generated_uid is not None:
            self.generated_uid = generated_uid
        if generated_upn is not None:
            self.generated_upn = generated_upn
        if gid is not None:
            self.gid = gid
        if home_directory is not None:
            self.home_directory = home_directory
        self.id = id
        self.locked = locked
        if max_password_age is not None:
            self.max_password_age = max_password_age
        if member_of is not None:
            self.member_of = member_of
        self.name = name
        if object_history is not None:
            self.object_history = object_history
        if on_disk_group_identity is not None:
            self.on_disk_group_identity = on_disk_group_identity
        if on_disk_user_identity is not None:
            self.on_disk_user_identity = on_disk_user_identity
        self.password_expired = password_expired
        self.password_expires = password_expires
        if password_expiry is not None:
            self.password_expiry = password_expiry
        if password_last_set is not None:
            self.password_last_set = password_last_set
        if primary_group_sid is not None:
            self.primary_group_sid = primary_group_sid
        self.prompt_password_change = prompt_password_change
        if provider is not None:
            self.provider = provider
        if sam_account_name is not None:
            self.sam_account_name = sam_account_name
        if shell is not None:
            self.shell = shell
        if sid is not None:
            self.sid = sid
        if ssh_public_keys is not None:
            self.ssh_public_keys = ssh_public_keys
        self.type = type
        if uid is not None:
            self.uid = uid
        if upn is not None:
            self.upn = upn
        self.user_can_change_password = user_can_change_password

    @property
    def dn(self):
        """Gets the dn of this AuthUserExtended.  # noqa: E501


        :return: The dn of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """Sets the dn of this AuthUserExtended.


        :param dn: The dn of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if dn is not None and len(dn) > 255:
            raise ValueError("Invalid value for `dn`, length must be less than or equal to `255`")  # noqa: E501
        if dn is not None and len(dn) < 0:
            raise ValueError("Invalid value for `dn`, length must be greater than or equal to `0`")  # noqa: E501

        self._dn = dn

    @property
    def dns_domain(self):
        """Gets the dns_domain of this AuthUserExtended.  # noqa: E501


        :return: The dns_domain of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._dns_domain

    @dns_domain.setter
    def dns_domain(self, dns_domain):
        """Sets the dns_domain of this AuthUserExtended.


        :param dns_domain: The dns_domain of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if dns_domain is not None and len(dns_domain) > 255:
            raise ValueError("Invalid value for `dns_domain`, length must be less than or equal to `255`")  # noqa: E501
        if dns_domain is not None and len(dns_domain) < 0:
            raise ValueError("Invalid value for `dns_domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._dns_domain = dns_domain

    @property
    def domain(self):
        """Gets the domain of this AuthUserExtended.  # noqa: E501


        :return: The domain of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AuthUserExtended.


        :param domain: The domain of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if domain is not None and len(domain) > 255:
            raise ValueError("Invalid value for `domain`, length must be less than or equal to `255`")  # noqa: E501
        if domain is not None and len(domain) < 0:
            raise ValueError("Invalid value for `domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._domain = domain

    @property
    def email(self):
        """Gets the email of this AuthUserExtended.  # noqa: E501


        :return: The email of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AuthUserExtended.


        :param email: The email of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 255:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501
        if email is not None and len(email) < 0:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `0`")  # noqa: E501

        self._email = email

    @property
    def enabled(self):
        """Gets the enabled of this AuthUserExtended.  # noqa: E501

        True, if the authenticated user is enabled.  # noqa: E501

        :return: The enabled of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AuthUserExtended.

        True, if the authenticated user is enabled.  # noqa: E501

        :param enabled: The enabled of this AuthUserExtended.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def expired(self):
        """Gets the expired of this AuthUserExtended.  # noqa: E501

        True, if the authenticated user has expired.  # noqa: E501

        :return: The expired of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this AuthUserExtended.

        True, if the authenticated user has expired.  # noqa: E501

        :param expired: The expired of this AuthUserExtended.  # noqa: E501
        :type: bool
        """
        if expired is None:
            raise ValueError("Invalid value for `expired`, must not be `None`")  # noqa: E501

        self._expired = expired

    @property
    def expiry(self):
        """Gets the expiry of this AuthUserExtended.  # noqa: E501


        :return: The expiry of this AuthUserExtended.  # noqa: E501
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this AuthUserExtended.


        :param expiry: The expiry of this AuthUserExtended.  # noqa: E501
        :type: int
        """
        if expiry is not None and expiry > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `expiry`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if expiry is not None and expiry < 0:  # noqa: E501
            raise ValueError("Invalid value for `expiry`, must be a value greater than or equal to `0`")  # noqa: E501

        self._expiry = expiry

    @property
    def gecos(self):
        """Gets the gecos of this AuthUserExtended.  # noqa: E501


        :return: The gecos of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._gecos

    @gecos.setter
    def gecos(self, gecos):
        """Sets the gecos of this AuthUserExtended.


        :param gecos: The gecos of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if gecos is not None and len(gecos) > 255:
            raise ValueError("Invalid value for `gecos`, length must be less than or equal to `255`")  # noqa: E501
        if gecos is not None and len(gecos) < 0:
            raise ValueError("Invalid value for `gecos`, length must be greater than or equal to `0`")  # noqa: E501

        self._gecos = gecos

    @property
    def generated_gid(self):
        """Gets the generated_gid of this AuthUserExtended.  # noqa: E501

        True, if the GID was generated.  # noqa: E501

        :return: The generated_gid of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._generated_gid

    @generated_gid.setter
    def generated_gid(self, generated_gid):
        """Sets the generated_gid of this AuthUserExtended.

        True, if the GID was generated.  # noqa: E501

        :param generated_gid: The generated_gid of this AuthUserExtended.  # noqa: E501
        :type: bool
        """

        self._generated_gid = generated_gid

    @property
    def generated_uid(self):
        """Gets the generated_uid of this AuthUserExtended.  # noqa: E501

        True, if the UID was generated.  # noqa: E501

        :return: The generated_uid of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._generated_uid

    @generated_uid.setter
    def generated_uid(self, generated_uid):
        """Sets the generated_uid of this AuthUserExtended.

        True, if the UID was generated.  # noqa: E501

        :param generated_uid: The generated_uid of this AuthUserExtended.  # noqa: E501
        :type: bool
        """

        self._generated_uid = generated_uid

    @property
    def generated_upn(self):
        """Gets the generated_upn of this AuthUserExtended.  # noqa: E501

        True, if the UPN was generated.  # noqa: E501

        :return: The generated_upn of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._generated_upn

    @generated_upn.setter
    def generated_upn(self, generated_upn):
        """Sets the generated_upn of this AuthUserExtended.

        True, if the UPN was generated.  # noqa: E501

        :param generated_upn: The generated_upn of this AuthUserExtended.  # noqa: E501
        :type: bool
        """

        self._generated_upn = generated_upn

    @property
    def gid(self):
        """Gets the gid of this AuthUserExtended.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The gid of this AuthUserExtended.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this AuthUserExtended.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param gid: The gid of this AuthUserExtended.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._gid = gid

    @property
    def home_directory(self):
        """Gets the home_directory of this AuthUserExtended.  # noqa: E501


        :return: The home_directory of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._home_directory

    @home_directory.setter
    def home_directory(self, home_directory):
        """Sets the home_directory of this AuthUserExtended.


        :param home_directory: The home_directory of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if home_directory is not None and len(home_directory) > 4096:
            raise ValueError("Invalid value for `home_directory`, length must be less than or equal to `4096`")  # noqa: E501
        if home_directory is not None and len(home_directory) < 0:
            raise ValueError("Invalid value for `home_directory`, length must be greater than or equal to `0`")  # noqa: E501

        self._home_directory = home_directory

    @property
    def id(self):
        """Gets the id of this AuthUserExtended.  # noqa: E501

        Specifies the user or group ID.  # noqa: E501

        :return: The id of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthUserExtended.

        Specifies the user or group ID.  # noqa: E501

        :param id: The id of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def locked(self):
        """Gets the locked of this AuthUserExtended.  # noqa: E501

        If true, indicates that the account is locked.  # noqa: E501

        :return: The locked of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this AuthUserExtended.

        If true, indicates that the account is locked.  # noqa: E501

        :param locked: The locked of this AuthUserExtended.  # noqa: E501
        :type: bool
        """
        if locked is None:
            raise ValueError("Invalid value for `locked`, must not be `None`")  # noqa: E501

        self._locked = locked

    @property
    def max_password_age(self):
        """Gets the max_password_age of this AuthUserExtended.  # noqa: E501

        Specifies the maximum time in seconds allowed before the password expires.  # noqa: E501

        :return: The max_password_age of this AuthUserExtended.  # noqa: E501
        :rtype: int
        """
        return self._max_password_age

    @max_password_age.setter
    def max_password_age(self, max_password_age):
        """Sets the max_password_age of this AuthUserExtended.

        Specifies the maximum time in seconds allowed before the password expires.  # noqa: E501

        :param max_password_age: The max_password_age of this AuthUserExtended.  # noqa: E501
        :type: int
        """

        self._max_password_age = max_password_age

    @property
    def member_of(self):
        """Gets the member_of of this AuthUserExtended.  # noqa: E501


        :return: The member_of of this AuthUserExtended.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._member_of

    @member_of.setter
    def member_of(self, member_of):
        """Sets the member_of of this AuthUserExtended.


        :param member_of: The member_of of this AuthUserExtended.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """

        self._member_of = member_of

    @property
    def name(self):
        """Gets the name of this AuthUserExtended.  # noqa: E501

        Specifies a user or group name.  # noqa: E501

        :return: The name of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthUserExtended.

        Specifies a user or group name.  # noqa: E501

        :param name: The name of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def object_history(self):
        """Gets the object_history of this AuthUserExtended.  # noqa: E501


        :return: The object_history of this AuthUserExtended.  # noqa: E501
        :rtype: list[AuthGroupObjectHistoryItem]
        """
        return self._object_history

    @object_history.setter
    def object_history(self, object_history):
        """Sets the object_history of this AuthUserExtended.


        :param object_history: The object_history of this AuthUserExtended.  # noqa: E501
        :type: list[AuthGroupObjectHistoryItem]
        """

        self._object_history = object_history

    @property
    def on_disk_group_identity(self):
        """Gets the on_disk_group_identity of this AuthUserExtended.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The on_disk_group_identity of this AuthUserExtended.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._on_disk_group_identity

    @on_disk_group_identity.setter
    def on_disk_group_identity(self, on_disk_group_identity):
        """Sets the on_disk_group_identity of this AuthUserExtended.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param on_disk_group_identity: The on_disk_group_identity of this AuthUserExtended.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._on_disk_group_identity = on_disk_group_identity

    @property
    def on_disk_user_identity(self):
        """Gets the on_disk_user_identity of this AuthUserExtended.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The on_disk_user_identity of this AuthUserExtended.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._on_disk_user_identity

    @on_disk_user_identity.setter
    def on_disk_user_identity(self, on_disk_user_identity):
        """Sets the on_disk_user_identity of this AuthUserExtended.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param on_disk_user_identity: The on_disk_user_identity of this AuthUserExtended.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._on_disk_user_identity = on_disk_user_identity

    @property
    def password_expired(self):
        """Gets the password_expired of this AuthUserExtended.  # noqa: E501

        If true, the password has expired.  # noqa: E501

        :return: The password_expired of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._password_expired

    @password_expired.setter
    def password_expired(self, password_expired):
        """Sets the password_expired of this AuthUserExtended.

        If true, the password has expired.  # noqa: E501

        :param password_expired: The password_expired of this AuthUserExtended.  # noqa: E501
        :type: bool
        """
        if password_expired is None:
            raise ValueError("Invalid value for `password_expired`, must not be `None`")  # noqa: E501

        self._password_expired = password_expired

    @property
    def password_expires(self):
        """Gets the password_expires of this AuthUserExtended.  # noqa: E501

        If true, the password is allowed to expire.  # noqa: E501

        :return: The password_expires of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._password_expires

    @password_expires.setter
    def password_expires(self, password_expires):
        """Sets the password_expires of this AuthUserExtended.

        If true, the password is allowed to expire.  # noqa: E501

        :param password_expires: The password_expires of this AuthUserExtended.  # noqa: E501
        :type: bool
        """
        if password_expires is None:
            raise ValueError("Invalid value for `password_expires`, must not be `None`")  # noqa: E501

        self._password_expires = password_expires

    @property
    def password_expiry(self):
        """Gets the password_expiry of this AuthUserExtended.  # noqa: E501


        :return: The password_expiry of this AuthUserExtended.  # noqa: E501
        :rtype: int
        """
        return self._password_expiry

    @password_expiry.setter
    def password_expiry(self, password_expiry):
        """Sets the password_expiry of this AuthUserExtended.


        :param password_expiry: The password_expiry of this AuthUserExtended.  # noqa: E501
        :type: int
        """
        if password_expiry is not None and password_expiry > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `password_expiry`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if password_expiry is not None and password_expiry < 0:  # noqa: E501
            raise ValueError("Invalid value for `password_expiry`, must be a value greater than or equal to `0`")  # noqa: E501

        self._password_expiry = password_expiry

    @property
    def password_last_set(self):
        """Gets the password_last_set of this AuthUserExtended.  # noqa: E501


        :return: The password_last_set of this AuthUserExtended.  # noqa: E501
        :rtype: int
        """
        return self._password_last_set

    @password_last_set.setter
    def password_last_set(self, password_last_set):
        """Sets the password_last_set of this AuthUserExtended.


        :param password_last_set: The password_last_set of this AuthUserExtended.  # noqa: E501
        :type: int
        """
        if password_last_set is not None and password_last_set > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `password_last_set`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if password_last_set is not None and password_last_set < 0:  # noqa: E501
            raise ValueError("Invalid value for `password_last_set`, must be a value greater than or equal to `0`")  # noqa: E501

        self._password_last_set = password_last_set

    @property
    def primary_group_sid(self):
        """Gets the primary_group_sid of this AuthUserExtended.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The primary_group_sid of this AuthUserExtended.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._primary_group_sid

    @primary_group_sid.setter
    def primary_group_sid(self, primary_group_sid):
        """Sets the primary_group_sid of this AuthUserExtended.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param primary_group_sid: The primary_group_sid of this AuthUserExtended.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._primary_group_sid = primary_group_sid

    @property
    def prompt_password_change(self):
        """Gets the prompt_password_change of this AuthUserExtended.  # noqa: E501

        Prompts the user to change their password at the next login.  # noqa: E501

        :return: The prompt_password_change of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._prompt_password_change

    @prompt_password_change.setter
    def prompt_password_change(self, prompt_password_change):
        """Sets the prompt_password_change of this AuthUserExtended.

        Prompts the user to change their password at the next login.  # noqa: E501

        :param prompt_password_change: The prompt_password_change of this AuthUserExtended.  # noqa: E501
        :type: bool
        """
        if prompt_password_change is None:
            raise ValueError("Invalid value for `prompt_password_change`, must not be `None`")  # noqa: E501

        self._prompt_password_change = prompt_password_change

    @property
    def provider(self):
        """Gets the provider of this AuthUserExtended.  # noqa: E501


        :return: The provider of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AuthUserExtended.


        :param provider: The provider of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if provider is not None and len(provider) > 255:
            raise ValueError("Invalid value for `provider`, length must be less than or equal to `255`")  # noqa: E501
        if provider is not None and len(provider) < 0:
            raise ValueError("Invalid value for `provider`, length must be greater than or equal to `0`")  # noqa: E501

        self._provider = provider

    @property
    def sam_account_name(self):
        """Gets the sam_account_name of this AuthUserExtended.  # noqa: E501


        :return: The sam_account_name of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._sam_account_name

    @sam_account_name.setter
    def sam_account_name(self, sam_account_name):
        """Sets the sam_account_name of this AuthUserExtended.


        :param sam_account_name: The sam_account_name of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if sam_account_name is not None and len(sam_account_name) > 255:
            raise ValueError("Invalid value for `sam_account_name`, length must be less than or equal to `255`")  # noqa: E501
        if sam_account_name is not None and len(sam_account_name) < 0:
            raise ValueError("Invalid value for `sam_account_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._sam_account_name = sam_account_name

    @property
    def shell(self):
        """Gets the shell of this AuthUserExtended.  # noqa: E501


        :return: The shell of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """Sets the shell of this AuthUserExtended.


        :param shell: The shell of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if shell is not None and len(shell) > 4096:
            raise ValueError("Invalid value for `shell`, length must be less than or equal to `4096`")  # noqa: E501
        if shell is not None and len(shell) < 0:
            raise ValueError("Invalid value for `shell`, length must be greater than or equal to `0`")  # noqa: E501

        self._shell = shell

    @property
    def sid(self):
        """Gets the sid of this AuthUserExtended.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The sid of this AuthUserExtended.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AuthUserExtended.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param sid: The sid of this AuthUserExtended.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._sid = sid

    @property
    def ssh_public_keys(self):
        """Gets the ssh_public_keys of this AuthUserExtended.  # noqa: E501

        Specifies the user's LDAP SSH Public Key.  # noqa: E501

        :return: The ssh_public_keys of this AuthUserExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._ssh_public_keys

    @ssh_public_keys.setter
    def ssh_public_keys(self, ssh_public_keys):
        """Sets the ssh_public_keys of this AuthUserExtended.

        Specifies the user's LDAP SSH Public Key.  # noqa: E501

        :param ssh_public_keys: The ssh_public_keys of this AuthUserExtended.  # noqa: E501
        :type: list[str]
        """

        self._ssh_public_keys = ssh_public_keys

    @property
    def type(self):
        """Gets the type of this AuthUserExtended.  # noqa: E501

        Specifies the object type.  # noqa: E501

        :return: The type of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuthUserExtended.

        Specifies the object type.  # noqa: E501

        :param type: The type of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if type is not None and len(type) > 255:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `255`")  # noqa: E501
        if type is not None and len(type) < 0:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `0`")  # noqa: E501

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this AuthUserExtended.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The uid of this AuthUserExtended.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AuthUserExtended.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param uid: The uid of this AuthUserExtended.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._uid = uid

    @property
    def upn(self):
        """Gets the upn of this AuthUserExtended.  # noqa: E501


        :return: The upn of this AuthUserExtended.  # noqa: E501
        :rtype: str
        """
        return self._upn

    @upn.setter
    def upn(self, upn):
        """Sets the upn of this AuthUserExtended.


        :param upn: The upn of this AuthUserExtended.  # noqa: E501
        :type: str
        """
        if upn is not None and len(upn) > 255:
            raise ValueError("Invalid value for `upn`, length must be less than or equal to `255`")  # noqa: E501
        if upn is not None and len(upn) < 0:
            raise ValueError("Invalid value for `upn`, length must be greater than or equal to `0`")  # noqa: E501

        self._upn = upn

    @property
    def user_can_change_password(self):
        """Gets the user_can_change_password of this AuthUserExtended.  # noqa: E501

        Specifies whether the password for the user can be changed.  # noqa: E501

        :return: The user_can_change_password of this AuthUserExtended.  # noqa: E501
        :rtype: bool
        """
        return self._user_can_change_password

    @user_can_change_password.setter
    def user_can_change_password(self, user_can_change_password):
        """Sets the user_can_change_password of this AuthUserExtended.

        Specifies whether the password for the user can be changed.  # noqa: E501

        :param user_can_change_password: The user_can_change_password of this AuthUserExtended.  # noqa: E501
        :type: bool
        """
        if user_can_change_password is None:
            raise ValueError("Invalid value for `user_can_change_password`, must not be `None`")  # noqa: E501

        self._user_can_change_password = user_can_change_password

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
        if not isinstance(other, AuthUserExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
