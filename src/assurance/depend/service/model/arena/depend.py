# src/assurance/depend/service/model/arena/depend.py

"""
Module: assurance.depend.service.model.arena.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Arena
from exchange import GameValidationService, PlayerValidationService


class ArenaDependency(ModelDependency[Arena]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy ArenaValidator's ResponseService dependencies.

    Attributes:
        game: GameValidationService
        player: PlayerValidationService

    Provides:

    Super Class:
        ModelDependency
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