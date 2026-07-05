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
from err import ManeuverNullException
from microservice import Microservice
from model import Maneuver
from operation import Operation
from search import TokenOriginSearcher
from toolkit import ModelToolkit
from validation import (
    ManeuverEndpointValidator, PathValidator, SquareValidator, TokenDestinationCertifier,
    TokenValidator
)
from validation.endpoint.origin import TokenOriginCertifier


class ManeuverToolkit(ModelToolkit[Maneuver]):
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

        path_validator: PathValidator
        token_validator: TokenValidator
        square_validator: SquareValidator
        origin_searcher: TokenOriginSearcher
        readiness_analyzer: TokenReadinessAnalyzer
        relation_analyzer: SquareTokenRelationAnalyzer
        endpoint_validator: ManeuverEndpointValidator
        origin_relation_validator: TokenOriginRelationValidator
        destination_relation_validator: TokenDestinationRelationValidator
        null_exception: ManeuverNullException
        model: Maneuver

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """

    DEPENDENCIES: List[Operation] = []
    SERVICE_DEPENDENCIES: List[Microservice] = []
    
    path_validator: PathValidator = PathValidator()
    token_validator: TokenValidator = TokenValidator()
    square_validator: SquareValidator = SquareValidator()
    origin_searcher: TokenOriginSearcher = TokenOriginSearcher()
    readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()
    endpoint_validator: ManeuverEndpointValidator = ManeuverEndpointValidator()
    origin_relation_validator: TokenOriginCertifier = TokenOriginCertifier()
    destination_relation_validator: TokenDestinationCertifier = TokenDestinationCertifier()
    null_exception: ManeuverNullException = ManeuverNullException()
    model: Maneuver = Maneuver