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
    ArenaValidationResponseWrapper, PlayerBinderValidationResponseWrapper,
    PlayerValidationResponseWrapper
)


class GameWrapperDependency(ModelWrapperDependency[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy GameValidator's ResponseWrapper dependencies.

    Attributes:
        arena: ArenaValidationResponseWrapper
        binder: PlayerBinderValidationResponseWrapper
        
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _arena: ArenaValidationResponseWrapper
    _binder: PlayerBinderValidationResponseWrapper
    
    def __init__(
            self,
            arena: Optional[ArenaValidationResponseWrapper] | None = None,
            binder: Optional[PlayerBinderValidationResponseWrapper] | None = None,
    ):
        super().__init__()
        self._arena = arena or ArenaValidationResponseWrapper()
        self._binder = binder or PlayerBinderValidationResponseWrapper()
        
    @property
    def arena(self) -> ArenaValidationResponseWrapper:
        return self._arena
    
    @property
    def binder(self) -> PlayerBinderValidationResponseWrapper:
        return self._binder