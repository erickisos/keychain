import os

from aws_xray_sdk.core import patch_all, xray_recorder

from keychain.components.telegram import Bot
from keychain.contracts.inputs.aws import LambdaApiEvent
from keychain.contracts.outputs.aws import LambdaApiResponse
from keychain.models.components import Components
from keychain.ports.http_inputs import webhook

patch_all()

components: Components = {
    'telegram-bot': Bot(os.environ['TELEGRAM_BOT_TOKEN'])
}


def webhook_handler(event: LambdaApiEvent, _) -> LambdaApiResponse:
    return webhook(event, components)
