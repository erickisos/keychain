import json

from hypothesis.strategies import composite, from_type
from pydantic_core import to_jsonable_python

from keychain.contracts.inputs.aws import LambdaApiEvent


@composite
def event_with_json_body(draw, body):
    """Add any Pydantic dataclass as body of ApiEvent."""
    api_event = draw(from_type(LambdaApiEvent))
    api_body = draw(from_type(body))
    return {
        **api_event,
        'body': json.dumps(to_jsonable_python(api_body)),
    }
