# src/chess/coord/context/context

"""
Module: chess.coord.context.context
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.system import Context


class CoordContext(Context[Coord]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provide an CoordFinder with an attribute-value which finds Coords which match the targeted attribute-value.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   row (Optional[int])
        *   coord (Optional[Coord])
        *   column (Optional[int])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _row: Optional[int] = None
    _coord: Optional[Coord] = None
    _column: Optional[int] = None
    
    def __init__(
            self,
            row: Optional[int] = None,
            coord: Optional[Coord] = None,
            column: Optional[int] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   row (Optional[int])
            *   coord (Optional[Coord])
            *   column (Optional[int])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=None, name=None)
        self._row = row
        self._coord = coord
        self._column = column
    
    @property
    def row(self) -> Optional[int]:
        return self._row
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def column(self) -> Optional[int]:
        return self._column
    
    def to_dict(self) -> dict:
        """
        # Convert the CoordContext object to a dictionary.

        # PARAMETERS:
        None

        # Returns:
        dict

        # Raises:
        None
        """
        method = "CoordContext.to_dict"
        return {
            "row": self._row,
            "coord": self._coord,
            "column": self._column,
        }
