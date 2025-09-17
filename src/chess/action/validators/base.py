from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.action.outcome import ActionOutcome

T = TypeVar('T')

class RequestValidator(ABC):


    @staticmethod
    @abstractmethod
    def validate(t: Generic[T]) -> ActionOutcome:
        pass