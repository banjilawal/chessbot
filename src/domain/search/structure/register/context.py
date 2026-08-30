# src/domain/search/structure/node/context.py

"""
Module: domain.search.structure.node.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar
from abc import ABC


from domain import Structure, StructureContext

T = TypeVar("T", bound="Structure")


class NodeContext(StructureContext[T], ABC, Generic[T]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply a Node attribute-value tuple used to search a NodeChain.
                
    Attributes:
        offset Optional[int]
        
    Provides:
        - to_dict() -> Dict[str, Any]
        
    Super Class:
        Context
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