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
from detector import TokenHomeDetector
from err import TokenBlueprintNullException, TokenNullException
from microservice import RankService
from model import Token
from toolkit import ModelToolkit
from validator import (
    BlueprintHomeSquareExtractor, BlueprintRankExtractor, CoordValidator, NumberValidator,
    SquareValidator, TeamValidator
)


@dataclass
class TokenToolkit:
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services an entity requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        model: Token
        blueprint_model: TokenBlueprint
        identity_service: IdentityService
        priming_validator: PrimingValidator
        blueprint_id_validator: BlueprintIdValidator
        null_exception: TokenNullException
        blueprint_null_exception: TokenBlueprintNullException

    Provides:

    Super Class:
       ModelToolkit
    """
    """
    Args:
        model: Token
        blueprint_model: TokenBlueprint
        identity_service: IdentityService
        priming_validator: PrimingValidator
        blueprint_id_validator: BlueprintIdValidator
        null_exception: TokenNullException
        blueprint_null_exception: TokenBlueprintNullException
        team_validator: TeamValidator
        
        home_detector: TokenHomeDetector
    """
    home_detector: TokenHomeDetector = TokenHomeDetector()
    square_validator: SquareValidator = SquareValidator()
    coord_validator: CoordValidator = CoordValidator()
    team_validator: TeamValidator = TeamValidator()
    rank_service: RankService = RankService()
    number_validator: NumberValidator = NumberValidator()
    blueprint_rank_processor: BlueprintRankExtractor = BlueprintRankExtractor()
    blueprint_home_square_processor: BlueprintHomeSquareExtractor = BlueprintHomeSquareExtractor()

    model: Token = Type[Token]
    blueprint_model = Type[TokenBlueprint]
    null_exception: TokenNullException = TokenNullException()
    blueprint_null_exception: TokenBlueprintNullException = TokenBlueprintNullException()