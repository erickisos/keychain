from datetime import datetime
from typing import Literal, TypedDict

ChatType = Literal['private', 'group', 'supergroup', 'channel']

User = TypedDict(
    'User',
    {
        'id': int,
        'first_name': str,
        'last_name': str,
        'username': str,
        'is_bot': bool,
    },
    total=False,
)


Chat = TypedDict(
    'Chat', {'id': int, 'type': ChatType, 'title': str}, total=False
)


Message = TypedDict(
    'Message',
    {
        'message_id': int,
        'text': str,
        'chat': Chat,
        'date': datetime,
        'from': User,
    },
)


Update = TypedDict(
    'Update',
    {'update_id': int, 'message': Message, 'edited_message': Message},
    total=False,
)
