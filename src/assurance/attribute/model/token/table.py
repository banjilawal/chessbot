# src/assurance/attrribute/model/token/table.py

"""
Module: assurance.attrribute.model.token.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, BoardValidator, SquareValidator, TeamValidator, PrimingValidator
from domain import Token
from microservice import IdentityService


class TokenHelperTable(AttributeHelperTable[Token]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Token needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        team_validator: TeamValidator
        board_validator: BoardValidator
        square_validator: SquareValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _team_validator: TeamValidator
    _board_validator: BoardValidator
    _square_validator: SquareValidator
    
    def __init__(
            self,
            team_validator: Optional[TeamValidator] | None = None,
            board_validator: Optional[BoardValidator] | None = None,
            square_validator: Optional[SquareValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            team_validator: Optional[TeamValidator]
            board_validator: Optional[BoardValidator]
            square_validator: Optional[SquareValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._team_validator = team_validator or TeamValidator()
        self._board_validator = board_validator or BoardValidator()
        self._square_validator = square_validator or SquareValidator()
    
    @property
    def team_validator(self) -> TeamValidator:
        return self._team_validator
    
    @property
    def board_validator(self) -> BoardValidator:
        return self._board_validator
    
    @property
    def square_validator(self) -> SquareValidator:
        return self._square_validator