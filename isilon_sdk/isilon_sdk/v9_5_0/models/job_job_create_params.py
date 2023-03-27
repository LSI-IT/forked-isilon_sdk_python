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

from isilon_sdk.v9_5_0.models.job_job_avscan_params import JobJobAvscanParams  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.job_job_changelistcreate_params import JobJobChangelistcreateParams  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.job_job_domainmark_params import JobJobDomainmarkParams  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.job_job_esrsmftdownload_params import JobJobEsrsmftdownloadParams  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.job_job_filepolicy_params import JobJobFilepolicyParams  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.job_job_prepair_params import JobJobPrepairParams  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.job_job_smartpoolstree_params import JobJobSmartpoolstreeParams  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.job_job_snaprevert_params import JobJobSnaprevertParams  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.job_job_treedelete_params import JobJobTreedeleteParams  # noqa: F401,E501


class JobJobCreateParams(object):
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
        'allow_dup': 'bool',
        'avscan_params': 'JobJobAvscanParams',
        'changelistcreate_params': 'JobJobChangelistcreateParams',
        'domainmark_params': 'JobJobDomainmarkParams',
        'esrsmftdownload_params': 'JobJobEsrsmftdownloadParams',
        'filepolicy_params': 'JobJobFilepolicyParams',
        'paths': 'list[str]',
        'policy': 'str',
        'prepair_params': 'JobJobPrepairParams',
        'priority': 'int',
        'smartpoolstree_params': 'JobJobSmartpoolstreeParams',
        'snaprevert_params': 'JobJobSnaprevertParams',
        'treedelete_params': 'JobJobTreedeleteParams',
        'type': 'str'
    }

    attribute_map = {
        'allow_dup': 'allow_dup',
        'avscan_params': 'avscan_params',
        'changelistcreate_params': 'changelistcreate_params',
        'domainmark_params': 'domainmark_params',
        'esrsmftdownload_params': 'esrsmftdownload_params',
        'filepolicy_params': 'filepolicy_params',
        'paths': 'paths',
        'policy': 'policy',
        'prepair_params': 'prepair_params',
        'priority': 'priority',
        'smartpoolstree_params': 'smartpoolstree_params',
        'snaprevert_params': 'snaprevert_params',
        'treedelete_params': 'treedelete_params',
        'type': 'type'
    }

    def __init__(self, allow_dup=None, avscan_params=None, changelistcreate_params=None, domainmark_params=None, esrsmftdownload_params=None, filepolicy_params=None, paths=None, policy=None, prepair_params=None, priority=None, smartpoolstree_params=None, snaprevert_params=None, treedelete_params=None, type=None):  # noqa: E501
        """JobJobCreateParams - a model defined in Swagger"""  # noqa: E501

        self._allow_dup = None
        self._avscan_params = None
        self._changelistcreate_params = None
        self._domainmark_params = None
        self._esrsmftdownload_params = None
        self._filepolicy_params = None
        self._paths = None
        self._policy = None
        self._prepair_params = None
        self._priority = None
        self._smartpoolstree_params = None
        self._snaprevert_params = None
        self._treedelete_params = None
        self._type = None
        self.discriminator = None

        if allow_dup is not None:
            self.allow_dup = allow_dup
        if avscan_params is not None:
            self.avscan_params = avscan_params
        if changelistcreate_params is not None:
            self.changelistcreate_params = changelistcreate_params
        if domainmark_params is not None:
            self.domainmark_params = domainmark_params
        if esrsmftdownload_params is not None:
            self.esrsmftdownload_params = esrsmftdownload_params
        if filepolicy_params is not None:
            self.filepolicy_params = filepolicy_params
        if paths is not None:
            self.paths = paths
        if policy is not None:
            self.policy = policy
        if prepair_params is not None:
            self.prepair_params = prepair_params
        if priority is not None:
            self.priority = priority
        if smartpoolstree_params is not None:
            self.smartpoolstree_params = smartpoolstree_params
        if snaprevert_params is not None:
            self.snaprevert_params = snaprevert_params
        if treedelete_params is not None:
            self.treedelete_params = treedelete_params
        self.type = type

    @property
    def allow_dup(self):
        """Gets the allow_dup of this JobJobCreateParams.  # noqa: E501

        Whether or not to queue the job if one of the same type is already running or queued.  # noqa: E501

        :return: The allow_dup of this JobJobCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._allow_dup

    @allow_dup.setter
    def allow_dup(self, allow_dup):
        """Sets the allow_dup of this JobJobCreateParams.

        Whether or not to queue the job if one of the same type is already running or queued.  # noqa: E501

        :param allow_dup: The allow_dup of this JobJobCreateParams.  # noqa: E501
        :type: bool
        """

        self._allow_dup = allow_dup

    @property
    def avscan_params(self):
        """Gets the avscan_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The avscan_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobAvscanParams
        """
        return self._avscan_params

    @avscan_params.setter
    def avscan_params(self, avscan_params):
        """Sets the avscan_params of this JobJobCreateParams.

          # noqa: E501

        :param avscan_params: The avscan_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobAvscanParams
        """

        self._avscan_params = avscan_params

    @property
    def changelistcreate_params(self):
        """Gets the changelistcreate_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The changelistcreate_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobChangelistcreateParams
        """
        return self._changelistcreate_params

    @changelistcreate_params.setter
    def changelistcreate_params(self, changelistcreate_params):
        """Sets the changelistcreate_params of this JobJobCreateParams.

          # noqa: E501

        :param changelistcreate_params: The changelistcreate_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobChangelistcreateParams
        """

        self._changelistcreate_params = changelistcreate_params

    @property
    def domainmark_params(self):
        """Gets the domainmark_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The domainmark_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobDomainmarkParams
        """
        return self._domainmark_params

    @domainmark_params.setter
    def domainmark_params(self, domainmark_params):
        """Sets the domainmark_params of this JobJobCreateParams.

          # noqa: E501

        :param domainmark_params: The domainmark_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobDomainmarkParams
        """

        self._domainmark_params = domainmark_params

    @property
    def esrsmftdownload_params(self):
        """Gets the esrsmftdownload_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The esrsmftdownload_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobEsrsmftdownloadParams
        """
        return self._esrsmftdownload_params

    @esrsmftdownload_params.setter
    def esrsmftdownload_params(self, esrsmftdownload_params):
        """Sets the esrsmftdownload_params of this JobJobCreateParams.

          # noqa: E501

        :param esrsmftdownload_params: The esrsmftdownload_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobEsrsmftdownloadParams
        """

        self._esrsmftdownload_params = esrsmftdownload_params

    @property
    def filepolicy_params(self):
        """Gets the filepolicy_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The filepolicy_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobFilepolicyParams
        """
        return self._filepolicy_params

    @filepolicy_params.setter
    def filepolicy_params(self, filepolicy_params):
        """Sets the filepolicy_params of this JobJobCreateParams.

          # noqa: E501

        :param filepolicy_params: The filepolicy_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobFilepolicyParams
        """

        self._filepolicy_params = filepolicy_params

    @property
    def paths(self):
        """Gets the paths of this JobJobCreateParams.  # noqa: E501

        For jobs which take paths, the IFS paths to pass to the job.  # noqa: E501

        :return: The paths of this JobJobCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this JobJobCreateParams.

        For jobs which take paths, the IFS paths to pass to the job.  # noqa: E501

        :param paths: The paths of this JobJobCreateParams.  # noqa: E501
        :type: list[str]
        """

        self._paths = paths

    @property
    def policy(self):
        """Gets the policy of this JobJobCreateParams.  # noqa: E501

        Impact policy of this job instance.  # noqa: E501

        :return: The policy of this JobJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this JobJobCreateParams.

        Impact policy of this job instance.  # noqa: E501

        :param policy: The policy of this JobJobCreateParams.  # noqa: E501
        :type: str
        """
        if policy is not None and len(policy) > 254:
            raise ValueError("Invalid value for `policy`, length must be less than or equal to `254`")  # noqa: E501
        if policy is not None and len(policy) < 1:
            raise ValueError("Invalid value for `policy`, length must be greater than or equal to `1`")  # noqa: E501

        self._policy = policy

    @property
    def prepair_params(self):
        """Gets the prepair_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The prepair_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobPrepairParams
        """
        return self._prepair_params

    @prepair_params.setter
    def prepair_params(self, prepair_params):
        """Sets the prepair_params of this JobJobCreateParams.

          # noqa: E501

        :param prepair_params: The prepair_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobPrepairParams
        """

        self._prepair_params = prepair_params

    @property
    def priority(self):
        """Gets the priority of this JobJobCreateParams.  # noqa: E501

        Priority of this job instance; lower numbers preempt higher numbers.  # noqa: E501

        :return: The priority of this JobJobCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JobJobCreateParams.

        Priority of this job instance; lower numbers preempt higher numbers.  # noqa: E501

        :param priority: The priority of this JobJobCreateParams.  # noqa: E501
        :type: int
        """
        if priority is not None and priority > 10:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `10`")  # noqa: E501
        if priority is not None and priority < 1:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `1`")  # noqa: E501

        self._priority = priority

    @property
    def smartpoolstree_params(self):
        """Gets the smartpoolstree_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The smartpoolstree_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobSmartpoolstreeParams
        """
        return self._smartpoolstree_params

    @smartpoolstree_params.setter
    def smartpoolstree_params(self, smartpoolstree_params):
        """Sets the smartpoolstree_params of this JobJobCreateParams.

          # noqa: E501

        :param smartpoolstree_params: The smartpoolstree_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobSmartpoolstreeParams
        """

        self._smartpoolstree_params = smartpoolstree_params

    @property
    def snaprevert_params(self):
        """Gets the snaprevert_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The snaprevert_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobSnaprevertParams
        """
        return self._snaprevert_params

    @snaprevert_params.setter
    def snaprevert_params(self, snaprevert_params):
        """Sets the snaprevert_params of this JobJobCreateParams.

          # noqa: E501

        :param snaprevert_params: The snaprevert_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobSnaprevertParams
        """

        self._snaprevert_params = snaprevert_params

    @property
    def treedelete_params(self):
        """Gets the treedelete_params of this JobJobCreateParams.  # noqa: E501

          # noqa: E501

        :return: The treedelete_params of this JobJobCreateParams.  # noqa: E501
        :rtype: JobJobTreedeleteParams
        """
        return self._treedelete_params

    @treedelete_params.setter
    def treedelete_params(self, treedelete_params):
        """Sets the treedelete_params of this JobJobCreateParams.

          # noqa: E501

        :param treedelete_params: The treedelete_params of this JobJobCreateParams.  # noqa: E501
        :type: JobJobTreedeleteParams
        """

        self._treedelete_params = treedelete_params

    @property
    def type(self):
        """Gets the type of this JobJobCreateParams.  # noqa: E501

        Job type to queue.  # noqa: E501

        :return: The type of this JobJobCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobJobCreateParams.

        Job type to queue.  # noqa: E501

        :param type: The type of this JobJobCreateParams.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if type is not None and len(type) > 100:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `100`")  # noqa: E501
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

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
        if not isinstance(other, JobJobCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
