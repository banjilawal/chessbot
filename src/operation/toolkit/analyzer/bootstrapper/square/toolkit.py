# src/operation/toolkit/analyzer/square/toolkit.py

"""
Module: operation.toolkit.analyzer.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from detection import SquareCollisionDetector
from microservice import FormationService, IdentityService
from sensor.analyzer import Square
from operation.toolkit.analyzer.bootstrapper.square.toolkit import AnalyzerBootstrapperToolkit
from transit.dispatcher.validator import BoardValidationDispatcher, CoordValidationDispatcher, TokenValidationDispatcher, PrimingValidator


@dataclass
class SquareToolkit(AnalyzerBootstrapperToolkit[Square]):
    """
    Role:
        -  Dependency Management

    Responsibilities:
        1.  Aggregates workers and services a Square requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        token_validator: TokenValidator
        board_validator: BoardValidator
        coord_validator: CoordValidator
        identity_service: IdentityService
        formation_service: FormationService
        priming_validator: PrimingValidator
        square_collision_detector: SquareCollisionAnalyst

    Provides:
        -  def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """
    DEPENDENCIES =[
        BoardValidationDispatcher,
        CoordValidationDispatcher,
        SquareCollisionDetector,
        PrimingValidator,
    ]
    
    SERVICE_DEPENDENCIES = [
        IdentityService,
        FormationService,
    ]
    token_validator: TokenValidationDispatcher = TokenValidationDispatcher()
    board_validator: BoardValidationDispatcher = BoardValidationDispatcher()
    coord_validator: CoordValidationDispatcher = CoordValidationDispatcher()
    identity_service: IdentityService = IdentityService()
    formation_service: FormationService = FormationService()
    priming_validator: PrimingValidator = PrimingValidator()
    square_collision_detector: SquareCollisionDetector = SquareCollisionDetector()

