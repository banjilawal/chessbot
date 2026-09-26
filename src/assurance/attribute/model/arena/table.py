# src/assurance/attrribute/model/arena/table.py

"""
Module: assurance.attrribute.model.arena.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable, PrimingValidator
from client import GameValidationResponseService, PlayerValidationResponseService
from domain import Arena
from microservice import IdentityService


class ArenaHelperTable(ModelHelperTable[Arena]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients an Arena needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        game_client: GameValidatorClient
        player_client: PlayerValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _game_client: GameValidationResponseService
    _player_client: PlayerValidationResponseService
    
    def __init__(
            self,
            game_client: Optional[GameValidationResponseService] | None = None,
            player_client: Optional[PlayerValidationResponseService] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            game_client: Optional[GameValidatorClient]
            player_client: Optional[PlayerValidatorClient]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._game_client = game_client or GameValidationResponseService()
        self._player_client = player_client or PlayerValidationResponseService()
        
    @property
    def game_client(self) -> GameValidationResponseService:
        return self._game_client
    
    @property
    def player_client(self) -> PlayerValidationResponseService:
        return self._player_client