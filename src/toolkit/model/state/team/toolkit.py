# src/toolkit/model/team/toolkit.py

"""
Module: toolkit.model.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from blueprint import TeamBlueprint, TokenBlueprint
from carrier import TokenCarrier
from detector import TokenHomeDetector
from err import (
    TeamBlueprintNullException, TeamNullException, TokenBlueprintNullException, TokenCarrierNullException,
    TokenNullException
)
from model import Team, Token
from tester import BlueprintHomeSquareExtractor, BlueprintRankExtractor
from toolkit import StateModelToolkit
from validator import BoardValidator, TeamValidator


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
    model: Type[Token] = Token
    carrier_model: Type[TokenCarrier] = TokenCarrier
    blueprint_model: Type[TokenBlueprint] = TokenBlueprint
    
    null_exception: TokenNullException = TokenNullException()
    carrier_null_exception: TokenCarrierNullException = TokenCarrierNullException()
    blueprint_null_exception: TokenBlueprintNullException = TokenBlueprintNullException()
    
    team_validator: TeamValidator = TeamValidator()
    home_detector: TokenHomeDetector = TokenHomeDetector()
    rank_extractor: BlueprintRankExtractor = BlueprintRankExtractor()
    home_square_extractor: BlueprintHomeSquareExtractor = BlueprintHomeSquareExtractor()


class TeamToolkit(StateModelToolkit[Team]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services a Team requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        board_validator: BoardValidator
        player_validator: PlayerValidator
        identity_service: IdentityService
        priming_validator: PrimingValidator

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
       ModelToolkit
    """
    DEPENDENCIES = []
    SERVICE_DEPENDENCIES = []
    board_validator: BoardValidator = BoardValidator()
    player_validator: PlayerValidator = PlayerValidator()
    model: Team = Type[Team]
    blueprint_model: TeamBlueprint = Type[TeamBlueprint]
    null_exception: TeamNullException()
    blueprint_null_exception = TeamBlueprintNullException()
    

