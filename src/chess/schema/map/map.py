# src/chess/schema/map/map.py

"""
Module: chess.schema.map.map
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.schema import Schema
from chess.system import Context, GameColor


class SchemaMap(Context[Schema]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    1.  Provide an SchemaLookup with a hash key-value to use in forward Schema entry lookups.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   color (Optional[GameColor])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _name: Optional[str]
    _color: Optional[GameColor]
    
    def __init__(
            self,
            name: Optional[str] = None,
            color: Optional[GameColor] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (Optional[str])
            *   color (Optional[Color])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=None, name=name)
        self._color = color

    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    def to_dict(self) -> dict:
        """
        # Convert the SchemaMap object to a dictionary.

        # PARAMETERS:
        None

        # Returns:
        dict

        # Raises:
        None
        """
        return {
            "name": self.name,
            "color": self._color,
        }