# src/toolkit/token/toolkit.py

"""
Module: toolkit.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from model import Token
from toolkit import Toolkit
from microservice import FormationService, IdentityService, Microservice, RankService
from operation import CoordValidator, Operation, SquareValidator, TeamValidator, ValidationBootstrapper



class TokenToolkit(Toolkit[Token]):
    """
    Role:
        -   Container
        -   Data Holder
        
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        DEPENDENCIES: List[Operation]
        SERVICE_DEPENDENCIES: List[Microservice]
        
    Provides:
    
    Super Class:
        Toolkit
    """

    DEPENDENCIES: List[Operation] = [
        SquareValidator,
        CoordValidator,
        TeamValidator,
        ValidationBootstrapper,
    ]
    
    SERVICE_DEPENDENCIES: List[Microservice] = [
        RankService,
        FormationService,
    ]
    square_validator: SquareValidator = SquareValidator()
    coord_validator: CoordValidator = CoordValidator()
    team_validator: TeamValidator = TeamValidator()
    identity_service: IdentityService = IdentityService()
    validation_bootstrap: ValidationBootstrapper = ValidationBootstrapper()