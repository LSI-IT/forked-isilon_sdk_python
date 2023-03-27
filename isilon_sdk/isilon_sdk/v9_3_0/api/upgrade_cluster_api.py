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


class UpgradeClusterApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_nodes_node_patch_sync_item(self, nodes_node_patch_sync_item, lnn, **kwargs):  # noqa: E501
        """create_nodes_node_patch_sync_item  # noqa: E501

        Retry any pending patch sync operations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_nodes_node_patch_sync_item(nodes_node_patch_sync_item, lnn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty nodes_node_patch_sync_item: (required)
        :param int lnn: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_nodes_node_patch_sync_item_with_http_info(nodes_node_patch_sync_item, lnn, **kwargs)  # noqa: E501
        else:
            (data) = self.create_nodes_node_patch_sync_item_with_http_info(nodes_node_patch_sync_item, lnn, **kwargs)  # noqa: E501
            return data

    def create_nodes_node_patch_sync_item_with_http_info(self, nodes_node_patch_sync_item, lnn, **kwargs):  # noqa: E501
        """create_nodes_node_patch_sync_item  # noqa: E501

        Retry any pending patch sync operations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_nodes_node_patch_sync_item_with_http_info(nodes_node_patch_sync_item, lnn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty nodes_node_patch_sync_item: (required)
        :param int lnn: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['nodes_node_patch_sync_item', 'lnn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_nodes_node_patch_sync_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'nodes_node_patch_sync_item' is set
        if ('nodes_node_patch_sync_item' not in params or
                params['nodes_node_patch_sync_item'] is None):
            raise ValueError("Missing the required parameter `nodes_node_patch_sync_item` when calling `create_nodes_node_patch_sync_item`")  # noqa: E501
        # verify the required parameter 'lnn' is set
        if ('lnn' not in params or
                params['lnn'] is None):
            raise ValueError("Missing the required parameter `lnn` when calling `create_nodes_node_patch_sync_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lnn' in params:
            path_params['Lnn'] = params['lnn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nodes_node_patch_sync_item' in params:
            body_params = params['nodes_node_patch_sync_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/4/upgrade/cluster/nodes/{Lnn}/patch/sync', 'POST',
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

    def get_nodes_node_firmware_device(self, lnn, **kwargs):  # noqa: E501
        """get_nodes_node_firmware_device  # noqa: E501

        The firmware status for the node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_node_firmware_device(lnn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int lnn: (required)
        :param bool devices: Show devices. If false, this returns an empty list. Default is false.
        :return: NodesNodeFirmwareDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nodes_node_firmware_device_with_http_info(lnn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_nodes_node_firmware_device_with_http_info(lnn, **kwargs)  # noqa: E501
            return data

    def get_nodes_node_firmware_device_with_http_info(self, lnn, **kwargs):  # noqa: E501
        """get_nodes_node_firmware_device  # noqa: E501

        The firmware status for the node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_node_firmware_device_with_http_info(lnn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int lnn: (required)
        :param bool devices: Show devices. If false, this returns an empty list. Default is false.
        :return: NodesNodeFirmwareDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lnn', 'devices']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nodes_node_firmware_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lnn' is set
        if ('lnn' not in params or
                params['lnn'] is None):
            raise ValueError("Missing the required parameter `lnn` when calling `get_nodes_node_firmware_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lnn' in params:
            path_params['Lnn'] = params['lnn']  # noqa: E501

        query_params = []
        if 'devices' in params:
            query_params.append(('devices', params['devices']))  # noqa: E501

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
            '/platform/10/upgrade/cluster/nodes/{Lnn}/firmware/device', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodesNodeFirmwareDevice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_nodes_node_firmware_status(self, lnn, **kwargs):  # noqa: E501
        """get_nodes_node_firmware_status  # noqa: E501

        The firmware status for the node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_node_firmware_status(lnn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int lnn: (required)
        :param bool devices: Show devices. If false, this returns an empty list. Default is false.
        :return: NodesNodeFirmwareDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_nodes_node_firmware_status_with_http_info(lnn, **kwargs)  # noqa: E501
        else:
            (data) = self.get_nodes_node_firmware_status_with_http_info(lnn, **kwargs)  # noqa: E501
            return data

    def get_nodes_node_firmware_status_with_http_info(self, lnn, **kwargs):  # noqa: E501
        """get_nodes_node_firmware_status  # noqa: E501

        The firmware status for the node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nodes_node_firmware_status_with_http_info(lnn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int lnn: (required)
        :param bool devices: Show devices. If false, this returns an empty list. Default is false.
        :return: NodesNodeFirmwareDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lnn', 'devices']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nodes_node_firmware_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lnn' is set
        if ('lnn' not in params or
                params['lnn'] is None):
            raise ValueError("Missing the required parameter `lnn` when calling `get_nodes_node_firmware_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lnn' in params:
            path_params['Lnn'] = params['lnn']  # noqa: E501

        query_params = []
        if 'devices' in params:
            query_params.append(('devices', params['devices']))  # noqa: E501

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
            '/platform/10/upgrade/cluster/nodes/{Lnn}/firmware/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodesNodeFirmwareDevice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
