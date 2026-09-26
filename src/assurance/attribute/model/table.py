# src/assurance/attrribute/model/table.py

"""
Module: assurance.attrribute.model.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from assurance import AttributeHelperTable, NumberValidator, PrimingValidator
from authorization import BlueprintIdExtractor
from domain import Model
from microservice import IdentityService

T = TypeVar("T", bound="Model")


class ModelHelperTable(AttributeHelperTable[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Model needs for its primitive and upstream
            relational partners attributes.

    Attributes:
        identity_service: IdentityService
        number_validator: NumberValidator
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        AttributeHelperTable
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
