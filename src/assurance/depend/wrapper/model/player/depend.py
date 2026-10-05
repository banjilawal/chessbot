# src/assurance/depend/wrapper/model/player/depend.py

"""
Module: assurance.depend.wrapper.model.player.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Player
from exchange import AccountValidationResponseWrapper, GameValidationResponseWrapper


class PlayerWrapperDependency(ModelWrapperDependency[Player]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy PlayerValidator's ResponseWrapper dependencies.

    Attributes:
        game: GameValidationResponseWrapper
        account: AccountValidationResponseWrapper
    
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _game: GameValidationResponseWrapper
    _account: AccountValidationResponseWrapper
    
    def __init__(
            self,
            game: Optional[GameValidationResponseWrapper] | None = None,
            account: Optional[AccountValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            game: Optional[GameValidationResponseWrapper]
            account: Optional[AccountValidationResponseWrapper]
        """
        super().__init__()
        self._game = game or GameValidationResponseWrapper()
        self._account = account or AccountValidationResponseWrapper()
        
    @property
    def game(self) -> GameValidationResponseWrapper:
        return self._game
    
    @property
    def account(self) -> AccountValidationResponseWrapper:
        return self._account
