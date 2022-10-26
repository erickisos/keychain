from typing import TypedDict

# Reference: https://core.telegram.org/bots/api#sendmessage
Message = TypedDict('Message', {'chat_id': str, 'text': str})
