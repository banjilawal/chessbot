# src/schema/ruleset/schema.py

"""
Module: schema.ruleset.schema
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum
from typing import Dict


from space import (
    EastTraversalPattern, NorthTraversalPattern, NortheastTraversalPattern, NorthwestTraversalPattern,
    SouthTraversalPattern, SoutheastTraversalPattern,
    SouthwestTraversalPattern, TraversalPattern, WestTraversalPattern
)


class Ruleset(Enum):
    def __new__(
            cls,
            entries: Dict[str: TraversalPattern],
    ):
        """
        Args:
            entries: Dict[str: TraversalPattern]
        """
        obj = object.__new__(cls)
        obj._entry = Dict[str: TraversalPattern]
        return obj
    
    BISHOP = (
        {
            "northeast": NortheastTraversalPattern(),
            "northwest": NorthwestTraversalPattern(),
            "southeast": SoutheastTraversalPattern(),
            "southwest": SouthwestTraversalPattern(),
        }
    ),
    QUEEN = (
        "queen",
        {
            "northeast": NortheastTraversalPattern(),
            "northwest": NorthwestTraversalPattern(),
            "southeast": SoutheastTraversalPattern(),
            "southwest": SouthwestTraversalPattern(),
            "north": NorthTraversalPattern(),
            "east": EastTraversalPattern(),
            "south": SouthTraversalPattern(),
            "west": WestTraversalPattern(),
        }
    ),
    ROOK = (
        "rook",
        {
            "north": NorthTraversalPattern(),
            "east": EastTraversalPattern(),
            "south": SouthTraversalPattern(),
            "west": WestTraversalPattern(),
        }
    ),
    
    @property
    def entries(self) -> Dict[str: TraversalPattern]:
        return self._entry
    

