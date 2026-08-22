# src/domain/search/context/chain/vector/context.py.py

"""
Module: domain.search.context.chain.vector.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import ChainSearchContext, Vector


class VectorNodeContext(ChainSearchContext[Vector]):
        """
        Role:
            -   Selection
            -   Routing mask
            -   Data-Holder
    
        Responsibilities:
            1.  Supply a Vector attribute-value search filter.
    
        Attributes:
            x: Optional[int]
            y: Optional[int]
    
        Provides:
            -   to_dict() -> Dict[str, Any]
    
        Super Class:
            Context
        """
        _x: Optional[int]
        _y: Optional[int]

        
        def __init__(
            self,
            x: Optional[int] | None = None,
            y: Optional[int] | None = None,
            offset: Optional[int] | None = None,
        ):
            """
            Args:
                x: Optional[int]
                y: Optional[int]
                offset: Optional[int]
            """
            super().__init__(offset=offset)
            self._x = x
            self._y = y
        
        @property
        def x(self) -> Optional[int]:
            return self._x
        
        @property
        def y(self) -> Optional[int]:
            return self._y
    
        @property
        def to_dict(self) -> Dict[str, Any]:
            return {
                "x:": self._x,
                "y": self._y,
                "offset": self.offset
            }