from typing import Any
import uuid


class PlayerId:
    """
    Value object representing a unique player identifier.
    Uses string-based IDs compatible with MongoDB ObjectId format.
    """
    
    def __init__(self, value: str):
        if not value or not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("PlayerId cannot be empty")
        self._value = value.strip()
    
    @property
    def value(self) -> str:
        return self._value
    
    @classmethod
    def generate(cls) -> 'PlayerId':
        """Generate a new unique PlayerId using UUID."""
        return cls(str(uuid.uuid4()))
    
    @classmethod
    def from_string(cls, value: str) -> 'PlayerId':
        """Create PlayerId from string value."""
        return cls(value)
    
    def __str__(self) -> str:
        return self._value
    
    def __repr__(self) -> str:
        return f"PlayerId('{self._value}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, PlayerId):
            return False
        return self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)
    
    def to_primitives(self) -> str:
        return self._value
    
    @classmethod
    def from_primitives(cls, plain_data: str) -> 'PlayerId':
        return cls(plain_data)
