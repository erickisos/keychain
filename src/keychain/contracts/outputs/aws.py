from typing import Text, TypedDict


class LambdaApiResponse(TypedDict):
    statusCode: int
    body: Text
