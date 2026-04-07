# src/toolkit/integrity/team/toolkit.py

"""
Module: toolkit.integrity.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

import dataclasses

from microservice import BoardService, PlayerService, SchemaService
from model import team
from toolkit import IntegrityToolkit



@dataclasses.dataclass
class TeamIntegrityToolkit(IntegrityToolkit[team]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Simplify entry Team builder and validator entry points.
        
    Attributes:
        board_service: BoardService
        player_service: PlayerService
        schema_service: SchemaService
        identity_service: IdentityService

    Provides:

    Super Class:
    IntegrityToolkit
    """
    board_service: BoardService
    player_service: PlayerService
    schema_service: SchemaService
    identity_service: IdentityService



        
