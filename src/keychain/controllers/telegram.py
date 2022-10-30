from ..models.telegram import Message, Update


def send_message(update: Update, components) -> Message:
    message = update.edited_message or update.message

    if not message:
        raise ValueError('Message not found')

    return components['bot'].send_message(message)
