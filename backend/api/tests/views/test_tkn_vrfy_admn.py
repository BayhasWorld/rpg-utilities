# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/views
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import ADMIN_USER
from api.tests.base import CODES
from api.tests.base import T_URL

FIXTURES = ['test_users']


@tag("views_admin")
class TestsAdmin(RpgtApiBTC):
    """
    Defines TestAdmin class
    """
    fixtures = FIXTURES
    response = RpgtApiBTC.rpgu_api_cli.post(T_URL,
                                            ADMIN_USER,
                                            format="json").json()
    token = response['access']
    refresh = response['refresh']

    def test_post_token_verify(self):
        """
        Submits a POST request
        """
        response = self.rpgu_api_cli.post(T_URL + '/refresh/',
                                          {"token": self.token},
                                          format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertFalse(response.json())
