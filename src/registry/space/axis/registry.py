# src/space/reservoir/axis/space.py

"""
Module: space.reservoir.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from model import Vector
from geometry.space import Axis, EastAxis, NorthAxis, SouthAxis, SpaceReservoir, WestAxis

class AxisReservoir(SpaceReservoir[Axis]):
    """
    Role:
        -   Selection
        -   Iterator
        -   Routing Mask

    Responsibilities:
        1.  Implement SpaceReservoir for type-preserving iteration through an origin's axes.

    Attributes:
        size: int
        origin: Vector
        iterator: iter
        is_empty: bool
        is_not_empty: bool
        
        east: Optional[EastAxis]
        north: Optional[NorthAxis]:
        south: Optional[SouthAxis]:
        west: Optional[WestAxis]:

    Provides:

    Super Class:
        SpaceReservoir
        
    Note:
        -   When the iterator is used, each item it produces must be cast to the correct type.
    """
    
    _reservoir: Dict[str, Axis]
    
    def __init__(self, origin: Vector,):
        super().__init__(origin=origin)
        
        self._reservoir = {
            "east_axis": EastAxis(self.origin),
            "north_axis": NorthAxis(self.origin),
            "south_axis": SouthAxis(self.origin),
            "west_axis": WestAxis(self.origin),
        }
    
    @property
    def size(self) -> int:
        return len(self._reservoir)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def east(self) -> Optional[EastAxis]:
        return cast(EastAxis, self._reservoir["east_axis"])
    
    @property
    def north(self) -> Optional[NorthAxis]:
        return cast(NorthAxis, self._reservoir["north_axis"])
    
    @property
    def south(self) -> Optional[SouthAxis]:
        return cast(SouthAxis, self._reservoir["east_axis"])
    
    @property
    def west(self) -> Optional[WestAxis]:
        return cast(WestAxis, self._reservoir["west_axis"])
    
    @property
    def space_type_dict(self) -> Dict[Type[Axis], Axis]:
        return {
            Type[EastAxis]: self.east,
            Type[NorthAxis]: self.north,
            Type[SouthAxis]: self.south,
            Type[WestAxis]: self.west,
        }
    

