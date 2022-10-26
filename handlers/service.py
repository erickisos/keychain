import os

from keychain.adapters.messages import event_to_internal, internal_to_event
from keychain.components.telegram import Bot
from keychain.contracts.inputs.aws import LambdaApiEvent
from keychain.contracts.outputs.aws import LambdaApiResponse
from keychain.controllers.messages import send
from keychain.models.components import Components

components: Components = {
    'telegram-bot': Bot(os.environ['TELEGRAM_BOT_TOKEN'])
}


def webhook_handler(event: LambdaApiEvent, _) -> LambdaApiResponse:
    return internal_to_event(send(event_to_internal(event), components))
