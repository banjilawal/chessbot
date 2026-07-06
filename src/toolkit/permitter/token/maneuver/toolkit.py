# src/toolkit/permitter/token/maneuver/toolkit.py

"""
Module: toolkit.permitter.token.maneuver.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from analyzer import SquareTokenRelationAnalyzer, TokenReadinessAnalyzer
from search import TokenOriginSearcher
from toolkit import PermitterToolkit
from validator import SquareValidator, TokenValidator

@dataclass
class TokenManeuverToolkit(PermitterToolkit):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services TokenManeuverPermitter requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        token_validator: TokenValidator
        square_validator: SquareValidator
        origin_searcher: TokenOriginSearcher
        readiness_analyzer: TokenReadinessAnalyzer
        destination_relation_validator: SquareTokenRelationAnalyzer

    Provides:

    Super Class:
        PermitterToolkit
    """
    token_validator: TokenValidator = TokenValidator()
    square_validator: SquareValidator = SquareValidator()
    origin_searcher: TokenOriginSearcher = TokenOriginSearcher()
    readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    destination_relation_validator: TokenDestinationRelationValidator = TokenDestinationRelationValidator()