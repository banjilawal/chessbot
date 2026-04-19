# src/model/blueprint/binder/model.py

"""
Module: model.blueprint.binder.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from microservice import PlayerService
from model import Blueprint, Arena, Schema, ArenaBinder


class ArenaPlayerBinderBlueprint(Blueprint[ArenaBinder]):
    _id: int
    _arena: Arena
    _schema: Schema
    _player_service: PlayerService
    
    def __init__(
            self,
            arena: Arena,
            id: Optional[int] | None = None,
            schema: Optional[Schema] | None = None,
            player_service: PlayerService | None = None
    ):
        """
        Args:
            id: int
            arena: Arena
            schema: Schema
            player_service: PlayerService
        """
        super().__init__()
        self._id = id
        self._arena = arena
        self._schema = schema or Schema()
        self._player_service = player_service or PlayerService()
        
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def schema(self) -> Schema:
        return self._schema
    
    @property
    def player_service(self) -> PlayerService:
        return self._player_service
    

