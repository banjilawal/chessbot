# src/chess/team/team.py

"""
Module: chess.team.team
Author: Banji Lawal
Created: 2025-08-04
version: 1.0.0
"""

from __future__ import annotations

from chess.board import Board, BoardState
from chess.schema import Schema
from chess.player import Player
from chess.team import TeamState
from chess.team.state import TeamBoardState, TeamRosterState
from chess.token import TokenDatabase


class Team:
    """
    # ROLE: Data-Holder

    # RESPONSIBILITY:
    1.  Disposition of Tokens the Player can move on a Board instance.
    2.  Holds the captured enemy Tokens.
    
    # PARENT:
    None
    
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   board (Board)
        *   owner (Player)
        *   schema (Schema)
        *   roster (TokenDatabase)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        Local:
        *   id (int)
        *   board (Board)
        *   owner (Player)
        *   schema (Schema)
        *   roster (TokenDatabase)

        Inherited:
        None

    # LOCAL ATTRIBUTES:
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
    _roster: TokenDatabase
    _board_state: TeamBoardState
    _roster_state: TeamRosterState


    def __init__(
            self,
            id: int,
            board: Board,
            schema: Schema,
            owner: Player,
            roster: TokenDatabase = TokenDatabase(),
    ):
        method = "Team.__init__"
        self._id = id
        self._board = board
        self._schema = schema
        self._roster = roster
        self._owner = owner
        self._roster_state = TeamRosterState.ROSTER_EMPTY
        self._board_state = TeamBoardState.WAITING_FOR_DEPLOYMENT

    
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
    def board_state(self) -> TeamBoardState:
        return self._board_state
    
    @board_state.setter
    def board_state(self, state: TeamBoardState):
        self._board_state = state
        
    @property
    def roster_state(self) -> TeamRosterState:
        return self._roster_state
    
    @roster_state.setter
    def roster_state(self, state: TeamRosterState):
        self._roster_state = state
        
    def is_roster_empty(self) -> bool:
        return self._roster.is_empty and self._roster_state == TeamRosterState.ROSTER_EMPTY
    
    def is_roster_full(self) -> bool:
        return self._roster.is_full and self._roster_state == TeamRosterState.ROSTER_FULL
    
    def is
    
    def is_deployment_complete(self) -> bool:
        return self.is_roster_empty() and self._board_state == TeamBoardState.FULLY_DEPLOYED_ON_BOARD
    
    def is_deployment_in_progress(self) -> bool:
        return self._board_state == TeamBoardState.WAITING_FOR_DEPLOYMENT
        
    def is_ready_to_play(self) -> bool:
    
    
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