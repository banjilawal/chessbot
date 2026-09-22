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
from domain import Model, Register
from microservice import IdentityService

T = TypeVar("T", bound="Model")


class RegisterHelperTable(StructureHelperTable[Register], ABC, Generic[T]):
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
    _model_validator: Validator[T]
    
    def __init__(
            self,
            model_validator: Validator[T],
            identity_service: Optional[IdentityService] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
            blueprint_id_extractor: Optional[BlueprintIdExtractor] | None = None,
    ):
        """
        Args:
            model_validator: Validator[T]
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
        self._model_validator = model_validator
        
    @property
    def model_validator(self) -> Validator[T]:
        return self._model_validator
    
    