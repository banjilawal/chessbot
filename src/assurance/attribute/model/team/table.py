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
from client import BoardValidatorClient, PlayerValidatorClient
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
    _board_client: BoardValidatorClient
    _owner_client: PlayerValidatorClient
    
    def __init__(
            self,
            board_client: Optional[BoardValidatorClient] | None = None,
            owner_client: Optional[PlayerValidatorClient] | None = None,
    ):
        """
        Args:
            board_client: Optional[BoardValidatorClient]
            owner_client: Optional[PlayerValidatorClient]
        """
        super().__init__()
        self._board_client = board_client or BoardValidatorClient()
        self._owner_client = owner_client or PlayerValidatorClient()
    
    @property
    def board_client(self) -> BoardValidatorClient:
        return self._board_client
    
    @property
    def owner_client(self) -> PlayerValidatorClient:
        return self._owner_client