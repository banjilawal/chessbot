# src/logic/span/ray/diagonal/provider/plane.py

"""
Module: logic.span.ray/diagonal.provider.plane
Author: Banji Lawal
Created: 2026-03-8
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from logic.coord import Coord
from logic.span import DiagonalRayFactors
from logic.system import NUMBER_OF_COLUMNS, NUMBER_OF_ROWS

class DiagonalPlaneFactors:
    """
    # ROLE: Data-Holder, Utility
    # TASK: Provide solution sets

    # RESPONSIBILITIES:
    1.  Derive the factors for computing the ray projections from an origin to its 
            * Northeast (Quadrant 0)
            * Northwest (Quadrant 1)
            * Southwest (Quadrant 2)
            * Southeast (Quadrant 3)

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
            origin: Coord

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
            origin:

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _origin: Coord
    
    def __init__(self, origin: Coord):
        """
        Args:
            origin: Coord
        """
        self._origin = origin
        
    @property
    def origin(self) -> Coord:
        return self._origin
        
    @property
    def northeast(self) -> DiagonalRayFactors:
        """
        Action:
            1.  Produce the points northeast from the origin to the top right corner.
                from:
                    *   origin.column, origin.row
                to:
                    *   NUMBER_OF_COLUMNS-1, 0
            2.  Increments
                    *   x-coordinate by 1 to get to the end of the columns.
                    *   y-coordinate by -1 to get to the first row.
        """
        return DiagonalRayFactors(
            start_x=self._origin.column,
            end_x=NUMBER_OF_COLUMNS-1,
            x_step=1,
            end_y=0,
            slope=-1,
        )
    
    @property
    def northwest(self) -> DiagonalRayFactors:
        """
        Action:
            1.  Produce the points northwest from the origin to the top left corner.
                from:
                    *   origin.column, origin.row
                to:
                    *    first column, first row
            2.  Decrements
                    *   x-coordinate by 1 to get to the first column.
                    *   y-coordinate by 1 to get to the first row.
        """
        return DiagonalRayFactors(
            start_x=self._origin.column,
            end_x=0,
            x_step=-1,
            end_y=0,
            slope=-1,
        )
    
    @property
    def southwest(self) -> DiagonalRayFactors:
        """
        Action:
            1.  Produce the points southwest from the origin to the bottom left corner.
                from:
                    *   origin.column, origin.row
                to:
                    *   first column, last row
            2.  Increments
                    *   x-coordinate by -1 to get to the first column.
                    *   y-coordinate by 1 to get to the first row.
        """
        return DiagonalRayFactors(
            start_x=self._origin.column,
            end_x=0,
            x_step=-1,
            end_y=NUMBER_OF_ROWS-1,
            slope=1,
        )
    
    @property
    def southeast(self) -> DiagonalRayFactors:
        """
        Action:
            1.  Produce the points southeast from the origin to the bottom right corner.
                from:
                    *   origin.column, origin.row
                to:
                    *   last column, last row
            2.  Decrements
                    *   x-coordinate by 1 to get to the end of the columns.
                    *   y-coordinate by 1 to get to the first row.
        """
        return DiagonalRayFactors(
            start_x=self._origin.column,
            end_x=NUMBER_OF_COLUMNS-1,
            x_step=1,
            end_y=NUMBER_OF_ROWS - 1,
            slope=1,
        )
    
    @property
    def to_list(self) -> list[DiagonalRayFactors]:
        """
        Create a list of projections from origin to the four corners.
        """
        return [self.northeast, self.northwest, self.southwest, self.southeast]
    
    @property
    def hash(self) -> Dict[str, DiagonalRayFactors]:
        """
        Create a hash of the projections from origin to the four corners.
        """
        return {
            "northeast": self.northeast,
            "northwest": self.northwest,
            "southwest": self.southwest,
            "southeast": self.southeast,
        }