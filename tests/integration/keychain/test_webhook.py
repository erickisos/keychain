import json
from unittest.mock import patch

from hypothesis import given
from pytest import raises

from keychain.contracts.inputs.aws import LambdaApiEvent
from keychain.contracts.inputs.telegram import Update
from keychain.models.components import Config
from keychain.ports.http_inputs import webhook

from ..aux.requests import from_dict
from ..aux.strategies import event_with_json_body

mock_config: Config = {
    'telegram-token': 'dummy-token',
    'telegram-url': 'dummy-url',
}


@given(event=event_with_json_body(Update))
@patch('keychain.components.telegram.requests.post')
def test_webhook(mock_req, event: LambdaApiEvent):
    """Test that no matter which event we receive, the answer is the same"""
    update = json.loads(event.get('body') or '{}')
    message = update.get('edited_message') or update.get('message')
    mock_req.return_value = from_dict({'result': message}, 200)
    if (
        update.get('update_id') != ''
        and update.get('update_id') is not None
        and message
        and message['chat'].get('id') not in ('', None)
        and message['from'].get('id') not in ('', None)
        and message['text'] != ''
    ):
        expected = {
            'statusCode': 200,
            'body': json.dumps(
                {
                    'chat_id': f"{message['chat']['id']}",
                    'text': message['text'],
                }
            ),
        }
        actual = webhook(event, mock_config)
        assert expected == actual
    else:
        with raises(Exception):
            webhook(event, mock_config)
