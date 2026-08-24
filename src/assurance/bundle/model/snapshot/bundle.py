# src/assurance/bundle/model/snapshot/bundle.py

"""
Module: assurance.bundle.model.snapshot.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NumberValidator, ValidationBundle
from domain import Snapshot, SnapshotTypeUnions, SnapshotNullExceptionRoster


@dataclass
class SnapshotValidationBundle(ValidationBundle[Snapshot]):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities SnapshotIntegrityChecker needs to
            run safety checks on a validation candidate. 

    Attributes:
        types: SnapshotTypeUnions
        nulls: SnapshotNullExceptionRoster
        
        number_validator: NumberValidator
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        ValidationBundle
    """
    types: SnapshotTypeUnions = SnapshotTypeUnions()
    nulls: SnapshotNullExceptionRoster = SnapshotNullExceptionRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "number_validator": NumberValidator(),
        }
    )
    
    @property
    def number_validator(self) -> NumberValidator:
        return self.resources["number_validator"]
