from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Specification(ABC, Generic[T]):

    @staticmethod
    @abstractmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        pass