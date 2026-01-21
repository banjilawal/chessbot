# src/chess/system/data/collection/stack/search/searcher.py

"""
Module: chess.system.data.collection.stack.search.searcher
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import abstractmethod
from typing import TypeVar, List

from chess.system import Context, Finder, Validator, SearchResult

T = TypeVar("T")


class StackSearcher(Finder[T]):
    """"""
    
    @classmethod
    @abstractmethod
    def find(
            cls,
            dataset: List[T],
            context: Context[T],
            context_validator: Validator[Context[T]]
    ) -> SearchResult[List[T]]:
        """
        ACTION:
        PARAMETERS:
            * dataset (List[D])
            * context (Context[D)
            * context_validator (Validator[Context[D])
        RETURNS:
            SearchResult[List[R]] or Void
        Raise:
            No exception. Subclasses raise exception.
        """
        pass