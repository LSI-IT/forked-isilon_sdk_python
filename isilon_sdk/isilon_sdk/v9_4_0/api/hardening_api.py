# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isilon_sdk.v9_4_0.api_client import ApiClient


class HardeningApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_hardening_apply_item(self, hardening_apply_item, **kwargs):  # noqa: E501
        """create_hardening_apply_item  # noqa: E501

        Apply hardening on the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_hardening_apply_item(hardening_apply_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HardeningApplyItem hardening_apply_item: (required)
        :return: CreateHardeningApplyItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_hardening_apply_item_with_http_info(hardening_apply_item, **kwargs)  # noqa: E501
        else:
            (data) = self.create_hardening_apply_item_with_http_info(hardening_apply_item, **kwargs)  # noqa: E501
            return data

    def create_hardening_apply_item_with_http_info(self, hardening_apply_item, **kwargs):  # noqa: E501
        """create_hardening_apply_item  # noqa: E501

        Apply hardening on the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_hardening_apply_item_with_http_info(hardening_apply_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HardeningApplyItem hardening_apply_item: (required)
        :return: CreateHardeningApplyItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardening_apply_item']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hardening_apply_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardening_apply_item' is set
        if ('hardening_apply_item' not in params or
                params['hardening_apply_item'] is None):
            raise ValueError("Missing the required parameter `hardening_apply_item` when calling `create_hardening_apply_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardening_apply_item' in params:
            body_params = params['hardening_apply_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardening/apply', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateHardeningApplyItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_hardening_resolve_item(self, hardening_resolve_item, **kwargs):  # noqa: E501
        """create_hardening_resolve_item  # noqa: E501

        Resolve issues related to hardening, found in current cluster configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_hardening_resolve_item(hardening_resolve_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HardeningResolveItem hardening_resolve_item: (required)
        :param bool accept: If true, execution proceeds to resolve all issues. If false, execution aborts. This is a required argument.
        :return: CreateHardeningResolveItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_hardening_resolve_item_with_http_info(hardening_resolve_item, **kwargs)  # noqa: E501
        else:
            (data) = self.create_hardening_resolve_item_with_http_info(hardening_resolve_item, **kwargs)  # noqa: E501
            return data

    def create_hardening_resolve_item_with_http_info(self, hardening_resolve_item, **kwargs):  # noqa: E501
        """create_hardening_resolve_item  # noqa: E501

        Resolve issues related to hardening, found in current cluster configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_hardening_resolve_item_with_http_info(hardening_resolve_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HardeningResolveItem hardening_resolve_item: (required)
        :param bool accept: If true, execution proceeds to resolve all issues. If false, execution aborts. This is a required argument.
        :return: CreateHardeningResolveItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardening_resolve_item', 'accept']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hardening_resolve_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardening_resolve_item' is set
        if ('hardening_resolve_item' not in params or
                params['hardening_resolve_item'] is None):
            raise ValueError("Missing the required parameter `hardening_resolve_item` when calling `create_hardening_resolve_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardening_resolve_item' in params:
            body_params = params['hardening_resolve_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardening/resolve', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateHardeningResolveItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_hardening_revert_item(self, hardening_revert_item, **kwargs):  # noqa: E501
        """create_hardening_revert_item  # noqa: E501

        Revert hardening on the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_hardening_revert_item(hardening_revert_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty hardening_revert_item: (required)
        :param bool force: If specified, revert operation continues even in case of a failure. Default is false in which case revert stops at the first failure.
        :return: CreateHardeningRevertItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_hardening_revert_item_with_http_info(hardening_revert_item, **kwargs)  # noqa: E501
        else:
            (data) = self.create_hardening_revert_item_with_http_info(hardening_revert_item, **kwargs)  # noqa: E501
            return data

    def create_hardening_revert_item_with_http_info(self, hardening_revert_item, **kwargs):  # noqa: E501
        """create_hardening_revert_item  # noqa: E501

        Revert hardening on the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_hardening_revert_item_with_http_info(hardening_revert_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty hardening_revert_item: (required)
        :param bool force: If specified, revert operation continues even in case of a failure. Default is false in which case revert stops at the first failure.
        :return: CreateHardeningRevertItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardening_revert_item', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hardening_revert_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardening_revert_item' is set
        if ('hardening_revert_item' not in params or
                params['hardening_revert_item'] is None):
            raise ValueError("Missing the required parameter `hardening_revert_item` when calling `create_hardening_revert_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardening_revert_item' in params:
            body_params = params['hardening_revert_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/hardening/revert', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateHardeningRevertItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hardening_state(self, **kwargs):  # noqa: E501
        """get_hardening_state  # noqa: E501

        Get the state of the current hardening operation, if one is happening.  Note that this is different from the /status resource, which returns the overall hardening status of the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hardening_state(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HardeningState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_hardening_state_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_hardening_state_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_hardening_state_with_http_info(self, **kwargs):  # noqa: E501
        """get_hardening_state  # noqa: E501

        Get the state of the current hardening operation, if one is happening.  Note that this is different from the /status resource, which returns the overall hardening status of the cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hardening_state_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HardeningState
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
                    " to method get_hardening_state" % key
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
            '/platform/3/hardening/state', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HardeningState',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hardening_status(self, **kwargs):  # noqa: E501
        """get_hardening_status  # noqa: E501

        Get a message indicating whether or not the cluster is hardened. Note that this is different from the /state resource, which returns the state of a specific hardening operation (apply or revert).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hardening_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HardeningStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_hardening_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_hardening_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_hardening_status_with_http_info(self, **kwargs):  # noqa: E501
        """get_hardening_status  # noqa: E501

        Get a message indicating whether or not the cluster is hardened. Note that this is different from the /state resource, which returns the state of a specific hardening operation (apply or revert).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_hardening_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: HardeningStatus
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
                    " to method get_hardening_status" % key
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
            '/platform/3/hardening/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HardeningStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
