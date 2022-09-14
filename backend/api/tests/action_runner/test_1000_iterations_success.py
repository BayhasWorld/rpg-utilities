# -*- coding: utf-8 -*-
# TODO: update docstring
"""Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import RESPONSE_CODES
from api.tests.action_runner.base import MODEL_URL
from api.tests.action_runner.base import ATTRIBUTE_RANGE

@tag("action_runner_anonymous")
class TestPost(RpgtApiBTC):
    # TODO: update docstring
    """Posts a json package to the action-runner url to test a specific use case.

    Attributes:
        JSON_INPUT [Static]: The json package to post to the target url
        ATTRIBUTE_RANGE [Static]: Value range for some of the assertions involving
                             a specific value range.
    """
    JSON_INPUT = {
        "action_input":  [
            {
                "name": "Fitness",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Agility",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Constitution",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Stature",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Intelligence",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            },
            {
                "name": "Education",
                "method": "die_roll",
                "input": {
                    "die_size": 6,
                    "die_count": 4,
                    "roll_modifier": {
                        "mod_type": "-",
                        "value": 4
                    },
                    "reroll": {
                        "condition": "==",
                        "value": 0
                    }
                }
            }
        ]
    }

    def test_run(self):
        # TODO: update docstring
        """Executes a test against the target url using the defined json package 1000 times.
        """
        for iteration in range(1000):  # pylint: disable=unused-variable
            response = self.rpgu_api_cli.post(MODEL_URL,
                                              self.JSON_INPUT,
                                              format="json")
            self.assertEqual(response.status_code, RESPONSE_CODES["created"])
            self.assertTrue(response.json())
            self.assertTrue(response.json()['Fitness'])
            self.assertIn(response.json()['Fitness'], ATTRIBUTE_RANGE)
            self.assertTrue(response.json()['Agility'])
            self.assertIn(response.json()['Agility'], ATTRIBUTE_RANGE)
            self.assertTrue(response.json()['Constitution'])
            self.assertIn(response.json()['Constitution'], ATTRIBUTE_RANGE)
            self.assertTrue(response.json()['Stature'])
            self.assertIn(response.json()['Stature'], ATTRIBUTE_RANGE)
            self.assertTrue(response.json()['Intelligence'])
            self.assertIn(response.json()['Intelligence'], ATTRIBUTE_RANGE)
            self.assertTrue(response.json()['Education'])
            self.assertIn(response.json()['Education'], ATTRIBUTE_RANGE)
