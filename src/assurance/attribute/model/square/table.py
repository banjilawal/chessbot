# src/assurance/attrribute/model/square/table.py

"""
Module: assurance.attrribute.model.square.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable
from client import BoardValidationResponseService, CoordValidationResponseService

f
from domain import Square
from microservice import IdentityService


class SquareHelperTable(ModelHelperTable[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Square needs for its primitive and upstream
            relational partners attributes.

    Attributes:
        board_client: BoardValidatorClient
        coord_client: CoordValidatorClient

    Provides:

    Super Class:
        ModelHelperTable
    """
    _board_client: BoardValidationResponseService
    _coord_client: CoordValidationResponseService
    
    def __init__(
            self,
            board_client: Optional[BoardValidationResponseService] | None = None,
            coord_client: Optional[CoordValidationResponseService] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            board_client: Optional[BoardValidatorClient]
            coord_client: Optional[CoordValidatorClient]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._board_client = board_client or BoardValidationResponseService()
        self._coord_client = coord_client or CoordValidationResponseService()
        
    @property
    def board_client(self) -> BoardValidationResponseService:
        return self._board_client
    
    @property
    def coord_client(self) -> CoordValidationResponseService:
        return self._coord_client