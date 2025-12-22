# src/chess/schema/map/key.py

"""
Module: chess.schema.map.key
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.schema import Schema
from chess.system import Context, GameColor


class SchemaSuperKey(Context[Schema]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    1.  Define a SuperKey from an attribute-value pair. The attribute must exist in the schema.
    2.  A forward lookup for a Schema variant requires a SchemaSuperKey.

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
        # Convert the SchemaSuperKey object to a dictionary.

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