# src/space/linear/section/axis/space.py

"""
Module: space.linear.section.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


import setting


from model import Vector
from space import LinearSection


class AxisSection(LinearSection):
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfSection errors by calculating the last point in the direction
            of travel

    Attributes:

    Provides:
        -   east(origin: Vector) -> AxisSection
        -   north(origin: Vector) -> AxisSection
        -   west(origin: Vector) -> AxisSection
        -   south(origin: Vector) -> AxisSection

    Super Class:
        SpaceSection

    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
    """
    def __init__(self, origin: Vector, terminus: Vector):
        super().__init__(origin=origin, terminus=terminus)
        """INTERNAL: Use factory methods instead of direct constructor."""
    
    
    @classmethod
    def east(cls, origin: Vector) -> AxisSection:
        """
        East towards num_columns - 1 (right)
        """
        return cls(
            origin=origin,
            terminus = Vector(
                x=setting.board.dimension.config.number_of_columns - 1,
                y=origin.y,
            )
        )
    
    @classmethod
    def north(cls, origin: Vector) -> AxisSection:
        """
        North towards 0  (up)
        """
        return cls(
            origin=origin,
            terminus=Vector(x=origin.x, y=0),
        )
    
    @classmethod
    def south(cls, origin: Vector) -> AxisSection:
        """
        South towards num_rows - 1 (up)
        """
        return cls(
            origin=origin,
            terminus=Vector(
                x=origin.x,
                y=setting.board.dimension.config.number_of_rows - 1,
            )
        )
    
    @classmethod
    def west(cls, origin: Vector) -> AxisSection:
        """
        West towards 0 (left)
        """
        return cls(
            origin=Vector(x=0, y=origin.y),
            terminus=origin
        )