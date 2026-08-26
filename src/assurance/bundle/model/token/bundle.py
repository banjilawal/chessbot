# src/assurance/bundle/model/token/bundle.py

"""
Module: assurance.bundle.model.token.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import NumberValidator, ValidationBundle
from domain import Token, TokenTypeUnions, TokenNullExceptionRoster


@dataclass
class TokenValidationBundle(ValidationBundle[Token]):
    """
    Role:
        -  Toolkit

    Responsibilities:
        1.  Bundles types, null-exceptions, attribute-validators, and utilities TokenIntegrityChecker
            needs to run safety checks on a validation candidate.

    Attributes:
        types: TokenTypeUnions
        nulls: TokenNullExceptionRoster
        
        team_validator: TeamValidator
        home_detector: TokenHomeReporter
        home_square_extractor: BlueprintHomeSquareExtractor
        
        identity_service: IdentityService
        priming_validator: PrimingValidator
        
    Provides:

    Super Class:
        ValidationBundle
    """
    types: TokenTypeUnions = TokenTypeUnions()
    nulls: TokenNullExceptionRoster = TokenNullExceptionRoster()
    resources: Dict[str, Any] = field(
        default_factory=lambda: {
            "team_validator": TeamValidator(),
            "home_detector": TokenHomeReporter(),
            "rank_extractor": BlueprintRankExtractor(),
            "home_square_extractor": BlueprintHomeSquareExtractor(),
        }
    )
    
    @property
    def team_validator(self) -> TeamValidator:
        return self.resources["team_validator"]
    
    @property
    def home_detector(self) -> TokenHomeReporter:
        return self.resources["hom_detector"]
    
    @property
    def rank_extractor(self) -> BlueprintRankExtractor:
        return self.resources["rank_extractor"]
    
    @property
    def home_square_extractor(self) -> BlueprintHomeSquareExtractor:
        return self.resources["home_square_extractor"]
