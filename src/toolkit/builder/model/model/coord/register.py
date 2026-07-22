# src/toolkit/builder/model/model/coord/toolkit.py

"""
Module: toolkit.builder.model.model.coord.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, cast

from model import Coord
from model import ModelModel


class CoordModel(ModelModel[Coord]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        origin: Coord
        terminus: Coord
        origin_is_terminus: bool
        origin_is_not_terminus: bool
            
    Provides:

    Super Class:
        Model
    """
    _origin: Coord
    _terminus: Coord
    
    def __init__(self, origin: Coord, terminus: Coord,):
        """
        Args:
            origin: Coord
            terminus: Coord
        """
        super().__init__(a=origin, b=terminus)
        
    @property
    def origin(self) -> Coord:
        return cast(Coord, self.a)
    
    @property
    def terminus(self) -> Coord:
        return cast(Coord, self.b)

    @property
    def origin_is_terminus(self) -> bool:
        return self.origin == self.terminus
    
    @property
    def origin_is_not_terminus(self) -> bool:
        return not self.origin_is_terminus
    
    @property
    def to_list(self) -> List[Coord]:
        return [self.origin, self.terminus]
    
    @property
    def to_dict(self) -> Dict[str, Coord]:
        return {
            "origin": self.origin,
            "terminus": self.terminus,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordModel):
            return (
                    self._origin == other.origin and
                    self._terminus == other.terminus
            )
    
