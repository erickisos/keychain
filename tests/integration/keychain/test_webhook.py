import json
from unittest.mock import patch

from hypothesis import given
from pytest import raises

from keychain.components.telegram import Bot
from keychain.contracts.inputs.aws import LambdaApiEvent
from keychain.contracts.inputs.telegram import Update
from keychain.models.components import Components
from keychain.ports.http_inputs import webhook

from ..aux.strategies import event_with_json_body

mock_components: Components = {
    'telegram-bot': Bot('dummy_token', 'https://dumyurl/{token}/{action}')
}


@given(event=event_with_json_body(Update))
def test_webhook(event: LambdaApiEvent):
    """Test that no matter which event we receive, the answer is the same"""
    update = json.loads(event.get('body') or '{}')
    message = update.get('edited_message') or update.get('message')
    with patch(
        'keychain.components.telegram.Bot.send_message',
        return_value=message,
    ) as mock_send_message:
        if (
            update.get('update_id') != ''
            and update.get('update_id') is not None
            and message
            and message['chat'].get('id') not in ('', None)
            and message['from'].get('id') not in ('', None)
            and message['text'] != ''
        ):
            assert {
                'statusCode': 200,
                'body': json.dumps(
                    {
                        'chat_id': f"{message['chat']['id']}",
                        'text': message['text'],
                    }
                ),
            } == webhook(event, mock_components)
            assert mock_send_message.call_count == 1
        else:
            with raises(Exception):
                webhook(event, mock_components)
