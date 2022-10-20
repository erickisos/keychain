import json
from typing import Any

from ..contracts.outputs.aws import LambdaApiResponse


def lambda_json(status_code: int, body: Any) -> LambdaApiResponse:
    return {'statusCode': status_code, 'body': json.dumps(body)}
