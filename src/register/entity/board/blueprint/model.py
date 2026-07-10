# src/model/register/entity/board/blueprint/model.py

"""
Module: model.register.entity.board.blueprint.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type, cast

from blueprint import BoardBlueprint
from err import BoardBlueprintNullException
from model import EntityRegister


class BoardBlueprintEntityRegister(EntityRegister[BoardBlueprint]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the model and null_exception for an entity.

    Attributes:
        model: BoardBlueprint
        null_exception: BoardBlueprintNullException
            
    Provides:

    Super Class:
    """
    
    def __init__(
            self,
            model: BoardBlueprint = Type[BoardBlueprint],
            null_exception: BoardBlueprintNullException = BoardBlueprintNullException(),
    ):
        """
        Args:
            model: Model
            null_exception: NullException
        """
        super().__init__(model=model, null_exception=null_exception)
        
    @property
    def model(self) -> BoardBlueprint:
        return cast(BoardBlueprint, self.model)
    
    @property
    def null_exception(self) -> BoardBlueprintNullException:
        return cast(BoardBlueprintNullException, self.null_exception)
    
    @property
    def is_board_blueprint_entity_register(self) -> bool:
        return isinstance(self, BoardBlueprintEntityRegister)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BoardBlueprintEntityRegister):
            return (
                    self.model == other.model and
                    self.null_exception == other.null_exception
            )
    
