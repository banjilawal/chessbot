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
from carrier import TokenCarrier
from detector import TokenHomeDetector
from err import TokenBlueprintNullException, TokenCarrierNullException, TokenNullException
from model import Token
from tester import BlueprintHomeSquareExtractor, BlueprintRankExtractor
from toolkit import StateModelToolkit
from validator import TeamValidator


@dataclass
class TokenToolkit(StateModelToolkit[Token]):
    """
    Role:
        -   Dependency Management

    Responsibilities:
        1.  Bundles dependencies a worker needs to complete its task.
        2.  Loose Coupling between an operation and its resources.
        3.  Simplify Entry points.

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
    carrier_model: Type[TokenCarrier] = (
        TokenCarrier
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