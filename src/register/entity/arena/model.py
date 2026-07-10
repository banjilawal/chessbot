# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import ArenaNullException
from model import EntityRegister, Arena


class ArenaEntityRegister(EntityRegister[Arena]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Arena
        null_exception: ArenaNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Arena = Type[Arena],
            null_exception: ArenaNullException = ArenaNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Arena:
        return cast(Arena, self.a)
    
    @property
    def null_exception(self) -> ArenaNullException:
        return cast(ArenaNullException, self.null_exception)
    
    @property
    def arena(self) -> Arena:
        return self.model
    
    @property
    def is_arena_entity_register(self) -> bool:
        return isinstance(self, ArenaEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ArenaEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
