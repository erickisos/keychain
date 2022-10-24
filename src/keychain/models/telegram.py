from datetime import datetime
from typing import Literal, Optional, Text, TypedDict
from xmlrpc.client import Boolean
from pydantic import Field
from pydantic.dataclasses import dataclass

ChatType = Literal['private', 'group', 'supergroup', 'channel']


@dataclass
class User:
    is_bot: Boolean
    first_name: Text
    last_name: Optional[Text]
    username: Optional[Text]
    user_id: int = Field(alias='id')


@dataclass
class Chat:
    title: Optional[Text]
    chat_id: int = Field(alias='id')
    chat_type: ChatType = Field(alias='type')


@dataclass
class Message:
    message_id: int
    text: Text
    chat: Chat
    date: datetime
    from_user: User = Field(alias='from')


@dataclass
class Update:
    """Basic message received through webhook updates"""

    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
