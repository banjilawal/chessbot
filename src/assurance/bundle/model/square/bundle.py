# src/assurance/bundle/model/square/bundle.py

"""
Module: assurance.bundle.model.square.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import BoardValidator, CoordValidator, TokenValidator, ValidationBundle
from domain import Square, SquareTypeUnions, SquareNullExceptionRoster
from sensor import SquareCollider


@dataclass
class SquareValidationBundle(ValidationBundle[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities SquareIntegrityChecker needs to
            run safety checks on a validation candidate. 

    Attributes:
        types: SquareTypeUnions
        nulls: SquareNullExceptionRoster
        
        token_validator: TokenValidator
        board_validator: BoardValidator
        coord_validator: CoordValidator
        collision_detector: SquareCollider

    Provides:

    Super Class:
        ValidationBundle
    """
    types: SquareTypeUnions = SquareTypeUnions()
    nulls: SquareNullExceptionRoster = SquareNullExceptionRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "token_validator": TokenValidator(),
            "board_validator": BoardValidator(),
            "coord_validator": CoordValidator(),
            "collision_detector": SquareCollider(),
        }
    )
    
    @property
    def token_validator(self) -> TokenValidator:
        return self.resources["token_validator"]
    
    @property
    def board_validator(self) -> BoardValidator:
        return self.resources["board_validator"]
    
    @property
    def coord_validator(self) -> CoordValidator:
        return self.resources["coord_validator("]
    
    @property
    def collision_detector(self) -> SquareCollider:
        return self.resources["collision_detector"]
