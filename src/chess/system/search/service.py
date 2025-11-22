from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from chess.system import Search, SearchContext, SearchResult

T = TypeVar("T")


class SearchService(ABC, Generic[T]):
    """"""
    
    @classmethod
    @abstractmethod
    def search(cls, data_set: List[T], search_context: SearchContext, **kwargs) -> SearchResult[[T]]:
        pass

    
    