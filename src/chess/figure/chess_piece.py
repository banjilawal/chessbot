from enum import Enum, auto

from chess.common.config import ChessPieceConfig
from chess.common.geometry import Coordinate
from chess.figure.figure_rank import PawnRank, Rank, QueenRank
from chess.figure.promotable import RankPromotable
from chess.movement.movement_strategy import QueenMovement
from chess.team.team import Team

from abc import ABC
from typing import List, Optional

class CaptivityStatus(Enum):
    FREE = auto()
    PRISONER = auto

class ChessPiece(ABC):
    _status: CaptivityStatus
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        if not chess_piece_id:
            raise ValueError("chess_piece_id cannot be null or empty.")
        if not name:
            raise ValueError("name cannot be null or empty.")
        if not team:
            raise ValueError("team cannot be null or empty.")
        if rank is None:
            raise ValueError("movement cannot be null.")
        self._status = CaptivityStatus.FREE
        self._piece_id = chess_piece_id
        self._name = name
        self._team = team
        self._rank = rank
        self._position_history: List['Coordinate'] = []

    # === Immutable attributes ===
    @property
    def piece_id(self) -> int:
        return self._piece_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def team(self) -> 'Team':
        return self._team

    @property
    def rank(self) -> 'Rank':
        return self._rank

    @property
    def status(self) -> CaptivityStatus:
        return self._status

    @status.setter
    def status(self, status: CaptivityStatus):
        if self._status != status:
            self._status = status

    # === Stack operations ===
    def add_position(self, coordinate: Coordinate) -> None:
        if coordinate is None:
            raise ValueError("coordinate cannot be null.")
        self._position_history.append(coordinate)

    def undo_last_position(self) -> Optional[Coordinate]:
        if self._position_history:
            return self._position_history.pop()
        return None

    @property
    def current_position(self) -> Optional[Coordinate]:
        return self._position_history[-1] if self._position_history else None

    @property
    def position_history(self) -> List[Coordinate]:
        return list(self._position_history)


class Pawn(ChessPiece, RankPromotable):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)

    def add_position(self, coordinate: Coordinate) -> None:
        super.add_position(coordinate)
        if coordinate.row == self.team.home.get_enemy_home().first_home_row():
            self.promote(self, QueenRank(QueenMovement))

    def promote(self, new_rank: Rank) -> Optional[ChessPiece]:
        if new_rank is None:
            print("new_rank cannot be null or empty.")
            return None
        if self.rank == QueenRank:
            print("Pawn is already promoted")
            return None
        if new_rank != QueenRank:
            print("New rank must be Queen")
            return None
        return Pawn(
            chess_piece_id=self.piece_id,
            name=self.name,
            team=self.team,
            rank=QueenRank(QueenMovement())
        )


class Knight(ChessPiece):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)


class Bishop(ChessPiece):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)


class Castle(ChessPiece):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)


class Queen(ChessPiece):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)

class King(ChessPiece, RankPromotable):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)

    def add_position(self, coordinate: Coordinate) -> None:
        super.add_position(coordinate)
        if coordinate.row == self.team.home.get_enemy_home().first_home_row():
            self.promote(self, QueenRank(QueenMovement))

    def promote(self, new_rank: Rank) -> Optional[ChessPiece]:
        if new_rank is None:
            print("new_rank cannot be null or empty.")
            return None
        if self.rank == QueenRank:
            print("Pawn is already promoted")
            return None
        if new_rank != QueenRank:
            print("New rank must be Queen")
            return None
        return King(
            chess_piece_id=self.piece_id,
            name=self.name,
            team=self.team,
            rank=QueenRank(QueenMovement())
        )

