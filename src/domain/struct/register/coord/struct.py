# src/domain/struct/register/coord/struct.py

"""
Module: domain.struct.register.coord.register
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, cast

from domain import Coord, Register


class CoordRegister(Register[Coord]):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        origin: Coord
        destination: Coord
        origin_same_as_destination: bool
        origin_differs_from_destination: bool
            
    Provides:

    Super Class:
        Register
    """
    
    def __init__(self, origin: Coord, destination: Coord,):
        """
        Args:
            origin: Coord
            destination: Coord
        """
        super().__init__(a=origin, b=destination)
        
    @property
    def origin(self) -> Coord:
        return cast(Coord, super().a)
    
    @property
    def a(self) -> Coord:
        return self.origin
    
    @property
    def destination(self) -> Coord:
        return cast(Coord, super().b)
    
    @property
    def b(self) -> Coord:
        return self.destination

    @property
    def origin_is_destination(self) -> bool:
        return self.origin == self.destination
    
    @property
    def origin_is_not_destination(self) -> bool:
        return not self.origin_is_destination
    
    @property
    def to_list(self) -> List[Coord]:
        return [self.origin, self.destination]
    
    @property
    def to_dict(self) -> Dict[str, Coord]:
        return {
            "origin": self.origin,
            "destination": self.destination,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordRegister):
            return (
                    self._origin == other.origin and
                    self._destination == other.destination
            )
        return False
    
