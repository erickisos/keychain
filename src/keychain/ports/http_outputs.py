from ..adapters.messages import internal_to_wire, wire_to_internal
from ..components.telegram import send_message as send
from ..contracts.outputs.telegram import Message as OutMessage
from ..models.components import Config
from ..models.messages import Message


def send_message(message: Message, config: Config) -> Message:
    url = (
        config['telegram-url']
        or 'https://api.telegram.org/bot{token}/{action}'
    )
    token = config['telegram-token']
    out_message: OutMessage = internal_to_wire(message)
    response = send(out_message, token, url)
    return wire_to_internal(response)
