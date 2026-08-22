# src/domain/schema/ruleset/schema.py

"""
Module: domain.schema.ruleset.schema
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum
from typing import Dict

from topology.pattern import TraversalSignature


class Ruleset(Enum):
    def __new__(
            cls,
            entries: Dict[str: TraversalSignature],
    ):
        """
        Args:
            entries: Dict[str: TraversalPattern]
        """
        obj = object.__new__(cls)
        obj._entry = Dict[str: TraversalSignature]
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
    def entries(self) -> Dict[str: TraversalSignature]:
        return self._entry
    

