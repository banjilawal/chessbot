# src/assurance/bundle/model/arena/bundle.py

"""
Module: assurance.bundle.model.arena.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NumberValidator, ValidationBundle
from domain import Arena, ArenaTypeUnions, ArenaNullExceptionRoster


@dataclass
class ArenaValidationBundle(ValidationBundle[Arena]):
    """
    Role:
        -   Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities ArenaIntegrityChecker needs to
            run safety checks on a validation candidate. 

    Attributes:
        types: ArenaTypeUnions
        nulls: ArenaNullExceptionRoster
        
        number_validator: NumberValidator
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        ValidationBundle
    """
    types: ArenaTypeUnions = ArenaTypeUnions()
    nulls: ArenaNullExceptionRoster = ArenaNullExceptionRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "number_validator": NumberValidator(),
        }
    )
    
    @property
    def number_validator(self) -> NumberValidator:
        return self.resources["number_validator"]
