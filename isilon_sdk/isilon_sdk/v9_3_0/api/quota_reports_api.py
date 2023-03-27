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


class QuotaReportsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_report_about(self, rid, **kwargs):  # noqa: E501
        """get_report_about  # noqa: E501

        Retrieve report meta-data information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_about(rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rid: (required)
        :return: ReportAbout
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_report_about_with_http_info(rid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_report_about_with_http_info(rid, **kwargs)  # noqa: E501
            return data

    def get_report_about_with_http_info(self, rid, **kwargs):  # noqa: E501
        """get_report_about  # noqa: E501

        Retrieve report meta-data information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_report_about_with_http_info(rid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str rid: (required)
        :return: ReportAbout
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_about" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'rid' is set
        if ('rid' not in params or
                params['rid'] is None):
            raise ValueError("Missing the required parameter `rid` when calling `get_report_about`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rid' in params:
            path_params['Rid'] = params['rid']  # noqa: E501

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
            '/platform/1/quota/reports/{Rid}/about', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportAbout',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
