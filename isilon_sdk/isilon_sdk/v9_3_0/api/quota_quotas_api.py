# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 14
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isilon_sdk.v9_3_0.api_client import ApiClient


class QuotaQuotasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_quota_notification(self, quota_notification, qid, **kwargs):  # noqa: E501
        """create_quota_notification  # noqa: E501

        Create a new notification rule specific to this quota.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_quota_notification(quota_notification, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuotaNotificationCreateParams quota_notification: (required)
        :param str qid: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_quota_notification_with_http_info(quota_notification, qid, **kwargs)  # noqa: E501
        else:
            (data) = self.create_quota_notification_with_http_info(quota_notification, qid, **kwargs)  # noqa: E501
            return data

    def create_quota_notification_with_http_info(self, quota_notification, qid, **kwargs):  # noqa: E501
        """create_quota_notification  # noqa: E501

        Create a new notification rule specific to this quota.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_quota_notification_with_http_info(quota_notification, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuotaNotificationCreateParams quota_notification: (required)
        :param str qid: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quota_notification', 'qid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_quota_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quota_notification' is set
        if ('quota_notification' not in params or
                params['quota_notification'] is None):
            raise ValueError("Missing the required parameter `quota_notification` when calling `create_quota_notification`")  # noqa: E501
        # verify the required parameter 'qid' is set
        if ('qid' not in params or
                params['qid'] is None):
            raise ValueError("Missing the required parameter `qid` when calling `create_quota_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'qid' in params:
            path_params['Qid'] = params['qid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'quota_notification' in params:
            body_params = params['quota_notification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/quota/quotas/{Qid}/notifications', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_quota_notification(self, quota_notification_id, qid, **kwargs):  # noqa: E501
        """delete_quota_notification  # noqa: E501

        Delete the notification rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_quota_notification(quota_notification_id, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quota_notification_id: Delete the notification rule. (required)
        :param str qid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_quota_notification_with_http_info(quota_notification_id, qid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_quota_notification_with_http_info(quota_notification_id, qid, **kwargs)  # noqa: E501
            return data

    def delete_quota_notification_with_http_info(self, quota_notification_id, qid, **kwargs):  # noqa: E501
        """delete_quota_notification  # noqa: E501

        Delete the notification rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_quota_notification_with_http_info(quota_notification_id, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quota_notification_id: Delete the notification rule. (required)
        :param str qid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quota_notification_id', 'qid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_quota_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quota_notification_id' is set
        if ('quota_notification_id' not in params or
                params['quota_notification_id'] is None):
            raise ValueError("Missing the required parameter `quota_notification_id` when calling `delete_quota_notification`")  # noqa: E501
        # verify the required parameter 'qid' is set
        if ('qid' not in params or
                params['qid'] is None):
            raise ValueError("Missing the required parameter `qid` when calling `delete_quota_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'quota_notification_id' in params:
            path_params['QuotaNotificationId'] = params['quota_notification_id']  # noqa: E501
        if 'qid' in params:
            path_params['Qid'] = params['qid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/quota/quotas/{Qid}/notifications/{QuotaNotificationId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_quota_notifications(self, qid, **kwargs):  # noqa: E501
        """delete_quota_notifications  # noqa: E501

        Delete all quota specific rules. The quota will then use the global rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_quota_notifications(qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str qid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_quota_notifications_with_http_info(qid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_quota_notifications_with_http_info(qid, **kwargs)  # noqa: E501
            return data

    def delete_quota_notifications_with_http_info(self, qid, **kwargs):  # noqa: E501
        """delete_quota_notifications  # noqa: E501

        Delete all quota specific rules. The quota will then use the global rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_quota_notifications_with_http_info(qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str qid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['qid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_quota_notifications" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'qid' is set
        if ('qid' not in params or
                params['qid'] is None):
            raise ValueError("Missing the required parameter `qid` when calling `delete_quota_notifications`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'qid' in params:
            path_params['Qid'] = params['qid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/quota/quotas/{Qid}/notifications', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_quota_notification(self, quota_notification_id, qid, **kwargs):  # noqa: E501
        """get_quota_notification  # noqa: E501

        Retrieve notification rule information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota_notification(quota_notification_id, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quota_notification_id: Retrieve notification rule information. (required)
        :param str qid: (required)
        :return: QuotaNotifications
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_quota_notification_with_http_info(quota_notification_id, qid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_quota_notification_with_http_info(quota_notification_id, qid, **kwargs)  # noqa: E501
            return data

    def get_quota_notification_with_http_info(self, quota_notification_id, qid, **kwargs):  # noqa: E501
        """get_quota_notification  # noqa: E501

        Retrieve notification rule information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota_notification_with_http_info(quota_notification_id, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quota_notification_id: Retrieve notification rule information. (required)
        :param str qid: (required)
        :return: QuotaNotifications
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quota_notification_id', 'qid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quota_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quota_notification_id' is set
        if ('quota_notification_id' not in params or
                params['quota_notification_id'] is None):
            raise ValueError("Missing the required parameter `quota_notification_id` when calling `get_quota_notification`")  # noqa: E501
        # verify the required parameter 'qid' is set
        if ('qid' not in params or
                params['qid'] is None):
            raise ValueError("Missing the required parameter `qid` when calling `get_quota_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'quota_notification_id' in params:
            path_params['QuotaNotificationId'] = params['quota_notification_id']  # noqa: E501
        if 'qid' in params:
            path_params['Qid'] = params['qid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/quota/quotas/{Qid}/notifications/{QuotaNotificationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuotaNotifications',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_quota_notifications(self, qid, **kwargs):  # noqa: E501
        """list_quota_notifications  # noqa: E501

        List all rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_quota_notifications(qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str qid: (required)
        :return: QuotaNotificationsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_quota_notifications_with_http_info(qid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_quota_notifications_with_http_info(qid, **kwargs)  # noqa: E501
            return data

    def list_quota_notifications_with_http_info(self, qid, **kwargs):  # noqa: E501
        """list_quota_notifications  # noqa: E501

        List all rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_quota_notifications_with_http_info(qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str qid: (required)
        :return: QuotaNotificationsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['qid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_quota_notifications" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'qid' is set
        if ('qid' not in params or
                params['qid'] is None):
            raise ValueError("Missing the required parameter `qid` when calling `list_quota_notifications`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'qid' in params:
            path_params['Qid'] = params['qid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/quota/quotas/{Qid}/notifications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuotaNotificationsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_quota_notification(self, quota_notification, quota_notification_id, qid, **kwargs):  # noqa: E501
        """update_quota_notification  # noqa: E501

        Modify notification rule. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_quota_notification(quota_notification, quota_notification_id, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuotaNotification quota_notification: (required)
        :param str quota_notification_id: Modify notification rule. All input fields are optional, but one or more must be supplied. (required)
        :param str qid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_quota_notification_with_http_info(quota_notification, quota_notification_id, qid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_quota_notification_with_http_info(quota_notification, quota_notification_id, qid, **kwargs)  # noqa: E501
            return data

    def update_quota_notification_with_http_info(self, quota_notification, quota_notification_id, qid, **kwargs):  # noqa: E501
        """update_quota_notification  # noqa: E501

        Modify notification rule. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_quota_notification_with_http_info(quota_notification, quota_notification_id, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuotaNotification quota_notification: (required)
        :param str quota_notification_id: Modify notification rule. All input fields are optional, but one or more must be supplied. (required)
        :param str qid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quota_notification', 'quota_notification_id', 'qid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_quota_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quota_notification' is set
        if ('quota_notification' not in params or
                params['quota_notification'] is None):
            raise ValueError("Missing the required parameter `quota_notification` when calling `update_quota_notification`")  # noqa: E501
        # verify the required parameter 'quota_notification_id' is set
        if ('quota_notification_id' not in params or
                params['quota_notification_id'] is None):
            raise ValueError("Missing the required parameter `quota_notification_id` when calling `update_quota_notification`")  # noqa: E501
        # verify the required parameter 'qid' is set
        if ('qid' not in params or
                params['qid'] is None):
            raise ValueError("Missing the required parameter `qid` when calling `update_quota_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'quota_notification_id' in params:
            path_params['QuotaNotificationId'] = params['quota_notification_id']  # noqa: E501
        if 'qid' in params:
            path_params['Qid'] = params['qid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'quota_notification' in params:
            body_params = params['quota_notification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/quota/quotas/{Qid}/notifications/{QuotaNotificationId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_quota_notifications(self, quota_notifications, qid, **kwargs):  # noqa: E501
        """update_quota_notifications  # noqa: E501

        This method creates an empty set of rules so that the global rules are not used. The input must be an empty JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_quota_notifications(quota_notifications, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty quota_notifications: (required)
        :param str qid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_quota_notifications_with_http_info(quota_notifications, qid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_quota_notifications_with_http_info(quota_notifications, qid, **kwargs)  # noqa: E501
            return data

    def update_quota_notifications_with_http_info(self, quota_notifications, qid, **kwargs):  # noqa: E501
        """update_quota_notifications  # noqa: E501

        This method creates an empty set of rules so that the global rules are not used. The input must be an empty JSON object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_quota_notifications_with_http_info(quota_notifications, qid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty quota_notifications: (required)
        :param str qid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quota_notifications', 'qid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_quota_notifications" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quota_notifications' is set
        if ('quota_notifications' not in params or
                params['quota_notifications'] is None):
            raise ValueError("Missing the required parameter `quota_notifications` when calling `update_quota_notifications`")  # noqa: E501
        # verify the required parameter 'qid' is set
        if ('qid' not in params or
                params['qid'] is None):
            raise ValueError("Missing the required parameter `qid` when calling `update_quota_notifications`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'qid' in params:
            path_params['Qid'] = params['qid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'quota_notifications' in params:
            body_params = params['quota_notifications']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/quota/quotas/{Qid}/notifications', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
