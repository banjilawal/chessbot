# src/assurance/attrribute/model/team/table.py

"""
Module: assurance.attrribute.model.team.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable
from client import BoardValidationResponseService, PlayerValidationResponseService
from domain import Team


class TeamHelperTable(ModelHelperTable[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a TeamValidator needs.
        
    Attributes:
        board_client: BoardValidatorClient
        owner_client: PlayerValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _board_client: BoardValidationResponseService
    _owner_client: PlayerValidationResponseService
    
    def __init__(
            self,
            board_client: Optional[BoardValidationResponseService] | None = None,
            owner_client: Optional[PlayerValidationResponseService] | None = None,
    ):
        """
        Args:
            board_client: Optional[BoardValidatorClient]
            owner_client: Optional[PlayerValidatorClient]
        """
        super().__init__()
        self._board_client = board_client or BoardValidationResponseService()
        self._owner_client = owner_client or PlayerValidationResponseService()
    
    @property
    def board_client(self) -> BoardValidationResponseService:
        return self._board_client
    
    @property
    def owner_client(self) -> PlayerValidationResponseService:
        return self._owner_client