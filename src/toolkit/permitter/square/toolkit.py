# src/toolkit/model/square/toolkit.py

"""
Module: toolkit.model.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from detection import SquareCollisionDetector
from microservice import FormationService, IdentityService
from model import Square
from toolkit import ModelToolkit
from validation import BoardValidator, CoordValidator, TokenValidator, PrimingValidator


@dataclass
class SquareToolkit(ModelToolkit[Square]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

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
        priming_validator: ValidationPrimer
        square_collision_detector: SquareCollisionAnalyst

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """
    DEPENDENCIES =[
        BoardValidator,
        CoordValidator,
        SquareCollisionDetector,
        PrimingValidator,
    ]
    
    SERVICE_DEPENDENCIES = [
        IdentityService,
        FormationService,
    ]
    token_validator: TokenValidator = TokenValidator()
    board_validator: BoardValidator = BoardValidator()
    coord_validator: CoordValidator = CoordValidator()
    identity_service: IdentityService = IdentityService()
    formation_service: FormationService = FormationService()
    priming_validator: PrimingValidator = PrimingValidator()
    square_collision_detector: SquareCollisionDetector = SquareCollisionDetector()

