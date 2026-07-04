# src/toolkit/model/board/toolkit.py

"""
Module: toolkit.model.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Board
from operation import ArenaValidator
from toolkit import ModelToolkit
from microservice import BoardTeamBinderService

class BoardToolkit(ModelToolkit[Board]):
    """
    Role:
        -   Container
        
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        arena_validator: ArenaValidator
        team_binder_service: BoardTeamBinderService
        
    Provides:

     Super Class:
         Toolkit
     """
    _arena_validator: ArenaValidator
    _team_binder_service: BoardBoardTeamBinderService

    def __init__(
            self,
            arena_validator: ArenaValidator | None = None,
            team_binder_service: BoardBoardTeamBinderService | None = None,
    ):
        """
        Args:
            arena_validator: ArenaValidator
        """
        super().__init__()
        self._arena_validator = arena_validator or ArenaValidator()
        self._team_binder_service = team_binder_service or BoardTeamBinderService()
        
    @property
    def arena_validator(self) -> ArenaValidator:
        return self._arena_validator
    
    @property
    def team_binder_service(self) -> BoardBoardTeamBinderService:
        return self._team_binder_service