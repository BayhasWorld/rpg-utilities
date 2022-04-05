# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/views
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import CODES
from api.tests.base import API_URL

@tag("views_anonymous")
class TestGet(RpgtApiBTC):
    """
    Defines TestsReadOnly class
    """

    def test_get_api_info(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgu_api_cli.get(API_URL + '/info',
                                          format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json())
