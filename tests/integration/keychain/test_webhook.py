from unittest.mock import patch

from hypothesis import given

from keychain.contracts.inputs.aws import LambdaApiEvent
from keychain.models.telegram import Update
from keychain.ports.http_inputs import webhook

from ..aux.strategies import event_with_json_body


@patch('builtins.print', autospec=True)
@given(event_with_json_body(Update))
def test_webhook(mocked_print, event: LambdaApiEvent):
    """Test that no matter which event we receive, the answer is the same"""
    assert {
        'statusCode': 200,
        'body': '{"message": "Hello, World!"}',
    } == webhook(event)

    assert mocked_print.called
