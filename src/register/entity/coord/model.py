# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import CoordNullException
from model import EntityRegister, Coord


class CoordEntityRegister(EntityRegister[Coord]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Coord
        null_exception: CoordNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Coord = Type[Coord],
            null_exception: CoordNullException = CoordNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Coord:
        return cast(Coord, self.a)
    
    @property
    def null_exception(self) -> CoordNullException:
        return cast(CoordNullException, self.null_exception)
    
    @property
    def coord(self) -> Coord:
        return self.model
    
    @property
    def is_coord_entity_register(self) -> bool:
        return isinstance(self, CoordEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
