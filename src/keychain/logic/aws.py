import json
from typing import Any, Dict

from ..contracts.inputs.aws import LambdaApiEvent
from ..contracts.outputs.aws import LambdaApiResponse


def from_json(event: LambdaApiEvent) -> Dict:
    return json.loads(event['body'])


def to_json(item: Any, status_code: int) -> LambdaApiResponse:
    return {'statusCode': status_code, 'body': json.dumps(item)}
