from ..contracts.inputs.aws import LambdaApiEvent
from ..contracts.outputs.aws import LambdaApiResponse
from ..logic.aws import lambda_json


def webhook(event: LambdaApiEvent, _) -> LambdaApiResponse:
    print(event)
    return lambda_json(200, {'message': 'Hello, World!'})
