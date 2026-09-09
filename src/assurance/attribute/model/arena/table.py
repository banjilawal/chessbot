# src/assurance/attrribute/model/arena/table.py

"""
Module: assurance.attrribute.model.arena.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, GameValidator, PlayerValidator, PrimingValidator
from domain import Arena
from microservice import IdentityService


class ArenaHelperTable(AttributeHelperTable[Arena]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators an Arena needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        game_validator: GameValidator
        player_validator: PlayerValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _game_validator: GameValidator
    _player_validator: PlayerValidator
    
    def __init__(
            self,
            game_validator: Optional[GameValidator] | None = None,
            player_validator: Optional[PlayerValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            game_validator: Optional[GameValidator]
            player_validator: Optional[PlayerValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._game_validator = game_validator or GameValidator()
        self._player_validator = player_validator or PlayerValidator()
        
    @property
    def game_validator(self) -> GameValidator:
        return self._game_validator
    
    @property
    def player_validator(self) -> PlayerValidator:
        return self._player_validator