# src/integrity/toolkit/team/toolkit.py

"""
Module: integrity.toolkit.team.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from integrity import Toolkit
from microservice import BoardService, IdentityService, PlayerService, SchemaService
from model import Team


class TeamToolkit(Toolkit[Team]):
    """
    Role:
        -   Container
        
    Responsibilities:
        1.  Collection of workers and services that are required for Board tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

     Attributes:
        board_service: Board service
        player_service: Player service
        schema_service: Schema service
        identity_service: Identity service

    Provides:
     Super Class:
         Toolkit
     """
    _board_service: BoardService
    _player_service: PlayerService
    _schema_service: SchemaService
    _identity_service: IdentityService

    def __init__(
            self,
            board_service: BoardService | None = None,
            player_service: PlayerService | None = None,
            schema_service: SchemaService | None = None,
            identity_service: IdentityService | None = None,
    ):
        """
        Args:
            board_service: Board service
            player_service: Player service
            schema_service: Schema service
            identity_service: Identity service
        """
        super().__init__()
        self._board_service = board_service
        self._player_service = player_service
        self._schema_service = schema_service
        self._identity_service = identity_service
        
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
