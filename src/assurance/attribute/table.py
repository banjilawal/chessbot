# src/assurance/attrribute/table.py

"""
Module: assurance.attrribute.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import NumberValidator, PrimingValidator
from authorization import BlueprintIdExtractor
from domain import Model
from microservice import IdentityService

T = TypeVar("T", bound="Model")


class AttributeHelperTable(ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validators a Model needs for its primitive and upstream relational partners attributes.

    Attributes:
        identity_service: IdentityService
        number_validator: NumberValidator
        primin_validator: PrimingValidator

    Provides:

    Super Class:
    """
    _identity_service: IdentityService
    _number_validator: NumberValidator
    _priming_validator: PrimingValidator
    _blueprint_id_extractor: BlueprintIdExtractor
    
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
        self._identity_service = identity_service or IdentityService()
        self._number_validator = number_validator or NumberValidator()
        self._priming_validator = priming_validator or PrimingValidator()
        self._blueprint_id_extractor = blueprint_id_extractor or BlueprintIdExtractor()
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def number_validator(self) -> NumberValidator:
        return self._number_validator
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @property
    def blueprint_id_extractor(self) -> BlueprintIdExtractor:
        return self._blueprint_id_extractor