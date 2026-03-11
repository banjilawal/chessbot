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
from logic.span import PerpendicularRayFactors
from logic.system import NUMBER_OF_COLUMNS, NUMBER_OF_ROWS


class PerpendicularPlaneFactors:
    """
    # ROLE: Data-Holder, Utility
    # TASK: Provide solution sets

    # RESPONSIBILITIES:
    1.  Derive the factors for computing the ray projections from an origin to its
            * North (0,j)
            * West (-i, 0)
            * South (0, -j)
            * East (i, 0)

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
        self._origin = origin
    
    @property
    def origin(self) -> Coord:
        return self._origin
        
    @property
    def north(self) -> PerpendicularRayFactors:
        """
        Action:
            1.  Produce the points north of the origin.
                from:
                    *   origin.column, origin.row
                to:
                    *   origin.column, 0
            2.  Increments
                    *   y-coordinate by -1 to get to the first row.
                    *   x-coordinate is constant
        """
        return PerpendicularRayFactors(
            start_x=self._origin.column,
            end_x=self._origin.column,
            x_step=0,
            start_y=self._origin.row,
            end_y=0,
            y_step=-1,
        )
    
    @property
    def west(self) -> PerpendicularRayFactors:
        """
        Action:
            1.  Produce the points west from the origin.
                from:
                    *   origin.column, origin.row
                to:
                    *   0, origin.row
            2.  Increments
                    *   x-coordinate by -1 to get to the first column.
                    *   y-coordinate is constant
        """
        return PerpendicularRayFactors(
            start_x=0,
            end_x=self._origin.column,
            x_step=-1,
            start_y=self._origin.row,
            end_y=self._origin.row,
            y_step=0,
        )
    
    @property
    def south(self) -> PerpendicularRayFactors:
        """
        Action:
            1.  Produce the points south of the origin.
                from:
                    *   origin.column, origin.row
                to:
                    *   origin.column, NUMBER_OF_ROWS - 1
            2.  Increments
                    *   y-coordinate by 1 to get to the last row.
                    *   x-coordinate is constant
        """
        return PerpendicularRayFactors(
            start_x=self._origin.column,
            end_x=self._origin.column,
            x_step=0,
            start_y=self._origin.row,
            end_y=NUMBER_OF_ROWS - 1,
            y_step=1,
        )
    
    @property
    def east(self) -> PerpendicularRayFactors:
        """
        Action:
            1.  Produce the points east from the origin.
                from:
                    *   origin.column, origin.row
                to:
                    *   origin.row, NUMBER_OF_COLUMNS - 1
            2.  Increments
                    *   x-coordinate by 1 to get to the last column.
                    *   y-coordinate is constant
        """
        return PerpendicularRayFactors(
            start_x=self._origin.column,
            end_x=NUMBER_OF_COLUMNS - 1,
            x_step=1,
            start_y=self._origin.row,
            end_y=self._origin.row,
            y_step=0,
        )
    
    @property
    def to_list(self) -> list[PerpendicularRayFactors]:
        """
        Create a list of projections from origin to the four corners.
        """
        return [self.north, self.west, self.south, self.east]
    
    @property
    def hash(self) -> Dict[str, PerpendicularRayFactors]:
        """
        Create a hash of the projections from origin to the four corners.
        """
        return {
            "north": self.north,
            "west": self.west,
            "south": self.south,
            "east": self.east,
        }