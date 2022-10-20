from typing import Dict, Text, TypedDict


class LambdaApiEvent(TypedDict):
    headers: Dict
    body: Text
    path: Text
    pathParameters: Dict
    queryStringParameters: Dict
