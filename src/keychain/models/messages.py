from datetime import datetime
from typing import Text

from pydantic.dataclasses import dataclass


@dataclass
class Message:
    chat_id: Text
    message_id: Text
    user_id: Text
    text: Text
    date: datetime
