# src/topology/registry/space/quadrant/space.py

"""
Module: topology.registry.space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, Type, cast

from domain.model import Vector
from topology.space import (
    Quadrant, NortheastQuadrant, NorthwestQuadrant, SoutheastQuadrant, SpaceReservoir, SouthwestQuadrant
)

class QuadrantReservoir(SpaceReservoir[Quadrant]):
    """
    Role:
        -   Selection
        -   Iterator
        -   Routing Mask

    Responsibilities:
        1.  Implement SpaceReservoir for type-preserving iteration through an origin's quadrants.

    Attributes:
        size: int
        origin: Vector
        iterator: iter
        is_empty: bool
        is_not_empty: bool

        northeast: Optional[NortheastQuadrant]
        northwest: Optional[NorthwestQuadrant]:
        southeast: Optional[SouthEastQuadrant]:
        southwest: Optional[SouthWestQuadrant]:

    Provides:

    Super Class:
        SpaceReservoir
    """
    _reservoir: Dict[str, Quadrant]
    
    def __init__(self, origin: Vector,):
        super().__init__(origin=origin)
        
        self._reservoir = {
            "northeast_quadrant": NortheastQuadrant(self.origin),
            "northwest_quadrant": NorthwestQuadrant(self.origin),
            "southeast_quadrant": SoutheastQuadrant(self.origin),
            "southwest_quadrant": SouthwestQuadrant(self.origin),
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
    def iterator(self) -> iter:
        quadrants: List[Quadrant] = []
        for key in self._reservoir:
            quadrants.append(self._reservoir[key])
        return quadrants.__iter__()
    
    @property
    def northeast(self) -> NortheastQuadrant:
        return cast(NortheastQuadrant, self._reservoir["northeast_quadrant"])
    
    @property
    def northwest(self) -> NorthwestQuadrant:
        return cast(NorthwestQuadrant, self._reservoir["northwest_quadrant"])
    
    @property
    def southeast(self) -> SoutheastQuadrant:
        return cast(SoutheastQuadrant, self._reservoir["southeast_quadrant"])
    
    @property
    def southwest(self) -> SouthwestQuadrant:
        return cast(SouthwestQuadrant, self._reservoir["southwest_quadrant"])
    
    @property
    def space_type_dict(self) -> Dict[Type[Quadrant], Quadrant]:
        return {
            Type[NortheastQuadrant]: self.northeast,
            Type[NorthwestQuadrant]: self.northwest,
            Type[SoutheastQuadrant]: self.southeast,
            Type[SouthwestQuadrant]: self.southwest,
        }
        
        
    

