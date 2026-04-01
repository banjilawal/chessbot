# src/logic/system/search/router.py

"""
Module: logic.system.search.router
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from typing import List, TypeVar, Generic

from logic.system import Query, Router, SearchResult, Validator

T = TypeVar("T")


class SearchRouter(Router, Generic[T]):
    
    @classmethod
    @abstractmethod
    def route(
            cls,
            query: Query[T],
            query_validator: Validator[Query[T]]
    ) -> SearchResult[List[T]]:
        pass