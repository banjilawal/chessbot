# src/register/model/square/register.py

"""
Module: register.model.square.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List

from model import Square
from register import ModelRegister


class SquareRegister(ModelRegister[Square]):
    """
    Role:
        -   Model
        -   Data Holder

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
    _origin: Square
    _destination: Square
    
    def __init__(self, origin: Square,destination: Square,):
        """
        Args:
            origin: Square
            destination: Square
        """
        super().__init__(a=origin, b=destination)
        
    @property
    def origin(self) -> Square:
        return self.a
    
    @property
    def destination(self) -> Square:
        return self.b

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
                    self._origin == other.origin and
                    self._destination == other.destination
            )
    
