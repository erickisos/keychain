from keychain.logic.aws import lambda_json


def test_lambda_json():
    assert {'statusCode': 404, 'body': '{}'} == lambda_json(404, {})
    assert {'statusCode': 200, 'body': '[]'} == lambda_json(200, [])
    assert {'statusCode': 201, 'body': '"hello world"'} == lambda_json(
        201, 'hello world'
    )
