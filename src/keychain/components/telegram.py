import json
from dataclasses import dataclass
from typing import Any, Text
from urllib.request import urlopen

from ..contracts.outputs.telegram import Message
from . import Singleton


@dataclass
class Bot(metaclass=Singleton):
    token: Text
    base_url: Text = 'https://api.telegram.org/bot{token}/{action}'

    def send_message(self, message: Message) -> Any:
        url = self.base_url.format(token=self.token, action='sendMessage')

        with urlopen(url, data=json.dumps(message).encode()) as response:
            return json.loads(response.read().decode())
