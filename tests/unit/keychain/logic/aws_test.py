from pytest import raises

from keychain.logic.aws import from_json, to_json


def test_to_json():
    assert {'statusCode': 404, 'body': '{}'} == to_json({}, 404)
    assert {'statusCode': 200, 'body': '[]'} == to_json([], 200)
    assert {'statusCode': 201, 'body': '"hello world"'} == to_json(
        'hello world', 201
    )


def test_from_json():
    with raises(KeyError):
        from_json({})

    assert {} == from_json({'body': '{}'})
    assert [] == from_json({'body': '[]'})
    assert 'hello world' == from_json({'body': '"hello world"'})
    assert {'a': 1} == from_json({'body': '{"a": 1}'})
