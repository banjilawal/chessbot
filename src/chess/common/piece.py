from enum import Enum, auto

from chess.common.geometry import Coordinate
from chess.common.rank import Rank
from chess.team.team import Team

from abc import ABC
from typing import List, Optional

class Label:
    _letters: str
    _number: int
    def __init__(self, letters: str, number: int):
        self._letters = letters
        self._number = number

    @property
    def letters(self) -> str:
        return self._letters

    @property
    def number(self) -> int:
        return self._number

    @property
    def label(self) -> str:
        return f"{self._letters}-{self._number}"

    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Label):
            return False
        return self._letters == other.letters and self._number == other.number


class CaptivityStatus(Enum):
    FREE = auto()
    PRISONER = auto

class Piece(ABC):
    _id: int
    _name: str
    _team: 'Team'
    _rank: 'Rank'
    _position_history: List['Coordinate']
    _status: CaptivityStatus

    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        if not chess_piece_id:
            raise ValueError("chess_piece_id cannot be null or empty.")
        if not name:
            raise ValueError("name cannot be null or empty.")
        if not team:
            raise ValueError("team cannot be null or empty.")
        if rank is None:
            raise ValueError("motion cannot be null.")
        self._id = chess_piece_id
        self._name = name
        self._team = team
        self._rank = rank
        self._status = CaptivityStatus.FREE
        self._position_history: List['Coordinate'] = []

    # === Immutable attributes ===
    @property
    def id(self) -> int:
        return self._id

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

    @property
    def position_history(self) -> List[Coordinate]:
        return self._position_history.copy()

    @status.setter
    def status(self, status: CaptivityStatus):
        if self._status != status:
            self._status = status

    def is_enemy(self, chess_piece: 'Piece'):
        return self._team.color == chess_piece.team.color

    # === Stack operations ===
    def add_position(self, coordinate: Coordinate) -> None:
        if coordinate is None:
            raise ValueError("coordinate cannot be null.")
        self._position_history.append(coordinate)

    def undo_last_position(self) -> Optional[Coordinate]:
        if self._position_history:
            return self._position_history.pop()
        return None

    def current_position(self) -> Optional[Coordinate]:
        return self._position_history[-1] if self._position_history else None


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Piece):
            return False
        if isinstance(other, Piece):
            self.id == other.id
        return False