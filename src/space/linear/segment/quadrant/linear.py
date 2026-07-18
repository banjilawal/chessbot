# src/space/linear/segment/quadrant/linear.py

"""
Module: space.linear.segment.quadrant.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector
from space import QuadrantTerminusEntry, LineSegment


class QuadrantSegment(LineSegment):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Prevent ArrayIndexOutOfSegment errors by calculating the upper and lower segment
            vectors of a Quadrant's incline.

    Attributes:
        terminus_entry: QuadrantTerminusEntry
        
    Provides:
        -   def northeast(cls, origin: Vector) -> QuadrantSegment
        -   def northwest(cls, origin: Vector) -> QuadrantSegment
        -   def southwest(cls, origin: Vector) -> QuadrantSegment
        -   def southeast(cls, origin: Vector) -> QuadrantSegment

    Super Class:
        SpaceSegment

    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
    """
    terminus_entry: QuadrantTerminusEntry = QuadrantTerminusEntry()
    
    def __init__(self, origin: Vector, terminus: Vector,):
        super().__init__(origin=origin, terminus=terminus)
        """INTERNAL: Use factory methods instead of direct constructor."""
        

    
    @classmethod
    def northeast(cls, origin: Vector) -> QuadrantSegment:
        return cls(
            origin=origin,
            terminus=cls.terminus_entry.northeast,
        )
    
    @classmethod
    def northwest(cls, origin: Vector) -> QuadrantSegment:
        return cls(
            origin=origin,
            terminus=cls.terminus_entry.northwest
        )
    
    @classmethod
    def southeast(cls, origin: Vector) -> QuadrantSegment:
        return cls(
            origin=origin,
            terminus=cls.terminus_entry.southeast
        )
    
    @classmethod
    def southwest(cls, origin: Vector) -> QuadrantSegment:
        return cls(
            origin=origin,
            terminus=cls.terminus_entry.southwest
        )