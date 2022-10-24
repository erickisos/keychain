from keychain.ports.http_inputs import webhook
from keychain.contracts.outputs.aws import LambdaApiResponse


def webhook_handler(event, _) -> LambdaApiResponse:
    return webhook(event)
