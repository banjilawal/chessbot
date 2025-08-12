from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Validator(ABC, Generic[T]):

    @staticmethod
    @abstractmethod
    def is_valid(item: Generic[T]) -> bool:
        pass