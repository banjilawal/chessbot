# src/assurance/bundle/model/vector/bundle.py

"""
Module: assurance.bundle.model.vector.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NumberValidator, ValidationBundle
from domain import Vector, VectorAssociationManifest, VectorNullExceptionRoster


@dataclass
class VectorValidationBundle(ValidationBundle[Vector]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities VectorIntegrityChecker needs to
            run safety checks on a validation candidate. 

    Attributes:
        identity_service: IdentityService
        priming_validator: PrimingValidator
        types: VectorAssociationManifest
        nulls: VectorNullExceptionRoster
        number_validator: NumberValidator

    Provides:

    Super Class:
        ValidationBundle
    """
    types: VectorAssociationManifest = VectorAssociationManifest()
    nulls: VectorNullExceptionRoster = VectorNullExceptionRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "number_validator": NumberValidator(),
        }
    )
    
    @property
    def number_validator(self) -> NumberValidator:
        return self.resources["number_validator"]
