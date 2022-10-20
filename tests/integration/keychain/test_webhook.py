from unittest.mock import patch
from pytest import fixture

from keychain.ports.http_inputs import webhook
from keychain.contracts.inputs.aws import LambdaApiEvent


@fixture
def event() -> LambdaApiEvent:
    # TODO: Replace this with a random generator
    return LambdaApiEvent(
        headers={},
        body='{}',
    )


@patch('builtins.print', autospec=True)
def test_webhook(mocked_print, event: LambdaApiEvent):
    """Test that no matter which event we receive, the answer is the same"""
    assert {
        'statusCode': 200,
        'body': '{"message": "Hello, World!"}',
    } == webhook(event, None)

    assert mocked_print.called
