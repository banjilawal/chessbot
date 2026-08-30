# src/domain/structure/register/square/structure.py

"""
Module: domain.structure.register.square.structure
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, cast

from domain import Register, Square


class SquareRegister(Register[Square]):
    """
    Role:
        - Model
        -  Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        origin: Square
        destination: Square
        origin_is_destination: bool
        origin_is_not_destination: bool
            
    Provides:

    Super Class:
        Register
    """
    
    def __init__(self, origin: Square,destination: Square,):
        """
        Args:
            origin: Square
            destination: Square
        """
        super().__init__(a=origin, b=destination)
    
    @property
    def origin(self) -> Square:
        return cast(Square, super().a)
    
    @property
    def a(self) -> Square:
        return self.origin
    
    @property
    def destination(self) -> Square:
        return cast(Square, super().b)
    
    @property
    def b(self) -> Square:
        return self.destination

    @property
    def origin_is_destination(self) -> bool:
        return self.origin == self.destination
    
    @property
    def origin_is_not_destination(self) -> bool:
        return not self.origin_is_destination
    
    @property
    def to_list(self) -> List[Square]:
        return [self.origin, self.destination]
    
    @property
    def to_dict(self) -> Dict[str, Square]:
        return {
            "origin": self.origin,
            "destination": self.destination,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareRegister):
            return (
                    self.origin == other.origin and
                    self.destination == other.destination
            )
    
