# src/logic/schema/key/key.py

# src/model/context/schema/__init__.py

"""
Module: model.context.schema.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from model.catalog import Schema
from model import Context
from system import GameColor


class SchemaContext(Context[Schema]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Schema attribute-value tuple which selects an execution path.

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
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema": self.name,
            "color": self._color,
        }