# src/chess/team/schema/lookup/context/context.py

"""
Module: chess.team.schema.lookup.context.context
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import Optional

from chess.team import TeamSchema
from chess.system import Context, GameColor


class SchemaContext(Context[TeamSchema]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provide an TeamSchemaFinder with an attribute value to find TeamSchemas with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
        *   SchemaContext

    # LOCAL ATTRIBUTES:
        *   color (Optional[ColorColor])

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
            *   designation (Optional[str])
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
        # Convert the SchemaContext object to a dictionary.

        # PARAMETERS:
        None

        # Returns:
        dict

        # Raises:
        None
        """
        return {
            "designation": self.name,
            "color": self._color,
        }