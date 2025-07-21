from abc import ABC, abstractmethod
from typing import List, Optional

from constants import GameColor
from geometry import GridCoordinate

@dataclass(frozen=True)
class Team:
    color: GameColor
    starting_row: int
    advancement_direction: int

class ChessPiece(ABC):
    def __init__(self, piece_id: int, name: str, color: GameColor, rank: 'Rank'):
        if not piece_id:
            raise ValueError("piece_id cannot be null or empty.")
        if not name:
            raise ValueError("name cannot be null or empty.")
        if not color:
            raise ValueError("color cannot be null or empty.")
        if rank is None:
            raise ValueError("rank cannot be null.")

        self._piece_id = piece_id
        self._name = name
        self._color = color
        self._rank = rank
        self._position_stack: List['GridCoordinate'] = []

    # === Immutable attributes ===
    @property
    def piece_id(self) -> str:
        return self._piece_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> str:
        return self._color

    @property
    def rank(self) -> 'Rank':
        return self._rank

    # === Stack operations ===
    def add_position(self, coordinate: 'GridCoordinate') -> None:
        if coordinate is None:
            raise ValueError("coordinate cannot be null.")
        self._position_stack.append(coordinate)

    def undo_last_position(self) -> Optional['GridCoordinate']:
        if self._position_stack:
            return self._position_stack.pop()
        return None

    @property
    def current_position(self) -> Optional['GridCoordinate']:
        return self._position_stack[-1] if self._position_stack else None

    @property
    def position_history(self) -> List['GridCoordinate']:
        return list(self._position_stack)  # Defensive copy

    # === Rank-defined strategy ===
    @abstractmethod
    def get_move_strategy(self) -> 'MoveStrategy':
        pass