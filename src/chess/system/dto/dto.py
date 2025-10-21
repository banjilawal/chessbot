from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import DTO, LoggingLevelRouter, Result

T = TypeVar('T')


class DTO(ABC, Generic[T]):
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def convert(cls, candidate: T) -> Result[DTO[T]]:
        pass
    
    
