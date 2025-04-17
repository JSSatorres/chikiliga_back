from abc import ABC, abstractmethod

class AggregateRoot(ABC):
    @abstractmethod
    def to_primitives(self):
        pass

    @classmethod
    @abstractmethod
    def from_primitives(cls, plain_data):
        pass