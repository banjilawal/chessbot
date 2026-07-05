# src/model/register/square/model.py

"""
Module: model.register.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, List

from model import Model, Square


class SquareRegister(Model):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
            origin: Square
            destination: Square
            
    Provides:

    Super Class:
    """
    _origin: Square
    _destination: Square
    
    def __init__(self, origin: Square,destination: Square,):
        """
        Args:
            origin: Square
            destination: Square
        """
        self._origin = origin
        self._destination = destination
        
    @property
    def origin(self) -> Square:
        return self._origin
    
    @property
    def destination(self) -> Square:
        return self._destination
    
    @property
    def to_list(self) -> List[Square]:
        return [self._origin, self._destination]
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {"origin": self._origin, "destination": self._destination}
    
    @property
    def origin_is_destination(self) -> bool:
        return self._origin == self._destination
    
    @property
    def origin_is_not_destination(self) -> bool:
        return self.origin_is_destination
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareRegister):
            return (
                    self._origin == other.origin and
                    self._destination == other.destination
            )
    
