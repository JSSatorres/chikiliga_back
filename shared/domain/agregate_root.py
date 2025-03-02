from abc import ABC, abstractmethod

class AggregateRoot(ABC):
    @abstractmethod
    def to_primitives(self):
        pass

    @classmethod
    def from_primitives(cls, data: dict):
        pass
