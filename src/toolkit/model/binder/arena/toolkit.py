# src/toolkit/model/binder/arena/toolkit.py

"""
Module: toolkit.model.binder.arena.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from microservice import ArenaService, IdentityService, SchemaService, PlayerService
from model import ArenaBinder
from toolkit import Toolkit


class ArenaPlayerBinderToolkit(Toolkit[ArenaBinder]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for ArenaPlayerBinder tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        player_service: PlayerService
        arena_service: ArenaService
        schema_service: SchemaService
        identity_service: IdentityService

    Provides:

    Super Class
        Toolkit
    """
    _player_service: PlayerService
    _arena_service: ArenaService
    _schema_service: SchemaService
    _identity_service: IdentityService
    
    def __init__(
            self,
            player_service: PlayerService | None = None,
            arena_service: ArenaService | None = None,
            schema_service: SchemaService | None = None,
            identity_service: IdentityService | None = None,
    ):
        """
        Args:
            player_service: PlayerService
            arena_service: ArenaService
            schema_service: SchemaService
            identity_service: IdentityService
        """
        self._player_service = player_service or PlayerService()
        self._arena_service = arena_service or ArenaService()
        self._schema_service = schema_service or SchemaService()
        self._identity_service = identity_service or IdentityService()
        
    @property
    def player_service(self) -> PlayerService:
        return self._player_service
        
    @property
    def arena_service(self) -> ArenaService:
        return self._arena_service
    
    @property
    def schema_service(self) -> SchemaService:
        return self._schema_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service