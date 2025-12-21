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


class SchemaSuperKey(Context[Schema]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    1.  Define a SuperKey from a attribute-value pair. The Super
    1.  Provide an SchemaLookup with a hash key-value to use in forward Schema entry lookups.
        1.  Run forward lookups on the Schema hashtable to find a Team's play_directive_metadata for a game.
    2.  Indicate there is no play_directive for a given key-value pair by returning an exception to the caller.
    3.  Verifies correctness of key-value map before running the forward lookup.

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