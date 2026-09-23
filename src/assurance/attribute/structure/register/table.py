# src/assurance/attrribute/structure/register/table.py

"""
Module: assurance.attrribute.structure.register.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import NumberValidator, PrimingValidator, StructureHelperTable, Validator
from authorization import BlueprintIdExtractor
from domain import Register
from microservice import IdentityService

T = TypeVar("T", bound="Register")


class RegisterHelperTable(StructureHelperTable[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Register needs for its primitive and upstream relational
            partners attributes.

    Attributes:

    Provides:

    Super Class:
        StructureHelperTable
    """
    
    def __init__(
            self,
            identity_service: Optional[IdentityService] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
            blueprint_id_extractor: Optional[BlueprintIdExtractor] | None = None,
    ):
        """
        Args:
            identity_service: Optional[IdentityService]
            number_validator: Optional[NumberValidator]
            priming_validator: Optional[PrimingValidator]
            blueprint_id_extractor: Optional[BlueprintIdExtractor]
        """
        super().__init__(
            identity_service=identity_service,
            number_validator=number_validator,
            priming_validator=priming_validator,
            blueprint_id_extractor=blueprint_id_extractor,
        )
    
    