from ..adapters.messages import internal_to_wire, wire_to_internal
from ..models.components import Components
from ..models.messages import Message


def send_message(message: Message, components: Components) -> Message:
    bot = components['telegram-bot']
    out_message = internal_to_wire(message)
    return wire_to_internal(bot.send_message(out_message))
