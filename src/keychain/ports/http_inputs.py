from ..adapters.messages import event_to_internal, internal_to_event
from ..contracts.inputs.aws import LambdaApiEvent
from ..contracts.outputs.aws import LambdaApiResponse
from ..controllers.messages import send
from ..models.components import Config


def webhook(event: LambdaApiEvent, config: Config) -> LambdaApiResponse:
    message = event_to_internal(event)
    response_message = send(message, config)
    return internal_to_event(response_message)
