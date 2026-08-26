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

from domain import CollectableModel, SearchContext

T = TypeVar("T", bound="CollectableModel")


class ModelSearchContext(SearchContext[T], ABC, Generic[T]):
    """
    Role:
        - Option Selector

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