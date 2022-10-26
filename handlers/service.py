import os

from keychain.components.telegram import Bot
from keychain.contracts.inputs.telegram import Update
from keychain.contracts.outputs.aws import LambdaApiResponse
from keychain.logic.aws import from_json
from keychain.ports.http_inputs import webhook

components = {'bot': Bot(os.environ['token'])}


def webhook_handler(event, _) -> LambdaApiResponse:
    update = Update(**from_json(event))
    return webhook(update, components)
