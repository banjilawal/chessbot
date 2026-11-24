# src/domain/context/struct/node/vector/context.py

"""
Module: domain.context.struct.node.vector.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import NodeContext, Vector, VectorNode


class VectorNodeContext(NodeContext[VectorNode]):
        """
        Role:
            - Option Selector
    
        Responsibilities:
            1.  Supply a Node attribute-value tuple used to search a NodeChain.
    
        Attributes:
            x: Optional[int]
            y: Optional[int]
    
        Provides:
            - to_dict() -> Dict[str, Any]
    
        Super Class:
            NodeContext
        """
        _x: Optional[int]
        _y: Optional[int]
        _vector: Optional[Vector]

        
        def __init__(
            self,
            x: Optional[int] | None = None,
            y: Optional[int] | None = None,
            offset: Optional[int] | None = None,
            vector: Optional[Vector] | None = None,
        ):
            """
            Args:
                x: Optional[int]
                y: Optional[int]
                offset: Optional[int]
                vector: Optional[Vector]
            """
            super().__init__(offset=offset)
            self._x = x
            self._y = y
            self._vector = vector
        
        @property
        def x(self) -> Optional[int]:
            return self._x
        
        @property
        def y(self) -> Optional[int]:
            return self._y
        
        @property
        def vector(self) -> Optional[Vector]:
            return self._vector
    
        @property
        def to_dict(self) -> Dict[str, Any]:
            return {
                "x:": self._x,
                "y": self._y,
                "offset": self.offset,
                "vector": self._vector,
            }