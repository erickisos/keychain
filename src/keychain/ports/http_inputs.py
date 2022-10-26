import os
from ..components.telegram import Bot
from ..contracts.inputs.aws import LambdaApiEvent
from ..contracts.outputs.aws import LambdaApiResponse
from ..logic.aws import to_json
from ..models.components import Components


def webhook(event: LambdaApiEvent, _: Components) -> LambdaApiResponse:
    print(event)

    return to_json({'message': 'Hello, World!'}, 200)
