# src/assurance/depend/wrapper/model/game/depend.py

"""
Module: assurance.depend.wrapper.model.game.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Game
from exchange import (
    ArenaValidationServer, PlayerBinderValidationServer,
    PlayerValidationServer
)


class GameWrapperDependency(ModelWrapperDependency[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy GameValidator's ResponseWrapper dependencies.

    Attributes:
        arena: ArenaValidationServer
        binder: PlayerBinderValidationServer
        
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _arena: ArenaValidationServer
    _binder: PlayerBinderValidationServer
    
    def __init__(
            self,
            arena: Optional[ArenaValidationServer] | None = None,
            binder: Optional[PlayerBinderValidationServer] | None = None,
    ):
        super().__init__()
        self._arena = arena or ArenaValidationServer()
        self._binder = binder or PlayerBinderValidationServer()
        
    @property
    def arena(self) -> ArenaValidationServer:
        return self._arena
    
    @property
    def binder(self) -> PlayerBinderValidationServer:
        return self._binder