# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import SquareNullException
from model import EntityRegister, Square


class SquareEntityRegister(EntityRegister[Square]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Square
        null_exception: SquareNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Square = Type[Square],
            null_exception: SquareNullException = SquareNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Square:
        return cast(Square, self.a)
    
    @property
    def null_exception(self) -> SquareNullException:
        return cast(SquareNullException, self.null_exception)
    
    @property
    def square(self) -> Square:
        return self.model
    
    @property
    def is_square_entity_register(self) -> bool:
        return isinstance(self, SquareEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SquareEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
