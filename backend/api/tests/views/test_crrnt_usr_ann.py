# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/views
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import API_URL
from api.tests.base import RESPONSE_CODES

FIXTURES = ['test_users']

@tag("views_anonymous")
class TestGet(RpgtApiBTC):
    """
    Defines TestsAnonymous class
    """

    def test_get_current_user(self):
        """
        test_get_current_user
        """
        response = self.rpgu_api_cli.get(API_URL + 'current-user')
        self.assertEqual(response.status_code, RESPONSE_CODES["success"])
        self.assertEqual(response.json()['is_authenticated'], False)
        self.assertEqual(response.json()['username'], None)
        self.assertEqual(response.json()['first_name'], None)
        self.assertEqual(response.json()['last_name'], None)
        self.assertEqual(response.json()['is_superuser'], None)
