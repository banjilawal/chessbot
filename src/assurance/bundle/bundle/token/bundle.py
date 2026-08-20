# src/assurance/manifest/bundle/token/bundle.py

"""
Module: assurance.manifest.bundle.token.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict

from assurance import ValidationBundle, TeamValidator, TokenNullRoster, TokenTypes
from authorization import BlueprintHomeSquareExtractor, BlueprintRankExtractor
from model import Token
from sensor import TokenHomeReporter


@dataclass
class TokenValidationBundle(ValidationBundle[Token]):
    types: TokenTypes = TokenTypes()
    nulls: TokenNullRoster = TokenNullRoster()
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