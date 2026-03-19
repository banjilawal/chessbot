# src/logic/system/collection/stack/search/process.py

"""
Module: logic.system.collection.stack.search.searcher
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import abstractmethod
from typing import TypeVar, List

from logic.system import Context, SearchProcess, ValidationProcess, SearchResult

T = TypeVar("T")


class StackSearchProcess(SearchProcess[T]):
    """"""
    
    @classmethod
    @abstractmethod
    def find(
            cls,
            dataset: List[T],
            context: Context[T],
            context_validator: ValidationProcess[Context[T]]
    ) -> SearchResult[List[T]]:
        """
        ACTION:
        PARAMETERS:
            * dataset (List[D])
            * context (Context[D)
            * context_validator (ValidationProcess[Context[D])
        RETURNS:
            SearchResult[List[R]] or Void
        Raise:
            No exception. Subclasses raise exception.
        """
        pass