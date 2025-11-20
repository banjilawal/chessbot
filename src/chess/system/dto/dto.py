from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('V')


class DTO(ABC, Generic[T]):
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    
