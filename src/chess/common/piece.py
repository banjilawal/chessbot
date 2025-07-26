from enum import Enum, auto

from chess.geometry.coordinate import Coordinate
from chess.rank.rank import Rank

from abc import ABC
from typing import List, Optional







class Piece(ABC):
    _id: int
    _label: Label
    _team: 'Team'
    _rank: 'Rank'
    _position_history: List['Coordinate']
    _status: CaptivityStatus

    def __init__(self, piece_id: int, label: Label, team: 'Team', rank: 'Rank'):
        if not piece_id:
            raise ValueError("piece_id cannot be null or empty.")
        if not label:
            raise ValueError("label cannot be null or empty.")
        if not team:
            raise ValueError("team cannot be null or empty.")
        if rank is None:
            raise ValueError("motion cannot be null.")
        self._id = piece_id
        self._label = label
        self._team = team
        self._rank = rank
        self._status = CaptivityStatus.FREE
        self._position_history: List['Coordinate'] = []

    # === Immutable attributes ===
    @property
    def id(self) -> int:
        return self._id

    @property
    def label(self) -> str:
        return self._label


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

    def is_enemy(self, piece: 'Piece'):
        return self._team == piece.team

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