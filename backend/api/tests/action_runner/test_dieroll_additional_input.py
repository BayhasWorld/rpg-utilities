# -*- coding: utf-8 -*- # pylint: disable=too-many-lines
"""Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import RESPONSE_CODES
from api.tests.action_runner.base import MODEL_URL

@tag("action_runner_anonymous")
class TestPostDieRollAddInput(RpgtApiBTC):
    # TODO: update docstring
    """Posts a json package to the action-runner url to test a specific use case.

    Attributes:
        JSON_INPUT [Static]: The json package to post to the target url
        VALUE_RANGE [Static]: Value range for some of the assertions involving
                              a specific value range.
    """
    JSON_INPUT = {
        "action_input": [
            {
                "name": "test_case",
                "method": "die_roll",
                "input": {
                    "die_size": "die_size",
                    "die_count": "die_count",
                    "per_modifier": {
                        "mod_type": "+",
                        "value": "per_value"
                    },
                    "roll_modifier": {
                        "mod_type": "+",
                        "value": "roll_value"
                    },
                    "post_modifier": {
                        "mod_type": "*",
                        "value": "post_value"
                    }
                }
            }
        ],
        "additional_input": {
            "die_size": 6,
            "die_count": 1,
            "per_value": 1,
            "roll_value": 3,
            "post_value": 10
        }
    }
    VALUE_RANGE = [50, 60, 70, 80, 90, 100]

    def test_run(self):
        # TODO: update docstring
        """Executes a test against the target url using the defined json package 1000 times.
        """
        for iteration in range(1000):  # pylint: disable=unused-variable
            response = self.rpgu_api_cli.post(MODEL_URL,
                                              self.JSON_INPUT,
                                              format="json")
            self.assertEqual(response.status_code, RESPONSE_CODES["created"])
            self.assertGreaterEqual(response.json()["test_case"], 50)
            self.assertLessEqual(response.json()["test_case"], 100)
