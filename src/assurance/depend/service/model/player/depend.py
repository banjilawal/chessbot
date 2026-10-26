# src/assurance/depend/service/model/player/depend.py

"""
Module: assurance.depend.service.model.player.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelDependency
from domain import Player
from exchange import AccountValidationService, GameValidationService


class PlayerDependency(ModelDependency[Player]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy PlayerValidator's ResponseService dependencies.

    Attributes:
        game: GameValidationService
        account: AccountValidationService
    
    Provides:

    Super Class:
        ModelDependency
    """
    _game: GameValidationService
    _account: AccountValidationService
    
    def __init__(
            self,
            game: Optional[GameValidationService] | None = None,
            account: Optional[AccountValidationService] | None = None,
    ):
        """
        Args:
            game: Optional[GameValidationService]
            account: Optional[AccountValidationService]
        """
        super().__init__()
        self._game = game or GameValidationService()
        self._account = account or AccountValidationService()
        
    @property
    def game(self) -> GameValidationService:
        return self._game
    
    @property
    def account(self) -> AccountValidationService:
        return self._account
