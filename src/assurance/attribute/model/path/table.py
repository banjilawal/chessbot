# src/assurance/attrribute/model/path/table.py

"""
Module: assurance.attrribute.model.path.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelHelperTable, SquareRegisterValidator, PrimingValidator
from domain import Path
from microservice import IdentityService


class PathHelperTable(ModelHelperTable[Path]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators an Path needs for its primitive and upstream relational
            partners attributes.

    Attributes:
        endpoint_validator: SquareRegisterValidator

    Provides:

    Super Class:
        ModelHelperTable
    """
    _endpoint_validator: SquareRegisterValidator
    
    def __init__(
            self,
            endpoint_validator: Optional[SquareRegisterValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            endpoint_validator: Optional[SquareRegisterValidator]
            identity_service: Optional[IdentityService]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            identity_service=identity_service,
            priming_validator=priming_validator,
        )
        self._endpoint_validator = endpoint_validator or SquareRegisterValidator()
        
    @property
    def endpoint_validator(self) -> SquareRegisterValidator:
        return self._endpoint_validator