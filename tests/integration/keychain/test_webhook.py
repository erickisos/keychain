import json
from unittest.mock import patch

from hypothesis import given
from hypothesis.strategies import from_type
from pytest import raises

from keychain.components.telegram import Bot
from keychain.contracts.inputs.telegram import Update
from keychain.contracts.outputs.telegram import Message
from keychain.ports.http_inputs import webhook

mock_components = (
    {'bot': Bot('dummy_token', 'https://dumyurl/{token}/{action}')},
)


@patch('urllib.request.urlopen')
@given(update=from_type(Update), message=from_type(Message))
def test_webhook(mock_urlopen, update: Update, message: Message):
    """Test that no matter which event we receive, the answer is the same"""
    if update.edited_message or update.message:
        mock_urlopen.return_value.content = json.dumps(dict(message))
        assert {
            'statusCode': 202,
            'body': '{"message": "Hello, World!"}',
        } == webhook(update, mock_components)
        assert mock_urlopen.call_count == 1
    else:
        with raises(Exception):
            webhook(update, {})
