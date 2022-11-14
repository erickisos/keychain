import requests

from ..contracts.inputs.telegram import Message as InMessage
from ..contracts.outputs.telegram import Message as OutMessage


def send_message(
    message: OutMessage,
    token: str,
    base_url: str = 'https://api.telegram.org/bot{token}/{action}',
) -> InMessage:
    url = base_url.format(token=token, action='sendMessage')
    response = requests.post(url, json=message).json()
    return response['result']
