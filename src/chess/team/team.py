# src/chess/team/team.py

"""
Module: chess.team.team
Author: Banji Lawal
Created: 2025-08-04
version: 1.0.0
"""

from __future__ import annotations

from chess.board import Board
from chess.schema import Schema
from chess.player import Player
from chess.token import TokenDatabase


class Team:
    """
    # ROLE: Data-Holding

    # RESPONSIBILITY:
    1.  Disposition of Tokens the Player can move on a Board instance.
    2.  Holds the captured enemy Tokens.
    
    # PARENT:
    None
    
    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   schema (Schema)
        *   board (Board)
        *   owner (Player)
        *   roster (HostageService)
        *   hostages (HostageService)
        
    # INHERITED ATTRIBUTES:
    None
    """
    MAX_ROSTER_SIZE = 16
    
    _id: int
    _board: Board
    _owner: Player
    _schema: Schema
    _roster: TokenDatabase

    def __init__(
            self,
            id: int,
            board: Board,
            schema: Schema,
            owner: Player,
            roster: TokenDatabase = TokenDatabase(),
    ):
        """
        # ACTION:
        Construct a Team object.

        # PARAMETERS:
            *   id (int)
            *   owner (Player)
            *   board (Board)
            *   team_schema (Schema)
            *   roster (HostageService)
            *   hostages (HostageService)

        # RETURNS:
        None

        # RAISES:
        None
        """
        method = "Team.__init__"
        self._id = id
        self._board = board
        self._schema = schema
        self._roster = roster
        self._owner = owner
    
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