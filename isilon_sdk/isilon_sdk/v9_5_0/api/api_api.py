# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 16
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isilon_sdk.v9_5_0.api_client import ApiClient


class ApiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_sessions_invalidation(self, sessions_invalidation, **kwargs):  # noqa: E501
        """create_sessions_invalidation  # noqa: E501

        Create a new Platform API session invalidation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sessions_invalidation(sessions_invalidation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SessionsInvalidationCreateParams sessions_invalidation: (required)
        :param str zone: The zone to create the invalidation in.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_sessions_invalidation_with_http_info(sessions_invalidation, **kwargs)  # noqa: E501
        else:
            (data) = self.create_sessions_invalidation_with_http_info(sessions_invalidation, **kwargs)  # noqa: E501
            return data

    def create_sessions_invalidation_with_http_info(self, sessions_invalidation, **kwargs):  # noqa: E501
        """create_sessions_invalidation  # noqa: E501

        Create a new Platform API session invalidation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sessions_invalidation_with_http_info(sessions_invalidation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SessionsInvalidationCreateParams sessions_invalidation: (required)
        :param str zone: The zone to create the invalidation in.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sessions_invalidation', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_sessions_invalidation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sessions_invalidation' is set
        if ('sessions_invalidation' not in params or
                params['sessions_invalidation'] is None):
            raise ValueError("Missing the required parameter `sessions_invalidation` when calling `create_sessions_invalidation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sessions_invalidation' in params:
            body_params = params['sessions_invalidation']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/14/api/sessions/invalidations', 'POST',
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

    def create_sessions_rekey_item(self, sessions_rekey_item, **kwargs):  # noqa: E501
        """create_sessions_rekey_item  # noqa: E501

        Delete all existing session API signing keys and create a new signing key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sessions_rekey_item(sessions_rekey_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty sessions_rekey_item: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_sessions_rekey_item_with_http_info(sessions_rekey_item, **kwargs)  # noqa: E501
        else:
            (data) = self.create_sessions_rekey_item_with_http_info(sessions_rekey_item, **kwargs)  # noqa: E501
            return data

    def create_sessions_rekey_item_with_http_info(self, sessions_rekey_item, **kwargs):  # noqa: E501
        """create_sessions_rekey_item  # noqa: E501

        Delete all existing session API signing keys and create a new signing key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_sessions_rekey_item_with_http_info(sessions_rekey_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty sessions_rekey_item: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sessions_rekey_item']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_sessions_rekey_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sessions_rekey_item' is set
        if ('sessions_rekey_item' not in params or
                params['sessions_rekey_item'] is None):
            raise ValueError("Missing the required parameter `sessions_rekey_item` when calling `create_sessions_rekey_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sessions_rekey_item' in params:
            body_params = params['sessions_rekey_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/14/api/sessions/rekey', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_sessions_invalidation(self, sessions_invalidation_id, **kwargs):  # noqa: E501
        """delete_sessions_invalidation  # noqa: E501

        Delete a user's Platform API session invalidation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sessions_invalidation(sessions_invalidation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sessions_invalidation_id: Delete a user's Platform API session invalidation. (required)
        :param str zone: The zone to delete an invalidation from.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sessions_invalidation_with_http_info(sessions_invalidation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_sessions_invalidation_with_http_info(sessions_invalidation_id, **kwargs)  # noqa: E501
            return data

    def delete_sessions_invalidation_with_http_info(self, sessions_invalidation_id, **kwargs):  # noqa: E501
        """delete_sessions_invalidation  # noqa: E501

        Delete a user's Platform API session invalidation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sessions_invalidation_with_http_info(sessions_invalidation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sessions_invalidation_id: Delete a user's Platform API session invalidation. (required)
        :param str zone: The zone to delete an invalidation from.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sessions_invalidation_id', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sessions_invalidation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sessions_invalidation_id' is set
        if ('sessions_invalidation_id' not in params or
                params['sessions_invalidation_id'] is None):
            raise ValueError("Missing the required parameter `sessions_invalidation_id` when calling `delete_sessions_invalidation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sessions_invalidation_id' in params:
            path_params['SessionsInvalidationId'] = params['sessions_invalidation_id']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

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
            '/platform/14/api/sessions/invalidations/{SessionsInvalidationId}', 'DELETE',
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

    def get_sessions_invalidation(self, sessions_invalidation_id, **kwargs):  # noqa: E501
        """get_sessions_invalidation  # noqa: E501

        Get user Platform API session invalidation information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sessions_invalidation(sessions_invalidation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sessions_invalidation_id: Get user Platform API session invalidation information. (required)
        :param str zone: The zone to get the invalidation from.
        :return: SessionsInvalidations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sessions_invalidation_with_http_info(sessions_invalidation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sessions_invalidation_with_http_info(sessions_invalidation_id, **kwargs)  # noqa: E501
            return data

    def get_sessions_invalidation_with_http_info(self, sessions_invalidation_id, **kwargs):  # noqa: E501
        """get_sessions_invalidation  # noqa: E501

        Get user Platform API session invalidation information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sessions_invalidation_with_http_info(sessions_invalidation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sessions_invalidation_id: Get user Platform API session invalidation information. (required)
        :param str zone: The zone to get the invalidation from.
        :return: SessionsInvalidations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sessions_invalidation_id', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sessions_invalidation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sessions_invalidation_id' is set
        if ('sessions_invalidation_id' not in params or
                params['sessions_invalidation_id'] is None):
            raise ValueError("Missing the required parameter `sessions_invalidation_id` when calling `get_sessions_invalidation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sessions_invalidation_id' in params:
            path_params['SessionsInvalidationId'] = params['sessions_invalidation_id']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

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
            '/platform/14/api/sessions/invalidations/{SessionsInvalidationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SessionsInvalidations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_settings_sessions(self, **kwargs):  # noqa: E501
        """get_settings_sessions  # noqa: E501

        Retrieve the HTTP API session settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_sessions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SettingsSessions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_settings_sessions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_settings_sessions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_settings_sessions_with_http_info(self, **kwargs):  # noqa: E501
        """get_settings_sessions  # noqa: E501

        Retrieve the HTTP API session settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_sessions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SettingsSessions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_settings_sessions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/platform/16/api/settings/sessions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingsSessions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_sessions_invalidations(self, **kwargs):  # noqa: E501
        """list_sessions_invalidations  # noqa: E501

        Get Platform API session invalidations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_sessions_invalidations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone: The zone to get invalidations from.
        :return: SessionsInvalidations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_sessions_invalidations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_sessions_invalidations_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_sessions_invalidations_with_http_info(self, **kwargs):  # noqa: E501
        """list_sessions_invalidations  # noqa: E501

        Get Platform API session invalidations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_sessions_invalidations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone: The zone to get invalidations from.
        :return: SessionsInvalidations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_sessions_invalidations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

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
            '/platform/14/api/sessions/invalidations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SessionsInvalidations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_sessions_invalidation(self, sessions_invalidation, sessions_invalidation_id, **kwargs):  # noqa: E501
        """update_sessions_invalidation  # noqa: E501

        Modify a user's Platform API session invalidation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sessions_invalidation(sessions_invalidation, sessions_invalidation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SessionsInvalidation sessions_invalidation: (required)
        :param str sessions_invalidation_id: Modify a user's Platform API session invalidation. (required)
        :param str zone: The zone to modify an invalidation in.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_sessions_invalidation_with_http_info(sessions_invalidation, sessions_invalidation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_sessions_invalidation_with_http_info(sessions_invalidation, sessions_invalidation_id, **kwargs)  # noqa: E501
            return data

    def update_sessions_invalidation_with_http_info(self, sessions_invalidation, sessions_invalidation_id, **kwargs):  # noqa: E501
        """update_sessions_invalidation  # noqa: E501

        Modify a user's Platform API session invalidation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sessions_invalidation_with_http_info(sessions_invalidation, sessions_invalidation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SessionsInvalidation sessions_invalidation: (required)
        :param str sessions_invalidation_id: Modify a user's Platform API session invalidation. (required)
        :param str zone: The zone to modify an invalidation in.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sessions_invalidation', 'sessions_invalidation_id', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_sessions_invalidation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sessions_invalidation' is set
        if ('sessions_invalidation' not in params or
                params['sessions_invalidation'] is None):
            raise ValueError("Missing the required parameter `sessions_invalidation` when calling `update_sessions_invalidation`")  # noqa: E501
        # verify the required parameter 'sessions_invalidation_id' is set
        if ('sessions_invalidation_id' not in params or
                params['sessions_invalidation_id'] is None):
            raise ValueError("Missing the required parameter `sessions_invalidation_id` when calling `update_sessions_invalidation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sessions_invalidation_id' in params:
            path_params['SessionsInvalidationId'] = params['sessions_invalidation_id']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sessions_invalidation' in params:
            body_params = params['sessions_invalidation']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/14/api/sessions/invalidations/{SessionsInvalidationId}', 'PUT',
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

    def update_settings_sessions(self, settings_sessions, **kwargs):  # noqa: E501
        """update_settings_sessions  # noqa: E501

        Modify the HTTP API session settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_sessions(settings_sessions, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsSessionsExtended settings_sessions: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_settings_sessions_with_http_info(settings_sessions, **kwargs)  # noqa: E501
        else:
            (data) = self.update_settings_sessions_with_http_info(settings_sessions, **kwargs)  # noqa: E501
            return data

    def update_settings_sessions_with_http_info(self, settings_sessions, **kwargs):  # noqa: E501
        """update_settings_sessions  # noqa: E501

        Modify the HTTP API session settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_sessions_with_http_info(settings_sessions, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsSessionsExtended settings_sessions: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_sessions']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_settings_sessions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_sessions' is set
        if ('settings_sessions' not in params or
                params['settings_sessions'] is None):
            raise ValueError("Missing the required parameter `settings_sessions` when calling `update_settings_sessions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_sessions' in params:
            body_params = params['settings_sessions']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/16/api/settings/sessions', 'PUT',
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
