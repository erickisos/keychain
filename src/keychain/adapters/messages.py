from ..contracts.inputs.telegram import Message as InMessage
from ..contracts.outputs.telegram import Message as OutMessage
from ..models.messages import Message


def internal_to_wire(message: Message) -> OutMessage:
    chat_id = message.chat_id
    text = message.text

    if chat_id == '' or text == '':
        raise ValueError('Invalid message')

    return OutMessage(chat_id=chat_id, text=text)


def wire_to_internal(wired: InMessage) -> Message:
    chat_id = f'{wired["chat"]["id"]}'.strip()
    user_id = f'{wired["from"]["id"]}'.strip()
    message_id = f'{wired["message_id"]}'.strip()

    if not chat_id or not user_id or not message_id:
        raise ValueError('Invalid message')

    return Message(
        chat_id=chat_id,
        user_id=user_id,
        message_id=message_id,
        text=wired['text'],
        date=wired['date'],
    )
