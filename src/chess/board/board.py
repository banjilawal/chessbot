# src/chess/board/board.py

"""
Module: chess.board.board
Author: Banji Lawal
Created: 2025-07-31
version: 1.0.0
"""

from __future__ import annotations

from chess.arena import Arena
from chess.team import TeamHash
from chess.board import BoardState
from chess.square import SquareDatabase
from chess.hostage import HostageDatabase

class Board:
    """
    # ROLE: Data-Holder/Data Owner
  
    # RESPONSIBILITIES:
    The Surface of Squares where Tokens are played.
  
    # PROVIDES:
      Board
  
    # ATTRIBUTES:
        * id (int)
        * arena (Arena)
        * NUMBER_OF_ROWS (int)
        * column_size (int)
        * tokens ([BoardTokenService])
        * squares ([[BoardSquareService]])
    """
    _id: int
    _arena: Arena
    _state: BoardState
    _squares: SquareDatabase
    _hostage_database: HostageDatabase
    
    def __init__(
            self,
            id: int,
            arena: Arena,
            squares: SquareDatabase = SquareDatabase(),
            hostage_database: HostageDatabase = HostageDatabase(),
    ):
        """
        # ACTION:
            Constructs Board object
        # PARAMETERS:
            *   id (int)
            *   arena (Arena)
            *   NUMBER_OF_ROWS (int)
            *   column_size (int)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "Board.__init__"
        
        self._id = id
        self._arena = arena
        self._squares = squares
        self._hostage_database = hostage_database
        self._state = BoardState.IS_EMPTY
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def state(self) -> BoardState:
        return self._state
    
    @state.setter
    def state(self, state: BoardState):
        self._state = state
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def squares(self) -> SquareDatabase:
        return self._squares
    
    @property
    def team_hash(self) -> TeamHash:
        return self._team_hash
    
    @property
    def hostage_database(self) -> HostageDatabase:
        return self._hostage_database
    
    def layout(self):
        for key in self._team_hash.table.keys():
            self._team_hash.table[key].roster.deploy_tokens_on_board()
    
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Board):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    # def __str__(self) -> str:
    #     """"""
    #     string = ""
    #     # Iterate from the top row (row 7) down to the bottom (row 0)
    #     for row in reversed(self._squares):
    #         row_str_parts = []
    #         for square_name in row:
    #             if square_name.occupant is not None:
    #                 # Display the discover's visitor_name if the square_name is occupied.
    #                 row_str_parts.append(f"[{square_name.occupant.designation}]")
    #             else:
    #                 # Display the square_name's visitor_name in brackets if it's empty.
    #                 row_str_parts.append(f"[{square_name.designation}]")
    #         string += " ".join(row_str_parts) + "\n"
    #     return string.strip()
