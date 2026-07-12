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
from searcher import TokenOriginSearcher
from toolkit import StateModelToolkit
from validator import (
    ManeuverEndpointValidator, PathValidator, SquareValidator, TokenDestinationCertifier,
    TokenValidator
)
from validator.model.endpoint import TokenOriginCertifier


class ManeuverToolkit(StateModelToolkit[Maneuver]):
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
        origin_certifier: TokenOriginRelationValidator
        destination_certifier: TokenDestinationRelationValidator
        null_exception: ManeuverNullException
        model: Maneuver

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
       ModelToolkit
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
    origin_certifier: TokenOriginCertifier = TokenOriginRootCertifier()
    destination_certifier: TokenDestinationCertifier = TokenDestinationRootCertifier()
    null_exception: ManeuverNullException = ManeuverNullException()
    model: Maneuver = Maneuver