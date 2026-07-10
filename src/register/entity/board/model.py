# src/register/entity/py

"""
Module: register.entity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Type, cast

from err import BoardNullException
from model import EntityRegister, Board


class BoardEntityRegister(EntityRegister[Board]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: Board
        null_exception: BoardNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: Board = Type[Board],
            null_exception: BoardNullException = BoardNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> Board:
        return cast(Board, self.a)
    
    @property
    def null_exception(self) -> BoardNullException:
        return cast(BoardNullException, self.null_exception)
    
    @property
    def board(self) -> Board:
        return self.model
    
    @property
    def is_board_entity_register(self) -> bool:
        return isinstance(self, BoardEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
