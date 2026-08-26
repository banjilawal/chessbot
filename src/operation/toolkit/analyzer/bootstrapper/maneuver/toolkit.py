# src/operation/toolkit/analyzer/maneuver/toolkit.py

"""
Module: operation.toolkit.analyzer.maneuver.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List

from sensor.analyzer import SquareTokenRelationAnalyzer, TokenReadinessAnalyzer
from err import ManeuverNullException
from microservice import Microservice
from sensor.analyzer import Maneuver
from operation import Operator
from operation.crud.search import TokenOriginSearcher
from operation.toolkit.analyzer.bootstrapper.maneuver.toolkit import AnalyzerBootstrapperToolkit
from transit.dispatcher.validator import (
    ManeuverEndpointValidator, PathValidationDispatcher, SquareValidationDispatcher, TokenDestinationCertifier,
    TokenValidationDispatcher
)
from transit.dispatcher.validator import TokenOriginCertifier


class ManeuverToolkit(AnalyzerBootstrapperToolkit[Maneuver]):
    """
    Role:
        -  Dependency Management

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
        analyzer: Maneuver

    Provides:
        -  def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """

    DEPENDENCIES: List[Operator] = []
    SERVICE_DEPENDENCIES: List[Microservice] = []
    
    path_validator: PathValidationDispatcher = PathValidationDispatcher()
    token_validator: TokenValidationDispatcher = TokenValidationDispatcher()
    square_validator: SquareValidationDispatcher = SquareValidationDispatcher()
    origin_searcher: TokenOriginSearcher = TokenOriginSearcher()
    readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()
    endpoint_validator: ManeuverEndpointValidator = ManeuverEndpointValidator()
    origin_relation_validator: TokenOriginCertifier = TokenOriginRootCertifier()
    destination_relation_validator: TokenDestinationCertifier = TokenDestinationRootCertifier()
    null_exception: ManeuverNullException = ManeuverNullException()
    analyzer: Maneuver = Maneuver