from shared.domain.value_objects.string_value_object import StringValueObject

class MarketId(StringValueObject):
    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def from_primitives(cls, plain_data: str) -> 'MarketId':
        return cls(plain_data)

    def to_primitives(self) -> str:
        return self.value

    def __eq__(self, other: 'MarketId') -> bool:
        return isinstance(other, MarketId) and self.value == other.value