#  src/domain/metadata/blueprint/context/graph/context.py

"""
Module: domain.metadata.blueprint.context.graph
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar
from abc import ABC

from domain import GraphComponent
from domain import Node, SearchContext

T = TypeVar("T", bound="GraphComponent")


class GraphSearchContext(SearchContext, ABC, Generic[T]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply an attribute-value tuple used to search a collection.
                
    Attributes:
        offset Optional[int]
        
    Provides:
        -  to_dict() -> Dict[str, Any]
        
    Super Class:
    
    Notes:
        1.  Attribute is an entity's property.
        2.  Attribute is routing key.
        3.  Execution logic performed on attribute value.
        
        4.  Why Not Union:
                Used optional attributes with null default values instead of a union type because:
                    -  It's easier to extend
                    -  Implementations can decide if context can be mutually exclusive or not.
                    -  Unions are clunky if there are many attributes.
                    -  Unions don't lower validation and build integrity overhead.
    """
    _offset: Optional[int]
    
    def __init__(self, offset: Optional[int] = None):
        """
        Args:
            offset Optional[int]
        """
        super().__init__()
        self._offset = offset
        
    @property
    def offset(self) -> Optional[int]:
        return self._offset