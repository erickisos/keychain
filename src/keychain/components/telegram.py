from dataclasses import dataclass
import json
from typing import Text

from ..models.telegram import Message
from . import Singleton
from urllib.request import Request, urlopen
from urllib.parse import urlencode


@dataclass
class Bot(metaclass=Singleton):
    token: Text
    base_url: Text = 'https://api.telegram.org/bot{token}/{action}'

    def send_message(self, message: Message) -> Message:
        url = self.base_url.format(token=self.token, action='sendMessage')

        data = {"chat_id": message.chat.chat_id, "text": message.text}
        try:
            request = Request(url, urlencode(data).encode())
            response = urlopen(request)
            return Message(**json.loads(response.read().decode()))
        except Exception as e:
            print(e)
            return message
