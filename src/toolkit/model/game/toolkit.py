# src/toolkit/model/game/toolkit.py

"""
Module: toolkit.model.game.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import BoardService, IdentityService, PlayerService
from model.state.game import Game, GameToolkitException
from system import Toolkit, ToolkitResult, LoggingLevelRouter


class GameToolkit(ModelToolkit[Game]):
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
        identity_service: IdentityService
        
    Provides:

     Super Class:
         Toolkit
     """
    board_service: BoardService
    _player_service: PlayerService
    _identity_service: IdentityService


    @LoggingLevelRouter.monitor()
    def __init__(
            self,
            board_service: BoardService | None = None,
            player_service: PlayerService | None = None,
            identity_service: IdentityService | None = None,
    ):
        """
        Args:
            board_service: BoardService
            player_service: PlayerService
            identity_service: IdentityService
        """
        self._board_service = board_service or BoardService()
        self._player_service = player_service or PlayerService()
        self._identity_service = identity_service or IdentityService()
    
    @property
    def board_service(self) -> BoardService:
        return self._board_service
    
    @property
    def player_service(self) -> PlayerService:
        return self._player_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
        
        