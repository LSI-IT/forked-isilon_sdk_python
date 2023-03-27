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


class FilesystemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_settings_access_time(self, **kwargs):  # noqa: E501
        """get_settings_access_time  # noqa: E501

        Retrieve settings for access time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_access_time(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SettingsAccessTime
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_settings_access_time_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_settings_access_time_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_settings_access_time_with_http_info(self, **kwargs):  # noqa: E501
        """get_settings_access_time  # noqa: E501

        Retrieve settings for access time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_access_time_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SettingsAccessTime
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
                    " to method get_settings_access_time" % key
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
            '/platform/1/filesystem/settings/access-time', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingsAccessTime',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_settings_character_encodings(self, **kwargs):  # noqa: E501
        """get_settings_character_encodings  # noqa: E501

        Retrieve current cluster character encoding settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_character_encodings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SettingsCharacterEncodings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_settings_character_encodings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_settings_character_encodings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_settings_character_encodings_with_http_info(self, **kwargs):  # noqa: E501
        """get_settings_character_encodings  # noqa: E501

        Retrieve current cluster character encoding settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_character_encodings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SettingsCharacterEncodings
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
                    " to method get_settings_character_encodings" % key
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
            '/platform/7/filesystem/settings/character-encodings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingsCharacterEncodings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_settings_compression(self, **kwargs):  # noqa: E501
        """get_settings_compression  # noqa: E501

        Retrieve settings for filesystem compression.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_compression(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SettingsCompression
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_settings_compression_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_settings_compression_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_settings_compression_with_http_info(self, **kwargs):  # noqa: E501
        """get_settings_compression  # noqa: E501

        Retrieve settings for filesystem compression.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_compression_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SettingsCompression
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
                    " to method get_settings_compression" % key
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
            '/platform/6/filesystem/settings/compression', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingsCompression',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_settings_access_time(self, settings_access_time, **kwargs):  # noqa: E501
        """update_settings_access_time  # noqa: E501

        Set settings for access time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_access_time(settings_access_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsAccessTimeExtended settings_access_time: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_settings_access_time_with_http_info(settings_access_time, **kwargs)  # noqa: E501
        else:
            (data) = self.update_settings_access_time_with_http_info(settings_access_time, **kwargs)  # noqa: E501
            return data

    def update_settings_access_time_with_http_info(self, settings_access_time, **kwargs):  # noqa: E501
        """update_settings_access_time  # noqa: E501

        Set settings for access time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_access_time_with_http_info(settings_access_time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsAccessTimeExtended settings_access_time: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_access_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_settings_access_time" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_access_time' is set
        if ('settings_access_time' not in params or
                params['settings_access_time'] is None):
            raise ValueError("Missing the required parameter `settings_access_time` when calling `update_settings_access_time`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_access_time' in params:
            body_params = params['settings_access_time']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/filesystem/settings/access-time', 'PUT',
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

    def update_settings_character_encodings(self, settings_character_encodings, **kwargs):  # noqa: E501
        """update_settings_character_encodings  # noqa: E501

        Set current character encoding.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_character_encodings(settings_character_encodings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsCharacterEncodingsExtended settings_character_encodings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_settings_character_encodings_with_http_info(settings_character_encodings, **kwargs)  # noqa: E501
        else:
            (data) = self.update_settings_character_encodings_with_http_info(settings_character_encodings, **kwargs)  # noqa: E501
            return data

    def update_settings_character_encodings_with_http_info(self, settings_character_encodings, **kwargs):  # noqa: E501
        """update_settings_character_encodings  # noqa: E501

        Set current character encoding.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_character_encodings_with_http_info(settings_character_encodings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsCharacterEncodingsExtended settings_character_encodings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_character_encodings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_settings_character_encodings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_character_encodings' is set
        if ('settings_character_encodings' not in params or
                params['settings_character_encodings'] is None):
            raise ValueError("Missing the required parameter `settings_character_encodings` when calling `update_settings_character_encodings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_character_encodings' in params:
            body_params = params['settings_character_encodings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/filesystem/settings/character-encodings', 'PUT',
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

    def update_settings_compression(self, settings_compression, **kwargs):  # noqa: E501
        """update_settings_compression  # noqa: E501

        Set settings for filesystem compression.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_compression(settings_compression, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsCompressionExtended settings_compression: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_settings_compression_with_http_info(settings_compression, **kwargs)  # noqa: E501
        else:
            (data) = self.update_settings_compression_with_http_info(settings_compression, **kwargs)  # noqa: E501
            return data

    def update_settings_compression_with_http_info(self, settings_compression, **kwargs):  # noqa: E501
        """update_settings_compression  # noqa: E501

        Set settings for filesystem compression.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_compression_with_http_info(settings_compression, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsCompressionExtended settings_compression: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['settings_compression']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_settings_compression" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'settings_compression' is set
        if ('settings_compression' not in params or
                params['settings_compression'] is None):
            raise ValueError("Missing the required parameter `settings_compression` when calling `update_settings_compression`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'settings_compression' in params:
            body_params = params['settings_compression']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/6/filesystem/settings/compression', 'PUT',
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
