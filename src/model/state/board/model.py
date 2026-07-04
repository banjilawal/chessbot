# src/model/state/board/model/state.py

"""
Module: model.state.board.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from controller import BoardTeamBinderController
from database import HostageDatabase, SquareDatabase
from model.arena import Arena
from model.board import BoardState

class Board:
    """
    Role:Data-Holder/Data Owner
  
    Responsibilities:
        1.  Surface where tokens move.
    
    Attributes:
        id: int
        biard: Board
        binder_controller: ArenaBinderController
        
    Super Class:
    """
    _id: int
    _arena: Arena
    _state: BoardState
    _squares: SquareDatabase
    _hostage_database: HostageDatabase
    _binder_controller: BoardTeamBinderController

    def __init__(self, id: int, arena: Arena,):
        """
        Args:
            id: int
            arena: Arena
        """
        self._id = id
        self._arena = arena
        self._squares = SquareDatabase()
        self._hostage_database = HostageDatabase()
        self._binder_controller = BoardTeamBinderController()
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
    def binder_controller(self) -> BoardTeamBinderController:
        return self._binder_controller
    
    @property
    def hostage_database(self) -> HostageDatabase:
        return self._hostage_database
    
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
    #         string += "".join(row_str_parts) + "\n"
    #     return string.strip()
