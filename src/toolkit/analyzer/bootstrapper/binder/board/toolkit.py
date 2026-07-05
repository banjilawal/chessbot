# src/toolkit/analyzer/binder/board/toolkit.py

"""
Module: toolkit.analyzer.binder.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import BoardService, SchemaService, TeamService
from bootstrap.validator.priming import PrimingValidator


class BoardTeamBinderToolkit(AnalyzerToolkit):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for BoardTeamBinder tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        team_service: TeamService
        board_validator: BoardService
        schema_service: SchemaService
        identity_service: IdentityService
        priming_validator: ValidationBootrapper

    Provides:

    Super Class
        Toolkit
    """
    _team_service: TeamService
    _board_validator: BoardService
    _schema_service: SchemaService    
    def __init__(
            self,
            team_service: TeamService | None = None,
            board_validator: BoardService | None = None,
            schema_service: SchemaService | None = None,

            priming_validator: PrimingValidator | None = None,
    ):
        """
        Args:
            team_service: TeamService
            board_validator: BoardService
            schema_service: SchemaService

            priming_validator: PrimingValidator
        """
        super().__init__()
        self._team_service = team_service or TeamService()
        self._board_validator = board_validator or BoardService()
        self._schema_service = schema_service or SchemaService()

        
    @property
    def team_service(self) -> TeamService:
        return self._team_service
        
    @property
    def board_validator(self) -> BoardService:
        return self._board_validator
    
    @property
    def schema_service(self) -> SchemaService:
        return self._schema_service
    

    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator