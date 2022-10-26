from typing import Optional

from ..adapters.messages import update_to_internal
from ..contracts.inputs.telegram import Update
from ..controllers.messages import send
from ..models.components import Components
from ..models.messages import Message


def webhook(event: Update, components: Components) -> Optional[Message]:
    message = update_to_internal(event)
    return send(message, components)
