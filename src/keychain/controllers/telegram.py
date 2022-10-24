from typing import Optional
from ..models.telegram import Update, Message


def send_message(update: Update, components) -> Optional[Message]:
    message = update.edited_message or update.message

    if not message:
        return

    # TODO: Add send_message business logic
    return components['bot'].send_message(message)
