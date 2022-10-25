from ..contracts.inputs.telegram import Update
from ..contracts.outputs.telegram import Message as WiredMessage
from ..models.messages import Message


def update_to_internal(update: Update) -> Message:
    message = update.edited_message or update.message
    return Message(
        chat_id=message.chat.chat_id,
        message_id=message.message_id,
        text=message.text,
        date=message.date,
        user_id=message.from_user.user_id,
    )


def internal_to_wire(message: Message) -> WiredMessage:
    ...


def wire_to_internal(wired: WiredMessage) -> Message:
    ...
