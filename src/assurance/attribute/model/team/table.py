# src/assurance/attrribute/model/team/table.py

"""
Module: assurance.attrribute.model.team.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from domain import Team
from microservice import IdentityService
from assurance import AttributeHelperTable, BoardValidator, PlayerValidator, PrimingValidator



class TeamHelperTable(AttributeHelperTable[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Team needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        board_validator: BoardValidator
        owner_validator: PlayerValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _board_validator: BoardValidator
    _owner_validator: PlayerValidator
    
    def __init__(
            self,
            board_validator: Optional[BoardValidator] | None = None,
            owner_validator: Optional[PlayerValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            board_validator: Optional[BoardValidator]
            owner_validator: Optional[PlayerValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._board_validator = board_validator or BoardValidator()
        self._owner_validator = owner_validator or PlayerValidator()
    
    @property
    def board_validator(self) -> BoardValidator:
        return self._board_validator
    
    @property
    def owner_validator(self) -> PlayerValidator:
        return self._owner_validator