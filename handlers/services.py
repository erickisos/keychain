"""This module includes all the handlers for http requests."""
import os

from aws_xray_sdk.core import patch_all

from keychain.contracts.inputs.aws import LambdaApiEvent
from keychain.contracts.outputs.aws import LambdaApiResponse
from keychain.models.components import Config
from keychain.ports.http_inputs import webhook

patch_all()

config: Config = {'telegram-token': os.environ['TELEGRAM_BOT_TOKEN']}


def webhook_handler(event: LambdaApiEvent, _) -> LambdaApiResponse:
    return webhook(event, config)
