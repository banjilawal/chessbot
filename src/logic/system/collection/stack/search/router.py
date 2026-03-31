# src/logic/system/collection/stack/search/exception.py

"""
Module: logic.system.collection.stack.search.searcher
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from abc import abstractmethod
from typing import TypeVar, List

from logic.system import Context, SearchRouter, Validator, SearchResult

T = TypeVar("T")


class StackSearchRouter(SearchRouter[T]):
    """"""
    
    @classmethod
    @abstractmethod
    def route(
            cls,
            dataset: List[T],
            context: Context[T],
            context_validator: Validator[Context[T]]
    ) -> SearchResult[List[T]]:
        pass