from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Flow(ABC, Generic[T]):

    @staticmethod
    @abstractmethod
    def enter(client: Generic[T], resource: Generic[T]):
        pass