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


class ProvidersLocalIdParams(object):
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
        'authentication': 'bool',
        'create_home_directory': 'bool',
        'delete_password_hashes': 'bool',
        'delete_password_history': 'bool',
        'home_directory_template': 'str',
        'lockout_duration': 'int',
        'lockout_threshold': 'int',
        'lockout_window': 'int',
        'login_shell': 'str',
        'machine_name': 'str',
        'max_inactivity_days': 'int',
        'max_password_age': 'int',
        'min_password_age': 'int',
        'min_password_length': 'int',
        'name': 'str',
        'password_chars_changed': 'int',
        'password_complexity': 'list[str]',
        'password_hash_type': 'str',
        'password_history_length': 'int',
        'password_percent_changed': 'int',
        'password_prompt_time': 'int'
    }

    attribute_map = {
        'authentication': 'authentication',
        'create_home_directory': 'create_home_directory',
        'delete_password_hashes': 'delete_password_hashes',
        'delete_password_history': 'delete_password_history',
        'home_directory_template': 'home_directory_template',
        'lockout_duration': 'lockout_duration',
        'lockout_threshold': 'lockout_threshold',
        'lockout_window': 'lockout_window',
        'login_shell': 'login_shell',
        'machine_name': 'machine_name',
        'max_inactivity_days': 'max_inactivity_days',
        'max_password_age': 'max_password_age',
        'min_password_age': 'min_password_age',
        'min_password_length': 'min_password_length',
        'name': 'name',
        'password_chars_changed': 'password_chars_changed',
        'password_complexity': 'password_complexity',
        'password_hash_type': 'password_hash_type',
        'password_history_length': 'password_history_length',
        'password_percent_changed': 'password_percent_changed',
        'password_prompt_time': 'password_prompt_time'
    }

    def __init__(self, authentication=None, create_home_directory=None, delete_password_hashes=None, delete_password_history=None, home_directory_template=None, lockout_duration=None, lockout_threshold=None, lockout_window=None, login_shell=None, machine_name=None, max_inactivity_days=None, max_password_age=None, min_password_age=None, min_password_length=None, name=None, password_chars_changed=None, password_complexity=None, password_hash_type=None, password_history_length=None, password_percent_changed=None, password_prompt_time=None):  # noqa: E501
        """ProvidersLocalIdParams - a model defined in Swagger"""  # noqa: E501

        self._authentication = None
        self._create_home_directory = None
        self._delete_password_hashes = None
        self._delete_password_history = None
        self._home_directory_template = None
        self._lockout_duration = None
        self._lockout_threshold = None
        self._lockout_window = None
        self._login_shell = None
        self._machine_name = None
        self._max_inactivity_days = None
        self._max_password_age = None
        self._min_password_age = None
        self._min_password_length = None
        self._name = None
        self._password_chars_changed = None
        self._password_complexity = None
        self._password_hash_type = None
        self._password_history_length = None
        self._password_percent_changed = None
        self._password_prompt_time = None
        self.discriminator = None

        if authentication is not None:
            self.authentication = authentication
        if create_home_directory is not None:
            self.create_home_directory = create_home_directory
        if delete_password_hashes is not None:
            self.delete_password_hashes = delete_password_hashes
        if delete_password_history is not None:
            self.delete_password_history = delete_password_history
        if home_directory_template is not None:
            self.home_directory_template = home_directory_template
        if lockout_duration is not None:
            self.lockout_duration = lockout_duration
        if lockout_threshold is not None:
            self.lockout_threshold = lockout_threshold
        if lockout_window is not None:
            self.lockout_window = lockout_window
        if login_shell is not None:
            self.login_shell = login_shell
        if machine_name is not None:
            self.machine_name = machine_name
        if max_inactivity_days is not None:
            self.max_inactivity_days = max_inactivity_days
        if max_password_age is not None:
            self.max_password_age = max_password_age
        if min_password_age is not None:
            self.min_password_age = min_password_age
        if min_password_length is not None:
            self.min_password_length = min_password_length
        if name is not None:
            self.name = name
        if password_chars_changed is not None:
            self.password_chars_changed = password_chars_changed
        if password_complexity is not None:
            self.password_complexity = password_complexity
        if password_hash_type is not None:
            self.password_hash_type = password_hash_type
        if password_history_length is not None:
            self.password_history_length = password_history_length
        if password_percent_changed is not None:
            self.password_percent_changed = password_percent_changed
        if password_prompt_time is not None:
            self.password_prompt_time = password_prompt_time

    @property
    def authentication(self):
        """Gets the authentication of this ProvidersLocalIdParams.  # noqa: E501

        If true, enables authentication and identity management through the authentication provider.  # noqa: E501

        :return: The authentication of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this ProvidersLocalIdParams.

        If true, enables authentication and identity management through the authentication provider.  # noqa: E501

        :param authentication: The authentication of this ProvidersLocalIdParams.  # noqa: E501
        :type: bool
        """

        self._authentication = authentication

    @property
    def create_home_directory(self):
        """Gets the create_home_directory of this ProvidersLocalIdParams.  # noqa: E501

        Automatically creates the home directory on the first login.  # noqa: E501

        :return: The create_home_directory of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: bool
        """
        return self._create_home_directory

    @create_home_directory.setter
    def create_home_directory(self, create_home_directory):
        """Sets the create_home_directory of this ProvidersLocalIdParams.

        Automatically creates the home directory on the first login.  # noqa: E501

        :param create_home_directory: The create_home_directory of this ProvidersLocalIdParams.  # noqa: E501
        :type: bool
        """

        self._create_home_directory = create_home_directory

    @property
    def delete_password_hashes(self):
        """Gets the delete_password_hashes of this ProvidersLocalIdParams.  # noqa: E501

        Delete all password hashes that do not match Password Hash Type and force password change at next login.  # noqa: E501

        :return: The delete_password_hashes of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: bool
        """
        return self._delete_password_hashes

    @delete_password_hashes.setter
    def delete_password_hashes(self, delete_password_hashes):
        """Sets the delete_password_hashes of this ProvidersLocalIdParams.

        Delete all password hashes that do not match Password Hash Type and force password change at next login.  # noqa: E501

        :param delete_password_hashes: The delete_password_hashes of this ProvidersLocalIdParams.  # noqa: E501
        :type: bool
        """

        self._delete_password_hashes = delete_password_hashes

    @property
    def delete_password_history(self):
        """Gets the delete_password_history of this ProvidersLocalIdParams.  # noqa: E501

        Delete password history for all local users  # noqa: E501

        :return: The delete_password_history of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: bool
        """
        return self._delete_password_history

    @delete_password_history.setter
    def delete_password_history(self, delete_password_history):
        """Sets the delete_password_history of this ProvidersLocalIdParams.

        Delete password history for all local users  # noqa: E501

        :param delete_password_history: The delete_password_history of this ProvidersLocalIdParams.  # noqa: E501
        :type: bool
        """

        self._delete_password_history = delete_password_history

    @property
    def home_directory_template(self):
        """Gets the home_directory_template of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the path to the home directory template.  # noqa: E501

        :return: The home_directory_template of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: str
        """
        return self._home_directory_template

    @home_directory_template.setter
    def home_directory_template(self, home_directory_template):
        """Sets the home_directory_template of this ProvidersLocalIdParams.

        Specifies the path to the home directory template.  # noqa: E501

        :param home_directory_template: The home_directory_template of this ProvidersLocalIdParams.  # noqa: E501
        :type: str
        """
        if home_directory_template is not None and len(home_directory_template) > 4096:
            raise ValueError("Invalid value for `home_directory_template`, length must be less than or equal to `4096`")  # noqa: E501
        if home_directory_template is not None and len(home_directory_template) < 0:
            raise ValueError("Invalid value for `home_directory_template`, length must be greater than or equal to `0`")  # noqa: E501
        if home_directory_template is not None and not re.search('^((\/[^\/[:cntrl:]]+)(\/?))*$', home_directory_template):  # noqa: E501
            raise ValueError("Invalid value for `home_directory_template`, must be a follow pattern or equal to `/^((\/[^\/[:cntrl:]]+)(\/?))*$/`")  # noqa: E501

        self._home_directory_template = home_directory_template

    @property
    def lockout_duration(self):
        """Gets the lockout_duration of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the length of time in seconds that an account will be inaccessible after multiple failed login attempts.  # noqa: E501

        :return: The lockout_duration of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._lockout_duration

    @lockout_duration.setter
    def lockout_duration(self, lockout_duration):
        """Sets the lockout_duration of this ProvidersLocalIdParams.

        Specifies the length of time in seconds that an account will be inaccessible after multiple failed login attempts.  # noqa: E501

        :param lockout_duration: The lockout_duration of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if lockout_duration is not None and lockout_duration > 5999940:  # noqa: E501
            raise ValueError("Invalid value for `lockout_duration`, must be a value less than or equal to `5999940`")  # noqa: E501
        if lockout_duration is not None and lockout_duration < 0:  # noqa: E501
            raise ValueError("Invalid value for `lockout_duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lockout_duration = lockout_duration

    @property
    def lockout_threshold(self):
        """Gets the lockout_threshold of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the number of failed login attempts necessary before an account is locked.  # noqa: E501

        :return: The lockout_threshold of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._lockout_threshold

    @lockout_threshold.setter
    def lockout_threshold(self, lockout_threshold):
        """Sets the lockout_threshold of this ProvidersLocalIdParams.

        Specifies the number of failed login attempts necessary before an account is locked.  # noqa: E501

        :param lockout_threshold: The lockout_threshold of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if lockout_threshold is not None and lockout_threshold > 999:  # noqa: E501
            raise ValueError("Invalid value for `lockout_threshold`, must be a value less than or equal to `999`")  # noqa: E501
        if lockout_threshold is not None and lockout_threshold < 0:  # noqa: E501
            raise ValueError("Invalid value for `lockout_threshold`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lockout_threshold = lockout_threshold

    @property
    def lockout_window(self):
        """Gets the lockout_window of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the duration of time in seconds in which the number of failed attempts set in the 'lockout_threshold' parameter must be made before an account is locked.  # noqa: E501

        :return: The lockout_window of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._lockout_window

    @lockout_window.setter
    def lockout_window(self, lockout_window):
        """Sets the lockout_window of this ProvidersLocalIdParams.

        Specifies the duration of time in seconds in which the number of failed attempts set in the 'lockout_threshold' parameter must be made before an account is locked.  # noqa: E501

        :param lockout_window: The lockout_window of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if lockout_window is not None and lockout_window > 5999940:  # noqa: E501
            raise ValueError("Invalid value for `lockout_window`, must be a value less than or equal to `5999940`")  # noqa: E501
        if lockout_window is not None and lockout_window < 0:  # noqa: E501
            raise ValueError("Invalid value for `lockout_window`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lockout_window = lockout_window

    @property
    def login_shell(self):
        """Gets the login_shell of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the login shell path.  # noqa: E501

        :return: The login_shell of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: str
        """
        return self._login_shell

    @login_shell.setter
    def login_shell(self, login_shell):
        """Sets the login_shell of this ProvidersLocalIdParams.

        Specifies the login shell path.  # noqa: E501

        :param login_shell: The login_shell of this ProvidersLocalIdParams.  # noqa: E501
        :type: str
        """
        if login_shell is not None and len(login_shell) > 4096:
            raise ValueError("Invalid value for `login_shell`, length must be less than or equal to `4096`")  # noqa: E501
        if login_shell is not None and len(login_shell) < 0:
            raise ValueError("Invalid value for `login_shell`, length must be greater than or equal to `0`")  # noqa: E501

        self._login_shell = login_shell

    @property
    def machine_name(self):
        """Gets the machine_name of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the domain for this provider through which users and groups are qualified.  # noqa: E501

        :return: The machine_name of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this ProvidersLocalIdParams.

        Specifies the domain for this provider through which users and groups are qualified.  # noqa: E501

        :param machine_name: The machine_name of this ProvidersLocalIdParams.  # noqa: E501
        :type: str
        """
        if machine_name is not None and len(machine_name) > 255:
            raise ValueError("Invalid value for `machine_name`, length must be less than or equal to `255`")  # noqa: E501
        if machine_name is not None and len(machine_name) < 0:
            raise ValueError("Invalid value for `machine_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._machine_name = machine_name

    @property
    def max_inactivity_days(self):
        """Gets the max_inactivity_days of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the maximum number of days a user account can be inactive before it will be disabled.  # noqa: E501

        :return: The max_inactivity_days of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._max_inactivity_days

    @max_inactivity_days.setter
    def max_inactivity_days(self, max_inactivity_days):
        """Sets the max_inactivity_days of this ProvidersLocalIdParams.

        Specifies the maximum number of days a user account can be inactive before it will be disabled.  # noqa: E501

        :param max_inactivity_days: The max_inactivity_days of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if max_inactivity_days is not None and max_inactivity_days > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `max_inactivity_days`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if max_inactivity_days is not None and max_inactivity_days < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_inactivity_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_inactivity_days = max_inactivity_days

    @property
    def max_password_age(self):
        """Gets the max_password_age of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the maximum password age in seconds.  # noqa: E501

        :return: The max_password_age of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._max_password_age

    @max_password_age.setter
    def max_password_age(self, max_password_age):
        """Sets the max_password_age of this ProvidersLocalIdParams.

        Specifies the maximum password age in seconds.  # noqa: E501

        :param max_password_age: The max_password_age of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if max_password_age is not None and max_password_age > 86313600:  # noqa: E501
            raise ValueError("Invalid value for `max_password_age`, must be a value less than or equal to `86313600`")  # noqa: E501
        if max_password_age is not None and max_password_age < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_password_age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_password_age = max_password_age

    @property
    def min_password_age(self):
        """Gets the min_password_age of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the minimum password age in seconds.  # noqa: E501

        :return: The min_password_age of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._min_password_age

    @min_password_age.setter
    def min_password_age(self, min_password_age):
        """Sets the min_password_age of this ProvidersLocalIdParams.

        Specifies the minimum password age in seconds.  # noqa: E501

        :param min_password_age: The min_password_age of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if min_password_age is not None and min_password_age > 86313600:  # noqa: E501
            raise ValueError("Invalid value for `min_password_age`, must be a value less than or equal to `86313600`")  # noqa: E501
        if min_password_age is not None and min_password_age < 0:  # noqa: E501
            raise ValueError("Invalid value for `min_password_age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_password_age = min_password_age

    @property
    def min_password_length(self):
        """Gets the min_password_length of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the minimum password length.  # noqa: E501

        :return: The min_password_length of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._min_password_length

    @min_password_length.setter
    def min_password_length(self, min_password_length):
        """Sets the min_password_length of this ProvidersLocalIdParams.

        Specifies the minimum password length.  # noqa: E501

        :param min_password_length: The min_password_length of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if min_password_length is not None and min_password_length > 256:  # noqa: E501
            raise ValueError("Invalid value for `min_password_length`, must be a value less than or equal to `256`")  # noqa: E501
        if min_password_length is not None and min_password_length < 0:  # noqa: E501
            raise ValueError("Invalid value for `min_password_length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_password_length = min_password_length

    @property
    def name(self):
        """Gets the name of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the local provider name.  # noqa: E501

        :return: The name of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvidersLocalIdParams.

        Specifies the local provider name.  # noqa: E501

        :param name: The name of this ProvidersLocalIdParams.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def password_chars_changed(self):
        """Gets the password_chars_changed of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the minimum number of characters changed when a password is updated.  # noqa: E501

        :return: The password_chars_changed of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._password_chars_changed

    @password_chars_changed.setter
    def password_chars_changed(self, password_chars_changed):
        """Sets the password_chars_changed of this ProvidersLocalIdParams.

        Specifies the minimum number of characters changed when a password is updated.  # noqa: E501

        :param password_chars_changed: The password_chars_changed of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if password_chars_changed is not None and password_chars_changed > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `password_chars_changed`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if password_chars_changed is not None and password_chars_changed < 0:  # noqa: E501
            raise ValueError("Invalid value for `password_chars_changed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._password_chars_changed = password_chars_changed

    @property
    def password_complexity(self):
        """Gets the password_complexity of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the conditions required for a password.  # noqa: E501

        :return: The password_complexity of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._password_complexity

    @password_complexity.setter
    def password_complexity(self, password_complexity):
        """Sets the password_complexity of this ProvidersLocalIdParams.

        Specifies the conditions required for a password.  # noqa: E501

        :param password_complexity: The password_complexity of this ProvidersLocalIdParams.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["lowercase", "uppercase", "numeric", "symbol", "repeat"]  # noqa: E501
        if not set(password_complexity).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `password_complexity` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(password_complexity) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._password_complexity = password_complexity

    @property
    def password_hash_type(self):
        """Gets the password_hash_type of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the password hash algorithm to use.  # noqa: E501

        :return: The password_hash_type of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: str
        """
        return self._password_hash_type

    @password_hash_type.setter
    def password_hash_type(self, password_hash_type):
        """Sets the password_hash_type of this ProvidersLocalIdParams.

        Specifies the password hash algorithm to use.  # noqa: E501

        :param password_hash_type: The password_hash_type of this ProvidersLocalIdParams.  # noqa: E501
        :type: str
        """

        self._password_hash_type = password_hash_type

    @property
    def password_history_length(self):
        """Gets the password_history_length of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the number of previous passwords to store.  # noqa: E501

        :return: The password_history_length of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._password_history_length

    @password_history_length.setter
    def password_history_length(self, password_history_length):
        """Sets the password_history_length of this ProvidersLocalIdParams.

        Specifies the number of previous passwords to store.  # noqa: E501

        :param password_history_length: The password_history_length of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if password_history_length is not None and password_history_length > 24:  # noqa: E501
            raise ValueError("Invalid value for `password_history_length`, must be a value less than or equal to `24`")  # noqa: E501
        if password_history_length is not None and password_history_length < 0:  # noqa: E501
            raise ValueError("Invalid value for `password_history_length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._password_history_length = password_history_length

    @property
    def password_percent_changed(self):
        """Gets the password_percent_changed of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the minimum percent of characters changed when a password is updated.  # noqa: E501

        :return: The password_percent_changed of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._password_percent_changed

    @password_percent_changed.setter
    def password_percent_changed(self, password_percent_changed):
        """Sets the password_percent_changed of this ProvidersLocalIdParams.

        Specifies the minimum percent of characters changed when a password is updated.  # noqa: E501

        :param password_percent_changed: The password_percent_changed of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if password_percent_changed is not None and password_percent_changed > 100:  # noqa: E501
            raise ValueError("Invalid value for `password_percent_changed`, must be a value less than or equal to `100`")  # noqa: E501
        if password_percent_changed is not None and password_percent_changed < 0:  # noqa: E501
            raise ValueError("Invalid value for `password_percent_changed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._password_percent_changed = password_percent_changed

    @property
    def password_prompt_time(self):
        """Gets the password_prompt_time of this ProvidersLocalIdParams.  # noqa: E501

        Specifies the time in seconds remaining before a user will be prompted for a password change.  # noqa: E501

        :return: The password_prompt_time of this ProvidersLocalIdParams.  # noqa: E501
        :rtype: int
        """
        return self._password_prompt_time

    @password_prompt_time.setter
    def password_prompt_time(self, password_prompt_time):
        """Sets the password_prompt_time of this ProvidersLocalIdParams.

        Specifies the time in seconds remaining before a user will be prompted for a password change.  # noqa: E501

        :param password_prompt_time: The password_prompt_time of this ProvidersLocalIdParams.  # noqa: E501
        :type: int
        """
        if password_prompt_time is not None and password_prompt_time > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `password_prompt_time`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if password_prompt_time is not None and password_prompt_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `password_prompt_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._password_prompt_time = password_prompt_time

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
        if not isinstance(other, ProvidersLocalIdParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
