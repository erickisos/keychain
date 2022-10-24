from ..models.telegram import Message
from ..components.telegram import Bot


def send_message(message: Message, bot: Bot) -> Message:
    return bot.send_message(message)
