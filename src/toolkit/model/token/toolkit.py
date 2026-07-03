# src/toolkit/model/token/toolkit.py

"""
Module: toolkit.model.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from model import Token
from operation import Operation
from toolkit import Toolkit
from microservice import FormationService, IdentityService, Microservice, RankService
from validation import CoordValidator, NumberValidator, SquareValidator, TeamValidator, PrimingValidator


class TokenToolkit(Toolkit[Token]):
    """
    Role:
        -   Dependency Container
        -   Dynamic Dependency Provider

    Responsibilities:
        1.  Aggregates workers and services an entity requires for its tasks.
        2.  Separates dependencies from data objects in operation calls.
        3.  Simplifies entry points.

    Attributes:
        DEPENDENCIES: List[Operation] = []
        SERVICE_DEPENDENCIES: List[Microservice] = []

        square_validator: SquareValidator
        coord_validator: CoordValidator
        team_validator: TeamValidator
        rank_service: RankService
        validation_primer: Primer
        identity_service: IdentityService

    Provides:
        -   def resolve_dependencies(s -> SearchResult[List[Dict[str, Any]]]:

    Super Class:
        Toolkit
    """

    DEPENDENCIES: List[Operation] = [
        SquareValidator,
        CoordValidator,
        TeamValidator,
        PrimingValidator,
        NumberValidator,
    ]
    
    SERVICE_DEPENDENCIES: List[Microservice] = [
        RankService,
        FormationService,
    ]
    square_validator: SquareValidator = SquareValidator()
    coord_validator: CoordValidator = CoordValidator()
    team_validator: TeamValidator = TeamValidator()
    identity_service: IdentityService = IdentityService()
    rank_service: RankService = RankService()
    validation_primer: PrimingValidator = PrimingValidator()
    number_validator: NumberValidator = NumberValidator()