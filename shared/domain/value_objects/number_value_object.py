from typing import Any

class NumberValueObject:
    def __init__(self, value: int):
        self.value = value

    def equals_to(self, other: 'NumberValueObject') -> bool:
        return self.value == other.value

    def is_bigger_than(self, other: 'NumberValueObject') -> bool:
        return self.value > other.value

    def to_primitives(self) -> Any:
        return self.value

    @classmethod
    def from_primitives(cls, plain_data: Any) -> 'NumberValueObject':
        return cls(plain_data)