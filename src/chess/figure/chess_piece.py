from abc import ABC, abstractmethod
from typing import List, Optional

from chess.team.team import Team
from geometry import GridCoordinate

from abc import ABC
from typing import List, Optional

class ChessPiece(ABC):
    def __init__(self, piece_id: int, name: str, team: 'Team', rank: 'FigureRank'):
        if not piece_id:
            raise ValueError("piece_id cannot be null or empty.")
        if not name:
            raise ValueError("name cannot be null or empty.")
        if not team:
            raise ValueError("team cannot be null or empty.")
        if rank is None:
            raise ValueError("movement cannot be null.")

        self._piece_id = piece_id
        self._name = name
        self._team = team
        self._rank = rank
        self._position_history: List['GridCoordinate'] = []

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
    def rank(self) -> 'FigureRank':
        return self._rank

    # === Stack operations ===
    def add_position(self, coordinate: 'GridCoordinate') -> None:
        if coordinate is None:
            raise ValueError("coordinate cannot be null.")
        self._position_history.append(coordinate)

    def undo_last_position(self) -> Optional['GridCoordinate']:
        if self._position_history:
            return self._position_history.pop()
        return None

    @property
    def current_position(self) -> Optional['GridCoordinate']:
        return self._position_history[-1] if self._position_history else None

    @property
    def position_history(self) -> List['GridCoordinate']:
        return list(self._position_history)  # Defensive copy


class Pawn(ChessPiece):
    def __init__(self, piece_id: int, name: str, team: 'Team', rank: 'FigureRank'):
        super().__init__(piece_id, name, team, rank)


class Knight(ChessPiece):
    def __init__(self, piece_id: int, name: str, team: 'Team', rank: 'FigureRank'):
        super().__init__(piece_id, name, team, rank)


class Bishop(ChessPiece):
    def __init__(self, piece_id: int, name: str, team: 'Team', rank: 'FigureRank'):
        super().__init__(piece_id, name, team, rank)


class Castle(ChessPiece):
    def __init__(self, piece_id: int, name: str, team: 'Team', rank: 'FigureRank'):
        super().__init__(piece_id, name, team, rank)


class Queen(ChessPiece):
    def __init__(self, piece_id: int, name: str, team: 'Team', rank: 'FigureRank'):
        super().__init__(piece_id, name, team, rank)


class King(ChessPiece):
    def __init__(self, piece_id: int, name: str, team: 'Team', rank: 'FigureRank'):
        super().__init__(piece_id, name, team, rank)

