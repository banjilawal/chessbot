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
from err import TokenBlueprintNullException, TokenEntityOperandNullException, TokenNullException
from model import Token
from operand import TokenEntityOperand
from tester import BlueprintHomeSquareExtractor, BlueprintRankExtractor
from toolkit import ModelToolkit
from validator import TeamValidator


@dataclass
class TokenToolkit(ModelToolkit[Token]):
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
    model: Type[Token] = Token
    blueprint_model: Type[TokenBlueprint] = TokenBlueprint
    operand_model: Type[TokenEntityOperand] = TokenEntityOperand
    
    null_exception: TokenNullException = TokenNullException()
    blueprint_null_exception: TokenBlueprintNullException = TokenBlueprintNullException()
    operand_null_exception: TokenEntityOperandNullException =TokenEntityOperandNullException()
    
    home_detector: TokenHomeDetector = TokenHomeDetector()
    team_validator: TeamValidator = TeamValidator()
    blueprint_rank_extractor: BlueprintRankExtractor = BlueprintRankExtractor()
    blueprint_home_square_extractor: BlueprintHomeSquareExtractor = BlueprintHomeSquareExtractor()