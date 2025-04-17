from typing import Any

class StringValueObject:
    def __init__(self, value: str):
        self.value = value

    def equals_to(self, other: 'StringValueObject') -> bool:
        return self.value == other.value

    def to_primitives(self) -> str:
        return self.value

    @classmethod
    def from_primitives(cls, plain_data: str) -> 'StringValueObject':
        return cls(plain_data)