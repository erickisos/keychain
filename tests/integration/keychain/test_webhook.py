from unittest.mock import patch

from hypothesis import given
from hypothesis.strategies import from_type
from pytest import raises

from keychain.components.telegram import Bot
from keychain.contracts.inputs.telegram import Update
from keychain.models.components import Components
from keychain.models.messages import Message
from keychain.ports.http_inputs import webhook

mock_components: Components = {
    'bot': Bot('dummy_token', 'https://dumyurl/{token}/{action}')
}


@given(update=from_type(Update))
def test_webhook(update: Update):
    """Test that no matter which event we receive, the answer is the same"""
    if message := update.edited_message or update.message:
        with patch(
            'keychain.components.telegram.Bot.send_message',
            return_value=message,
        ) as mock_send_message:
            expected = Message(
                chat_id=f'{message.chat.chat_id}',
                message_id=f'{message.message_id}',
                user_id=f'{message.from_user.user_id}',
                text=message.text,
                date=message.date,
            )
            assert expected == webhook(update, mock_components)
            assert mock_send_message.call_count == 1
    else:
        with raises(ValueError):
            webhook(update, mock_components)
