from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from assurance.result.event import CommandOutcome

T = TypeVar('T')

class RequestValidator(ABC):


    @staticmethod
    @abstractmethod
    def validate(t: Generic[T]) -> CommandOutcome:
        pass