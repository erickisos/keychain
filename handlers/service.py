from keychain.contracts.outputs.aws import LambdaApiResponse
from keychain.ports.http_inputs import webhook


def webhook_handler(event, _) -> LambdaApiResponse:
    return webhook(event)
