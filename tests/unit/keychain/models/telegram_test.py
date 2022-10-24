from keychain.models.telegram import User


def test_generate_user():
    user_dict = {
        'id': '1',
        'first_name': 'John',
        'last_name': 'Doe',
        'username': 'johndoe',
        'is_bot': False,
    }
    user = User(**user_dict)
    assert user.user_id == 1
    assert user.is_bot is False
