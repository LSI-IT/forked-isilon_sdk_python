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
from isi_sdk_8_2_2.api.filesystem_api import FilesystemApi  # noqa: E501
from isi_sdk_8_2_2.rest import ApiException


class TestFilesystemApi(unittest.TestCase):
    """FilesystemApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_2.api.filesystem_api.FilesystemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_settings_access_time(self):
        """Test case for get_settings_access_time

        """
        pass

    def test_get_settings_character_encodings(self):
        """Test case for get_settings_character_encodings

        """
        pass

    def test_get_settings_compression(self):
        """Test case for get_settings_compression

        """
        pass

    def test_update_settings_access_time(self):
        """Test case for update_settings_access_time

        """
        pass

    def test_update_settings_character_encodings(self):
        """Test case for update_settings_character_encodings

        """
        pass

    def test_update_settings_compression(self):
        """Test case for update_settings_compression

        """
        pass


if __name__ == '__main__':
    unittest.main()
