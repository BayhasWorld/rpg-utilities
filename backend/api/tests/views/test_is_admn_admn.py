# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/views
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import ADMIN_USER
from api.tests.base import API_URL
from api.tests.base import RESPONSE_CODES
from api.tests.base import TOKEN_URL

FIXTURES = ['test_users']

@tag("views_admin")
class TestGet(RpgtApiBTC):
    """
    Defines TestAdmin class
    """
    fixtures = FIXTURES
    response = RpgtApiBTC.rpgu_api_cli.post(TOKEN_URL,
                                            ADMIN_USER,
                                            format="json").json()
    token = response['access']
    refresh = response['refresh']

    def test_get_is_admin(self):
        """
        Submits a POST request
        """
        response = self.rpgu_api_cli.get(API_URL + 'is-admin',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, RESPONSE_CODES["success"])
