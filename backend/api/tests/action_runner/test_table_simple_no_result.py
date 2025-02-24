# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import RESPONSE_CODES
from api.tests.action_runner.base import MODEL_URL

@tag("action_runner_anonymous")
class TestPost(RpgtApiBTC):
    # TODO: update docstring
    """Posts a json package to the action-runner url to test a specific use case.

    Attributes:
        JSON_INPUT [Static]: The json package to post to the target url
    """
    JSON_INPUT = {
        "action_input": [
            {
                "name": "test_case",
                "method": "table",
                "input": {
                    "style": "simple",
                    "choice": 12,
                    "choices": {
                        "-1": "2nd Lieutenant",
                        "0": "2nd Lieutenant",
                        "1": "2nd Lieutenant",
                        "2": "1st Lieutenant",
                        "3": "1st Lieutenant",
                        "4": "Captain",
                        "5": "Captain",
                        "6": "Major",
                        "7": "Major",
                        "8": "Lieutenant Colonel"
                    }
                }
            }
        ]
    }

    def test_run(self):
        # TODO: update docstring
        """Executes a test against the target url using the defined json package
        """
        response = self.rpgu_api_cli.post(MODEL_URL,
                                          self.JSON_INPUT,
                                          format="json")
        self.assertEqual(response.status_code, RESPONSE_CODES["created"])
        self.assertEqual(response.json()["test_case"], "no result matched")
