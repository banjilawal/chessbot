# src/model/team/model.py

"""
Module: model.team.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from database import TokenDatabase
from model.board import Board
from model.catalog import Schema
from model.player import Player
from model.team import TeamState

class Team:
    """
    Role:Data-Holder

    # RESPONSIBILITY:
    1.  Disposition of Tokens the Player can move on a Board instance.
    2.  Holds the captured enemy Tokens.
    
    Super Class:
    None
    
    Provides:

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   board (Board)
        *   owner (Player)
        *   schema (Schema)
        *   roster (TokenDatabase)

    # INHERITED ATTRIBUTES:
    None

    Attributes:
        Local:
        *   id (int)
        *   board (Board)
        *   owner (Player)
        *   schema (Schema)
        *   roster (TokenDatabase)

        Inherited:
        None


    # INHERITED ATTRIBUTES:
    None

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    MAX_ROSTER_SIZE = 16
    
    _id: int
    _board: Board
    _owner: Player
    _schema: Schema
    _state: TeamState
    _roster: TokenDatabase

    def __init__(
            self,
            id: int,
            board: Board,
            schema: Schema,
            owner: Player,
    ):
        """
        Args:
            id: int
            board: Board
            schema: Schema
            owner: Player
        """
        self._id = id
        self._board = board
        self._schema = schema
        self._owner = owner
        self._state = TeamState.NOT_READY_TO_PLAY
        self._roster = TokenDatabase()

    
    @property
    def id(self) -> int:
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

    @property
    def roster(self) -> TokenDatabase:
        return self._roster
    
    @property
    def state(self) -> TeamState:
        return self._state
    
    @state.setter
    def state(self, state: TeamState):
        self._state = state
        
    def is_ready_to_play(self) -> bool:
        return self._roster.is_deployed_on_board and self._state == TeamState.READY_TO_PLAY
    
    def is_not_ready_to_play(self) -> bool:
        return not self._roster.is_deployed_on_board and not self._state != TeamState.NOT_READY_TO_PLAY
    
    def is_waiting_to_play(self) -> bool:
        return self._roster.is_deployed_on_board and self._state == TeamState.WAITING_TO_PLAY
    
    def __eq__(self, other) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, Team):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return f"Team{{id:{self._id} {self._owner.name} {self._schema}}}"