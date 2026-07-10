# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import CoordNullException
from operand import EntityRegister, Coord


class CoordEntityRegister(EntityRegister[Coord]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Coord
        null_exception: CoordNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            operand: Coord = Type[Coord],
            null_exception: CoordNullException = CoordNullException(),
    ):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(operand=operand, null_exception=null_exception)
        
    @property
    def operand(self) -> Coord:
        return cast(Coord, self.a)
    
    @property
    def null_exception(self) -> CoordNullException:
        return cast(CoordNullException, self.null_exception)
    
    @property
    def coord(self) -> Coord:
        return self.operand
    
    @property
    def is_coord_entity_register(self) -> bool:
        return isinstance(self, CoordEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordEntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
