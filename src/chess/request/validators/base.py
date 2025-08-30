from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from assurance.result.permission import PermissionResult

T = TypeVar('T')

class RequestValidator(ABC):


    @staticmethod
    @abstractmethod
    def validate(t: Generic[T]) -> PermissionResult:
        pass