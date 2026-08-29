# src/domain/metadata/blueprint/search/vector/context.py

"""
Module: domain.metadata.blueprint.search.vector
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Vector, ModelSearchContext


class VectorSearchContext(ModelSearchContext[Vector]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a VectorModelSearcher uses to find a hit.

    Attributes:
        y: Optional[int]
        x: Optional[int]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelSearchContext
    """
    _x: Optional[int]
    _y: Optional[int]
    
    def __init__(
            self,
            x: Optional[int] | None = None,
            y: Optional[int] | None = None,
    ):
        """
        Args:
            y: Optional[int]
            x: Optional[int]
        """
        super().__init__()
        self._y = y
        self._x = x
        
    @property
    def y(self) -> Optional[int]:
        return self._y
    
    @property
    def x(self) -> Optional[int]:
        return self._x

    def to_dict(self) -> Dict[str, Any]:
        return {
            "y": self._y,
            "x": self._x,
        }
