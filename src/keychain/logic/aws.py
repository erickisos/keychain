from typing import Any

import json
from ..contracts.outputs.aws import LambdaApiResponse


def lambda_json(status_code: int, body: Any) -> LambdaApiResponse:
    return {'statusCode': status_code, 'body': json.dumps(body)}
