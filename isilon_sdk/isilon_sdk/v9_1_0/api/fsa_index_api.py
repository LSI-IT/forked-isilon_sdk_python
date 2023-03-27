# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isilon_sdk.v9_1_0.api_client import ApiClient


class FsaIndexApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_name_lin(self, name_lin_id, name, **kwargs):  # noqa: E501
        """get_name_lin  # noqa: E501

        Get a single index entry from the index table.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_name_lin(name_lin_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int name_lin_id: Get a single index entry from the index table. (required)
        :param str name: (required)
        :param bool path: Resolve the path for an index entry. This query argument is invalid if an initial index job is in progress or incomplete or if an incremental index job is in progress or incomplete.
        :return: NameLins
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_name_lin_with_http_info(name_lin_id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_name_lin_with_http_info(name_lin_id, name, **kwargs)  # noqa: E501
            return data

    def get_name_lin_with_http_info(self, name_lin_id, name, **kwargs):  # noqa: E501
        """get_name_lin  # noqa: E501

        Get a single index entry from the index table.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_name_lin_with_http_info(name_lin_id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int name_lin_id: Get a single index entry from the index table. (required)
        :param str name: (required)
        :param bool path: Resolve the path for an index entry. This query argument is invalid if an initial index job is in progress or incomplete or if an incremental index job is in progress or incomplete.
        :return: NameLins
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name_lin_id', 'name', 'path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_name_lin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name_lin_id' is set
        if ('name_lin_id' not in params or
                params['name_lin_id'] is None):
            raise ValueError("Missing the required parameter `name_lin_id` when calling `get_name_lin`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_name_lin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name_lin_id' in params:
            path_params['NameLinId'] = params['name_lin_id']  # noqa: E501
        if 'name' in params:
            path_params['Name'] = params['name']  # noqa: E501

        query_params = []
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501

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
            '/platform/8/fsa/index/{Name}/lins/{NameLinId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NameLins',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_name_lins(self, name, **kwargs):  # noqa: E501
        """get_name_lins  # noqa: E501

        Get index entries from the given index table.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_name_lins(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param int limit: Return no more than this many results at once (see resume).
        :param list[int] lin: LIN of file or directory to lookup. Accepts multiple query arguments.
        :param bool path: Resolve the path for an index entry. This query argument is invalid if an initial index job is in progress or incomplete or if an incremental index job is in progress or incomplete.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: NameLinsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_name_lins_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_name_lins_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_name_lins_with_http_info(self, name, **kwargs):  # noqa: E501
        """get_name_lins  # noqa: E501

        Get index entries from the given index table.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_name_lins_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param int limit: Return no more than this many results at once (see resume).
        :param list[int] lin: LIN of file or directory to lookup. Accepts multiple query arguments.
        :param bool path: Resolve the path for an index entry. This query argument is invalid if an initial index job is in progress or incomplete or if an incremental index job is in progress or incomplete.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: NameLinsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'limit', 'lin', 'path', 'resume']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_name_lins" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_name_lins`")  # noqa: E501

        if 'limit' in params and params['limit'] > 100000:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_name_lins`, must be a value less than or equal to `100000`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_name_lins`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_name_lins`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_name_lins`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['Name'] = params['name']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'lin' in params:
            query_params.append(('lin', params['lin']))  # noqa: E501
            collection_formats['lin'] = 'csv'  # noqa: E501
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501

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
            '/platform/8/fsa/index/{Name}/lins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NameLinsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
