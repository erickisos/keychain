from unittest.mock import patch

from hypothesis import given
from hypothesis.strategies import from_type

from keychain.contracts.inputs.aws import LambdaApiEvent
from keychain.ports.http_inputs import webhook


@patch('builtins.print', autospec=True)
@given(from_type(LambdaApiEvent))
def test_webhook(mocked_print, event: LambdaApiEvent):
    """Test that no matter which event we receive, the answer is the same"""
    assert {
        'statusCode': 200,
        'body': '{"message": "Hello, World!"}',
    } == webhook(event, None)

    assert mocked_print.called
