from ..adapters.messages import update_to_internal
from ..contracts.inputs.telegram import Update
from ..controllers.messages import send
from ..models.components import Components


def webhook(event: Update, components: Components):
    message = update_to_internal(event)
    return send(message, components)
