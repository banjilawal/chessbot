# src/assurance/depend/service/model/game/depend.py

"""
Module: assurance.depend.service.model.game.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Game
from exchange import (
    ArenaValidationService, PlayerBinderValidationService,
    PlayerValidationService
)


class GameDependency(ModelDependency[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy GameValidator's ResponseService dependencies.

    Attributes:
        arena: ArenaValidationService
        binder: PlayerBinderValidationService
        
    Provides:

    Super Class:
        ModelDependency
    """
    _arena: ArenaValidationService
    _binder: PlayerBinderValidationService
    
    def __init__(
            self,
            arena: Optional[ArenaValidationService] | None = None,
            binder: Optional[PlayerBinderValidationService] | None = None,
    ):
        super().__init__()
        self._arena = arena or ArenaValidationService()
        self._binder = binder or PlayerBinderValidationService()
        
    @property
    def arena(self) -> ArenaValidationService:
        return self._arena
    
    @property
    def binder(self) -> PlayerBinderValidationService:
        return self._binder