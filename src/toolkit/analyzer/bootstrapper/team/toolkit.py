# src/toolkit/analyzer/team/toolkit.py

"""
Module: toolkit.analyzer.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import IdentityService
from analyzer import Team
from toolkit import AnalyzerBootstrapperToolkit
from validation import BoardValidator, PlayerValidator, PrimingValidator


class TeamToolkit(AnalyzerBootstrapperToolkit[Team]):
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
        Toolkit
    """
    DEPENDENCIES = [
        BoardValidator,
        PlayerValidator,
        PrimingValidator
    ]
    SERVICE_DEPENDENCIES = [ IdentityService, ]
    
    board_validator: BoardValidator = BoardValidator()
    identity_service: IdentityService = IdentityService()
    player_validator: PlayerValidator = PlayerValidator()
    priming_validator: PrimingValidator = PrimingValidator()
