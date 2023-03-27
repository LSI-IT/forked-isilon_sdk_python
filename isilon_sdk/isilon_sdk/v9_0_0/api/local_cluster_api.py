# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isilon_sdk.v9_0_0.api_client import ApiClient


class LocalClusterApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_nodes_node_internal_ip_address(self, lnn, **kwargs):  # noqa: E501
        """get_nodes_node_internal_ip_address  # noqa: E501

        View internal ip address with respect to node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_node_internal_ip_address(lnn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int lnn: (required)
        :return: NodesNodeInternalIpAddress
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nodes_node_internal_ip_address_with_http_info(lnn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_nodes_node_internal_ip_address_with_http_info(lnn, **kwargs)  # noqa: E501
            return data

    def get_nodes_node_internal_ip_address_with_http_info(self, lnn, **kwargs):  # noqa: E501
        """get_nodes_node_internal_ip_address  # noqa: E501

        View internal ip address with respect to node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_node_internal_ip_address_with_http_info(lnn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int lnn: (required)
        :return: NodesNodeInternalIpAddress
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lnn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nodes_node_internal_ip_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lnn' is set
        if ('lnn' not in params or
                params['lnn'] is None):
            raise ValueError("Missing the required parameter `lnn` when calling `get_nodes_node_internal_ip_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lnn' in params:
            path_params['Lnn'] = params['lnn']  # noqa: E501

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
            '/platform/7/local/cluster/nodes/{Lnn}/internal-ip-address', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodesNodeInternalIpAddress',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)