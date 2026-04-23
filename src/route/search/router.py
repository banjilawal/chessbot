# src/logic/system/search/resource/route/router.py

"""
Module: logic.system.search.resource.route.router
Author: Banji Lawal
Created: 2026-03-31
Version: 1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from typing import List, TypeVar, Generic

from operation import Validator
from model.query import Query
from result import SearchResult
from route import Router

T = TypeVar("T")


class SearchRouter(Router, Generic[T]):
    """
    Role
        -   Routing
        -   Stateless Search Engine

   Responsibilities:
        1.  Process a search query which contains:
                -   The dataset
                -   Search criteria
        2.  Authoritative single-source-of-truth for search results.

    Attributes:

    Provides:
        -   def route(
                    query: Query[T],
                    query_validator: Validator[Query[T]]
            ) -> SearchResult[List[T]]

     Super Class:
         Builder
     """
    
    @classmethod
    @abstractmethod
    def route(
            cls,
            query: Query[T],
            query_validator: Validator[Query[T]]
    ) -> SearchResult[List[T]]:
        pass