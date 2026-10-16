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
from exchange import AccountValidationServer, GameValidationServer


class PlayerWrapperDependency(ModelWrapperDependency[Player]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy PlayerValidator's ResponseWrapper dependencies.

    Attributes:
        game: GameValidationServer
        account: AccountValidationServer
    
    Provides:

    Super Class:
        ModelWrapperDependency
    """
    _game: GameValidationServer
    _account: AccountValidationServer
    
    def __init__(
            self,
            game: Optional[GameValidationServer] | None = None,
            account: Optional[AccountValidationServer] | None = None,
    ):
        """
        Args:
            game: Optional[GameValidationServer]
            account: Optional[AccountValidationServer]
        """
        super().__init__()
        self._game = game or GameValidationServer()
        self._account = account or AccountValidationServer()
        
    @property
    def game(self) -> GameValidationServer:
        return self._game
    
    @property
    def account(self) -> AccountValidationServer:
        return self._account
