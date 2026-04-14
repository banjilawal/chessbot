# src/model/blueprint/team/blueprint.py

"""
Module: model.blueprint.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from microservice import TeamBinderService
from model.catalog import Schema
from model import Blueprint, Board, Player, Team


class TeamBlueprint(Blueprint[Team]):
    _id: int
    _owner: Player
    _board: Board
    _schema: Schema

    
    def __init__(
            self,
            owner: Player,
            board: Board,
            schema: Schema,
            id: Optional[int] | None = None,
    ):
        super().__init__()
        self._id = id
        self._owner = owner
        self._board = board
        self._schema = schema
        
    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def owner(self) -> Player:
        return self._owner
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def schema(self) -> Schema:
        return self._schema
    

