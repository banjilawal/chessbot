# src/toolkit/model/maneuver/toolkit.py

"""
Module: toolkit.model.maneuver.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from analyzer import SquareTokenRelationAnalyzer, TokenReadinessAnalyzer
from microservice import Microservice
from model import Maneuver
from operation import Operation
from search import TokenOriginSearcher
from toolkit import Toolkit
from validation import SquareValidator, TokenDestinationRelationValidator, TokenValidator


class ManeuverToolkit(Toolkit[Maneuver]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services a Maneuver object requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        token_validator: TokenValidator
        square_validator: SquareValidator
        origin_searcher: TokenOriginSearcher
        readiness_analyzer: TokenReadinessAnalyzer
        relation_analyzer: SquareTokenRelationAnalyzer
        destination_validator: TokenDestinationRelationValidator

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """

    DEPENDENCIES: List[Operation] = []
    SERVICE_DEPENDENCIES: List[Microservice] = []
    
    
    token_validator: TokenValidator = TokenValidator()
    square_validator: SquareValidator = SquareValidator()
    origin_searcher: TokenOriginSearcher = TokenOriginSearcher()
    readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()
    destination_validator: TokenDestinationRelationValidator = TokenDestinationRelationValidator()