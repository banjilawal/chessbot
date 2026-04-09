# src/logic/schema/key/key.py

# src/model/context/schema/init.py

"""
Module: model.context.schema.init
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from future import annotations

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
        1.  Supply a Schema attribute-value search filter.

Attributes:
        name: Optional[str]
        color: Optional[GameColor]

    Provides:
        -   todict() -> Dict[str, Any]

    Super Class:
        Context
    """
    name: Optional[str] = None
    color: Optional[GameColor] = None

    @property
    def todict(self) -> Dict[str, Any]:
        return {
            "schema": self.name,
            "color": self.color,
        }