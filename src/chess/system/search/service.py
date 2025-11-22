from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from chess.system import LoggingLevelRouter, SearchContext, SearchResult, Validator

T = TypeVar("T")


class SearchService(ABC, Generic[T]):
    """"""
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            data_set: List[T],
            context: SearchContext,
            context_validator: Validator[SearchContext]
    ) -> SearchResult[[T]]:
        pass

    
    