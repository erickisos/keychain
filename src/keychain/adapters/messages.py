from ..contracts.inputs.aws import LambdaApiEvent
from ..contracts.inputs.telegram import Message as InMessage
from ..contracts.inputs.telegram import Update as InUpdate
from ..contracts.outputs.aws import LambdaApiResponse
from ..contracts.outputs.telegram import Message as OutMessage
from ..logic.aws import from_json, to_json
from ..models.messages import Message


def event_to_internal(event: LambdaApiEvent) -> Message:
    update_json = from_json(event)
    update = InUpdate(
        update_id=update_json['update_id'],
        message=update_json.get('message'),
        edited_message=update_json.get('edited_message'),
    )
    message = update.get('edited_message') or update.get('message')

    if not message:
        raise ValueError('Message not found')

    return wire_to_internal(message)


def internal_to_event(message: Message) -> LambdaApiResponse:
    wired = internal_to_wire(message)
    return to_json(wired, 200)


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
