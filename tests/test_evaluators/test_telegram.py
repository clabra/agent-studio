# pytest -s tests/test_evaluators/test_telegram.py
import pytest

from playground.env.desktop_env.eval.evaluator_helper import evaluator_router

TASK_CONFIGS = [
    {
        "evals": [
            {
                "eval_type": "telegram",
                "eval_procedure": [
                    {
                        "message_match": {
                            "chat_id": "me",
                            "ref_messages": [
                                {
                                    "type": "text",
                                    "compare_method": "exact",
                                    "value": "hi",
                                },
                                {
                                    "type": "text",
                                    "compare_method": "exact",
                                    "value": "Welcome to the playground!",
                                },
                            ],
                        }
                    }
                ],
                "reset_procedure": [
                    {"delete_recent_messages": {"chat_id": "me", "n": 2}},
                    {"send_message": {"chat_id": "me", "message": "hi"}},
                    {
                        "send_message": {
                            "chat_id": "me",
                            "message": "Welcome to the playground!",
                        }
                    },
                ],
            }
        ]
    }
]


@pytest.mark.parametrize("task_config", TASK_CONFIGS)
def test_telegram(task_config):
    comb = evaluator_router(task_config)
    comb.reset()
    score = comb()
    assert score[0] == 1.0, score