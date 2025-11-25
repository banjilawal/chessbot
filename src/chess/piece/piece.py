# src/chess/piece/piece.py

"""
Module: chess.piece.piece
Author: Banji Lawal
Created: 2025-07-22
version: 1.0.0
"""

from abc import ABC
from typing import Optional


from chess.team import Team
from chess.rank import Rank
from chess.coord import Coord, CoordDataService
from chess.piece import CoordStack, CoordStackService, Piece


class Piece(ABC):
    """
    # ROLE: Data-Holding, Abstract Data Type
  
    # RESPONSIBILITIES:
    1.  Travels to attack or avoid enemies on the Board.
    2.  Capture any Piece except KingPiece.
    2.  Keep immutable record of Coords occupied.
    3.  Superclass of CombatantPiece, KingPiece, and PawnPiece.
  
    # PROVIDES:
    Piece
  
    # ATTRIBUTES:
        *   id (int):                                   Globally unique identifier.
        *   name (str):                                 Conventional name of chess piece
        *   team (Team):
        *   rank (Rank):
        *   roster_number (int):                        initial number on its team's roster.
        *   current_position (Coord):                   Coord at last move
        *   positions (CoordDataService):
    """
    _id: int
    _name: str
    _team: Team
    _rank: Rank
    _roster_number: int
    _current_position: Coord
    _positions: CoordDataService

    
    def __init__(
            self,
            id: int,
            name: str,
            rank: Rank,
            team: Team,
            positions: CoordStackService = CoordStackService()
    ):
        method = "Piece.__init__"

        self._id = id
        self._name = name
        self._team = team
        self._rank = rank
        self._positions = positions
        self._current_position = self._positions.current_item
        
        if self not in team.roster:
            team.roster.append(self)
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def roster_number(self) -> int:
        return self._roster_number
    
    @property
    def team(self) -> 'Team':
        return self._team
    
    @property
    def rank(self) -> 'Rank':
        return self._rank
    
    @property
    def positions(self) -> CoordDataService:
        return self._positions
    
    @property
    def current_position(self) -> Optional[Coord]:
        return self._positions.current_item
    
    def _set_rank(self, rank: Rank) -> None:
        self._rank = rank
    
    def is_enemy(self, piece: Piece) -> bool:
        return self._team != piece.team
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other in None: return False
        if isinstance(other, Piece):
            return self._id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return (
            f"Piece[id:{self._id} "
            f"name:{self._name} "
            f"rank:{self._rank.name} "
            f"team_name:{self._team.schema.name} "
            f"position:{self._positions.current_coord} "
            f"moves:{self._positions.size}]"
        )
