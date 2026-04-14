# src/toolkit/team/toolkit.py

"""
Module: toolkit.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Team
from toolkit import Toolkit
from microservice import BoardService, IdentityService, PlayerService, SchemaService, TeamBinderService


class TeamToolkit(Toolkit[Team]):
    """
    Role:
    -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.
    
    Attributes:
        board_service: BoardService
        player_service: PlayerService
        schema_service: SchemaService
        identity_service: IdentityService
    
    Provides:
    Super Class:
        Toolkit
    """
    _board_service: BoardService
    _player_service: PlayerService
    _schema_service: SchemaService
    _team_binder_service: TeamBinderService
    _identity_service: IdentityService

    def __init__(
            self,
            board_service: BoardService | None = None,
            player_service: PlayerService | None = None,
            schema_service: SchemaService | None = None,
            identity_service: IdentityService | None = None,
            team_binder_service: TeamBinderService | None = None,
    ):
        """
        Args:
            board_service: BoardService
            player_service: PlayerService
            schema_service: SchemaService
            identity_service: IdentityService
        """
        super().__init__()
        self._board_service = board_service or BoardService()
        self._player_service = player_service or PlayerService()
        self._schema_service = schema_service or SchemaService()
        self._identity_service = identity_service or IdentityService()
        self._team_binder_service = team_binder_service or TeamBinderService()
        
    @property
    def board_service(self) -> BoardService:
        return self._board_service
    
    @property
    def player_service(self) -> PlayerService:
        return self._player_service
    
    @property
    def schema_service(self) -> SchemaService:
        return self._schema_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    
    @property
    def team_binder_service(self) -> TeamBinderService:
        return self._team_binder_service
