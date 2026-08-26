# src/assurance/bundle/model/rank/bundle.py

"""
Module: assurance.bundle.model.rank.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NumberValidator, ValidationBundle
from domain import Rank, RankTypeUnions, RankNullExceptionRoster


@dataclass
class RankValidationBundle(ValidationBundle[Rank]):
    """
    Role:
        -  Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities RankIntegrityChecker needs to
            run safety checks on a validation candidate. 

    Attributes:
        types: RankTypeUnions
        nulls: RankNullExceptionRoster
        
        number_validator: NumberValidator
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        ValidationBundle
    """
    types: RankTypeUnions = RankTypeUnions()
    nulls: RankNullExceptionRoster = RankNullExceptionRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "number_validator": NumberValidator(),
        }
    )
    
    @property
    def number_validator(self) -> NumberValidator:
        return self.resources["number_validator"]
