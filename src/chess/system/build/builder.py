from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import BuildResult

T = TypeVar('T')

class Builder(ABC, Generic[T]):

    @classmethod
    @abstractmethod
    def build(cls, *args, **kwargs) -> BuildResult[T]:
        pass