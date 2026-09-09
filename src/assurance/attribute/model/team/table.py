# src/assurance/attrribute/model/team/table.py

"""
Module: assurance.attrribute.model.team.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, BoardValidator, PrimingValidator
from domain import Team
from microservice import IdentityService


class TeamHelperTable(AttributeHelperTable[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Team needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        board_validator: BoardValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _board_validator: BoardValidator
    
    def __init__(
            self,
            board_validator: Optional[BoardValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            board_validator: Optional[BoardValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._board_validator = board_validator or BoardValidator()
    
    @property
    def board_validator(self) -> BoardValidator:
        return self._board_validator