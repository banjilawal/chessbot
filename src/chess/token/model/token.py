# src/chess/token/model/token.py

"""
Module: chess.token.model.piece
Author: Banji Lawal
Created: 2025-07-22
version: 1.0.0
"""

from abc import ABC
from typing import Optional

from chess.rank import Rank
from chess.team import Team
from chess.token import Token
from chess.square import Square
from chess.coord import Coord, CoordDataService

class Token(ABC):
    """
    # ROLE: Data-Holding, Abstract Data Type
  
    # RESPONSIBILITIES:
    1.  Travels to attack or avoid enemies on the Board.
    2.  Capture any Token except KingPiece.
    2.  Keep immutable record of Coords occupied.
    3.  Superclass of CombatantPiece, KingPiece, and PawnPiece.
  
    # PROVIDES:
    Token
  
    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   team (Team)
        *   rank (Rank)
        *   roster_number (int)
        *   current_position (Coord)
        *   positions (CoordDataService):
    """
    _id: int
    _team: Team
    _rank: Rank
    _designation: str
    _roster_number: int
    _current_position: Optional[Coord]
    _previous_address: Optional[Coord]
    _positions: CoordDataService

    def __init__(
            self,
            id: int,
            rank: Rank,
            team: Team,
            designation: str,
            roster_number: int,
            opening_square: Square,
            positions: CoordDataService = CoordDataService()
    ):
        method = "Token.__init__"
        self._id = id
        self._team = team
        self._rank = rank
        self._positions = positions
        self._designation = designation
        self._roster_number = roster_number
        self._opening_square = opening_square
        self._current_position = self._positions.current_item
        self.previous_address = self._positions.previous_item
        
        if self not in team.roster:
            team.roster.append(self)
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def designation(self) -> str:
        return self._designation
    
    @property
    def roster_number(self) -> int:
        return self._roster_number
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def rank(self) -> Rank:
        return self._rank
    
    @property
    def opening_square(self) -> Square:
        return self._opening_square
    
    @property
    def positions(self) -> CoordDataService:
        return self._positions
    
    @property
    def current_position(self) -> Optional[Coord]:
        return self._positions.current_item
    
    @property
    def previous_address(self) -> Optional[Coord]:
        return self._previous_address
    
    def _set_rank(self, rank: Rank) -> None:
        self._rank = rank
    
    def is_enemy(self, token: Token) -> bool:
        return self._team != token.team
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other in None: return False
        if isinstance(other, Token):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return (
            f"Token[id:{self._id} "
            f"designation:{self._designation} "
            f"rank:{self._rank.name} "
            f"team:{self._team.schema.name} "
            f"position:{self.current_position}"
        )
