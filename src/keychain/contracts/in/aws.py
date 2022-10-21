from typing import Dict, Text, TypedDict


class LambdaEvent(TypedDict):
    headers: Dict
    body: Text
    path: Text
    pathParameters: Dict
    queryStringParameters: Dict
