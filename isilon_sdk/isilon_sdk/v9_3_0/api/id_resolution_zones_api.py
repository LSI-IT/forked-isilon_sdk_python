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


class IdResolutionZonesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_zone_group(self, zone_group_id, zid, **kwargs):  # noqa: E501
        """get_zone_group  # noqa: E501

        List a mapping of gid/gsid to groupname.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zone_group(zone_group_id, zid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone_group_id: List a mapping of gid/gsid to groupname. (required)
        :param str zid: (required)
        :return: ZoneGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_zone_group_with_http_info(zone_group_id, zid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_zone_group_with_http_info(zone_group_id, zid, **kwargs)  # noqa: E501
            return data

    def get_zone_group_with_http_info(self, zone_group_id, zid, **kwargs):  # noqa: E501
        """get_zone_group  # noqa: E501

        List a mapping of gid/gsid to groupname.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zone_group_with_http_info(zone_group_id, zid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone_group_id: List a mapping of gid/gsid to groupname. (required)
        :param str zid: (required)
        :return: ZoneGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone_group_id', 'zid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zone_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone_group_id' is set
        if ('zone_group_id' not in params or
                params['zone_group_id'] is None):
            raise ValueError("Missing the required parameter `zone_group_id` when calling `get_zone_group`")  # noqa: E501
        # verify the required parameter 'zid' is set
        if ('zid' not in params or
                params['zid'] is None):
            raise ValueError("Missing the required parameter `zid` when calling `get_zone_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_group_id' in params:
            path_params['ZoneGroupId'] = params['zone_group_id']  # noqa: E501
        if 'zid' in params:
            path_params['Zid'] = params['zid']  # noqa: E501

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
            '/platform/7/id-resolution/zones/{Zid}/groups/{ZoneGroupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZoneGroups',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_zone_groups(self, zid, **kwargs):  # noqa: E501
        """get_zone_groups  # noqa: E501

        List gid/gsid to groupname mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zone_groups(zid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zid: (required)
        :param str dir: The direction of the sort.
        :param str gids: A comma separated list specifying the gids to map with a groupname.
        :param str gsids: A comma separated list specifying the gsids to map with a groupname.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :return: ZoneGroupsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_zone_groups_with_http_info(zid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_zone_groups_with_http_info(zid, **kwargs)  # noqa: E501
            return data

    def get_zone_groups_with_http_info(self, zid, **kwargs):  # noqa: E501
        """get_zone_groups  # noqa: E501

        List gid/gsid to groupname mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zone_groups_with_http_info(zid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zid: (required)
        :param str dir: The direction of the sort.
        :param str gids: A comma separated list specifying the gids to map with a groupname.
        :param str gsids: A comma separated list specifying the gsids to map with a groupname.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :return: ZoneGroupsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zid', 'dir', 'gids', 'gsids', 'limit', 'resume', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zone_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zid' is set
        if ('zid' not in params or
                params['zid'] is None):
            raise ValueError("Missing the required parameter `zid` when calling `get_zone_groups`")  # noqa: E501

        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `get_zone_groups`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_zone_groups`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_zone_groups`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_zone_groups`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_zone_groups`, length must be greater than or equal to `0`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `get_zone_groups`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `get_zone_groups`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'zid' in params:
            path_params['Zid'] = params['zid']  # noqa: E501

        query_params = []
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'gids' in params:
            query_params.append(('gids', params['gids']))  # noqa: E501
        if 'gsids' in params:
            query_params.append(('gsids', params['gsids']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

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
            '/platform/7/id-resolution/zones/{Zid}/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZoneGroupsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_zone_user(self, zone_user_id, zid, **kwargs):  # noqa: E501
        """get_zone_user  # noqa: E501

        List a mapping of uid/sid to username.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zone_user(zone_user_id, zid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone_user_id: List a mapping of uid/sid to username. (required)
        :param str zid: (required)
        :return: ZoneUsers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_zone_user_with_http_info(zone_user_id, zid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_zone_user_with_http_info(zone_user_id, zid, **kwargs)  # noqa: E501
            return data

    def get_zone_user_with_http_info(self, zone_user_id, zid, **kwargs):  # noqa: E501
        """get_zone_user  # noqa: E501

        List a mapping of uid/sid to username.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zone_user_with_http_info(zone_user_id, zid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone_user_id: List a mapping of uid/sid to username. (required)
        :param str zid: (required)
        :return: ZoneUsers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone_user_id', 'zid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zone_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone_user_id' is set
        if ('zone_user_id' not in params or
                params['zone_user_id'] is None):
            raise ValueError("Missing the required parameter `zone_user_id` when calling `get_zone_user`")  # noqa: E501
        # verify the required parameter 'zid' is set
        if ('zid' not in params or
                params['zid'] is None):
            raise ValueError("Missing the required parameter `zid` when calling `get_zone_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_user_id' in params:
            path_params['ZoneUserId'] = params['zone_user_id']  # noqa: E501
        if 'zid' in params:
            path_params['Zid'] = params['zid']  # noqa: E501

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
            '/platform/7/id-resolution/zones/{Zid}/users/{ZoneUserId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZoneUsers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_zone_users(self, zid, **kwargs):  # noqa: E501
        """get_zone_users  # noqa: E501

        List uid/sid to username mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zone_users(zid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zid: (required)
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sids: A comma separated list specifying the sids to map with a username.
        :param str sort: The field that will be used for sorting.
        :param str uids: A comma separated list specifying the uids to map with a username.
        :return: ZoneUsersExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_zone_users_with_http_info(zid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_zone_users_with_http_info(zid, **kwargs)  # noqa: E501
            return data

    def get_zone_users_with_http_info(self, zid, **kwargs):  # noqa: E501
        """get_zone_users  # noqa: E501

        List uid/sid to username mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zone_users_with_http_info(zid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zid: (required)
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sids: A comma separated list specifying the sids to map with a username.
        :param str sort: The field that will be used for sorting.
        :param str uids: A comma separated list specifying the uids to map with a username.
        :return: ZoneUsersExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zid', 'dir', 'limit', 'resume', 'sids', 'sort', 'uids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zone_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zid' is set
        if ('zid' not in params or
                params['zid'] is None):
            raise ValueError("Missing the required parameter `zid` when calling `get_zone_users`")  # noqa: E501

        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `get_zone_users`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_zone_users`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_zone_users`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_zone_users`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_zone_users`, length must be greater than or equal to `0`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `get_zone_users`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `get_zone_users`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'zid' in params:
            path_params['Zid'] = params['zid']  # noqa: E501

        query_params = []
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'sids' in params:
            query_params.append(('sids', params['sids']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'uids' in params:
            query_params.append(('uids', params['uids']))  # noqa: E501

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
            '/platform/7/id-resolution/zones/{Zid}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ZoneUsersExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
