import os
from ..components.telegram import Bot
from ..contracts.inputs.aws import LambdaApiEvent
from ..contracts.outputs.aws import LambdaApiResponse
from ..logic.aws import to_json


components = {'bot': Bot(os.getenv('TELEGRAM_TOKEN'))}


def webhook(event: LambdaApiEvent) -> LambdaApiResponse:
    print(event)

    return to_json({'message': 'Hello, World!'}, 200)
