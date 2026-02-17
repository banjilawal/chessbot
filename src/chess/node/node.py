from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar('T')


class Node(ABC, Generic[T]):
    
    @abstractmethod
    def incoming(self) -> List[Node[T]]:
        pass
    
    @abstractmethod
    def outgoing(self) -> List[Node[T]]:
        pass