# src/chess/token/model/abstract.py

"""
Module: chess.token.model.abstract
Author: Banji Lawal
Created: 2025-07-22
version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Optional

from chess.rank import Rank
from chess.team import Team
from chess.square import Square
from chess.token import Token, TokenBoardState
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
    _opening_square: Square
    _positions: CoordDataService
    _current_position: Optional[Coord]
    _previous_address: Optional[Coord]
    _token_board_state: TokenBoardState

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
        self._current_position = self._positions.current_coord
        self._previous_address = self._positions.previous_coord
        self._token_board_state = TokenBoardState.NEVER_BEEN_PLACED
    
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
    def previous_coord(self) -> Optional[Coord]:
        return self._previous_address
    
    @property
    def board_state(self) -> TokenBoardState:
        return self._token_board_state
    
    @property
    def is_not_formed(self):
    
    @property
    @abstractmethod
    def is_active(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_disabled(self) -> bool:
        pass
    
    @board_state.setter
    def board_state(self, token_board_state: TokenBoardState):
        self._token_board_state = token_board_state
    
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
    
    @property
    def has_not_been_formed(self) -> bool:
        return (
                self.positions.size == 0 and
                self._token_board_state == TokenBoardState.NEVER_BEEN_PLACED
        )
    
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
