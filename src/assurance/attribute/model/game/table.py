# src/assurance/attrribute/model/game/table.py

"""
Module: assurance.attrribute.model.game.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable, PrimingValidator
from client import PlayerValidationResponseService
from domain import Game
from microservice import IdentityService


class GameHelperTable(ModelHelperTable[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients an Game needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        player_client: PlayerValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _player_client: PlayerValidationResponseService
    
    def __init__(
            self,
            player_client: Optional[PlayerValidationResponseService] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            player_client: Optional[PlayerValidatorClient]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._player_client = player_client or PlayerValidationResponseService()
    
    @property
    def player_client(self) -> PlayerValidationResponseService:
        return self._player_client