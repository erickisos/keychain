import os

from keychain.components.telegram import Bot
from keychain.contracts.outputs.aws import LambdaApiResponse
from keychain.ports.http_inputs import webhook

components = {'bot': Bot(os.environ['token'])}


def webhook_handler(event, _) -> LambdaApiResponse:
    return webhook(event, components)
