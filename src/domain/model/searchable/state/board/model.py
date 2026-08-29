# src/domain/model/searchable/state/board/model.py

"""
Module: domain.model.searchable.state.board.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from collection import AttackDatabase, ManeuverDatabase, SquareDatabase, TokenDatabase
from domain import Arena, BoardState, BoardTeamColorBinder, StateModel


class Board(StateModel):
    """
    Role:Data-Holder/Data Owner
  
    Responsibilities:
        1.  Surface where tokens move.
    
    Attributes:
        id: int
        arena: Arena
        squares: SquareDatabase
        maneuver_log: ManeuverDatabase
        attack_records: AttackDatabase
        captured_tokens: TokenDatabase
        team_binder: BoardTeamColorBinder
        
    Super Class:
        StateModel
    """
    _id: int
    _arena: Arena
    _state: BoardState
    _squares: SquareDatabase
    _maneuver_log: ManeuverDatabase
    _attack_records: AttackDatabase
    _captured_tokens: TokenDatabase
    _team_binder: BoardTeamColorBinder

    def __init__(
            self,
            id: int,
            arena: Arena,
            team_binder: BoardTeamColorBinder,
            squares: Optional[SquareDatabase] | None = None,
            maneuver_log: Optional[ManeuverDatabase] | None = None,
            attack_records: Optional[AttackDatabase] | None = None,
            captured_tokens: Optional[TokenDatabase] | None = None,
    ):
        """
        Args:
            id: int
            arena: Arena
            team_binder: BoardTeamColorBinder
            squares: Optional[SquareDatabase]
            maneuver_log: Optional[ManeuverDatabase]
            attack_records: Optional[AttackDatabase]
            captured_tokens: Optional[TokenDatabase]
        """
        super().__init__(id=id)
        self._arena = arena
        self._team_binder = team_binder
        self._squares = squares or SquareDatabase()
        self._maneuver_log = maneuver_log or ManeuverDatabase()
        self._attack_records = attack_records or AttackDatabase()
        self._captured_tokens = captured_tokens or TokenDatabase()
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
    def team_binder(self) -> BoardTeamColorBinder:
        return self._team_binder
    
    @property
    def maneuver_log(self) -> ManeuverDatabase:
        return self._maneuver_log
    
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
