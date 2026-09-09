# src/assurance/attrribute/model/maneuver/table.py

"""
Module: assurance.attrribute.model.maneuver.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import (
    AttributeHelperTable, NumberValidator, PathValidator, TokenValidator, PrimingValidator
)
from domain import Maneuver
from microservice import IdentityService


class ManeuverHelperTable(AttributeHelperTable[Maneuver]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Maneuver needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        path_validator: PathValidator
        token_validator: TokenValidator

    Provides:

    Super Class:
        AttributeHelperTable
    """
    _path_validator: PathValidator
    _token_validator: TokenValidator
    
    def __init__(
            self,
            path_validator: Optional[PathValidator] | None = None,
            token_validator: Optional[TokenValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            path_validator: Optional[PathValidator]
            token_validator: Optional[TokenValidator]
            identity_service: Optional[IdentityService]
            number_validator: Optional[NumberValidator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            number_validator=number_validator,
            priming_validator=priming_validator,
        )
        self._path_validator = path_validator or PathValidator()
        self._token_validator = token_validator or TokenValidator()
        
    @property
    def path_validator(self) -> PathValidator:
        return self._path_validator
    
    @property
    def token_validator(self) -> TokenValidator:
        return self._token_validator