# src/toolkit/builder/model/model/square/toolkit.py

"""
Module: toolkit.builder.model.model.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict, List, cast

from model import Square
from model import ModelModel


class SquareModel(ModelModel[Square]):
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
        Model
    """
    
    def __init__(self, origin: Square,destination: Square,):
        """
        Args:
            origin: Square
            destination: Square
        """
        super().__init__(a=origin, b=destination)
    
    @property
    def a(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def b(self) -> Square:
        return cast(Square, super().b)
    
    @property
    def origin(self) -> Square:
        return cast(Square, super().a)
    
    @property
    def destination(self) -> Square:
        return cast(Square, self.b)

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
        if isinstance(other, SquareModel):
            return (
                    self._origin == other.origin and
                    self._destination == other.destination
            )
    
