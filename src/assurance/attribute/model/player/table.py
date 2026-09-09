# src/assurance/attrribute/model/player/table.py

"""
Module: assurance.attrribute.model.player.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import AttributeHelperTable, StringValidator, PrimingValidator
from domain import Player
from microservice import IdentityService


class PlayerHelperTable(AttributeHelperTable[Player]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators an Player needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        string_validator: StringValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _string_validator: StringValidator
    
    def __init__(
            self,
            string_validator: Optional[StringValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            string_validator: Optional[StringValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._string_validator = string_validator or StringValidator()
    
    @property
    def string_validator(self) -> StringValidator:
        return self._string_validator