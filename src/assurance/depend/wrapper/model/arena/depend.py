# src/assurance/depend/wrapper/model/arena/depend.py

"""
Module: assurance.depend.wrapper.model.arena.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Arena
from exchange import GameValidationResponseWrapper, PlayerValidationResponseWrapper


class ArenaWrapperDependency(ModelWrapperDependency[Arena]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy ArenaValidator's ResponseWrapper dependencies.

    Attributes:
        game: GameValidationResponseWrapper
        player: PlayerValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    _game: GameValidationResponseWrapper
    _player: PlayerValidationResponseWrapper
    
    def __init__(
            self,
            game: Optional[GameValidationResponseWrapper] | None = None,
            player: Optional[PlayerValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            game: Optional[GameValidatorClient]
            player: Optional[PlayerValidatorClient]
        """
        super().__init__()
        self._game = game or GameValidationResponseWrapper()
        self._player = player or PlayerValidationResponseWrapper()
        
    @property
    def game(self) -> GameValidationResponseWrapper:
        return self._game
    
    @property
    def player(self) -> PlayerValidationResponseWrapper:
        return self._player