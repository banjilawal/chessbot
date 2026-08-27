# src/operation/toolkit/analyzer/team/toolkit.py

"""
Module: operation.toolkit.analyzer.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from microservice import IdentityService
from sensor.analyzer import Team
from operation.toolkit.analyzer.bootstrapper.team.toolkit import AnalyzerBootstrapperToolkit
from transit.dispatcher.validator import BoardValidationDispatcher, PlayerValidationDispatcher, PrimingValidator


class TeamToolkit(AnalyzerBootstrapperToolkit[Team]):
    """
    Role:
        - Dependency Management

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
        -  def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """
    DEPENDENCIES = [
        BoardValidationDispatcher,
        PlayerValidationDispatcher,
        PrimingValidator
    ]
    SERVICE_DEPENDENCIES = [ IdentityService, ]
    
    board_validator: BoardValidationDispatcher = BoardValidationDispatcher()
    identity_service: IdentityService = IdentityService()
    player_validator: PlayerValidationDispatcher = PlayerValidationDispatcher()
    priming_validator: PrimingValidator = PrimingValidator()
