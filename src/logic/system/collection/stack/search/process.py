# src/logic/system/collection/stack/search/exception.py

"""
Module: logic.system.collection.stack.search.searcher
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import abstractmethod
from typing import TypeVar, List

from logic.system import Context, SearchProcess, Validator, SearchResult

T = TypeVar("T")


class StackSearchRouter(SearchProcess[T]):
    """"""
    
    @classmethod
    @abstractmethod
    def route(
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