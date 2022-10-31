from dataclasses import dataclass

import requests

from ..contracts.inputs.telegram import Message as InMessage
from ..contracts.outputs.telegram import Message as OutMessage
from . import Singleton


@dataclass
class Bot(metaclass=Singleton):
    token: str
    base_url: str = 'https://api.telegram.org/bot{token}/{action}'

    def send_message(self, message: OutMessage) -> InMessage:
        url = self.base_url.format(token=self.token, action='sendMessage')
        response = requests.post(url, json=message)
        print(response.json())
        return response.json()['body']
