# src/assurance/attrribute/model/attack/table.py

"""
Module: assurance.attrribute.model.attack.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import (
    AttributeHelperTable, ManeuverValidator, NumberValidator, PrimingValidator, TokenValidator
)
from domain import Attack
from microservice import IdentityService


class AttackHelperTable(AttributeHelperTable[Attack]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators an Attack needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        token_validator: TokenValidator
        maneuver_validator: ManeuverValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _token_validator: TokenValidator
    _maneuver_validator: ManeuverValidator
    
    def __init__(
            self,
            token_validator: Optional[TokenValidator] | None = None,
            maneuver_validator: Optional[ManeuverValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            token_validator: Optional[TokenValidator]
            maneuver_validator: Optional[ManeuverValidator]
            identity_service: Optional[IdentityService]
            number_validator: Optional[NumberValidator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            number_validator=number_validator,
            priming_validator=priming_validator,
        )
        self._token_validator = token_validator or TokenValidator()
        self._maneuver_validator = maneuver_validator or ManeuverValidator()
        
    @property
    def token_validator(self) -> TokenValidator:
        return self._token_validator
    
    @property
    def maneuver_validator(self) -> ManeuverValidator:
        return self._maneuver_validator