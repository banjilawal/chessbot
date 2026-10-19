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
from exchange import GameValidationService, PlayerValidationService


class ArenaWrapperDependency(ModelWrapperDependency[Arena]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy ArenaValidator's ResponseWrapper dependencies.

    Attributes:
        game: GameValidationServer
        player: PlayerValidationServer

    Provides:

    Super Class:
        ModelWrapperDependency
    """
    
    _game: GameValidationService
    _player: PlayerValidationService
    
    def __init__(
            self,
            game: Optional[GameValidationService] | None = None,
            player: Optional[PlayerValidationService] | None = None,
    ):
        """
        Args:
            game: Optional[GameValidatorClient]
            player: Optional[PlayerValidatorClient]
        """
        super().__init__()
        self._game = game or GameValidationService()
        self._player = player or PlayerValidationService()
        
    @property
    def game(self) -> GameValidationService:
        return self._game
    
    @property
    def player(self) -> PlayerValidationService:
        return self._player