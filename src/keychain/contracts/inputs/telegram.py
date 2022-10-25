from datetime import datetime
from typing import Literal, Optional, Text

from pydantic.dataclasses import dataclass

ChatType = Literal['private', 'group', 'supergroup', 'channel']


@dataclass
class User:
    user_id: int  # id
    first_name: Text
    last_name: Optional[Text]
    username: Optional[Text]
    is_bot: bool


@dataclass
class Chat:
    chat_id: int  # id
    title: Optional[Text]
    chat_type: ChatType  # type


@dataclass
class Message:
    message_id: int
    text: Text
    chat: Chat
    date: datetime
    from_user: User  # from


@dataclass
class Update:
    """Basic message received through webhook updates"""

    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
