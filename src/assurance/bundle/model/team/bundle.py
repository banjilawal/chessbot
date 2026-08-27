# src/assurance/bundle/model/team/bundle.py

"""
Module: assurance.bundle.model.team.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import BoardValidator, PlayerValidator, ValidationBundle
from domain import Team, TeamTypeUnions, TeamNullExceptionRoster


@dataclass
class TeamValidationBundle(ValidationBundle[Team]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities TeamIntegrityChecker needs to
            run safety checks on a validation candidate. 

    Attributes:
        types: TeamTypeUnions
        nulls: TeamNullExceptionRoster
        
        number_validator: NumberValidator
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:

    Super Class:
        ValidationBundle
    """
    types: TeamTypeUnions = TeamTypeUnions()
    nulls: TeamNullExceptionRoster = TeamNullExceptionRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "owner_validator": PlayerValidator(),
            "board_validator": BoardValidator(),
        }
    )
    
    @property
    def owner_validator(self) -> PlayerValidator:
        return self.resources["owner_validator"]
    
    @property
    def board_validator(self) -> BoardValidator:
        return self.resources["board_validator"]
