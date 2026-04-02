# src/logic/schema/database/search/context/model/context.py

"""
Module: logic.schema.database.search.context.model.context
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from logic.schema import Schema
from logic.system import Context, GameColor, LoggingLevelRouter


class SchemaContext(Context[Schema]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Schema attribute-value pair for a worker's execution path routing.

    Attributes:
        name: Optional[str]
        color: Optional[GameColor]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _name: Optional[str]
    _color: Optional[GameColor]
    
    @LoggingLevelRouter.monitor
    def __init__(
            self,
            name: Optional[str] = None,
            color: Optional[GameColor] = None,
    ):
        """
        Args:
            name: Optional[str]
            color: Optional[GameColor]
        """
        super().__init__(id=None, name=name)
        self._color = color
    
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    def to_dict(self) -> {}:
        return {
            "name": self.name,
            "color": self._color,
        }