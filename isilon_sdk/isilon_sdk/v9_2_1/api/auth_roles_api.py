# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 12
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isilon_sdk.v9_2_1.api_client import ApiClient


class AuthRolesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_role_member(self, role_member, role, **kwargs):  # noqa: E501
        """create_role_member  # noqa: E501

        Add a member to the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_member(role_member, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthAccessAccessItemFileGroup role_member: (required)
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_role_member_with_http_info(role_member, role, **kwargs)  # noqa: E501
        else:
            (data) = self.create_role_member_with_http_info(role_member, role, **kwargs)  # noqa: E501
            return data

    def create_role_member_with_http_info(self, role_member, role, **kwargs):  # noqa: E501
        """create_role_member  # noqa: E501

        Add a member to the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_member_with_http_info(role_member, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthAccessAccessItemFileGroup role_member: (required)
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_member', 'role', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_role_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_member' is set
        if ('role_member' not in params or
                params['role_member'] is None):
            raise ValueError("Missing the required parameter `role_member` when calling `create_role_member`")  # noqa: E501
        # verify the required parameter 'role' is set
        if ('role' not in params or
                params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `create_role_member`")  # noqa: E501

        if ('zone' in params and
                len(params['zone']) > 255):
            raise ValueError("Invalid value for parameter `zone` when calling `create_role_member`, length must be less than or equal to `255`")  # noqa: E501
        if ('zone' in params and
                len(params['zone']) < 0):
            raise ValueError("Invalid value for parameter `zone` when calling `create_role_member`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role' in params:
            path_params['Role'] = params['role']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'role_member' in params:
            body_params = params['role_member']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/8/auth/roles/{Role}/members', 'POST',
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

    def create_role_privilege(self, role_privilege, role, **kwargs):  # noqa: E501
        """create_role_privilege  # noqa: E501

        Add a privilege to the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_privilege(role_privilege, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthIdNtokenPrivilegeItem role_privilege: (required)
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_role_privilege_with_http_info(role_privilege, role, **kwargs)  # noqa: E501
        else:
            (data) = self.create_role_privilege_with_http_info(role_privilege, role, **kwargs)  # noqa: E501
            return data

    def create_role_privilege_with_http_info(self, role_privilege, role, **kwargs):  # noqa: E501
        """create_role_privilege  # noqa: E501

        Add a privilege to the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_role_privilege_with_http_info(role_privilege, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthIdNtokenPrivilegeItem role_privilege: (required)
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_privilege', 'role', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_role_privilege" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_privilege' is set
        if ('role_privilege' not in params or
                params['role_privilege'] is None):
            raise ValueError("Missing the required parameter `role_privilege` when calling `create_role_privilege`")  # noqa: E501
        # verify the required parameter 'role' is set
        if ('role' not in params or
                params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `create_role_privilege`")  # noqa: E501

        if ('zone' in params and
                len(params['zone']) > 255):
            raise ValueError("Invalid value for parameter `zone` when calling `create_role_privilege`, length must be less than or equal to `255`")  # noqa: E501
        if ('zone' in params and
                len(params['zone']) < 0):
            raise ValueError("Invalid value for parameter `zone` when calling `create_role_privilege`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role' in params:
            path_params['Role'] = params['role']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'role_privilege' in params:
            body_params = params['role_privilege']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/7/auth/roles/{Role}/privileges', 'POST',
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

    def delete_role_member(self, role_member_id, role, **kwargs):  # noqa: E501
        """delete_role_member  # noqa: E501

        Remove a member from the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_member(role_member_id, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_member_id: Remove a member from the role. (required)
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_role_member_with_http_info(role_member_id, role, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_role_member_with_http_info(role_member_id, role, **kwargs)  # noqa: E501
            return data

    def delete_role_member_with_http_info(self, role_member_id, role, **kwargs):  # noqa: E501
        """delete_role_member  # noqa: E501

        Remove a member from the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_member_with_http_info(role_member_id, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_member_id: Remove a member from the role. (required)
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_member_id', 'role', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_role_member" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_member_id' is set
        if ('role_member_id' not in params or
                params['role_member_id'] is None):
            raise ValueError("Missing the required parameter `role_member_id` when calling `delete_role_member`")  # noqa: E501
        # verify the required parameter 'role' is set
        if ('role' not in params or
                params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `delete_role_member`")  # noqa: E501

        if ('zone' in params and
                len(params['zone']) > 255):
            raise ValueError("Invalid value for parameter `zone` when calling `delete_role_member`, length must be less than or equal to `255`")  # noqa: E501
        if ('zone' in params and
                len(params['zone']) < 0):
            raise ValueError("Invalid value for parameter `zone` when calling `delete_role_member`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role_member_id' in params:
            path_params['RoleMemberId'] = params['role_member_id']  # noqa: E501
        if 'role' in params:
            path_params['Role'] = params['role']  # noqa: E501

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
            '/platform/8/auth/roles/{Role}/members/{RoleMemberId}', 'DELETE',
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

    def delete_role_privilege(self, role_privilege_id, role, **kwargs):  # noqa: E501
        """delete_role_privilege  # noqa: E501

        Remove a privilege from a role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_privilege(role_privilege_id, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_privilege_id: Remove a privilege from a role. (required)
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_role_privilege_with_http_info(role_privilege_id, role, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_role_privilege_with_http_info(role_privilege_id, role, **kwargs)  # noqa: E501
            return data

    def delete_role_privilege_with_http_info(self, role_privilege_id, role, **kwargs):  # noqa: E501
        """delete_role_privilege  # noqa: E501

        Remove a privilege from a role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_role_privilege_with_http_info(role_privilege_id, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_privilege_id: Remove a privilege from a role. (required)
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_privilege_id', 'role', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_role_privilege" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_privilege_id' is set
        if ('role_privilege_id' not in params or
                params['role_privilege_id'] is None):
            raise ValueError("Missing the required parameter `role_privilege_id` when calling `delete_role_privilege`")  # noqa: E501
        # verify the required parameter 'role' is set
        if ('role' not in params or
                params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `delete_role_privilege`")  # noqa: E501

        if ('zone' in params and
                len(params['zone']) > 255):
            raise ValueError("Invalid value for parameter `zone` when calling `delete_role_privilege`, length must be less than or equal to `255`")  # noqa: E501
        if ('zone' in params and
                len(params['zone']) < 0):
            raise ValueError("Invalid value for parameter `zone` when calling `delete_role_privilege`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role_privilege_id' in params:
            path_params['RolePrivilegeId'] = params['role_privilege_id']  # noqa: E501
        if 'role' in params:
            path_params['Role'] = params['role']  # noqa: E501

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
            '/platform/7/auth/roles/{Role}/privileges/{RolePrivilegeId}', 'DELETE',
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

    def list_role_members(self, role, **kwargs):  # noqa: E501
        """list_role_members  # noqa: E501

        List all the members of the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_members(role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role: (required)
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param bool resolve_names: Resolve names of personas.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :param str zone: Specifies which access zone to use.
        :return: GroupMembers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_role_members_with_http_info(role, **kwargs)  # noqa: E501
        else:
            (data) = self.list_role_members_with_http_info(role, **kwargs)  # noqa: E501
            return data

    def list_role_members_with_http_info(self, role, **kwargs):  # noqa: E501
        """list_role_members  # noqa: E501

        List all the members of the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_members_with_http_info(role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role: (required)
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param bool resolve_names: Resolve names of personas.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :param str zone: Specifies which access zone to use.
        :return: GroupMembers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role', 'dir', 'limit', 'resolve_names', 'resume', 'sort', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_role_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role' is set
        if ('role' not in params or
                params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `list_role_members`")  # noqa: E501

        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `list_role_members`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_role_members`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_role_members`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `list_role_members`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `list_role_members`, length must be greater than or equal to `0`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `list_role_members`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `list_role_members`, length must be greater than or equal to `0`")  # noqa: E501
        if ('zone' in params and
                len(params['zone']) > 255):
            raise ValueError("Invalid value for parameter `zone` when calling `list_role_members`, length must be less than or equal to `255`")  # noqa: E501
        if ('zone' in params and
                len(params['zone']) < 0):
            raise ValueError("Invalid value for parameter `zone` when calling `list_role_members`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role' in params:
            path_params['Role'] = params['role']  # noqa: E501

        query_params = []
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resolve_names' in params:
            query_params.append(('resolve_names', params['resolve_names']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
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
            '/platform/8/auth/roles/{Role}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupMembers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_role_privileges(self, role, **kwargs):  # noqa: E501
        """list_role_privileges  # noqa: E501

        List all privileges in the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_privileges(role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: RolePrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_role_privileges_with_http_info(role, **kwargs)  # noqa: E501
        else:
            (data) = self.list_role_privileges_with_http_info(role, **kwargs)  # noqa: E501
            return data

    def list_role_privileges_with_http_info(self, role, **kwargs):  # noqa: E501
        """list_role_privileges  # noqa: E501

        List all privileges in the role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_privileges_with_http_info(role, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role: (required)
        :param str zone: Specifies which access zone to use.
        :return: RolePrivileges
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_role_privileges" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role' is set
        if ('role' not in params or
                params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `list_role_privileges`")  # noqa: E501

        if ('zone' in params and
                len(params['zone']) > 255):
            raise ValueError("Invalid value for parameter `zone` when calling `list_role_privileges`, length must be less than or equal to `255`")  # noqa: E501
        if ('zone' in params and
                len(params['zone']) < 0):
            raise ValueError("Invalid value for parameter `zone` when calling `list_role_privileges`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role' in params:
            path_params['Role'] = params['role']  # noqa: E501

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
            '/platform/7/auth/roles/{Role}/privileges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RolePrivileges',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
