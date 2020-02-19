# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 9
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_2_2
from isi_sdk_8_2_2.api.zones_api import ZonesApi  # noqa: E501
from isi_sdk_8_2_2.rest import ApiException


class TestZonesApi(unittest.TestCase):
    """ZonesApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_2.api.zones_api.ZonesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_zone(self):
        """Test case for create_zone

        """
        pass

    def test_delete_zone(self):
        """Test case for delete_zone

        """
        pass

    def test_get_zone(self):
        """Test case for get_zone

        """
        pass

    def test_list_zones(self):
        """Test case for list_zones

        """
        pass

    def test_update_zone(self):
        """Test case for update_zone

        """
        pass


if __name__ == '__main__':
    unittest.main()
