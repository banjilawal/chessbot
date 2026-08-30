# src/domain/search/model/coord/context.py

"""
Module: domain.search.model.coord
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Coord, ModelContext


class CoordContext(ModelContext[Coord]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a CoordModelSearcher uses to find a hit.

    Attributes:
        row: Optional[int]
        column: Optional[int]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    
    _row: Optional[int]
    _column: Optional[int]
    
    def __init__(
            self,
            row: Optional[int] | None = None,
            column: Optional[int] | None = None,
            max_size: int = 2
    ):
        """
        Args:
            row: Optional[int]
            column: Optional[int]
            max_size: Optional[int]
        """
        super().__init__(max_size=max_size)
        self._row = row
        self._column = column
        
    @property
    def row(self) -> Optional[int]:
        return self._row
    
    @property
    def column(self) -> Optional[int]:
        return self._column

    def to_dict(self) -> Dict[str, Any]:
        return {
            "row": self._row,
            "column": self._column,
        }
