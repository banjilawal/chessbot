# src/toolkit/team/toolkit.py

"""
Module: toolkit.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import IdentityService
from model import Team
from operation import BoardValidator, PlayerValidator, SchemaValidator, ValidationBootstrapper
from toolkit import Toolkit

class TeamToolkit(Toolkit[Team]):
    """
    Role:
    -   Container
    
    Responsibilities:
        1.  Collection of workers and validators that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        board_validator: BoardValidator
        player_validator: PlayerValidator
        schema_validator: SchemaValidator
        identity_validator: IdentityValidator
    
    Provides:
    Super Class:
        Toolkit
    """
    DEPENDENCIES = [
        BoardValidator,
        IdentityService,
        SchemaValidator,
        PlayerValidator,
        ValidationBootstrapper
    ]
    board_validator: BoardValidator = BoardValidator()
    identity_service: IdentityService = IdentityService()
    player_validator: PlayerValidator = PlayerValidator()
