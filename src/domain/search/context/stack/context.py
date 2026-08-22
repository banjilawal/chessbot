# src/domain/search/stack/context/context.py

"""
Module: domain.search.stack.context.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar
from abc import ABC

from domain import Model, SearchContext

T = TypeVar("T", bound="Model")


class StackSearchContext(SearchContext, ABC, Generic[T]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply an attribute-value tuple for selecting an execution path.
                
    Attributes:
        id: Optional[int]
        name: Optional[str]
        max_enabled_toggles: Optional[int]
        
    Provides:
        -   to_dict() -> Dict[str, Any]
        
    Super Class:
    
    Notes:
        1.  Attribute is an entity's property.
        2.  Attribute is routing key.
        3.  Execution logic performed on attribute value.
        
        4.  Why Not Union:
                Used optional attributes with null default values instead of a union type because:
                    -   It's easier to extend
                    -   Implementations can decide if context can be mutually exclusive or not.
                    -   Unions are clunky if there are many attributes.
                    -   Unions don't lower validation and build integrity overhead.
    """
    pass