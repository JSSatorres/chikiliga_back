from shared.domain.value_objects.string_value_object import StringValueObject

class TeamId(StringValueObject):
    def __init__(self, value: str):
        super().__init__(value)

    @classmethod
    def from_primitives(cls, plain_data: str) -> 'TeamId':
        return cls(plain_data)

    def to_primitives(self) -> str:
        return self.value

    def __eq__(self, other: 'TeamId') -> bool:
        return isinstance(other, TeamId) and self.value == other.value