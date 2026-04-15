# src/toolkit/binder/toolkit.py

"""
Module: toolkit.binder.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import BoardService, IdentityService, TeamService
from model import Board
from model.catalog import SchemaService
from system import BuildResult, Builder, LoggingLevelRouter
from model.team import (
    BlackTeamHasWrongSchemaException, Team, TeamBinder, TeamBinderBuildException,
    TeamSchemaCollisionException, TeamValidator, WhiteTeamHasWrongSchemaException
)


class TeamBinderToolkit(Toolkit[TeamBinder]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for TeamBinder tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        board_service: BoardService
        schema_service: SchemaService
        identity_service: IdentityService


    Provides:

    Super Class
        Toolkit
    """
    _board_service: BoardService
    _schema_service: SchemaService
    _identity_service: IdentityService
    
    def __init__(
            self,
            board_service: BoardService | None = None,
            schema_service: SchemaService | None = None,
            identity_service: IdentityService | None = None,
    ):
        """
        Args:
            board_service: BoardService
            schema_service: SchemaService
            identity_service: IdentityService
        """
        self._board_service = board_service or BoardService()
        self._schema_service = schema_service or SchemaService()
        self._identity_service = identity_service or IdentityService()
        
    @property
    def board_service(self) -> BoardService:
        return self._board_service
    
    @property
    def schema_service(self) -> SchemaService:
        return self._schema_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service