from dataclasses import dataclass
from typing import Any


@dataclass
class Response:
    data: Any
    status_code: int

    def json(self) -> Any:
        return self.data


def from_dict(data, status_code):
    return Response(data=data, status_code=status_code)
