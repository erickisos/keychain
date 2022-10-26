from keychain.adapters.messages import wire_to_internal, internal_to_wire
from hypothesis.strategies import from_type
from hypothesis import given

from keychain.models.messages import Message
from keychain.contracts.inputs.telegram import Message as InMessage
from pytest import raises


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


@given(from_type(Message))
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
