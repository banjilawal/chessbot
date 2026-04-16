# src/model/blueprint/binder/model.py

"""
Module: model.blueprint.binder.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from microservice import TeamService
from model import Blueprint, Board, Schema, BoardTeamBinder


class BoardTeamBinderBlueprint(Blueprint[BoardTeamBinder]):
    _id: int
    _board: Board
    _schema: Schema
    _team_service: TeamService
    
    def __init__(
            self,
            board: Board,
            id: Optional[int] | None = None,
            schema: Optional[Schema] | None = None,
            team_service: TeamService | None = None
    ):
        """
        Args:
            id: int
            board: Board
            schema: Schema
            team_service: TeamService
        """
        super().__init__()
        self._id = id
        self._board = board
        self._schema = schema or Schema()
        self._team_service = team_service or TeamService()
        
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def schema(self) -> Schema:
        return self._schema
    
    @property
    def team_service(self) -> TeamService:
        return self._team_service
    

