# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/views
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import RESPONSE_CODES
from api.tests.base import TOKEN_URL

FIXTURES = ['test_users']

@tag("views_anonymous")
class TestPost(RpgtApiBTC):
    """
    Defines TestsAnonymous class
    """

    def test_post_token_failure(self):
        """
        test_post_token_failure
        """
        response = RpgtApiBTC.rpgu_api_cli.post(TOKEN_URL,
                                                {"username": "foo",
                                                 "password": "bar"},
                                                format="json")
        self.assertEqual(response.status_code, RESPONSE_CODES["no_creds"])
