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
from isi_sdk_8_2_2.api.certificate_api import CertificateApi  # noqa: E501
from isi_sdk_8_2_2.rest import ApiException


class TestCertificateApi(unittest.TestCase):
    """CertificateApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_2.api.certificate_api.CertificateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_certificate_authority_item(self):
        """Test case for create_certificate_authority_item

        """
        pass

    def test_create_certificate_server_item(self):
        """Test case for create_certificate_server_item

        """
        pass

    def test_delete_certificate_authority_by_id(self):
        """Test case for delete_certificate_authority_by_id

        """
        pass

    def test_delete_certificate_server_by_id(self):
        """Test case for delete_certificate_server_by_id

        """
        pass

    def test_get_certificate_authority_by_id(self):
        """Test case for get_certificate_authority_by_id

        """
        pass

    def test_get_certificate_server_by_id(self):
        """Test case for get_certificate_server_by_id

        """
        pass

    def test_get_certificate_settings(self):
        """Test case for get_certificate_settings

        """
        pass

    def test_list_certificate_authority(self):
        """Test case for list_certificate_authority

        """
        pass

    def test_list_certificate_server(self):
        """Test case for list_certificate_server

        """
        pass

    def test_update_certificate_authority_by_id(self):
        """Test case for update_certificate_authority_by_id

        """
        pass

    def test_update_certificate_server_by_id(self):
        """Test case for update_certificate_server_by_id

        """
        pass

    def test_update_certificate_settings(self):
        """Test case for update_certificate_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
