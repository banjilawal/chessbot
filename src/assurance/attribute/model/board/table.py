# src/assurance/attrribute/model/board/table.py

"""
Module: assurance.attrribute.model.board.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable, PrimingValidator
from client import ArenaValidatorClient
from domain import Board
from microservice import IdentityService


class BoardHelperTable(ModelHelperTable[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients an Board needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        arena_client: ArenaValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _arena_client: ArenaValidatorClient
    
    def __init__(
            self,
            arena_client: Optional[ArenaValidatorClient] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            arena_client: Optional[ArenaValidatorClient]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._arena_client = arena_client or ArenaValidatorClient()
    
    @property
    def arena_client(self) -> ArenaValidatorClient:
        return self._arena_client