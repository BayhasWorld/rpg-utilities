# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/views
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import API_URL
from api.tests.base import CODES
from api.tests.base import RO_USER
from api.tests.base import T_URL

FIXTURES = ['test_users']

@tag("views_readonly")
class TestGet(RpgtApiBTC):
    """
    Defines TestsReadOnly class
    """
    fixtures = FIXTURES
    response = RpgtApiBTC.rpgu_api_cli.post(T_URL,
                                            RO_USER,
                                            format="json").json()
    token = response['access']
    refresh = response['refresh']

    def test_get_current_user(self):
        """
        Submits a POST request
        """
        response = self.rpgu_api_cli.get(API_URL + 'current-user',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertEqual(response.json()['is_authenticated'], True)
        self.assertEqual(response.json()['username'], 'read-only')
        self.assertEqual(response.json()['first_name'], 'read')
        self.assertEqual(response.json()['last_name'], 'only')
        self.assertEqual(response.json()['is_superuser'], False)
