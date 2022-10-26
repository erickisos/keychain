from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class Message:
    chat_id: str
    message_id: str
    user_id: str
    text: str
    date: datetime
