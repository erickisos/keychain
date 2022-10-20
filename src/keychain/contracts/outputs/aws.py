from typing import Text, TypedDict


class LambdaResponse(TypedDict):
    statusCode: int
    body: Text
