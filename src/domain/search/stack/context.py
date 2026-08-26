# src/domain/search/stack/context.py

"""
Module: domain.search.stack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar
from abc import ABC

from domain import DataModel, SearchContext

T = TypeVar("T", bound="DataModel")


class StackSearchContext(SearchContext, ABC, Generic[T]):
    """
    Role:
        -   Selection
        -   Routing mask

    Responsibilities:
        1.  Supply the criteria a StackSearcher uses to find a hit in a StackService.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        max_activated_filters: int

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        SearchContext
    """
    pass