import json
from dataclasses import dataclass
from urllib.request import urlopen

from ..contracts.inputs.telegram import Message as InMessage
from ..contracts.outputs.telegram import Message as OutMessage
from . import Singleton


@dataclass
class Bot(metaclass=Singleton):
    token: str
    base_url: str = 'https://api.telegram.org/bot{token}/{action}'

    def send_message(self, message: OutMessage) -> InMessage:
        url = self.base_url.format(token=self.token, action='sendMessage')
        with urlopen(url, data=json.dumps(message).encode()) as response:
            return json.loads(response.read().decode())
