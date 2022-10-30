from ..adapters.messages import event_to_internal, internal_to_event
from ..contracts.inputs.aws import LambdaApiEvent
from ..contracts.outputs.aws import LambdaApiResponse
from ..controllers.messages import send
from ..models.components import Components


def webhook(
    event: LambdaApiEvent, components: Components
) -> LambdaApiResponse:
    message = event_to_internal(event)
    response_message = send(message, components)
    return internal_to_event(response_message)
