# src/domain/search/model/context.py

"""
Module: domain.search.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar
from abc import ABC

from domain import SearchableModel, SearchContext

T = TypeVar("T", bound="SearchableModel")


class ModelSearchContext(SearchContext[T], ABC, Generic[T]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply an attribute-value tuple used to search a StackService.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        max_activated_filters: int

    Provides:
        - def to_dict() -> Dict[str, Any]

    Super Class:
        SearchContext
    """
    pass
    