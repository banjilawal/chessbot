# src/assurance/attrribute/model/game/table.py

"""
Module: assurance.attrribute.model.game.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, PlayerValidator, PrimingValidator
from domain import Game
from microservice import IdentityService


class GameHelperTable(AttributeHelperTable[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators an Game needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        player_validator: PlayerValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _player_validator: PlayerValidator
    
    def __init__(
            self,
            player_validator: Optional[PlayerValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            player_validator: Optional[PlayerValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._player_validator = player_validator or PlayerValidator()
    
    @property
    def player_validator(self) -> PlayerValidator:
        return self._player_validator