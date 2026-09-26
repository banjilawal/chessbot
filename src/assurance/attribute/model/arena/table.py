# src/assurance/attrribute/model/arena/table.py

"""
Module: assurance.attrribute.model.arena.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelValidationWrapperDict, PrimingValidator
from client import GameValidationResponseWrapper, PlayerValidationResponseWrapper
from domain import Arena
from microservice import IdentityService


class ArenaValidationWrapperDict(ModelValidationWrapperDict[Arena]):
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
    _game_client: GameValidationResponseWrapper
    _player_client: PlayerValidationResponseWrapper
    
    def __init__(
            self,
            game_client: Optional[GameValidationResponseWrapper] | None = None,
            player_client: Optional[PlayerValidationResponseWrapper] | None = None,
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
        self._game_client = game_client or GameValidationResponseWrapper()
        self._player_client = player_client or PlayerValidationResponseWrapper()
        
    @property
    def game_client(self) -> GameValidationResponseWrapper:
        return self._game_client
    
    @property
    def player_client(self) -> PlayerValidationResponseWrapper:
        return self._player_client