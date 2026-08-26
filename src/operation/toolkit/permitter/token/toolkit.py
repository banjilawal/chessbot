# src/operation/toolkit/permitter/token/toolkit.py

"""
Module: operation.toolkit.permitter.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from detection import TokenHomeDetector
from err import TokenNullException
from microservice import RankService
from domain.model import Token
from operation.toolkit.permitter.token.toolkit import PermitterToolkit
from transit.dispatcher.validator import (
    BlueprintHomeSquareExtractor, BlueprintRankExtractor, CoordValidationDispatcher, NumberValidator,
    SquareValidationDispatcher, TeamValidationDispatcher
)


@dataclass
class ManeuverToolkit(PermitterToolkit):
    """
    Role:
        -  Dependency Management

    Responsibilities:
        1.  Bundles dependencies a worker needs to complete its task.
        2.  Loose Coupling between an operation and its resources.
        3.  Simplify Entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        home_square_detector: HomeSquareDetector
        square_validator: SquareValidator
        coord_validator: CoordValidator
        team_validator: TeamValidator
        rank_service: RankService
        priming_validator: Primer
        identity_service: IdentityService

    Provides:
        -  def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """
    home_detector: TokenHomeDetector = TokenHomeDetector()
    square_validator: SquareValidationDispatcher = SquareValidationDispatcher()
    coord_validator: CoordValidationDispatcher = CoordValidationDispatcher()
    team_validator: TeamValidationDispatcher = TeamValidationDispatcher()
    rank_service: RankService = RankService()
    number_validator: NumberValidator = NumberValidator()
    blueprint_rank_processor: BlueprintRankExtractor = BlueprintRankExtractor()
    blueprint_home_square_processor: BlueprintHomeSquareExtractor = BlueprintHomeSquareExtractor()
    null_exception: TokenNullException = TokenNullException()
    permitter: Token = Token