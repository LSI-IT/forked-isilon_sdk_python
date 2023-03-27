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


class IdResolutionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_id_resolution_domain(self, id_resolution_domain_id, **kwargs):  # noqa: E501
        """get_id_resolution_domain  # noqa: E501

        List domain to path mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_domain(id_resolution_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_resolution_domain_id: List domain to path mappings. (required)
        :return: IdResolutionDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_id_resolution_domain_with_http_info(id_resolution_domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_id_resolution_domain_with_http_info(id_resolution_domain_id, **kwargs)  # noqa: E501
            return data

    def get_id_resolution_domain_with_http_info(self, id_resolution_domain_id, **kwargs):  # noqa: E501
        """get_id_resolution_domain  # noqa: E501

        List domain to path mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_domain_with_http_info(id_resolution_domain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_resolution_domain_id: List domain to path mappings. (required)
        :return: IdResolutionDomains
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_resolution_domain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_id_resolution_domain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_resolution_domain_id' is set
        if ('id_resolution_domain_id' not in params or
                params['id_resolution_domain_id'] is None):
            raise ValueError("Missing the required parameter `id_resolution_domain_id` when calling `get_id_resolution_domain`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_resolution_domain_id' in params:
            path_params['IdResolutionDomainId'] = params['id_resolution_domain_id']  # noqa: E501

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
            '/platform/7/id-resolution/domains/{IdResolutionDomainId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResolutionDomains',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_id_resolution_domains(self, **kwargs):  # noqa: E501
        """get_id_resolution_domains  # noqa: E501

        List domain to path mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_domains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dir: The direction of the sort.
        :param str domains: A comma separated list specifying the domains that will be mapped with a path. Only the domains specified in this list will be mapped.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :return: IdResolutionDomainsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_id_resolution_domains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_id_resolution_domains_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_id_resolution_domains_with_http_info(self, **kwargs):  # noqa: E501
        """get_id_resolution_domains  # noqa: E501

        List domain to path mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_domains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dir: The direction of the sort.
        :param str domains: A comma separated list specifying the domains that will be mapped with a path. Only the domains specified in this list will be mapped.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :return: IdResolutionDomainsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dir', 'domains', 'limit', 'resume', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_id_resolution_domains" % key
                )
            params[key] = val
        del params['kwargs']

        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `get_id_resolution_domains`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_id_resolution_domains`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_id_resolution_domains`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_id_resolution_domains`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_id_resolution_domains`, length must be greater than or equal to `0`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `get_id_resolution_domains`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `get_id_resolution_domains`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'domains' in params:
            query_params.append(('domains', params['domains']))  # noqa: E501
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
            '/platform/7/id-resolution/domains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResolutionDomainsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_id_resolution_lin(self, id_resolution_lin_id, **kwargs):  # noqa: E501
        """get_id_resolution_lin  # noqa: E501

        List lin to path mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_lin(id_resolution_lin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id_resolution_lin_id: List lin to path mappings. (required)
        :return: IdResolutionLins
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_id_resolution_lin_with_http_info(id_resolution_lin_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_id_resolution_lin_with_http_info(id_resolution_lin_id, **kwargs)  # noqa: E501
            return data

    def get_id_resolution_lin_with_http_info(self, id_resolution_lin_id, **kwargs):  # noqa: E501
        """get_id_resolution_lin  # noqa: E501

        List lin to path mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_lin_with_http_info(id_resolution_lin_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id_resolution_lin_id: List lin to path mappings. (required)
        :return: IdResolutionLins
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_resolution_lin_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_id_resolution_lin" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_resolution_lin_id' is set
        if ('id_resolution_lin_id' not in params or
                params['id_resolution_lin_id'] is None):
            raise ValueError("Missing the required parameter `id_resolution_lin_id` when calling `get_id_resolution_lin`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_resolution_lin_id' in params:
            path_params['IdResolutionLinId'] = params['id_resolution_lin_id']  # noqa: E501

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
            '/platform/7/id-resolution/lins/{IdResolutionLinId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResolutionLins',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_id_resolution_lins(self, **kwargs):  # noqa: E501
        """get_id_resolution_lins  # noqa: E501

        List lin to path mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_lins(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param str lins: A comma separated list specifying the lins that will be mapped with a path. Only the lins specified in this list will be mapped.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :return: IdResolutionLinsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_id_resolution_lins_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_id_resolution_lins_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_id_resolution_lins_with_http_info(self, **kwargs):  # noqa: E501
        """get_id_resolution_lins  # noqa: E501

        List lin to path mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_lins_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param str lins: A comma separated list specifying the lins that will be mapped with a path. Only the lins specified in this list will be mapped.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :return: IdResolutionLinsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dir', 'limit', 'lins', 'resume', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_id_resolution_lins" % key
                )
            params[key] = val
        del params['kwargs']

        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `get_id_resolution_lins`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_id_resolution_lins`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_id_resolution_lins`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_id_resolution_lins`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_id_resolution_lins`, length must be greater than or equal to `0`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `get_id_resolution_lins`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `get_id_resolution_lins`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'lins' in params:
            query_params.append(('lins', params['lins']))  # noqa: E501
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
            '/platform/7/id-resolution/lins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResolutionLinsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_id_resolution_zone(self, id_resolution_zone_id, **kwargs):  # noqa: E501
        """get_id_resolution_zone  # noqa: E501

        List zone id to zone name mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_zone(id_resolution_zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_resolution_zone_id: List zone id to zone name mappings. (required)
        :return: IdResolutionZones
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_id_resolution_zone_with_http_info(id_resolution_zone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_id_resolution_zone_with_http_info(id_resolution_zone_id, **kwargs)  # noqa: E501
            return data

    def get_id_resolution_zone_with_http_info(self, id_resolution_zone_id, **kwargs):  # noqa: E501
        """get_id_resolution_zone  # noqa: E501

        List zone id to zone name mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_zone_with_http_info(id_resolution_zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_resolution_zone_id: List zone id to zone name mappings. (required)
        :return: IdResolutionZones
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_resolution_zone_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_id_resolution_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_resolution_zone_id' is set
        if ('id_resolution_zone_id' not in params or
                params['id_resolution_zone_id'] is None):
            raise ValueError("Missing the required parameter `id_resolution_zone_id` when calling `get_id_resolution_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_resolution_zone_id' in params:
            path_params['IdResolutionZoneId'] = params['id_resolution_zone_id']  # noqa: E501

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
            '/platform/7/id-resolution/zones/{IdResolutionZoneId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResolutionZones',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_id_resolution_zones(self, **kwargs):  # noqa: E501
        """get_id_resolution_zones  # noqa: E501

        List zone id to zone name mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_zones(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :param str zone_ids: A comma separated list specifying the zone IDs to map with a zone name.
        :return: IdResolutionZonesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_id_resolution_zones_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_id_resolution_zones_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_id_resolution_zones_with_http_info(self, **kwargs):  # noqa: E501
        """get_id_resolution_zones  # noqa: E501

        List zone id to zone name mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_id_resolution_zones_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :param str zone_ids: A comma separated list specifying the zone IDs to map with a zone name.
        :return: IdResolutionZonesExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dir', 'limit', 'resume', 'sort', 'zone_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_id_resolution_zones" % key
                )
            params[key] = val
        del params['kwargs']

        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `get_id_resolution_zones`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_id_resolution_zones`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_id_resolution_zones`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `get_id_resolution_zones`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `get_id_resolution_zones`, length must be greater than or equal to `0`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `get_id_resolution_zones`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `get_id_resolution_zones`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'zone_ids' in params:
            query_params.append(('zone_ids', params['zone_ids']))  # noqa: E501

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
            '/platform/7/id-resolution/zones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResolutionZonesExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
