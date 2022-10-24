from typing import TypedDict, Union, Text


class Message(TypedDict):
    """Main fields for the message

    Reference: https://core.telegram.org/bots/api#sendmessage
    """

    chat_id: Union[Text, int]
    text: Text
