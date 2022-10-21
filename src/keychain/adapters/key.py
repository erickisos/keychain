from ..models.keychain import KeychainEntity
from ..contracts.output.aws import LambdaResponse
from ..contracts.input.aws import LambdaEvent


def wire_to_internal(key_schema: LambdaEvent) -> KeychainEntity:
    pass


def internal_to_wire(key_entity: KeychainEntity) -> LambdaResponse:
    pass
