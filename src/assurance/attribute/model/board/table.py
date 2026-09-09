# src/assurance/attrribute/model/board/table.py

"""
Module: assurance.attrribute.model.board.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, ArenaValidator, PrimingValidator
from domain import Board
from microservice import IdentityService


class BoardHelperTable(AttributeHelperTable[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators an Board needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        arena_validator: ArenaValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _arena_validator: ArenaValidator
    
    def __init__(
            self,
            arena_validator: Optional[ArenaValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            arena_validator: Optional[ArenaValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._arena_validator = arena_validator or ArenaValidator()
    
    @property
    def arena_validator(self) -> ArenaValidator:
        return self._arena_validator