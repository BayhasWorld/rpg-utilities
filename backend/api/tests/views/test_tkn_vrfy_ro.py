# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/views
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import RESPONSE_CODES
from api.tests.base import RO_USER
from api.tests.base import TOKEN_URL

FIXTURES = ['test_users']

@tag("views_readonly")
class TestsReadOnly(RpgtApiBTC):
    """
    Defines TestsReadOnly class
    """
    fixtures = FIXTURES
    response = RpgtApiBTC.rpgu_api_cli.post(TOKEN_URL,
                                            RO_USER,
                                            format="json").json()
    token = response['access']
    refresh = response['refresh']

    def test_post_token_verify(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgu_api_cli.post(TOKEN_URL + '/verify',
                                          {"token": self.token},
                                          format="json")
        self.assertEqual(response.status_code, RESPONSE_CODES["success"])
        self.assertFalse(response.json())
