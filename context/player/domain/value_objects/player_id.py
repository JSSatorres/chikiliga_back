from pydantic import BaseModel, constr

class PlayerId(BaseModel):
    value: constr(min_length=1)

    def __init__(self, value: str):
        super().__init__(value=value)

    def __eq__(self, other: 'PlayerId') -> bool:
        return self.value == other.value

    def to_primitives(self) -> dict:
        return {"value": self.value}

    @classmethod
    def from_primitives(cls, plain_data: dict) -> 'PlayerId':
        return cls(value=plain_data["value"])