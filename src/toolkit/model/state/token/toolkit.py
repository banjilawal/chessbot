# src/toolkit/model/token/toolkit.py

"""
Module: toolkit.model.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import TokenBlueprint
from carrier import TokenCarrierToggle
from detector import TokenHomeDetector
from err import TokenBlueprintNullException, TokenNullException
from model import Token
from tester import BlueprintHomeSquareExtractor, BlueprintRankExtractor
from toolkit import StateModelToolkit
from validator import TeamValidator


@dataclass
class TokenToolkit(StateModelToolkit[Token]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services an entity requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        model: Type[Token]
        carrier_model: Type[TokenCarrier]
        blueprint_model: Type[TokenBlueprint]
        
        null_exception: TokenNullException
        carrier_null_exception: TokenCarrierNullException
        blueprint_null_exception: TokenBlueprintNullException
        
        team_validator: TeamValidator
        home_detector: TokenHomeDetector
        rank_extractor: BlueprintRankExtractor
        home_square_extractor: BlueprintHomeSquareExtractor

    Provides:

    Super Class:
       ModelToolkit
    """
    model: Type[Token] = (
        Token
    )
    carrier_model: Type[TokenCarrierToggle] = (
        TokenCarrierToggle
    )
    blueprint_model: Type[TokenBlueprint] = (
        TokenBlueprint
    )
    
    null_exception: TokenNullException = (
        TokenNullException()
    )
    carrier_null_exception: TokenCarrierNullException = (
        TokenCarrierNullException()
    )
    blueprint_null_exception: TokenBlueprintNullException = (
        TokenBlueprintNullException()
    )
    
    team_validator: TeamValidator = TeamValidator()
    home_detector: TokenHomeDetector = TokenHomeDetector()
    rank_extractor: BlueprintRankExtractor = BlueprintRankExtractor()
    home_square_extractor: BlueprintHomeSquareExtractor = BlueprintHomeSquareExtractor()