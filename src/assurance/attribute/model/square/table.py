# src/assurance/attrribute/model/square/table.py

"""
Module: assurance.attrribute.model.square.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, BoardValidator, CoordValidator, PrimingValidator
from domain import Square
from microservice import IdentityService


class SquareHelperTable(AttributeHelperTable[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Square needs for its primitive and upstream
            relational partners attributes.

    Attributes:
        board_validator: BoardValidator
        coord_validator: CoordValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _board_validator: BoardValidator
    _coord_validator: CoordValidator
    
    def __init__(
            self,
            board_validator: Optional[BoardValidator] | None = None,
            coord_validator: Optional[CoordValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            board_validator: Optional[BoardValidator]
            coord_validator: Optional[CoordValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._board_validator = board_validator or BoardValidator()
        self._coord_validator = coord_validator or CoordValidator()
        
    @property
    def board_validator(self) -> BoardValidator:
        return self._board_validator
    
    @property
    def coord_validator(self) -> CoordValidator:
        return self._coord_validator