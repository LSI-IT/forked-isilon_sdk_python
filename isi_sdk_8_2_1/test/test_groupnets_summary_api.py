# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_2_1
from isi_sdk_8_2_1.api.groupnets_summary_api import GroupnetsSummaryApi  # noqa: E501
from isi_sdk_8_2_1.rest import ApiException


class TestGroupnetsSummaryApi(unittest.TestCase):
    """GroupnetsSummaryApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_1.api.groupnets_summary_api.GroupnetsSummaryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_groupnets_summary(self):
        """Test case for get_groupnets_summary

        """
        pass


if __name__ == '__main__':
    unittest.main()