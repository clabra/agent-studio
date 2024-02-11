# pytest -s tests/test_evaluators/test_gdocs.py
import pytest

from playground.env.desktop_env.eval.evaluator_helper import evaluator_router

TASK_CONFIGS = [
    {
        "evals": [
            {
                "eval_type": "google_docs",
                "eval_procedure": [
                    {
                        "check_doc_exists": {
                            "title": "Sample Document",
                            "content": "This is the content of the sample document",
                            "exists": False,
                        }
                    }
                ],
                "reset_procedure": [
                    {
                        "delete_document": {
                            "title": "Sample Document",
                            "content": "This is the content of the sample document",
                        }
                    },
                ],
            }
        ]
    },
    {
        "evals": [
            {
                "eval_type": "google_docs",
                "eval_procedure": [
                    {
                        "check_doc_exists": {
                            "title": "Sample Document",
                            "content": "This is the content of the sample document",
                            "exists": True,
                        }
                    }
                ],
                "reset_procedure": [
                    {
                        "create_document": {
                            "title": "Sample Document",
                            "content": "This is the content of the sample document",
                        }
                    },
                ],
            }
        ]
    },
    {
        "evals": [
            {
                "eval_type": "google_docs",
                "eval_procedure": [
                    {
                        "check_doc_exists": {
                            "title": "Sample Document",
                            "content": "This is the content of the sample document",
                            "exists": False,
                        }
                    }
                ],
                "reset_procedure": [
                    {
                        "delete_document": {
                            "title": "Sample Document",
                            "content": "This is the content of the sample document",
                        }
                    },
                ],
            }
        ]
    },
]


@pytest.mark.parametrize("task_config", TASK_CONFIGS)
def test_gdocs(task_config):
    comb = evaluator_router(task_config)
    comb.reset()
    score = comb()
    assert score == 1.0