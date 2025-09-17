from hypothesis import given
from hypothesis.strategies import from_type, text, datetimes, builds
from pytest import raises

from keychain.adapters.messages import internal_to_wire, wire_to_internal
from keychain.contracts.inputs.telegram import Message as InMessage
from keychain.models.messages import Message


def valid_message_strategy():
    """Generate Message instances with valid non-None, non-empty strings for critical fields."""
    valid_string = text(min_size=1).filter(lambda x: x != 'None' and x.strip() != '')

    return builds(
        Message,
        chat_id=valid_string,
        message_id=text(),  # Can be empty for some tests
        user_id=text(),     # Can be empty for some tests
        text=valid_string,
        date=datetimes()
    )


@given(from_type(InMessage))
def test_wire_to_internal(wired: InMessage):
    if 'id' not in wired['chat'] or 'id' not in wired['from']:
        with raises(KeyError):
            wire_to_internal(wired)
    else:
        value = wire_to_internal(wired)
        assert f"{wired['chat']['id']}" == value.chat_id
        assert f"{wired['from']['id']}" == value.user_id
        assert wired['text'] == value.text
        assert wired['date'] == value.date

        assert value.chat_id != ''
        assert value.chat_id != 'None'

        assert value.user_id != ''
        assert value.user_id != 'None'


@given(valid_message_strategy())
def test_internal_to_wire(internal: Message):
    if internal.chat_id == '' or internal.text == '':
        with raises(ValueError):
            internal_to_wire(internal)

    else:
        value = internal_to_wire(internal)
        assert internal.chat_id == value['chat_id']
        assert internal.chat_id != ''
        assert internal.chat_id != 'None'

        assert internal.text == value['text']
        assert internal.text != ''
        assert internal.text != 'None'
